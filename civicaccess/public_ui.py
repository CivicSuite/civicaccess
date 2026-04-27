"""Static public UI shell for CivicAccess v0.1.0."""

from __future__ import annotations


def render_public_lookup_page() -> str:
    """Render the accessible public-facing CivicAccess sample page."""

    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CivicAccess Public Accessibility Review</title>
<style>
  :root { --ink:#17202a; --muted:#56606a; --paper:#fffdf7; --blue:#175b83; --green:#2f6b50; --gold:#d8b45b; --line:#d7c8a8; }
  * { box-sizing: border-box; }
  body { margin:0; color:var(--ink); font-family:"Aptos","Segoe UI",sans-serif; background:linear-gradient(135deg,#f7f1e6,#eef6f8); }
  .skip-link { position:absolute; left:1rem; top:-4rem; background:var(--ink); color:white; padding:.7rem 1rem; border-radius:999px; }
  .skip-link:focus { top:1rem; }
  header, main, footer { width:min(1120px, calc(100% - 32px)); margin:0 auto; }
  header { padding:48px 0 24px; }
  .eyebrow { color:var(--blue); text-transform:uppercase; letter-spacing:.18em; font-weight:800; font-size:.78rem; }
  h1 { max-width:920px; margin:0; font-family:Georgia,"Times New Roman",serif; font-size:clamp(2.8rem,8vw,6rem); line-height:.92; letter-spacing:-.05em; }
  .lede { max-width:820px; font-size:clamp(1.1rem,2.4vw,1.45rem); line-height:1.55; color:#31404a; }
  .badge { display:inline-flex; width:fit-content; padding:.45rem .75rem; border-radius:999px; background:var(--green); color:white; font-weight:900; }
  .grid { display:grid; grid-template-columns:repeat(12,1fr); gap:18px; }
  .card { grid-column:span 6; min-width:0; padding:24px; border:1px solid var(--line); border-radius:28px; background:rgba(255,253,247,.9); box-shadow:0 18px 40px rgba(35,43,50,.10); }
  .card.large { grid-column:span 12; }
  h2,h3 { font-family:Georgia,"Times New Roman",serif; letter-spacing:-.03em; }
  h2 { margin:0 0 14px; font-size:clamp(1.8rem,4vw,3rem); }
  p, li { line-height:1.65; }
  label { font-weight:800; }
  textarea, input, button { width:100%; border:1px solid #b9c6cc; border-radius:16px; padding:.85rem 1rem; font:inherit; }
  textarea, input { background:#f3f7f8; color:var(--ink); }
  button { width:fit-content; min-width:190px; border:0; background:var(--blue); color:white; font-weight:900; cursor:default; }
  .result { margin-top:18px; padding:18px; border-left:6px solid var(--green); border-radius:18px; background:white; }
  .warning { border-left-color:#b2603f; background:#fff8f4; }
  .kicker { color:var(--muted); font-size:.86rem; font-weight:900; letter-spacing:.08em; text-transform:uppercase; }
  .notice { margin:24px 0 0; padding:18px; border:1px dashed #b2603f; border-radius:22px; background:rgba(178,96,63,.10); }
  footer { padding:38px 0 56px; color:var(--muted); }
  :focus-visible { outline:4px solid var(--gold); outline-offset:3px; }
  @media (max-width:760px) { header{padding-top:34px}.card{grid-column:span 12;padding:20px;border-radius:22px}button{width:100%} }
</style>
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<header>
  <p class="eyebrow">CivicSuite / CivicAccess public sample</p>
  <h1>Make public information easier to read, reach, and preserve.</h1>
  <p class="lede">CivicAccess demonstrates the suite-wide accessibility layer: review public copy, surface WCAG-aligned fixes, create plain-language and multilingual samples, and preserve records-ready export context.</p>
  <p><span class="badge">v0.1.0 accessibility foundation</span></p>
</header>
<main id="main" tabindex="-1">
  <section class="grid" aria-labelledby="review-title">
    <article class="card large">
      <p class="kicker">Sample accessibility review</p>
      <h2 id="review-title">Public notice check</h2>
      <label for="notice">Sample notice text</label>
      <textarea id="notice" rows="4">Pursuant to municipal code, residents must remit payment prior to the deadline.</textarea>
      <button type="button">Run sample review</button>
      <div class="result" role="status" aria-live="polite">
        <h3>Needs fixes</h3>
        <ul>
          <li>Add descriptive title metadata.</li>
          <li>Add alt text for non-decorative images.</li>
          <li>Provide a plain-language summary before detailed instructions.</li>
        </ul>
      </div>
    </article>
    <article class="card">
      <p class="kicker">Plain language</p>
      <h2>Replace jargon</h2>
      <div class="result"><p><strong>Before:</strong> remit payment prior to the deadline.</p><p><strong>After:</strong> pay before the deadline.</p></div>
    </article>
    <article class="card">
      <p class="kicker">Multilingual support</p>
      <h2>Human-reviewed variants</h2>
      <div class="result"><p>Sample Spanish and Vietnamese variants are marked as requiring human review before publication.</p></div>
    </article>
    <article class="card">
      <p class="kicker">Records-ready export</p>
      <h2>Keep provenance</h2>
      <div class="result"><p>Exports preserve source text, rewritten text, reviewer, checklist, and publication context for records requests.</p></div>
    </article>
    <article class="card">
      <p class="kicker">ADA boundary</p>
      <h2>Support, not certification</h2>
      <div class="result warning"><p>CivicAccess does not provide legal advice, certified ADA compliance, or final publication approval. ADA coordinators and qualified reviewers remain responsible for official decisions.</p></div>
    </article>
  </section>
  <section class="notice" aria-labelledby="boundary-title">
    <h2 id="boundary-title">Important boundaries</h2>
    <p>This foundation release does not ship live LLM calls, certified accessibility audits, production translation workflows, document ingestion, or suite-wide integration APIs.</p>
  </section>
</main>
<footer><p>CivicAccess is part of the Apache 2.0 CivicSuite open-source municipal AI project.</p></footer>
</body>
</html>
"""
