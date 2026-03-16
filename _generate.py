#!/usr/bin/env python3
"""Generate all EchoDepth Defence HTML pages."""

import sys, os
sys.path.insert(0, '/home/claude/vercel-site')
from _shared import page, trust_bar, footer, js, CSS, FONTS, nav

import json

ORG_SCHEMA = json.dumps({
  "@context":"https://schema.org",
  "@type":"Organization",
  "name":"EchoDepth Defence",
  "url":"https://echodefence.co.uk",
  "description":"Camera-based facial Action Unit analysis for defence, intelligence, and security. Emotional AI for critical environments.",
  "parentOrganization":{"@type":"Organization","name":"Cavefish AI","url":"https://cavefish.co.uk"},
  "address":{"@type":"PostalAddress","addressLocality":"Cardiff","addressCountry":"GB"},
  "areaServed":"GB",
  "knowsAbout":["deception detection","credibility assessment","insider threat","polygraph alternative","facial emotion recognition","operator fatigue monitoring"]
})

TICKER_HTML = """
<div style="background:rgba(224,59,59,0.08);border-top:1px solid rgba(224,59,59,.2);border-bottom:1px solid rgba(224,59,59,.2);padding:10px 0;overflow:hidden;" aria-hidden="true">
  <div style="display:flex;gap:4rem;animation:ticker 30s linear infinite;white-space:nowrap;">
    <span style="display:flex;align-items:center;gap:10px;font-family:'DM Mono',monospace;font-size:.63rem;letter-spacing:.1em;color:#637A96;"><span style="width:5px;height:5px;border-radius:50%;background:#E03B3B;display:inline-block;flex-shrink:0"></span>INSIDER THREAT ACCOUNTS FOR 60% OF DATA BREACHES</span>
    <span style="display:flex;align-items:center;gap:10px;font-family:'DM Mono',monospace;font-size:.63rem;letter-spacing:.1em;color:#637A96;"><span style="width:5px;height:5px;border-radius:50%;background:#E03B3B;display:inline-block;flex-shrink:0"></span>POLYGRAPH ACCURACY DISPUTED — NO SCIENTIFIC CONSENSUS (NAS 2003)</span>
    <span style="display:flex;align-items:center;gap:10px;font-family:'DM Mono',monospace;font-size:.63rem;letter-spacing:.1em;color:#637A96;"><span style="width:5px;height:5px;border-radius:50%;background:#E03B3B;display:inline-block;flex-shrink:0"></span>OPERATOR FATIGUE IMPLICATED IN 40% OF CRITICAL INCIDENTS</span>
    <span style="display:flex;align-items:center;gap:10px;font-family:'DM Mono',monospace;font-size:.63rem;letter-spacing:.1em;color:#637A96;"><span style="width:5px;height:5px;border-radius:50%;background:#E03B3B;display:inline-block;flex-shrink:0"></span>US DOD 2023: CAMERA-BASED PHYSIOLOGICAL SENSING IS THE TARGET FUTURE FOR CREDIBILITY ASSESSMENT</span>
    <span style="display:flex;align-items:center;gap:10px;font-family:'DM Mono',monospace;font-size:.63rem;letter-spacing:.1em;color:#637A96;"><span style="width:5px;height:5px;border-radius:50%;background:#E03B3B;display:inline-block;flex-shrink:0"></span>74% OF COMPLIANCE FAILURES STEM FROM POOR KNOWLEDGE RETENTION</span>
    <span style="display:flex;align-items:center;gap:10px;font-family:'DM Mono',monospace;font-size:.63rem;letter-spacing:.1em;color:#637A96;"><span style="width:5px;height:5px;border-radius:50%;background:#E03B3B;display:inline-block;flex-shrink:0"></span>INSIDER THREAT ACCOUNTS FOR 60% OF DATA BREACHES</span>
    <span style="display:flex;align-items:center;gap:10px;font-family:'DM Mono',monospace;font-size:.63rem;letter-spacing:.1em;color:#637A96;"><span style="width:5px;height:5px;border-radius:50%;background:#E03B3B;display:inline-block;flex-shrink:0"></span>POLYGRAPH ACCURACY DISPUTED — NO SCIENTIFIC CONSENSUS (NAS 2003)</span>
    <span style="display:flex;align-items:center;gap:10px;font-family:'DM Mono',monospace;font-size:.63rem;letter-spacing:.1em;color:#637A96;"><span style="width:5px;height:5px;border-radius:50%;background:#E03B3B;display:inline-block;flex-shrink:0"></span>OPERATOR FATIGUE IMPLICATED IN 40% OF CRITICAL INCIDENTS</span>
    <span style="display:flex;align-items:center;gap:10px;font-family:'DM Mono',monospace;font-size:.63rem;letter-spacing:.1em;color:#637A96;"><span style="width:5px;height:5px;border-radius:50%;background:#E03B3B;display:inline-block;flex-shrink:0"></span>US DOD 2023: CAMERA-BASED PHYSIOLOGICAL SENSING IS THE TARGET FUTURE FOR CREDIBILITY ASSESSMENT</span>
    <span style="display:flex;align-items:center;gap:10px;font-family:'DM Mono',monospace;font-size:.63rem;letter-spacing:.1em;color:#637A96;"><span style="width:5px;height:5px;border-radius:50%;background:#E03B3B;display:inline-block;flex-shrink:0"></span>74% OF COMPLIANCE FAILURES STEM FROM POOR KNOWLEDGE RETENTION</span>
  </div>
</div>
<style>@keyframes ticker{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}</style>"""

CTA_BLOCK = """
<section class="cta-section">
  <div class="cta-inner">
    <div class="cta-eyebrow"><span class="label" style="margin:0">Briefings Available</span></div>
    <h2>See What Your Security Stack <span style="color:var(--teal)">Is Missing.</span></h2>
    <p class="sub">Structured technical briefings for defence procurement, security leadership, and intelligence teams. NDA available. Air-gapped demo environment on request.</p>
    <div class="cta-actions">
      <a href="/contact/" class="btn-primary btn-large">Request a Classified Briefing</a>
      <a href="/technology/" class="btn-ghost btn-large">How It Works</a>
    </div>
    <p style="font-family:'DM Mono',monospace;font-size:.6rem;color:#3A506A;margin-top:2.5rem;letter-spacing:.1em;">CONTACT: DEFENCE@CAVEFISH.CO.UK &nbsp;&middot;&nbsp; CARDIFF, WALES &nbsp;&middot;&nbsp; UK DATA RESIDENCY STANDARD</p>
  </div>
</section>"""


