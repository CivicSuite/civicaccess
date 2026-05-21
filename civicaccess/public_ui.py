"""Static public UI for CivicAccess v1.0.0."""

from __future__ import annotations


def render_public_lookup_page() -> str:
    """Render the accessible public-facing CivicAccess page."""

    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CivicAccess Public Accessibility Support</title>
<style>
  :root { --ink:#17202a; --muted:#56606a; --paper:#fffdf7; --blue:#175b83; --green:#2f6b50; --gold:#d8b45b; --line:#d7c8a8; --danger:#9a3d2f; }
  * { box-sizing: border-box; }
  body { margin:0; color:var(--ink); font-family:"Aptos","Segoe UI",sans-serif; background:#f7f1e6; }
  .skip-link { position:absolute; left:1rem; top:-4rem; background:var(--ink); color:white; padding:.7rem 1rem; border-radius:4px; z-index:10; }
  .skip-link:focus { top:1rem; }
  header, main, footer { width:min(1120px, calc(100% - 32px)); margin:0 auto; }
  header { padding:44px 0 22px; }
  .eyebrow { color:var(--blue); text-transform:uppercase; font-weight:800; font-size:.8rem; }
  h1 { max-width:920px; margin:0; font-family:Georgia,"Times New Roman",serif; font-size:clamp(2.4rem,7vw,4.8rem); line-height:1; }
  .lede { max-width:820px; font-size:clamp(1.05rem,2.2vw,1.35rem); line-height:1.55; color:#31404a; }
  .badge { display:inline-block; padding:.45rem .75rem; border-radius:4px; background:var(--green); color:white; font-weight:900; }
  .grid { display:grid; grid-template-columns:repeat(12,1fr); gap:16px; }
  .panel { grid-column:span 6; min-width:0; padding:22px; border:1px solid var(--line); border-radius:8px; background:rgba(255,253,247,.94); }
  .panel.large { grid-column:span 12; }
  h2,h3 { font-family:Georgia,"Times New Roman",serif; }
  h2 { margin:0 0 14px; font-size:clamp(1.45rem,3vw,2.3rem); }
  p, li { line-height:1.6; }
  label { display:block; margin:.8rem 0 .35rem; font-weight:800; }
  textarea, input, select, button { width:100%; border:1px solid #9fb0b8; border-radius:6px; padding:.8rem 1rem; font:inherit; }
  textarea, input, select { background:#f3f7f8; color:var(--ink); }
  button { width:fit-content; min-width:180px; margin-top:1rem; border:0; background:var(--blue); color:white; font-weight:900; cursor:pointer; }
  button:hover { background:#104462; }
  button:disabled { background:#6d7b83; cursor:not-allowed; }
  .result { margin-top:18px; padding:16px; border-left:6px solid var(--green); border-radius:6px; background:white; }
  .result.warning { border-left-color:var(--danger); background:#fff8f4; }
  .result.pending { border-left-color:var(--gold); }
  .kicker { color:var(--muted); font-size:.86rem; font-weight:900; text-transform:uppercase; }
  .notice { margin:24px 0 0; padding:18px; border:1px dashed var(--danger); border-radius:8px; background:rgba(154,61,47,.10); }
  .stack { display:grid; gap:12px; }
  footer { padding:38px 0 56px; color:var(--muted); }
  :focus-visible { outline:4px solid var(--gold); outline-offset:3px; }
  @media (max-width:760px) { header{padding-top:34px}.panel{grid-column:span 12;padding:18px}button{width:100%} }
</style>
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<header>
  <p class="eyebrow">CivicSuite / CivicAccess</p>
  <h1>Make public information easier to read, reach, and preserve.</h1>
  <p class="lede">CivicAccess gives staff a deterministic review path for accessible forms, public notices, plain-language rewrites, multilingual samples, ADA Title II review support, tagged-PDF expectations, and municipal-record exports.</p>
  <p><span class="badge">v1.0.0 public-use support release</span></p>
</header>
<main id="main" tabindex="-1">
  <section class="grid" aria-labelledby="review-title">
    <article class="panel large">
      <p class="kicker">Accessibility review</p>
      <h2 id="review-title">Public notice check</h2>
      <label for="title">Notice title</label>
      <input id="title" value="Water shutoff notice">
      <label for="notice">Notice text</label>
      <textarea id="notice" rows="5">Pursuant to municipal code, residents must remit payment prior to the deadline.</textarea>
      <label><input id="altText" type="checkbox" style="width:auto"> Images already have alt text</label>
      <button id="runReview" type="button">Run review</button>
      <button id="showEmpty" type="button">Show empty state</button>
      <button id="showError" type="button">Show error state</button>
      <div id="reviewResult" class="result pending" role="status" aria-live="polite">
        <h3>Partial review pending</h3>
        <p>Add or confirm the notice fields, then run the review. CivicAccess will show actionable fixes before staff publication review.</p>
      </div>
    </article>
    <article class="panel">
      <p class="kicker">Accessible forms</p>
      <h2>Form publication plan</h2>
      <div class="result"><p>Required fields: name, contact, and request. Errors must stay next to the field they describe.</p></div>
    </article>
    <article class="panel">
      <p class="kicker">Plain language</p>
      <h2>Replace jargon</h2>
      <div class="result"><p><strong>Before:</strong> remit payment prior to the deadline.</p><p><strong>After:</strong> pay before the deadline.</p></div>
    </article>
    <article class="panel">
      <p class="kicker">Multilingual support</p>
      <h2>Human-reviewed variants</h2>
      <div class="result"><p>Spanish and Vietnamese samples are marked as draft variants that need qualified human review before publication.</p></div>
    </article>
    <article class="panel">
      <p class="kicker">Tagged PDF</p>
      <h2>Heading expectations</h2>
      <div class="result"><p>PDF packages must start with one H1, keep heading levels in order, and verify tags before publication.</p></div>
    </article>
    <article class="panel">
      <p class="kicker">Records export</p>
      <h2>Keep provenance</h2>
      <div class="result"><p>Exports preserve source text, rewritten text, reviewer, checklist, and publication context for records requests.</p></div>
    </article>
    <article class="panel">
      <p class="kicker">ADA boundary</p>
      <h2>Support, not certification</h2>
      <div class="result warning"><p>CivicAccess does not provide legal advice, certified ADA compliance, official translation certification, or final publication approval. ADA coordinators and qualified reviewers remain responsible for official decisions.</p></div>
    </article>
  </section>
  <section class="notice" aria-labelledby="boundary-title">
    <h2 id="boundary-title">Publication boundary</h2>
    <p>Every output is advisory support. Staff must review fixes, translation drafts, ADA Title II notes, and export packages before publication.</p>
  </section>
</main>
<footer><p>CivicAccess is part of the Apache 2.0 CivicSuite open-source municipal AI project.</p></footer>
<script>
  const result = document.getElementById("reviewResult");
  const title = document.getElementById("title");
  const notice = document.getElementById("notice");
  const altText = document.getElementById("altText");
  const runReview = document.getElementById("runReview");
  const showEmpty = document.getElementById("showEmpty");
  const showError = document.getElementById("showError");

  function setResult(kind, heading, body, items) {
    result.className = "result" + (kind ? " " + kind : "");
    const list = items && items.length ? "<ul>" + items.map((item) => "<li>" + item + "</li>").join("") + "</ul>" : "";
    result.innerHTML = "<h3>" + heading + "</h3><p>" + body + "</p>" + list;
  }

  runReview.addEventListener("click", () => {
    setResult("pending", "Loading review", "Checking the notice text and publication fields.", []);
    window.setTimeout(() => {
      const fixes = [];
      if (!title.value.trim()) fixes.push("Add a short title that names the service, deadline, or public action.");
      if (!notice.value.trim()) fixes.push("Add the resident-facing notice text before publication review.");
      if (!altText.checked) fixes.push("Add alt text for non-decorative images or mark decorative images as decorative.");
      fixes.push("Add a plain-language summary and preserve the source text with the record.");
      if (fixes.length > 1) {
        setResult("warning", "Needs fixes", "Resolve these items before staff publication approval.", fixes);
      } else {
        setResult("", "Sample checks passed", "Staff review is still required before publication.", fixes);
      }
    }, 250);
  });

  showEmpty.addEventListener("click", () => {
    title.value = "";
    notice.value = "";
    altText.checked = false;
    setResult("warning", "No notice text yet", "Add a title, resident-facing notice text, and image context before running the review.", []);
  });

  showError.addEventListener("click", () => {
    setResult("warning", "Review could not finish", "Check that the notice text is present, then run the review again. If this happens in the installed stack, staff should check the CivicAccess service health endpoint.", []);
  });
</script>
</body>
</html>
"""
