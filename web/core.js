/* tonemaker core — faithful JS port of engine.py / validate.py / build.py.
   Pure logic, no DOM. Works in the browser (data injected as globals MODELS/BLOCKS)
   and in Node (call TM.setData(models, blocks)) so it can be tested against the
   Python builder. Keep in lockstep with src/tonemaker/*.py. */
(function (global) {
  "use strict";
  let MODELS = global.MODELS || null;
  let BLOCKS = global.BLOCKS || null;

  const clone = (x) => (typeof structuredClone === "function"
    ? structuredClone(x) : JSON.parse(JSON.stringify(x)));

  function setData(models, blocks) { MODELS = models; BLOCKS = blocks; }

  function buildIndex() {
    const idx = {};
    for (const cat in MODELS) {
      if (cat.startsWith("_")) continue;
      const entries = MODELS[cat];
      if (!entries || typeof entries !== "object") continue;
      for (const mid in entries) {
        if (mid.startsWith("HD2_") && entries[mid] && typeof entries[mid] === "object") {
          idx[mid] = entries[mid];
        }
      }
    }
    return idx;
  }

  // engine.load — raw only; detect & refuse DRM / compressed
  function loadPreset(text) {
    const d = JSON.parse(text);
    if ("encoded_data" in d) {
      const enc = d.encryption;
      if (enc && enc.type && enc.type !== "none") {
        throw new Error("This is a DRM-protected (hxmp) commercial preset. "
          + "tonemaker only works on your own unencrypted exports.");
      }
      throw new Error("This is a compressed export. In POD Go Edit, re-export the "
        + "preset (uncompressed) and try again.");
    }
    if (!(d.data && d.data.tone && d.data.tone.dsp0)) {
      throw new Error("This doesn't look like a POD Go preset (no signal chain found).");
    }
    return d;
  }

  const toneOf = (d) => d.data.tone;
  const dsp0Of = (d) => d.data.tone.dsp0;

  function chain(d) {
    const g = dsp0Of(d), rows = [];
    for (const k in g) {
      const v = g[k];
      if (k.startsWith("block") && v && typeof v === "object") {
        const params = {};
        for (const pk in v) if (!pk.startsWith("@")) params[pk] = v[pk];
        rows.push({ position: v["@position"] ?? 99, key: k,
          model: v["@model"] || "(empty)", enabled: v["@enabled"], params });
      }
    }
    rows.sort((a, b) => a.position - b.position);
    return rows;
  }

  // validate.validate_doc
  function validateDoc(d) {
    const idx = buildIndex(), g = dsp0Of(d), tone = toneOf(d);
    const errors = [], warnings = [];
    const blocks = {};
    for (const k in g) if (k.startsWith("block") && g[k] && typeof g[k] === "object") blocks[k] = g[k];

    for (const k of Object.keys(blocks).sort()) {
      const v = blocks[k], keyIndex = parseInt(k.slice(5), 10);
      if (v["@position"] !== keyIndex) {
        errors.push(`${k}: @position ${v["@position"]} != block-key index ${keyIndex}`);
      }
      const model = v["@model"];
      if (model == null) continue;
      const info = idx[model];
      if (!info) {
        errors.push(`${k}: unknown @model "${model}" (not in verified library) — POD Go will reject the whole preset`);
        continue;
      }
      for (const ef of info.extra_fields || []) {
        if (!(ef in v)) errors.push(`${k}: model ${model} is missing required field ${ef}`);
      }
      const known = new Set(info.params || []);
      if (known.size) {
        for (const pk in v) if (!pk.startsWith("@") && !known.has(pk)) {
          warnings.push(`${k}: param "${pk}" not among known params for ${model}`);
        }
      }
    }
    const present = Object.keys(blocks).filter((k) => /^\d+$/.test(k.slice(5)))
      .map((k) => parseInt(k.slice(5), 10)).sort((a, b) => a - b);
    if (present.length) {
      const contiguous = present.every((n, i) => n === i);
      if (!contiguous) errors.push(`block positions not contiguous from 0: [${present}]`);
    }
    const cur = (tone.global && tone.global["@current_snapshot"]) || 0;
    const snap = tone["snapshot" + cur];
    if (snap && typeof snap === "object") {
      const sb = (snap.blocks && snap.blocks.dsp0) || {};
      for (const k in blocks) {
        const v = blocks[k];
        if (v["@model"] == null) continue;
        if (v["@enabled"] === true && sb[k] === false) {
          warnings.push(`${k}: enabled in dsp0 but OFF in active snapshot${cur} — it will sound bypassed`);
        }
      }
    }
    return { errors, warnings };
  }

  // build.build_from_spec
  function buildFromSpec(spec) {
    if (!BLOCKS._shell) throw new Error("missing block templates (blocks.json)");
    const doc = clone(BLOCKS._shell);
    doc.data.meta.name = spec.name;

    const dsp0 = { input: clone(BLOCKS._input || {}), output: clone(BLOCKS._output || {}) };
    for (const k in (spec.input || {})) dsp0.input[k] = spec.input[k];
    for (const k in (spec.output || {})) dsp0.output[k] = spec.output[k];

    for (const blk of spec.blocks) {
      const pos = blk.position, model = blk.model;
      if (!(model in BLOCKS)) {
        throw new Error(`model "${model}" has no template — pick a model that exists in the library`);
      }
      const body = clone(BLOCKS[model]);
      body["@position"] = pos;
      body["@enabled"] = blk.enabled === undefined ? true : !!blk.enabled;
      for (const pk in (blk.params || {})) body[pk] = blk.params[pk];
      dsp0["block" + pos] = body;
    }
    for (let i = 0; i < 10; i++) if (!("block" + i in dsp0)) dsp0["block" + i] = { "@position": i };

    const tone = {
      dsp0,
      global: { "@model": "@global_params", "@cursor_group": "block0",
        "@pedalstate": 2, "@current_snapshot": 0, "@tempo": 120 },
      footswitch: { dsp0: {} },
    };

    const snaps = spec.snapshots || [];
    const controlled = {};
    for (const s of snaps) for (const bk in (s.params || {})) for (const pk in s.params[bk]) {
      (controlled[bk + "|" + pk] = controlled[bk + "|" + pk] || []).push(s.params[bk][pk]);
    }
    if (snaps.length) {
      const s0 = snaps[0];
      for (const bk in (s0.params || {})) if (dsp0[bk] && typeof dsp0[bk] === "object") {
        for (const pk in s0.params[bk]) dsp0[bk][pk] = s0.params[bk][pk];
      }
      for (const bk in (s0.bypass || {})) {
        if (dsp0[bk] && typeof dsp0[bk] === "object" && "@model" in dsp0[bk]) dsp0[bk]["@enabled"] = !!s0.bypass[bk];
      }
    }
    const controller = { dsp0: {} };
    for (const key in controlled) {
      const [bk, pk] = key.split("|");
      const base = dsp0[bk] ? dsp0[bk][pk] : undefined;
      const nums = controlled[key].concat(typeof base === "number" ? [base] : []).filter((x) => typeof x === "number");
      const vals = nums.length ? nums : [0, 1];
      const lo = Math.min(0, ...vals), hi = Math.max(1, ...vals);
      (controller.dsp0[bk] = controller.dsp0[bk] || {})[pk] = { "@min": lo, "@max": hi, "@controller": 11 };
    }
    tone.controller = controller;

    const bypassMap = (overrides) => {
      const m = {};
      for (const key in dsp0) {
        const v = dsp0[key];
        if (key.startsWith("block") && v && typeof v === "object") m[key] = ("@model" in v) ? !!v["@enabled"] : false;
      }
      for (const bk in (overrides || {})) m[bk] = !!overrides[bk];
      return m;
    };

    for (let i = 0; i < 4; i++) {
      const sn = "snapshot" + i;
      if (i < snaps.length) {
        const s = snaps[i], ctrls = { dsp0: {} };
        for (const bk in (s.params || {})) for (const pk in s.params[bk]) {
          (ctrls.dsp0[bk] = ctrls.dsp0[bk] || {})[pk] = { "@fs_enabled": false, "@value": s.params[bk][pk] };
        }
        tone[sn] = { "@name": s.name || ("Snapshot " + (i + 1)), "@tempo": 120, "@valid": true,
          blocks: { dsp0: bypassMap(s.bypass) }, controllers: ctrls };
      } else {
        tone[sn] = { "@name": "Snapshot " + (i + 1), "@tempo": 120, "@valid": true,
          blocks: { dsp0: bypassMap(snaps.length ? snaps[0].bypass : null) },
          controllers: snaps.length ? clone(tone.snapshot0.controllers) : { dsp0: {} } };
      }
    }
    doc.data.tone = tone;
    return doc;
  }

  function buildAndValidate(spec) {
    const doc = buildFromSpec(spec);
    const { errors, warnings } = validateDoc(doc);
    return { doc, errors, warnings };
  }

  // Pull the first balanced {...} JSON object out of a possibly-chatty LLM reply.
  function extractSpec(text) {
    const t = text.trim();
    try { return JSON.parse(t); } catch (e) { /* fall through */ }
    const start = t.indexOf("{");
    if (start < 0) throw new Error("No JSON found. Paste the tone spec your AI gave you (the part in { }).");
    let depth = 0, inStr = false, esc = false;
    for (let i = start; i < t.length; i++) {
      const c = t[i];
      if (inStr) { if (esc) esc = false; else if (c === "\\") esc = true; else if (c === '"') inStr = false; }
      else if (c === '"') inStr = true;
      else if (c === "{") depth++;
      else if (c === "}") { depth--; if (depth === 0) return JSON.parse(t.slice(start, i + 1)); }
    }
    throw new Error("Couldn't read the JSON. Make sure you copied the whole { ... } block.");
  }

  const presetToText = (doc) => JSON.stringify(doc);

  global.TM = { setData, buildIndex, loadPreset, chain, validateDoc,
    buildFromSpec, buildAndValidate, extractSpec, presetToText, toneOf, dsp0Of };
})(typeof window !== "undefined" ? window : globalThis);

if (typeof module !== "undefined" && module.exports) module.exports = globalThis.TM;