# ─────────────────────────────────────────────
# 1. INDEX / HOMEPAGE
# ─────────────────────────────────────────────
HOMEPAGE_SCHEMA = json.dumps({
  "@context":"https://schema.org",
  "@type":"WebPage",
  "name":"EchoDepth Defence — Emotional Intelligence for Critical Environments",
  "description":"Camera-based facial Action Unit analysis detecting stress, deception, fatigue, and cognitive readiness. A scientifically grounded polygraph alternative for defence, intelligence, and security.",
  "url":"https://echodefence.co.uk/",
  "breadcrumb":{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://echodefence.co.uk/"}]},
  "publisher":{"@type":"Organization","name":"EchoDepth Defence / Cavefish AI","url":"https://echodefence.co.uk"}
})

HOMEPAGE_BODY = f"""
<!-- HERO -->
<section id="hero" style="min-height:100vh;display:grid;grid-template-columns:1fr 1fr;padding-top:68px;position:relative;overflow:hidden;">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse 60% 60% at 70% 50%,rgba(0,212,180,.05) 0%,transparent 70%),radial-gradient(ellipse 40% 40% at 20% 80%,rgba(240,165,0,.03) 0%,transparent 60%);"></div>
  <div style="position:absolute;inset:0;background-image:linear-gradient(rgba(28,46,74,.35) 1px,transparent 1px),linear-gradient(90deg,rgba(28,46,74,.35) 1px,transparent 1px);background-size:60px 60px;mask-image:radial-gradient(ellipse 80% 80% at 50% 50%,black 20%,transparent 80%);"></div>
  <div style="display:flex;flex-direction:column;justify-content:center;padding:5rem 4rem 5rem 5rem;position:relative;z-index:2;">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:1.8rem;">
      <span style="width:32px;height:1px;background:var(--teal);"></span>
      <span class="label" style="margin:0">Cavefish AI &middot; EchoDepth Defence</span>
    </div>
    <h1 style="font-size:clamp(3rem,5vw,5.2rem);line-height:.95;margin-bottom:1.4rem;">
      THE HUMAN<br>
      <span style="color:var(--teal)">THREAT VECTOR</span><br>
      <span style="font-style:italic;color:var(--grey-2);font-weight:300;font-family:var(--font-body);font-size:.44em;display:block;margin:.4em 0;letter-spacing:.04em;">has always been the one you couldn't measure</span>
    </h1>
    <p style="font-size:1.02rem;color:var(--grey-1);max-width:480px;margin-bottom:2.5rem;line-height:1.78;">EchoDepth analyses facial Action Units in real time — detecting stress, deception, cognitive overload, and emotional readiness with no wearables, no contact, no disruption to workflow.</p>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;">
      <a href="/contact/" class="btn-primary btn-large">Request Classified Briefing</a>
      <a href="/technology/" class="btn-ghost btn-large">How It Works</a>
    </div>
    <div style="display:flex;gap:2.5rem;margin-top:3.5rem;padding-top:2.5rem;border-top:1px solid var(--border);flex-wrap:wrap;">
      <div><span style="font-family:var(--font-display);font-size:1.9rem;font-weight:700;color:var(--teal);display:block;">~700ms</span><span style="font-size:.7rem;color:var(--grey-2);font-family:var(--font-condensed);letter-spacing:.1em;text-transform:uppercase;">Detection latency</span></div>
      <div><span style="font-family:var(--font-display);font-size:1.9rem;font-weight:700;color:var(--teal);display:block;">43+</span><span style="font-size:.7rem;color:var(--grey-2);font-family:var(--font-condensed);letter-spacing:.1em;text-transform:uppercase;">Action Units tracked</span></div>
      <div><span style="font-family:var(--font-display);font-size:1.9rem;font-weight:700;color:var(--teal);display:block;">Zero</span><span style="font-size:.7rem;color:var(--grey-2);font-family:var(--font-condensed);letter-spacing:.1em;text-transform:uppercase;">Contact required</span></div>
    </div>
  </div>
  <div style="display:flex;align-items:center;justify-content:center;position:relative;z-index:2;padding:2rem;">
    <div style="position:relative;width:360px;max-width:100%;">
      <svg viewBox="0 0 360 440" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;" role="img" aria-label="Facial Action Unit analysis visualisation">
        <path d="M34 34 L34 8 L8 8 L8 34" stroke="#00D4B4" stroke-width="1.5"/><path d="M326 34 L326 8 L352 8 L352 34" stroke="#00D4B4" stroke-width="1.5"/>
        <path d="M34 406 L34 432 L8 432 L8 406" stroke="#00D4B4" stroke-width="1.5"/><path d="M326 406 L326 432 L352 432 L352 406" stroke="#00D4B4" stroke-width="1.5"/>
        <ellipse cx="180" cy="220" rx="105" ry="135" stroke="#1C2E4A" stroke-width="1" stroke-dasharray="4 3"/>
        <ellipse cx="140" cy="188" rx="24" ry="14" stroke="#2A4570" stroke-width="1"/>
        <ellipse cx="220" cy="188" rx="24" ry="14" stroke="#2A4570" stroke-width="1"/>
        <circle cx="140" cy="188" r="7" stroke="#00D4B4" stroke-width=".75" opacity=".6"/>
        <circle cx="220" cy="188" r="7" stroke="#00D4B4" stroke-width=".75" opacity=".6"/>
        <circle cx="140" cy="188" r="2.5" fill="#00D4B4" opacity=".8"/>
        <circle cx="220" cy="188" r="2.5" fill="#00D4B4" opacity=".8"/>
        <path d="M180 200 L168 240 M180 200 L192 240 M166 242 Q180 250 194 242" stroke="#1C2E4A" stroke-width=".75" opacity=".6"/>
        <path d="M148 280 Q180 305 212 280" stroke="#2A4570" stroke-width="1"/>
        <line x1="180" y1="85" x2="180" y2="355" stroke="#1C2E4A" stroke-width=".5" opacity=".25"/>
        <line x1="75" y1="220" x2="285" y2="220" stroke="#1C2E4A" stroke-width=".5" opacity=".25"/>
        <rect x="75" y="85" width="210" height="270" stroke="#00D4B4" stroke-width=".5" opacity=".1"/>
        <line x1="42" y1="130" x2="68" y2="130" stroke="#3A506A" stroke-width=".5"/>
        <line x1="42" y1="330" x2="68" y2="330" stroke="#3A506A" stroke-width=".5"/>
        <line x1="42" y1="130" x2="42" y2="330" stroke="#3A506A" stroke-width=".5"/>
      </svg>
      <!-- Animated scan line -->
      <div style="position:absolute;left:10%;right:10%;height:2px;background:linear-gradient(90deg,transparent,var(--teal),transparent);animation:scanDown 3s ease-in-out infinite;opacity:.65;" id="scanLine"></div>
      <!-- Data readout -->
      <div style="position:absolute;right:-30px;top:50%;transform:translateY(-50%);background:rgba(8,13,24,.95);border:1px solid var(--border);border-left:2px solid var(--teal);padding:14px 16px;width:160px;">
        <div style="font-family:'DM Mono',monospace;font-size:.53rem;color:var(--teal);letter-spacing:.15em;text-transform:uppercase;margin-bottom:10px;">// ECHOCORE</div>
        <div style="display:flex;justify-content:space-between;padding:3px 0;border-bottom:1px solid rgba(28,46,74,.5);font-size:.62rem;"><span style="color:var(--grey-2);font-family:var(--font-condensed);">VALENCE</span><span style="font-family:'DM Mono',monospace;color:var(--amber)" id="rVal">−0.47</span></div>
        <div style="display:flex;justify-content:space-between;padding:3px 0;border-bottom:1px solid rgba(28,46,74,.5);font-size:.62rem;"><span style="color:var(--grey-2);font-family:var(--font-condensed);">AROUSAL</span><span style="font-family:'DM Mono',monospace;color:var(--red)" id="rAro">+0.83</span></div>
        <div style="display:flex;justify-content:space-between;padding:3px 0;border-bottom:1px solid rgba(28,46,74,.5);font-size:.62rem;"><span style="color:var(--grey-2);font-family:var(--font-condensed);">DOMINANCE</span><span style="font-family:'DM Mono',monospace;color:var(--teal)">+0.12</span></div>
        <div style="display:flex;justify-content:space-between;padding:3px 0;border-bottom:1px solid rgba(28,46,74,.5);font-size:.62rem;"><span style="color:var(--grey-2);font-family:var(--font-condensed);">DECEPTION</span><span style="font-family:'DM Mono',monospace;color:var(--red)">HIGH</span></div>
        <div style="display:flex;justify-content:space-between;padding:3px 0;font-size:.62rem;"><span style="color:var(--grey-2);font-family:var(--font-condensed);">READINESS</span><span style="font-family:'DM Mono',monospace;color:var(--teal)" id="rRdy">67%</span></div>
      </div>
    </div>
  </div>
</section>
<style>
@keyframes scanDown{{0%{{top:10%;opacity:0}}10%{{opacity:.65}}90%{{opacity:.65}}100%{{top:85%;opacity:0}}}}
#scanLine{{position:absolute;left:10%;right:10%;height:2px;background:linear-gradient(90deg,transparent,var(--teal),transparent);animation:scanDown 3s ease-in-out infinite;opacity:.65;}}
@media(max-width:900px){{#hero{{grid-template-columns:1fr!important;}} #hero > div:last-child{{display:none;}} }}
</style>

{TICKER_HTML}

<!-- PROBLEM -->
<section style="background:var(--deep);border-top:1px solid var(--border);">
  <div class="section-inner">
    <div class="section-header fade-up">
      <span class="label red">The Gap In Your Security Stack</span>
      <h2>Every defence system monitors everything<br>except <span style="color:var(--teal)">the human.</span></h2>
    </div>
    <div class="card-grid-2 fade-up d1">
      <div class="card" style="border-left:0;"><div style="--after-color:var(--red)"></div>
        <span class="label red">Insider Threat</span><h3>You Cannot Vet What You Cannot See</h3>
        <p>Security clearances and annual reviews catch nothing in real time. Stress indicators, behavioural anomalies, and emotional changes that precede incidents go entirely undetected by existing TSCM and access control infrastructure.</p>
        <p style="font-family:'DM Mono',monospace;font-size:.63rem;color:var(--amber);margin-top:1rem;">// COST PER INSIDER INCIDENT: £3.2M AVERAGE (PONEMON 2024)</p>
      </div>
      <div class="card">
        <span class="label amber">Compliance Training</span><h3>Tick-Box Training Doesn't Build Readiness</h3>
        <p>Mandatory training completion rates mean nothing if personnel are disengaged, overwhelmed, or not retaining critical information. You have no measure of whether training is landing — until it doesn't matter.</p>
        <p style="font-family:'DM Mono',monospace;font-size:.63rem;color:var(--amber);margin-top:1rem;">// 74% OF COMPLIANCE FAILURES STEM FROM POOR KNOWLEDGE RETENTION</p>
      </div>
      <div class="card">
        <span class="label red">Operator Fatigue</span><h3>Fatigued Operators Make Critical Errors</h3>
        <p>Drone pilots, SOC analysts, control room operators, and intelligence reviewers face sustained cognitive load with no real-time monitoring of readiness. Fatigue and overload are invisible until an incident occurs.</p>
        <p style="font-family:'DM Mono',monospace;font-size:.63rem;color:var(--amber);margin-top:1rem;">// FATIGUE FACTOR IN 23% OF MILITARY NEAR-MISSES (NATO REVIEW)</p>
      </div>
      <div class="card">
        <span class="label">Deception Detection</span><h3>Polygraph Is Pseudoscience. You Know It.</h3>
        <p>Courts, procurement officers, and security professionals are aware that polygraph lacks scientific validity. Border screening, interview assessment, and source credibility require a defensible, evidence-based alternative.</p>
        <p style="font-family:'DM Mono',monospace;font-size:.63rem;color:var(--amber);margin-top:1rem;">// POLYGRAPH FALSE NEGATIVE RATE: UP TO 47% IN CONTROLLED STUDIES</p>
      </div>
    </div>
  </div>
</section>

<!-- SOLUTIONS OVERVIEW -->
<section style="background:var(--void);">
  <div class="section-inner">
    <div class="section-header fade-up">
      <span class="label">EchoDepth Solution Areas</span>
      <h2>Four Vectors.<br>One Engine.</h2>
    </div>
    <div class="card-grid-2 fade-up d1">
      <a href="/solutions/compliance/" style="text-decoration:none;" class="card">
        <span class="label">01 &middot; Compliance &amp; Training</span>
        <h3>Know if Training is Actually Landing</h3>
        <p>Real-time engagement and comprehension scoring during mandatory training modules. DSAT-compatible audit records. LMS integration.</p>
        <span style="font-family:var(--font-condensed);font-size:.72rem;letter-spacing:.1em;color:var(--teal);margin-top:1.2rem;display:inline-block;">Explore Solution ▸</span>
      </a>
      <a href="/solutions/insider-threat/" style="text-decoration:none;" class="card">
        <span class="label amber">02 &middot; Insider Threat &amp; Vetting</span>
        <h3>Continuous Emotional Anomaly Monitoring</h3>
        <p>Behavioural baseline profiling per individual. Anomaly scoring. SIEM integration. Earlier signal, earlier intervention.</p>
        <span style="font-family:var(--font-condensed);font-size:.72rem;letter-spacing:.1em;color:var(--amber);margin-top:1.2rem;display:inline-block;">Explore Solution ▸</span>
      </a>
      <a href="/solutions/operator-readiness/" style="text-decoration:none;" class="card">
        <span class="label">03 &middot; Operator Readiness</span>
        <h3>Quantify Human Readiness. Live.</h3>
        <p>Pre-mission readiness scoring, live fatigue monitoring, and post-incident timeline reconstruction for UAS, SOC, and control room operators.</p>
        <span style="font-family:var(--font-condensed);font-size:.72rem;letter-spacing:.1em;color:var(--teal);margin-top:1.2rem;display:inline-block;">Explore Solution ▸</span>
      </a>
      <a href="/solutions/deception-detection/" style="text-decoration:none;" class="card">
        <span class="label red">04 &middot; Deception Detection</span>
        <h3>A Defensible Alternative to Polygraph</h3>
        <p>43 FACS-compliant Action Units. Timestamped per-question stress mapping. Structured analytical output for intelligence and legal review.</p>
        <span style="font-family:var(--font-condensed);font-size:.72rem;letter-spacing:.1em;color:var(--red);margin-top:1.2rem;display:inline-block;">Explore Solution ▸</span>
      </a>
    </div>
  </div>
</section>

<!-- TECH SNAPSHOT -->
<section style="background:var(--deep);border-top:1px solid var(--border);">
  <div class="section-inner">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:center;" class="fade-up">
      <div>
        <span class="label">The EchoDepth Engine</span>
        <h2 style="margin-bottom:1.2rem;">Facial Action Units.<br><span style="color:var(--teal)">Decoded at Scale.</span></h2>
        <p style="color:var(--grey-1);margin-bottom:1.5rem;">Standard RGB camera. 68-point facial landmark detection. 43 FACS-compliant Action Units extracted per frame. VAD mapping. REST API or on-premise deployment. Works with your existing camera infrastructure — no specialist hardware.</p>
        <a href="/technology/" class="btn-ghost">Full Technical Overview</a>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--border);border:1px solid var(--border);">
        <div style="background:var(--panel);padding:1.5rem;"><span style="font-size:1.3rem;display:block;margin-bottom:.7rem;">🔒</span><strong style="font-size:.9rem;display:block;margin-bottom:.4rem;">Air-Gap Ready</strong><p style="font-size:.78rem;color:var(--grey-2);">Full on-premise deployment. SCIF-compatible. Zero external data transmission.</p></div>
        <div style="background:var(--panel);padding:1.5rem;"><span style="font-size:1.3rem;display:block;margin-bottom:.7rem;">⚡</span><strong style="font-size:.9rem;display:block;margin-bottom:.4rem;">~700ms Latency</strong><p style="font-size:.78rem;color:var(--grey-2);">Sub-second emotional state output. Suitable for live interview and real-time alerting.</p></div>
        <div style="background:var(--panel);padding:1.5rem;"><span style="font-size:1.3rem;display:block;margin-bottom:.7rem;">🌐</span><strong style="font-size:.9rem;display:block;margin-bottom:.4rem;">API-First</strong><p style="font-size:.78rem;color:var(--grey-2);">REST / WebSocket. Integrates with SIEM, LMS, C2. SDK in Python and Node.js.</p></div>
        <div style="background:var(--panel);padding:1.5rem;"><span style="font-size:1.3rem;display:block;margin-bottom:.7rem;">🇬🇧</span><strong style="font-size:.9rem;display:block;margin-bottom:.4rem;">UK Data Residency</strong><p style="font-size:.78rem;color:var(--grey-2);">All data processed within UK borders as standard. UK GDPR compliant.</p></div>
      </div>
    </div>
  </div>
</section>

{trust_bar()}
{CTA_BLOCK}

<script>
const vals = {{
  rVal:['−0.47','−0.51','−0.38','−0.55','−0.42'],
  rAro:['+0.83','+0.79','+0.91','+0.85','+0.77'],
  rRdy:['67%','64%','71%','68%','62%']
}};
let idx=0;
setInterval(()=>{{
  idx=(idx+1)%5;
  for(const[id,arr] of Object.entries(vals)){{
    const el=document.getElementById(id);
    if(el){{el.style.opacity='.3';setTimeout(()=>{{el.textContent=arr[idx];el.style.opacity='1';el.style.transition='opacity .3s';}},200);}}
  }}
}},2200);
</script>
"""

# ─────────────────────────────────────────────
# 2. DECEPTION DETECTION PAGE
# ─────────────────────────────────────────────
DECEPTION_SCHEMA = json.dumps({
  "@context":"https://schema.org",
  "@type":"WebPage",
  "name":"Polygraph Alternative UK | Credibility Assessment Technology | EchoDepth Defence",
  "description":"A camera-only, FACS-grounded alternative to polygraph and EyeDetect. 43 facial Action Units analysed in real time. Structured credibility assessment for defence, intelligence, and border security.",
  "url":"https://echodefence.co.uk/solutions/deception-detection/",
  "breadcrumb":{"@type":"BreadcrumbList","itemListElement":[
    {"@type":"ListItem","position":1,"name":"Home","item":"https://echodefence.co.uk/"},
    {"@type":"ListItem","position":2,"name":"Solutions","item":"https://echodefence.co.uk/solutions/"},
    {"@type":"ListItem","position":3,"name":"Deception Detection","item":"https://echodefence.co.uk/solutions/deception-detection/"}
  ]},
  "mainEntity":{"@type":"FAQPage","mainEntity":[
    {"@type":"Question","name":"How does EchoDepth differ from polygraph?","acceptedAnswer":{"@type":"Answer","text":"Polygraph measures physiological responses via physical sensors attached to the body. EchoDepth analyses 43 FACS-compliant facial Action Units using a standard camera — no contact, no specialist hardware. Unlike polygraph, EchoDepth produces timestamped, per-question analytical output that can be integrated into case management systems. UK courts do not admit polygraph evidence; EchoDepth provides a structured analytical signal layer designed for evidential use."}},
    {"@type":"Question","name":"How does EchoDepth compare to EyeDetect?","acceptedAnswer":{"@type":"Answer","text":"EyeDetect (by Converus) measures pupil dilation and eye movement — a single channel based on cognitive load theory. EchoDepth analyses 43 facial Action Units across the full FACS system, providing substantially broader signal coverage. EchoDepth also supports continuous monitoring, API integration, and UK on-premise deployment — capabilities EyeDetect does not offer."}},
    {"@type":"Question","name":"Does EchoDepth detect lies?","acceptedAnswer":{"@type":"Answer","text":"No. EchoDepth does not claim to detect lies. It detects involuntary physiological markers — across 43 FACS-coded Action Units — that are correlated with deception attempts, stress, and cognitive suppression. Output is structured analytical data to support trained interviewer judgement. The determination of credibility remains with the human analyst."}},
    {"@type":"Question","name":"Is EchoDepth admissible as evidence in UK courts?","acceptedAnswer":{"@type":"Answer","text":"EchoDepth is not positioned as standalone evidence. It provides timestamped, structured analytical output — per-question emotional variance records — that can form part of an evidential picture alongside other investigative material. Unlike polygraph, which is inadmissible in UK criminal proceedings, EchoDepth's output is designed with audit-trail and legal review requirements in mind."}}
  ]}
})

DECEPTION_BODY = f"""
<div class="page-hero">
  <div class="page-hero-inner">
    <nav aria-label="Breadcrumb" class="breadcrumb"><a href="/">Home</a> / <a href="/solutions/">Solutions</a> / Deception Detection</nav>
    <span class="label red">Module 04 &middot; Credibility Assessment</span>
    <h1>Beyond Polygraph.<br><span style="color:var(--red)">Beyond EyeDetect.</span></h1>
    <p class="sub">Polygraph measures anxiety. EyeDetect measures pupils. Clearspeed measures voice. None measures the full involuntary facial signal set — the 43 Action Units that FACS-based research has spent four decades correlating with deception, stress, and suppressed emotion. EchoDepth does.</p>
    <div style="display:flex;gap:1rem;margin-top:2rem;flex-wrap:wrap;">
      <a href="/contact/" class="btn-primary red btn-large">Request Credibility Assessment Briefing</a>
      <a href="/technology/" class="btn-ghost btn-large">How It Works</a>
    </div>
  </div>
</div>

<!-- CORE FRAMING -->
<section style="background:var(--void);">
  <div class="section-inner">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:start;">
      <div class="fade-up">
        <span class="label red">The Problem With Current Tools</span>
        <h2 style="margin-bottom:1.2rem;">Every alternative you've evaluated has a ceiling.</h2>
        <p style="color:var(--grey-1);margin-bottom:1.2rem;line-height:1.8;">Polygraph was built in 1939. Its scientific basis was formally challenged by the National Academy of Sciences in 2003, which found it <em>"lacks scientific validity"</em> for security screening. UK courts do not admit polygraph evidence. Yet it remains the default — not because it works, but because nothing credible enough has replaced it.</p>
        <p style="color:var(--grey-1);margin-bottom:1.2rem;line-height:1.8;">EyeDetect is the most credible commercial alternative — and it measures <strong style="color:var(--white)">one channel</strong>. The pupil. Pupil dilation is a proxy for cognitive load, which may indicate deception. But it is one of 43 involuntary facial signals documented in the Facial Action Coding System. Measuring only the pupil leaves the rest of the face — and a substantial body of peer-reviewed signal — completely unread.</p>
        <p style="font-family:var(--font-display);font-size:1.4rem;font-weight:700;color:var(--teal);letter-spacing:.02em;">EchoDepth reads all of it.</p>
      </div>
      <div class="fade-up d2">
        <div style="background:rgba(0,212,180,.04);border:1px solid rgba(0,212,180,.2);border-left:3px solid var(--teal);padding:1.8rem 2rem;margin-bottom:1.2rem;">
          <div style="font-family:'DM Mono',monospace;font-size:.58rem;color:var(--teal);letter-spacing:.15em;text-transform:uppercase;margin-bottom:.8rem;">// US DOD POLYGRAPH+ PROGRAMME · 2023</div>
          <p style="font-size:.88rem;color:var(--grey-1);line-height:1.8;">"Advancements in <strong style="color:var(--white)">standoff physiology sensing using cameras</strong> have the potential to be less intrusive and more reliable than existing methods." — US Department of Defense / Defense Innovation Unit. EchoDepth is that architecture.</p>
        </div>
        <div class="metric-card red"><div class="metric-label">Polygraph false-negative rate</div><div class="metric-value">Up to 47%</div><div class="metric-desc">Inadmissible in UK courts. Scientifically disputed since NAS 2003. EchoDepth provides a FACS-grounded corroborating layer.</div></div>
        <div class="metric-card"><div class="metric-label">Action Unit coverage vs EyeDetect</div><div class="metric-value">43 vs ~6</div><div class="metric-desc">EyeDetect measures eye-based metrics only. EchoDepth analyses all 43 FACS-compliant AUs — the complete involuntary facial signal set.</div></div>
      </div>
    </div>
  </div>
</section>

<!-- WHAT ECHODEPTH PROVIDES -->
<section style="background:var(--deep);border-top:1px solid var(--border);">
  <div class="section-inner">
    <div class="fade-up">
      <span class="label">What EchoDepth Provides</span>
      <h2 style="margin-bottom:.5rem;">Structured analytical output.<br><span style="color:var(--grey-2);font-style:italic;font-family:var(--font-body);font-weight:300;font-size:.6em;">Not a verdict.</span></h2>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5rem;margin-top:3rem;align-items:start;">
      <div class="fade-up d1">
        <ul class="cap-list">
          <li>Per-question stress and arousal mapping — emotional state timestamped to each question moment during a structured interview</li>
          <li>AU activation log — which specific Action Units fired, at what intensity, across all 43 FACS-compliant markers</li>
          <li>Temporal anomaly detection — deviation from the subject's own baseline, not population averages</li>
          <li>Structured report export — formatted for interview case files, legal review, or intelligence reporting chains</li>
          <li>Live interview overlay — optional real-time display for the interviewer, not visible to the subject</li>
          <li>Standard camera operation — no IR kiosk, no physical attachment, no specialist hardware</li>
          <li>UK data residency and air-gap deployment — for STRAP and above environments</li>
        </ul>
        <div style="background:rgba(224,59,59,.06);border:1px solid rgba(224,59,59,.2);border-left:3px solid var(--red);padding:1.5rem;margin-top:1.5rem;">
          <p style="font-size:.9rem;color:var(--grey-1);line-height:1.8;font-style:italic;">"EchoDepth does not claim to detect lies. No technology reliably detects lies. EchoDepth detects the involuntary physiological markers — across 43 FACS-coded Action Units — that accompany deception attempts. The determination of credibility remains with the human analyst."</p>
        </div>
      </div>
      <div class="fade-up d2">
        <div class="metric-card"><div class="metric-label">Output format</div><div class="metric-value">Audit-ready</div><div class="metric-desc">Timestamped per-question emotional variance records. Structured for evidential use and legal review.</div></div>
        <div class="metric-card amber"><div class="metric-label">Deployment</div><div class="metric-value">Camera-only</div><div class="metric-desc">Operates on existing interview room cameras, laptop webcams, or portable setups. No specialist hardware required.</div></div>
        <div class="metric-card red"><div class="metric-label">Integration</div><div class="metric-value">API-First</div><div class="metric-desc">REST and WebSocket output. Feeds directly into case management, SIEM, and interview record systems.</div></div>
      </div>
    </div>
  </div>
</section>

<!-- COMPETITOR COMPARISON -->
<section style="background:var(--void);">
  <div class="section-inner">
    <div class="fade-up">
      <span class="label red">Competitive Landscape</span>
      <h2>The tools your buyers<br>have already evaluated.</h2>
      <p style="color:var(--grey-1);max-width:600px;margin-top:.8rem;line-height:1.75;font-size:.95rem;">Below is a direct comparison of every credibility assessment tool currently available in the defence and security market. All information sourced from vendor documentation and independent academic review.</p>
    </div>
    <div style="overflow-x:auto;margin-top:2.5rem;" class="fade-up d1">
      <table class="comp-table" style="min-width:800px;">
        <thead>
          <tr>
            <th>Capability</th>
            <th>Polygraph</th>
            <th>EyeDetect <small style="opacity:.6">(Converus)</small></th>
            <th>Clearspeed</th>
            <th>AVATAR <small style="opacity:.6">(Discern)</small></th>
            <th class="col-echo">EchoDepth</th>
          </tr>
        </thead>
        <tbody>
          <tr><td class="aspect">Contact / hardware</td><td class="neg">Physical sensors + examiner</td><td class="neg">IR kiosk required</td><td class="echo-col">Phone/web</td><td class="neg">6ft kiosk</td><td class="echo-col"><span class="tick">✓</span>Standard camera only</td></tr>
          <tr><td class="aspect">Continuous monitoring</td><td class="neg">Session only</td><td class="neg">Session only</td><td class="neg">Session only</td><td class="neg">Session only</td><td class="echo-col"><span class="tick">✓</span>24/7 passive baseline</td></tr>
          <tr><td class="aspect">Signal channels</td><td class="amber-col">Cardio / GSR / breath</td><td class="amber-col">Eyes only</td><td class="neg">Voice only</td><td class="amber-col">Face + voice</td><td class="echo-col"><span class="tick">✓</span>43 FACS Action Units</td></tr>
          <tr><td class="aspect">Scientific basis</td><td class="amber-col">Disputed (NAS 2003)</td><td class="amber-col">Limited independent replication</td><td class="amber-col">Proprietary</td><td class="neg">Not independently replicated</td><td class="echo-col"><span class="tick">✓</span>FACS peer-reviewed (Ekman)</td></tr>
          <tr><td class="aspect">UK admissibility</td><td class="neg">Inadmissible</td><td class="neg">Not established</td><td class="neg">Not established</td><td class="neg">Not established</td><td class="echo-col"><span class="tick">✓</span>Timestamped audit output</td></tr>
          <tr><td class="aspect">API / integration</td><td class="neg">None</td><td class="neg">None</td><td class="neg">Limited</td><td class="neg">None</td><td class="echo-col"><span class="tick">✓</span>REST / WebSocket / SIEM</td></tr>
          <tr><td class="aspect">Air-gap deployment</td><td class="neg">N/A</td><td class="neg">Not offered</td><td class="neg">Cloud-only</td><td class="neg">Not offered</td><td class="echo-col"><span class="tick">✓</span>Full on-premise available</td></tr>
          <tr><td class="aspect">UK data residency</td><td class="amber-col">Examiner-held</td><td class="neg">US-hosted cloud</td><td class="amber-col">Partial</td><td class="neg">Not confirmed</td><td class="echo-col"><span class="tick">✓</span>UK standard</td></tr>
          <tr><td class="aspect">Multi-use platform</td><td class="neg">Deception only</td><td class="neg">Deception only</td><td class="neg">Risk triage only</td><td class="neg">Border screening only</td><td class="echo-col"><span class="tick">✓</span>Deception + fatigue + training + insider</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- FAQ (structured data) -->
<section style="background:var(--deep);border-top:1px solid var(--border);" id="faq">
  <div class="section-inner">
    <div class="fade-up">
      <span class="label">Common Questions</span>
      <h2>Frequently Asked</h2>
    </div>
    <div style="max-width:800px;margin-top:2.5rem;" class="fade-up d1">
      <details style="border-bottom:1px solid var(--border);padding:1.2rem 0;" open>
        <summary style="cursor:pointer;font-family:var(--font-display);font-size:1.05rem;font-weight:600;list-style:none;display:flex;justify-content:space-between;align-items:center;">How does EchoDepth differ from polygraph? <span style="color:var(--teal);font-size:1.2rem;">+</span></summary>
        <p style="color:var(--grey-1);font-size:.88rem;line-height:1.8;margin-top:.8rem;padding-left:.5rem;">Polygraph measures physiological responses via physical sensors attached to the body — heart rate, respiration, skin conductance. EchoDepth analyses 43 FACS-compliant facial Action Units using a standard camera. No contact, no specialist hardware. Unlike polygraph, UK courts do not admit polygraph evidence; EchoDepth produces structured, timestamped analytical output designed for evidential use and integration into case management systems.</p>
      </details>
      <details style="border-bottom:1px solid var(--border);padding:1.2rem 0;">
        <summary style="cursor:pointer;font-family:var(--font-display);font-size:1.05rem;font-weight:600;list-style:none;display:flex;justify-content:space-between;align-items:center;">How does EchoDepth compare to EyeDetect? <span style="color:var(--teal);font-size:1.2rem;">+</span></summary>
        <p style="color:var(--grey-1);font-size:.88rem;line-height:1.8;margin-top:.8rem;padding-left:.5rem;">EyeDetect (Converus) measures pupil dilation and eye movement — one signal channel based on cognitive load theory. EchoDepth analyses 43 facial Action Units across the full FACS system. EchoDepth also supports continuous monitoring, API integration into existing security platforms, and UK on-premise deployment — capabilities EyeDetect does not offer. EyeDetect requires a dedicated IR hardware kiosk; EchoDepth operates on standard cameras.</p>
      </details>
      <details style="border-bottom:1px solid var(--border);padding:1.2rem 0;">
        <summary style="cursor:pointer;font-family:var(--font-display);font-size:1.05rem;font-weight:600;list-style:none;display:flex;justify-content:space-between;align-items:center;">Does EchoDepth detect lies? <span style="color:var(--teal);font-size:1.2rem;">+</span></summary>
        <p style="color:var(--grey-1);font-size:.88rem;line-height:1.8;margin-top:.8rem;padding-left:.5rem;">No. EchoDepth does not claim to detect lies — and any system that makes this claim should be treated with scepticism. EchoDepth detects involuntary physiological markers across 43 FACS-coded Action Units that are correlated with deception attempts, stress, and cognitive suppression. Output is structured analytical data to support trained interviewer judgement. The determination of credibility remains with the human analyst.</p>
      </details>
      <details style="border-bottom:1px solid var(--border);padding:1.2rem 0;">
        <summary style="cursor:pointer;font-family:var(--font-display);font-size:1.05rem;font-weight:600;list-style:none;display:flex;justify-content:space-between;align-items:center;">Is EchoDepth suitable for UK intelligence and government use? <span style="color:var(--teal);font-size:1.2rem;">+</span></summary>
        <p style="color:var(--grey-1);font-size:.88rem;line-height:1.8;margin-top:.8rem;padding-left:.5rem;">Yes. EchoDepth offers full on-premise and air-gapped deployment for classified environments, UK data residency as standard, and role-based access controls compliant with UK GDPR and the HMG Security Policy Framework. The system is designed to operate within existing security infrastructure — not alongside it as a standalone tool.</p>
      </details>
      <details style="padding:1.2rem 0;">
        <summary style="cursor:pointer;font-family:var(--font-display);font-size:1.05rem;font-weight:600;list-style:none;display:flex;justify-content:space-between;align-items:center;">What searches does EchoDepth address? <span style="color:var(--teal);font-size:1.2rem;">+</span></summary>
        <p style="color:var(--grey-1);font-size:.88rem;line-height:1.8;margin-top:.8rem;padding-left:.5rem;">EchoDepth is evaluated by buyers searching for: polygraph alternative UK, credibility assessment software, deception detection technology, EyeDetect alternative, non-contact lie detection, facial micro-expression analysis security, automated credibility assessment, source credibility assessment intelligence, standoff physiology sensing, and interview support technology.</p>
      </details>
    </div>
  </div>
</section>

{trust_bar()}
{CTA_BLOCK}
"""

# ─────────────────────────────────────────────
# 3. INSIDER THREAT PAGE
# ─────────────────────────────────────────────
INSIDER_BODY = f"""
<div class="page-hero">
  <div class="page-hero-inner">
    <nav aria-label="Breadcrumb" class="breadcrumb"><a href="/">Home</a> / <a href="/solutions/">Solutions</a> / Insider Threat &amp; Vetting</nav>
    <span class="label amber">Module 02 &middot; Insider Threat &amp; Vetting</span>
    <h1>Continuous<br><span style="color:var(--amber)">Emotional Anomaly</span><br>Monitoring.</h1>
    <p class="sub">Static security clearances only confirm who someone was. EchoDepth provides continuous baseline monitoring in high-security environments — establishing emotional norms per individual and alerting when significant anomalies emerge. Earlier signal. Earlier intervention.</p>
    <div style="display:flex;gap:1rem;margin-top:2rem;flex-wrap:wrap;">
      <a href="/contact/" class="btn-primary amber btn-large">Insider Threat Briefing</a>
      <a href="/technology/" class="btn-ghost btn-large">Technical Overview</a>
    </div>
  </div>
</div>
<section style="background:var(--void);">
  <div class="section-inner">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:start;">
      <div class="fade-up">
        <span class="label amber">The Problem</span>
        <h2 style="margin-bottom:1.2rem;">You cannot vet<br>what you cannot see.</h2>
        <p style="color:var(--grey-1);margin-bottom:1.2rem;line-height:1.8;">Security clearances and annual reviews catch nothing in real time. Stress indicators, behavioural anomalies, and emotional changes that precede insider incidents go entirely undetected by existing TSCM and access control infrastructure. Traditional vetting misses approximately 83% of insider threats until the post-incident investigation.</p>
        <ul class="cap-list">
          <li>Behavioural baseline profiling per individual across working periods</li>
          <li>Anomaly scoring when emotional state deviates significantly from personal norm</li>
          <li>Integration with SIEM platforms — Splunk, Microsoft Sentinel</li>
          <li>Alert escalation workflows for security operations teams</li>
          <li>Pre-interview emotional state capture for HR and security investigations</li>
          <li>GDPR-compliant architecture with role-based data access controls</li>
          <li>UK data residency and air-gap deployment available</li>
        </ul>
        <a href="/contact/" class="btn-primary amber" style="margin-top:1rem;">Request Briefing</a>
      </div>
      <div class="fade-up d2">
        <div class="metric-card amber"><div class="metric-label">Average time to detect anomaly</div><div class="metric-value">Real-time</div><div class="metric-desc">vs 6–18 months post-incident for traditional methods</div></div>
        <div class="metric-card red"><div class="metric-label">Incidents preceded by detectable signals</div><div class="metric-value">~82%</div><div class="metric-desc">Of insider incidents show elevated emotional markers in the 30 days prior (CISA data)</div></div>
        <div class="metric-card amber"><div class="metric-label">Deployment footprint</div><div class="metric-value">Camera-only</div><div class="metric-desc">Existing CCTV infrastructure reuse possible. Zero additional hardware in most environments.</div></div>
        <div style="margin-top:1.2rem;padding:1.2rem;background:var(--panel);border:1px solid var(--border);border-left:2px solid var(--amber);">
          <p style="font-size:.78rem;color:var(--grey-2);margin-bottom:.4rem;font-family:var(--font-condensed);letter-spacing:.08em;text-transform:uppercase;">Cost per insider incident</p>
          <p style="font-family:var(--font-display);font-size:2rem;font-weight:700;color:var(--amber);">£3.2M</p>
          <p style="font-size:.75rem;color:var(--grey-2);">Average (Ponemon Institute 2024)</p>
        </div>
      </div>
    </div>
  </div>
</section>
{trust_bar()}
{CTA_BLOCK}
"""

# ─────────────────────────────────────────────
# 4. COMPLIANCE PAGE
# ─────────────────────────────────────────────
COMPLIANCE_BODY = f"""
<div class="page-hero">
  <div class="page-hero-inner">
    <nav aria-label="Breadcrumb" class="breadcrumb"><a href="/">Home</a> / <a href="/solutions/">Solutions</a> / Compliance &amp; Training</nav>
    <span class="label">Module 01 &middot; Compliance &amp; Training</span>
    <h1>Know if Training<br>is <span style="color:var(--teal)">Actually Landing.</span></h1>
    <p class="sub">EchoDepth integrates with your existing LMS or training environment. As personnel complete mandatory modules — CBRN, cyber security awareness, safeguarding, DSAT compliance — the system continuously measures cognitive engagement, comprehension signals, and stress indicators.</p>
    <div style="display:flex;gap:1rem;margin-top:2rem;flex-wrap:wrap;">
      <a href="/contact/" class="btn-primary btn-large">See Training Integration</a>
      <a href="/technology/" class="btn-ghost btn-large">Technical Overview</a>
    </div>
  </div>
</div>
<section style="background:var(--void);">
  <div class="section-inner">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:start;">
      <div class="fade-up">
        <span class="label">The Problem</span>
        <h2 style="margin-bottom:1.2rem;">Completion rates measure<br>nothing that matters.</h2>
        <p style="color:var(--grey-1);margin-bottom:1.2rem;line-height:1.8;">74% of compliance failures stem from poor knowledge retention — not from personnel who skipped training, but from personnel who completed it while disengaged, overwhelmed, or not genuinely processing the material. EchoDepth makes that invisible problem visible.</p>
        <ul class="cap-list">
          <li>Real-time engagement and comprehension scoring via AU analysis during video or screen-based training</li>
          <li>Flags disengagement, confusion, and overload at individual level — without self-reporting</li>
          <li>Generates training effectiveness reports per cohort, per module, per individual</li>
          <li>Identifies which specific content segments cause cognitive dropout</li>
          <li>API integration with LMS platforms — Moodle, SAP SuccessFactors, Cornerstone</li>
          <li>DSAT-compatible audit trail records per individual — timestamped engagement evidence</li>
          <li>Fully passive — no headsets, no interruptions, no workflow changes</li>
        </ul>
        <a href="/contact/" class="btn-primary" style="margin-top:1rem;">Request Integration Demo</a>
      </div>
      <div class="fade-up d2">
        <div class="metric-card"><div class="metric-label">Engagement visibility increase</div><div class="metric-value">+340%</div><div class="metric-desc">vs self-assessment methods</div></div>
        <div class="metric-card amber"><div class="metric-label">Knowledge retention uplift</div><div class="metric-value">+29%</div><div class="metric-desc">When adaptive pacing is applied from EchoDepth signals</div></div>
        <div class="metric-card"><div class="metric-label">Compliance audit defensibility</div><div class="metric-value">Timestamped</div><div class="metric-desc">Per-individual engagement records for DSAT/DLE audit trail requirements</div></div>
      </div>
    </div>
  </div>
</section>
{trust_bar()}
{CTA_BLOCK}
"""

# ─────────────────────────────────────────────
# 5. OPERATOR READINESS PAGE
# ─────────────────────────────────────────────
OPERATOR_BODY = f"""
<div class="page-hero">
  <div class="page-hero-inner">
    <nav aria-label="Breadcrumb" class="breadcrumb"><a href="/">Home</a> / <a href="/solutions/">Solutions</a> / Operator Readiness</nav>
    <span class="label">Module 03 &middot; Operator Readiness</span>
    <h1>Quantify Human<br><span style="color:var(--teal)">Readiness. Live.</span></h1>
    <p class="sub">For drone operators, SOC analysts, air traffic controllers, and any high-stakes operational role — EchoDepth provides a real-time VAD score. Commanders receive dashboard visibility of team cognitive readiness before and during critical operations.</p>
    <div style="display:flex;gap:1rem;margin-top:2rem;flex-wrap:wrap;">
      <a href="/contact/" class="btn-primary btn-large">Operator Readiness Demo</a>
      <a href="/technology/" class="btn-ghost btn-large">Technical Overview</a>
    </div>
  </div>
</div>
<section style="background:var(--void);">
  <div class="section-inner">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:start;">
      <div class="fade-up">
        <span class="label">Capabilities</span>
        <h2 style="margin-bottom:1.2rem;">From pre-mission scoring<br>to post-incident analysis.</h2>
        <ul class="cap-list">
          <li>Pre-mission readiness scoring — go/no-go informed by emotional baseline</li>
          <li>Live fatigue and cognitive overload monitoring during sustained operations</li>
          <li>Alert system for threshold breaches — supervisor notification without disrupting operator</li>
          <li>Post-incident timeline reconstruction showing operator state at decision points</li>
          <li>Shift handover readiness reports for control room and field operations</li>
          <li>Integration with existing C2 and workforce management platforms</li>
          <li>Operates on existing workstation cameras — zero hardware change for operators</li>
        </ul>
        <a href="/contact/" class="btn-primary" style="margin-top:1rem;">Request Briefing</a>
      </div>
      <div class="fade-up d2">
        <div class="metric-card"><div class="metric-label">Cognitive load visibility</div><div class="metric-value">Continuous</div><div class="metric-desc">Near real-time frame analysis — emotional state updated every ~700ms</div></div>
        <div class="metric-card amber"><div class="metric-label">Operational incidents linked to fatigue</div><div class="metric-value">40%</div><div class="metric-desc">Of avoidable incidents involve a fatigued or cognitively overloaded operator</div></div>
        <div class="metric-card"><div class="metric-label">Deployment</div><div class="metric-value">Passive</div><div class="metric-desc">Works with existing workstation cameras. No change to operator workflow or equipment.</div></div>
      </div>
    </div>
  </div>
</section>
{trust_bar()}
{CTA_BLOCK}
"""

# ─────────────────────────────────────────────
# 6. TECHNOLOGY PAGE
# ─────────────────────────────────────────────
TECH_BODY = f"""
<div class="page-hero">
  <div class="page-hero-inner">
    <nav aria-label="Breadcrumb" class="breadcrumb"><a href="/">Home</a> / Technology</nav>
    <span class="label">The EchoDepth Engine</span>
    <h1>Facial Action Units.<br><span style="color:var(--teal)">Decoded at Scale.</span></h1>
    <p class="sub">FACS-compliant. Camera-only. API-first. EchoDepth analyses 43 facial Action Units in near real-time — producing structured VAD output suitable for defence, intelligence, and security integration.</p>
  </div>
</div>
<section style="background:var(--void);" id="pipeline">
  <div class="section-inner">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5rem;">
      <div class="fade-up">
        <span class="label">Processing Pipeline</span>
        <h2 style="margin-bottom:2rem;">Five-Step<br>Architecture.</h2>
        <div style="display:flex;flex-direction:column;">
          <div style="display:flex;gap:1.5rem;padding:1.5rem 0;border-bottom:1px solid var(--border);">
            <span style="font-family:'DM Mono',monospace;font-size:.63rem;color:var(--teal);width:28px;flex-shrink:0;padding-top:3px;">01</span>
            <div><h4 style="font-size:1rem;margin-bottom:.4rem;">Camera Ingestion</h4><p style="font-size:.82rem;color:var(--grey-1);line-height:1.65;">Standard RGB camera feed — existing CCTV, laptop webcams, or dedicated hardware. Minimum 720p. No infrared, no specialist equipment required.</p></div>
          </div>
          <div style="display:flex;gap:1.5rem;padding:1.5rem 0;border-bottom:1px solid var(--border);">
            <span style="font-family:'DM Mono',monospace;font-size:.63rem;color:var(--teal);width:28px;flex-shrink:0;padding-top:3px;">02</span>
            <div><h4 style="font-size:1rem;margin-bottom:.4rem;">Face Detection &amp; Landmark Mapping</h4><p style="font-size:.82rem;color:var(--grey-1);line-height:1.65;">68-point facial landmark detection at 30fps+. Robust to partial occlusion, varied lighting, and head rotation up to ±30 degrees.</p></div>
          </div>
          <div style="display:flex;gap:1.5rem;padding:1.5rem 0;border-bottom:1px solid var(--border);">
            <span style="font-family:'DM Mono',monospace;font-size:.63rem;color:var(--teal);width:28px;flex-shrink:0;padding-top:3px;">03</span>
            <div><h4 style="font-size:1rem;margin-bottom:.4rem;">Action Unit Extraction</h4><p style="font-size:.82rem;color:var(--grey-1);line-height:1.65;">FACS-compliant analysis of 43 facial Action Units — muscle group activations mapped to the Facial Action Coding System. Intensity scored 0–5 per AU per frame.</p></div>
          </div>
          <div style="display:flex;gap:1.5rem;padding:1.5rem 0;border-bottom:1px solid var(--border);">
            <span style="font-family:'DM Mono',monospace;font-size:.63rem;color:var(--teal);width:28px;flex-shrink:0;padding-top:3px;">04</span>
            <div><h4 style="font-size:1rem;margin-bottom:.4rem;">VAD Mapping &amp; Temporal Smoothing</h4><p style="font-size:.82rem;color:var(--grey-1);line-height:1.65;">AU combinations mapped to Valence–Arousal–Dominance space. Temporal smoothing eliminates noise and surfaces meaningful state changes.</p></div>
          </div>
          <div style="display:flex;gap:1.5rem;padding:1.5rem 0;">
            <span style="font-family:'DM Mono',monospace;font-size:.63rem;color:var(--teal);width:28px;flex-shrink:0;padding-top:3px;">05</span>
            <div id="api"><h4 style="font-size:1rem;margin-bottom:.4rem;">Output &amp; Integration Layer</h4><p style="font-size:.82rem;color:var(--grey-1);line-height:1.65;">REST API, WebSocket stream, or direct SDK. Structured JSON output per frame, per second, or aggregated per session. Webhook alerting for threshold events.</p></div>
          </div>
        </div>
      </div>
      <div class="fade-up d2" id="deployment">
        <span class="label">Deployment Specifications</span>
        <h2 style="margin-bottom:2rem;">Built for Classified<br>Environments.</h2>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--border);border:1px solid var(--border);margin-bottom:2rem;">
          <div style="background:var(--panel);padding:1.8rem;"><span style="font-size:1.3rem;display:block;margin-bottom:.7rem;">🔒</span><h4 style="font-size:.95rem;margin-bottom:.4rem;">On-Premise Deployment</h4><p style="font-size:.78rem;color:var(--grey-1);line-height:1.6;">Fully air-gapped operation. No external data transmission. Docker containerised for SCIF and classified environments.</p></div>
          <div style="background:var(--panel);padding:1.8rem;"><span style="font-size:1.3rem;display:block;margin-bottom:.7rem;">⚡</span><h4 style="font-size:.95rem;margin-bottom:.4rem;">~700ms Latency</h4><p style="font-size:.78rem;color:var(--grey-1);line-height:1.6;">Sub-second emotional state output. Suitable for real-time alerting and live interview support.</p></div>
          <div style="background:var(--panel);padding:1.8rem;"><span style="font-size:1.3rem;display:block;margin-bottom:.7rem;">🌐</span><h4 style="font-size:.95rem;margin-bottom:.4rem;">API-First</h4><p style="font-size:.78rem;color:var(--grey-1);line-height:1.6;">REST / WebSocket. SDK in Python and Node.js. Integrates with SIEM, LMS, access control, and C2 platforms.</p></div>
          <div style="background:var(--panel);padding:1.8rem;"><span style="font-size:1.3rem;display:block;margin-bottom:.7rem;">⚖️</span><h4 style="font-size:.95rem;margin-bottom:.4rem;">GDPR-Compliant</h4><p style="font-size:.78rem;color:var(--grey-1);line-height:1.6;">Pseudonymised processing by default. Role-based access controls. Full audit logging. UK data residency standard.</p></div>
        </div>
        <div style="background:var(--panel);border:1px solid var(--border);border-left:2px solid var(--teal);padding:1.5rem;">
          <div style="font-family:'DM Mono',monospace;font-size:.58rem;color:var(--teal);letter-spacing:.12em;text-transform:uppercase;margin-bottom:.6rem;">vs Polygraph / Legacy Methods</div>
          <table class="comp-table" style="font-size:.72rem;">
            <tr><td class="aspect">Contact</td><td class="neg">Physical sensors</td><td class="echo-col"><span class="tick">✓</span>Camera only</td></tr>
            <tr><td class="aspect">Continuous</td><td class="neg">Session only</td><td class="echo-col"><span class="tick">✓</span>24/7 passive</td></tr>
            <tr><td class="aspect">Science</td><td class="amber-col">Disputed NAS 2003</td><td class="echo-col"><span class="tick">✓</span>FACS peer-reviewed</td></tr>
            <tr><td class="aspect">UK courts</td><td class="neg">Inadmissible</td><td class="echo-col"><span class="tick">✓</span>Structured evidence layer</td></tr>
            <tr><td class="aspect">Integration</td><td class="neg">Standalone</td><td class="echo-col"><span class="tick">✓</span>API / SIEM / LMS</td></tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>
{trust_bar()}
{CTA_BLOCK}
"""

# ─────────────────────────────────────────────
# 7. CONTACT PAGE
# ─────────────────────────────────────────────
CONTACT_SCHEMA = json.dumps({
  "@context":"https://schema.org",
  "@type":"ContactPage",
  "name":"Request a Briefing — EchoDepth Defence",
  "url":"https://echodefence.co.uk/contact/",
  "description":"Request a structured technical briefing for defence procurement, security leadership, or intelligence teams. NDA available. Air-gapped demo environment on request."
})

CONTACT_BODY = f"""
<div class="page-hero">
  <div class="page-hero-inner">
    <nav aria-label="Breadcrumb" class="breadcrumb"><a href="/">Home</a> / Contact</nav>
    <span class="label">Secure Enquiry</span>
    <h1>Request a<br><span style="color:var(--teal)">Classified Briefing.</span></h1>
    <p class="sub">Structured technical briefings for defence procurement, security leadership, and intelligence teams. All enquiries handled within 24 hours. NDA available on request.</p>
  </div>
</div>
<section style="background:var(--void);">
  <div class="section-inner">
    <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:6rem;align-items:start;">
      <div class="fade-up">
        <form id="contactForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST" novalidate style="display:flex;flex-direction:column;gap:1.2rem;">
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
            <div>
              <label for="name" style="font-family:var(--font-condensed);font-size:.65rem;letter-spacing:.18em;text-transform:uppercase;color:var(--grey-2);display:block;margin-bottom:.5rem;">Full Name *</label>
              <input type="text" id="name" name="name" required placeholder="Your name" style="width:100%;background:var(--surface);border:1px solid var(--border);color:var(--white);padding:12px 14px;font-family:var(--font-body);font-size:.88rem;outline:none;transition:border-color .2s;" onfocus="this.style.borderColor='var(--teal)'" onblur="this.style.borderColor='var(--border)'">
            </div>
            <div>
              <label for="org" style="font-family:var(--font-condensed);font-size:.65rem;letter-spacing:.18em;text-transform:uppercase;color:var(--grey-2);display:block;margin-bottom:.5rem;">Organisation *</label>
              <input type="text" id="org" name="organisation" required placeholder="Organisation" style="width:100%;background:var(--surface);border:1px solid var(--border);color:var(--white);padding:12px 14px;font-family:var(--font-body);font-size:.88rem;outline:none;transition:border-color .2s;" onfocus="this.style.borderColor='var(--teal)'" onblur="this.style.borderColor='var(--border)'">
            </div>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
            <div>
              <label for="role" style="font-family:var(--font-condensed);font-size:.65rem;letter-spacing:.18em;text-transform:uppercase;color:var(--grey-2);display:block;margin-bottom:.5rem;">Role / Title *</label>
              <input type="text" id="role" name="role" required placeholder="Your role" style="width:100%;background:var(--surface);border:1px solid var(--border);color:var(--white);padding:12px 14px;font-family:var(--font-body);font-size:.88rem;outline:none;transition:border-color .2s;" onfocus="this.style.borderColor='var(--teal)'" onblur="this.style.borderColor='var(--border)'">
            </div>
            <div>
              <label for="email" style="font-family:var(--font-condensed);font-size:.65rem;letter-spacing:.18em;text-transform:uppercase;color:var(--grey-2);display:block;margin-bottom:.5rem;">Email Address *</label>
              <input type="email" id="email" name="email" required placeholder="work@organisation.gov.uk" style="width:100%;background:var(--surface);border:1px solid var(--border);color:var(--white);padding:12px 14px;font-family:var(--font-body);font-size:.88rem;outline:none;transition:border-color .2s;" onfocus="this.style.borderColor='var(--teal)'" onblur="this.style.borderColor='var(--border)'">
            </div>
          </div>
          <div>
            <label for="interest" style="font-family:var(--font-condensed);font-size:.65rem;letter-spacing:.18em;text-transform:uppercase;color:var(--grey-2);display:block;margin-bottom:.5rem;">Area of Interest</label>
            <select id="interest" name="interest" style="width:100%;background:var(--surface);border:1px solid var(--border);color:var(--grey-1);padding:12px 14px;font-family:var(--font-body);font-size:.88rem;outline:none;cursor:pointer;">
              <option value="">Select an area</option>
              <option value="deception">Deception Detection / Credibility Assessment</option>
              <option value="insider">Insider Threat &amp; Continuous Vetting</option>
              <option value="compliance">Compliance &amp; Training</option>
              <option value="operator">Operator Readiness &amp; Fatigue</option>
              <option value="general">General / Platform Enquiry</option>
            </select>
          </div>
          <div>
            <label for="message" style="font-family:var(--font-condensed);font-size:.65rem;letter-spacing:.18em;text-transform:uppercase;color:var(--grey-2);display:block;margin-bottom:.5rem;">Message (optional)</label>
            <textarea id="message" name="message" rows="4" placeholder="Briefly describe your requirement or the environment you're evaluating for." style="width:100%;background:var(--surface);border:1px solid var(--border);color:var(--white);padding:12px 14px;font-family:var(--font-body);font-size:.88rem;outline:none;resize:vertical;transition:border-color .2s;" onfocus="this.style.borderColor='var(--teal)'" onblur="this.style.borderColor='var(--border)'"></textarea>
          </div>
          <div style="display:flex;align-items:center;gap:10px;">
            <input type="checkbox" id="nda" name="nda" value="yes" style="accent-color:var(--teal);width:16px;height:16px;">
            <label for="nda" style="font-size:.82rem;color:var(--grey-1);cursor:pointer;">I would like to sign an NDA before the briefing</label>
          </div>
          <button type="submit" class="btn-primary" style="align-self:flex-start;margin-top:.5rem;">Send Secure Enquiry</button>
          <p style="font-size:.72rem;color:var(--grey-3);line-height:1.6;">Your details will not be shared with third parties. Processed in accordance with UK GDPR. All enquiries handled within 24 hours.</p>
        </form>
        <div id="formSuccess" style="display:none;background:rgba(0,212,180,.08);border:1px solid var(--teal);border-left:3px solid var(--teal);padding:1.5rem;margin-top:1rem;">
          <p style="color:var(--teal);font-family:var(--font-display);font-size:1.1rem;font-weight:700;">Enquiry received.</p>
          <p style="color:var(--grey-1);font-size:.85rem;margin-top:.4rem;">We will respond within 24 hours. If you requested an NDA, this will be sent with our initial response.</p>
        </div>
      </div>
      <div class="fade-up d2">
        <div style="background:var(--panel);border:1px solid var(--border);padding:2rem;margin-bottom:1.2rem;">
          <span class="label" style="margin-bottom:.8rem">Contact Details</span>
          <p style="font-family:'DM Mono',monospace;font-size:.68rem;color:var(--grey-1);line-height:2;letter-spacing:.05em;">DEFENCE@CAVEFISH.CO.UK<br>CARDIFF, WALES, UK<br>UK DATA RESIDENCY STANDARD</p>
        </div>
        <div style="background:var(--panel);border:1px solid var(--border);padding:2rem;margin-bottom:1.2rem;">
          <span class="label" style="margin-bottom:.8rem">What to Expect</span>
          <ul style="list-style:none;display:flex;flex-direction:column;gap:.7rem;">
            <li style="font-size:.82rem;color:var(--grey-1);display:flex;gap:10px;"><span style="color:var(--teal)">01.</span>Response within 24 hours from a technical team member</li>
            <li style="font-size:.82rem;color:var(--grey-1);display:flex;gap:10px;"><span style="color:var(--teal)">02.</span>NDA executed if requested before any technical detail is shared</li>
            <li style="font-size:.82rem;color:var(--grey-1);display:flex;gap:10px;"><span style="color:var(--teal)">03.</span>Structured briefing — 45–60 minutes, technical or procurement focus depending on your role</li>
            <li style="font-size:.82rem;color:var(--grey-1);display:flex;gap:10px;"><span style="color:var(--teal)">04.</span>Air-gapped demo environment available for classified-environment clients</li>
          </ul>
        </div>
        <div style="background:rgba(0,212,180,.04);border:1px solid rgba(0,212,180,.2);padding:1.5rem;">
          <span class="label" style="margin-bottom:.5rem">Pilot Programme</span>
          <p style="font-size:.82rem;color:var(--grey-1);line-height:1.7;">8-week structured pilot with defined success criteria. Integration support, baseline profiling, and full technical evaluation documentation included.</p>
        </div>
      </div>
    </div>
  </div>
</section>
{trust_bar()}
<script>
const form=document.getElementById('contactForm');
const success=document.getElementById('formSuccess');
if(form){{
  form.addEventListener('submit',async(e)=>{{
    e.preventDefault();
    const data=new FormData(form);
    try{{
      const r=await fetch(form.action,{{method:'POST',body:data,headers:{{'Accept':'application/json'}}}});
      if(r.ok){{form.style.display='none';success.style.display='block';}}
    }}catch(err){{console.error(err);}}
  }});
}}
</script>
"""

# ─────────────────────────────────────────────
# 8. 404 PAGE
# ─────────────────────────────────────────────
NOT_FOUND_BODY = """
<section style="min-height:100vh;display:flex;align-items:center;justify-content:center;padding-top:68px;">
  <div style="text-align:center;max-width:500px;padding:2rem;">
    <span style="font-family:'DM Mono',monospace;font-size:.65rem;color:var(--teal);letter-spacing:.2em;display:block;margin-bottom:1.5rem;">// ERROR 404</span>
    <h1 style="font-size:6rem;line-height:1;color:var(--grey-3);margin-bottom:.5rem;">404</h1>
    <h2 style="font-size:1.8rem;margin-bottom:1rem;">Signal Not Found</h2>
    <p style="color:var(--grey-1);margin-bottom:2rem;">This page doesn't exist or has moved. Return to base.</p>
    <a href="/" class="btn-primary">Return to Homepage</a>
  </div>
</section>
"""

# ─────────────────────────────────────────────
# GENERATE ALL FILES
# ─────────────────────────────────────────────
pages = [
  ("/home/claude/vercel-site/index.html",
   "EchoDepth Defence | Emotional Intelligence for Critical Environments | Polygraph Alternative UK",
   "Camera-based emotional AI for defence and security. Detects stress, deception, fatigue, and cognitive readiness in real time. No contact. No wearables. A scientifically grounded polygraph alternative.",
   "/",
   "EchoDepth Defence — Emotional Intelligence for Critical Environments",
   "Camera-based emotional AI detecting stress, deception, fatigue, and cognitive readiness for defence, intelligence, and security.",
   HOMEPAGE_SCHEMA, "", HOMEPAGE_BODY, ""),

  ("/home/claude/vercel-site/solutions/deception-detection/index.html",
   "Polygraph Alternative UK | Credibility Assessment Technology | EchoDepth Defence",
   "A camera-only, FACS-grounded alternative to polygraph and EyeDetect. 43 facial Action Units in real time. Timestamped credibility assessment output for defence, intelligence, and border security. UK data residency. Air-gap deployable.",
   "/solutions/deception-detection/",
   "Polygraph Alternative UK — Credibility Assessment Technology | EchoDepth Defence",
   "Camera-only, FACS-grounded credibility assessment. 43 AU analysis. Structured evidential output. Polygraph alternative for UK defence and intelligence.",
   DECEPTION_SCHEMA, "", DECEPTION_BODY, "deception"),

  ("/home/claude/vercel-site/solutions/insider-threat/index.html",
   "Insider Threat Detection Software | Continuous Personnel Monitoring | EchoDepth Defence",
   "Camera-based continuous emotional anomaly monitoring for defence and high-security environments. Behavioural baseline profiling, SIEM integration, and real-time anomaly alerts for insider threat detection.",
   "/solutions/insider-threat/",
   "Insider Threat Detection — Continuous Emotional Monitoring | EchoDepth Defence",
   "Continuous camera-based behavioural monitoring. Emotional baseline profiling. SIEM integration. Insider threat detection for defence and security.",
   ORG_SCHEMA, "", INSIDER_BODY, "insider"),

  ("/home/claude/vercel-site/solutions/compliance/index.html",
   "Defence Training Effectiveness | Compliance Monitoring Technology | EchoDepth Defence",
   "Real-time engagement and comprehension scoring during mandatory defence training. DSAT-compatible audit records. LMS integration. Know if training is actually landing.",
   "/solutions/compliance/",
   "Defence Training Effectiveness — Compliance Monitoring | EchoDepth Defence",
   "Real-time engagement scoring during mandatory training. DSAT-compatible. LMS integration. Know if training is actually landing.",
   ORG_SCHEMA, "", COMPLIANCE_BODY, "compliance"),

  ("/home/claude/vercel-site/solutions/operator-readiness/index.html",
   "Operator Fatigue Monitoring | Cognitive Load Detection | EchoDepth Defence",
   "Real-time operator readiness and fatigue monitoring for UAS pilots, SOC analysts, and control room operators. Pre-mission readiness scoring, live cognitive load alerts, and post-incident reconstruction.",
   "/solutions/operator-readiness/",
   "Operator Fatigue Monitoring — Cognitive Readiness | EchoDepth Defence",
   "Real-time fatigue and cognitive load monitoring for drone operators, SOC analysts, and control rooms.",
   ORG_SCHEMA, "", OPERATOR_BODY, ""),

  ("/home/claude/vercel-site/technology/index.html",
   "FACS Emotion Recognition Technology | EchoDepth Engine | Facial AU Analysis",
   "EchoDepth analyses 43 FACS-compliant facial Action Units in real time. Camera-only. REST API. Air-gap deployable. VAD mapping. GDPR-compliant. Built for defence, intelligence, and security integration.",
   "/technology/",
   "EchoDepth Engine — FACS Facial AU Analysis Technology",
   "43 FACS-compliant Action Units. Camera-only. REST API. On-premise deployment. Built for defence and security.",
   ORG_SCHEMA, "", TECH_BODY, "tech"),

  ("/home/claude/vercel-site/contact/index.html",
   "Request a Defence Security Briefing | EchoDepth Defence",
   "Request a structured technical briefing for defence procurement, security leadership, or intelligence teams. NDA available. Air-gapped demo environment on request. Cardiff, Wales.",
   "/contact/",
   "Request a Briefing — EchoDepth Defence",
   "Structured technical briefings for defence procurement and security leadership. NDA available.",
   CONTACT_SCHEMA, "", CONTACT_BODY, "contact"),

  ("/home/claude/vercel-site/404.html",
   "Page Not Found | EchoDepth Defence",
   "Page not found.",
   "/",
   "404 — EchoDepth Defence",
   "Page not found.",
   ORG_SCHEMA, "", NOT_FOUND_BODY, ""),
]

for path, title, desc, canonical, og_title, og_desc, schema, head_extra, body, active in pages:
    html = page(title, desc, canonical, og_title, og_desc, schema, head_extra, body, active)
    with open(path, 'w') as f:
        f.write(html)
    print(f"✓ {path}")

print("\nAll pages generated.")
