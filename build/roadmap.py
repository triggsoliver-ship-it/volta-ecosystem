import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from shared import SITES, ORDER, ROLES, GOLD, v_mark

G, T, M, C, I, A = [SITES[k] for k in ORDER]

CSS = """
@page{size:A4;margin:16mm 14mm 16mm 14mm}
*{box-sizing:border-box}
body{font-family:"Archivo",system-ui,sans-serif;color:#121212;font-size:10.5pt;line-height:1.45;margin:0}
h1{font-size:34pt;font-weight:800;line-height:.95;letter-spacing:-.02em;text-transform:uppercase;margin:0 0 10pt}
h2{font-size:20pt;font-weight:800;line-height:1.05;margin:0 0 8pt;letter-spacing:-.01em}
h3{font-size:12pt;font-weight:800;margin:0 0 4pt}
p{margin:0 0 7pt}
a{color:#14355E}
.page{page-break-after:always}
.page:last-child{page-break-after:auto}
.kicker{font-weight:700;color:#A8853A;font-size:9.5pt;margin:0 0 6pt}
.lede{font-size:12pt;line-height:1.4;color:#3A3732;max-width:70ch}
.mute{color:#6E6A62;font-size:9pt}
.cover{height:257mm;display:flex;flex-direction:column;justify-content:space-between;border-top:10pt solid #C9A24B;padding-top:18pt}
.cover .vm{width:120pt}
.bar{background:#121212;color:#fff;padding:7pt 10pt;font-weight:700;font-size:9pt;letter-spacing:.08em;text-transform:uppercase;margin:0 0 14pt;display:flex;justify-content:space-between}
.bar i{color:#C9A24B;font-style:normal}
table{width:100%;border-collapse:collapse;font-size:9.5pt;margin:6pt 0 10pt}
th,td{text-align:left;padding:6pt 8pt 6pt 0;border-bottom:1px solid #D9D2C3;vertical-align:top}
th{border-bottom:2px solid #121212;font-weight:700}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12pt}
.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12pt}
.cell{border-top:3pt solid #C9A24B;padding-top:6pt}
.cell p{color:#3A3732;margin:0}
.step{display:grid;grid-template-columns:34pt 1fr;gap:8pt;padding:7pt 0;border-bottom:1.5px solid #121212;align-items:start}
.step::before{content:attr(data-n);font-weight:800;font-size:20pt;line-height:1;color:#A8853A}
.step p{margin:0;color:#3A3732}
.steps{border-top:1.5px solid #121212;margin-bottom:10pt}
.flow{display:flex;border:1.5px solid #121212;border-radius:4pt;overflow:hidden;margin:6pt 0 12pt}
.flow div{flex:1;padding:7pt 6pt;border-right:1.5px solid #121212;font-weight:700;font-size:8pt;text-transform:uppercase;letter-spacing:.04em}
.flow div:last-child{border-right:0}
.flow div.on{background:#C9A24B;color:#fff}
.flow div small{display:block;text-transform:none;letter-spacing:0;font-weight:500;color:#6E6A62;font-size:7.5pt;margin-top:2pt}
.flow div.on small{color:#fff;opacity:.9}
.site{display:grid;grid-template-columns:54pt 1fr;gap:10pt;align-items:center;border:1.5px solid #121212;border-radius:4pt;padding:9pt 10pt;margin-bottom:8pt}
.site h3{margin:0 0 2pt}
.site p{margin:0;font-size:9.5pt;color:#3A3732}
.site a{font-weight:700;font-size:10pt;word-break:break-all}
.pill{display:inline-block;border:1.5px solid #121212;border-radius:999pt;padding:2pt 8pt;font-weight:600;font-size:8.5pt;margin:0 4pt 4pt 0}
.foot{position:fixed;bottom:-8mm;left:0;right:0;font-size:8pt;color:#6E6A62;display:flex;justify-content:space-between}
.check{list-style:none;padding:0;margin:0}
.check li{padding:4pt 0 4pt 18pt;position:relative;border-bottom:1px solid #D9D2C3}
.check li::before{content:"";position:absolute;left:0;top:6pt;width:9pt;height:9pt;border:1.5px solid #121212;border-radius:2pt}
.check li.done::before{background:#0F5F3C;border-color:#0F5F3C}
.check li.done::after{content:"";position:absolute;left:3pt;top:7.5pt;width:3pt;height:5pt;border:solid #fff;border-width:0 1.5pt 1.5pt 0;transform:rotate(45deg)}
"""


def site_card(k):
    s = SITES[k]
    return (f'<div class="site">{v_mark(s["accent"], s["symbol"], 50)}<div><h3>{s["name"]}</h3>'
            f'<p>{ROLES[k]} · {s["tag"]}</p><a href="{s["url"]}/">{s["url"]}</a></div></div>')


html = f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>Volta ecosystem launch roadmap</title>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>

<section class="page"><div class="cover">
<div>{v_mark(GOLD, 'mark', 120, 'vm')}
<p class="kicker" style="margin-top:28pt">Volta ecosystem · Launch roadmap · 19 October 2026</p>
<h1>Six sites.<br>One connected<br>Volta.</h1>
<p class="lede">How the Volta ecosystem websites are built, how they link together, where they are live today, and the plan to take them from partner preview to public launch and strong Google visibility.</p></div>
<div><div class="grid3">
<div class="cell"><h3>Live today</h3><p>Six sites deployed on Vercel, each with its own shareable link, all cross-linked.</p></div>
<div class="cell"><h3>For</h3><p>Rene Schuster, Oli Triggs and the Volta business partners.</p></div>
<div class="cell"><h3>Prepared by</h3><p>Ship It Studio web and ecosystem build, from the four Volta strategy documents.</p></div>
</div><p class="mute" style="margin-top:14pt">Confidential partner preview. Links are live preview addresses on Vercel; custom domains follow in Phase 2.</p></div>
</div></section>

<section class="page">
<div class="bar"><span>01 <i>/</i> The ecosystem</span><span>Volta launch roadmap</span></div>
<p class="kicker">What has been built</p>
<h2>One family identity. Six parts, each with its own site.</h2>
<p class="lede">Every site shares the Volta V mark with a gold outline, the Archivo type system and the same page structure, then takes its own colour and secondary symbol from the Volta logo brief. Each site carries an ecosystem section and footer that links to all six, so a partner can land anywhere and reach everything.</p>
<div class="flow"><div class="on">Media<small>Stories that build trust</small></div><div>Lead generation<small>Qualified enquiries</small></div><div>Intelligence<small>Who needs what</small></div><div>CRM<small>Relationships with memory</small></div><div>Opportunities<small>Assessments, mandates, deals</small></div><div class="on">Commercial growth<small>Repeatable, measurable</small></div></div>
<table><thead><tr><th>Site</th><th>Role in the ecosystem</th><th>Colour and symbol</th><th>Primary audience</th></tr></thead><tbody>
<tr><td><b>Volta</b> (hub)</td><td>Group story, ecosystem map, scaling plan, roadmap</td><td>Gold on ivory, diamond</td><td>Partners, investors, press</td></tr>
<tr><td><b>Team Volta</b></td><td>Player development, assessments, pathways, parents</td><td>Team Volta red, boy and football</td><td>Players, families, coaches</td></tr>
<tr><td><b>Volta Management</b></td><td>Representation, athlete care, One Player One Team</td><td>Black and gold, star</td><td>Players, clubs, agents</td></tr>
<tr><td><b>Volta Consultancy</b></td><td>Club acquisitions, MCO, investor mandates</td><td>Forest green and gold, circle</td><td>Investors, family offices, advisers</td></tr>
<tr><td><b>Volta Intelligence</b></td><td>Global football CRM and opportunity engine</td><td>Navy and gold, node</td><td>Agencies, clubs, scouts, tech partners</td></tr>
<tr><td><b>Volta Africa</b></td><td>African talent intelligence, Ghana pilot</td><td>Sunset orange and gold, sun</td><td>Clubs, academies, federations, investors</td></tr>
</tbody></table>
<div class="grid">
<div class="cell"><h3>Built in</h3><p>Hand-written static HTML with inline CSS: nothing to break, fastest possible load, perfect Lighthouse scores achievable. Source on GitHub at <a href="https://github.com/triggsoliver-ship-it/volta-ecosystem">triggsoliver-ship-it/volta-ecosystem</a>; each folder deploys as its own Vercel project on every push.</p></div>
<div class="cell"><h3>Already in every page</h3><p>Semantic headings, meta description, canonical URL, Open Graph and Twitter cards, Organization JSON-LD with parent-organisation and sameAs links across the family, sitemap.xml, robots.txt, security headers, mobile layout, keyboard focus states and reduced-motion support.</p></div>
</div>
</section>

<section class="page">
<div class="bar"><span>02 <i>/</i> Live links</span><span>Volta launch roadmap</span></div>
<p class="kicker">Share these with partners</p>
<h2>Every part of the ecosystem is clickable today.</h2>
<p class="lede">All six are public preview addresses with no login. Tap any one and use the ecosystem section or footer to move between sites.</p>
{''.join(site_card(k) for k in ORDER)}
<p class="mute">Preview addresses stay live permanently and will redirect to the custom domains once those are connected.</p>
</section>

<section class="page">
<div class="bar"><span>03 <i>/</i> Launch phases</span><span>Volta launch roadmap</span></div>
<p class="kicker">From partner preview to public launch</p>
<h2>Four phases. Each one ends with something partners can see.</h2>
<div class="steps">
<div class="step" data-n="01"><div><h3>Partner preview · now to end of October 2026</h3><p>Six sites live on Vercel preview links. Circulate to Rene, business partners and the technology partner alongside the four strategy documents. Collect feedback on positioning, wording and anything that must not be public. Supply the final vector logos from the logo brief and any real photography and footage.</p></div></div>
<div class="step" data-n="02"><div><h3>Domains and brand lock · November 2026</h3><p>Register and connect custom domains (see page 05), swap the Vercel preview links in every footer and sitemap for the real domains in one build, add the final logos, team biographies, contact routing and a real inbox behind every enquiry form. Add Google Analytics 4 and Google Search Console to every property.</p></div></div>
<div class="step" data-n="03"><div><h3>Public launch and content engine · December 2026 to January 2027</h3><p>Submit sitemaps, verify all six in Search Console, publish the first Team Volta stories (The Journey, Built Not Discovered), the Volta Management One Player One Team explainer, and the first Volta Consultancy Football Investment Brief. Launch the regional assessment landing pages so lead generation starts.</p></div></div>
<div class="step" data-n="04"><div><h3>Platform and Africa · 2027</h3><p>Volta Intelligence moves from marketing site to product login as Phase 1 of the CRM ships. Volta Africa gains the Ghana pilot pages, partner portal and, once evidence is credible, verified club access. Sites begin to share live data (assessment calendars, stories, opportunities) from the CRM.</p></div></div>
</div>
<div class="grid">
<div class="cell"><h3>Decisions needed from Volta</h3><p>Which domains to register · the public contact email or CRM inbox for enquiries · approval of all copy, especially claims about credentials and relationships · which real players and stories may appear with consent · whether Volta Africa is public now or stays partner-only until the pilot is agreed.</p></div>
<div class="cell"><h3>What is deliberately not on the sites yet</h3><p>Real player names as clients, team biographies, photography, pricing, and any guarantee language. Everything published is drawn from the four Volta documents and framed as current activity or proposals, not promises.</p></div>
</div>
</section>

<section class="page">
<div class="bar"><span>04 <i>/</i> Search visibility</span><span>Volta launch roadmap</span></div>
<p class="kicker">How Volta ranks</p>
<h2>Google rewards the same thing Volta does: proof, consistency and real stories.</h2>
<p class="lede">There is no trick that beats being the most useful, best-connected set of pages for the searches that matter. The plan below is the full playbook, in the order that works.</p>
<div class="grid">
<div class="cell"><h3>Foundation (done)</h3><p>Static pages that load in under a second · one clear H1 per page with the search intent in it · descriptive titles and meta descriptions · canonical URLs · Organization schema linking all six sites as one family · sitemap and robots on every property · mobile-first layout.</p></div>
<div class="cell"><h3>Entity building (Phase 2)</h3><p>Six sites with sameAs and parentOrganization schema teach Google that Volta is one entity. Add a Google Business Profile for Volta, LinkedIn company pages per division linking back, consistent name and description everywhere, and a Wikipedia-style "About Volta" page on the hub.</p></div>
<div class="cell"><h3>Search terms to own</h3><p><span class="pill">football assessment days UK</span><span class="pill">released academy player trial</span><span class="pill">football agent UK</span><span class="pill">football club acquisition advisory</span><span class="pill">multi-club ownership consultancy</span><span class="pill">football scouting CRM</span><span class="pill">Ghana football scouting</span><span class="pill">African football talent</span></p></div>
<div class="cell"><h3>Content engine (Phase 3 on)</h3><p>The 35/30/20/15 media mix becomes pages, not just posts: one regional assessment page per city, one story page per verified journey, one investment brief per quarter. Each is a new indexable page with internal links to the right division. This is where ranking compounds.</p></div>
<div class="cell"><h3>Links and authority</h3><p>Every piece of coverage, partner site, charity (Street to School), club or academy relationship links to the relevant Volta site. Cross-links between the six sites already pass authority around the family.</p></div>
<div class="cell"><h3>Measure monthly</h3><p>Search Console impressions and clicks per site, Core Web Vitals (all green by design), enquiries by source via campaign-tagged links, and which pages bring assessment registrations or investor conversations.</p></div>
</div>
</section>

<section class="page">
<div class="bar"><span>05 <i>/</i> Domains and technical</span><span>Volta launch roadmap</span></div>
<p class="kicker">Recommended domain structure</p>
<h2>One root brand, clear sub-brands.</h2>
<p class="lede">Availability must be checked at the point of purchase. The preference order is a single memorable root for the hub, with each division on its own domain or a clean subdomain, matching the Prime Origins pattern.</p>
<table><thead><tr><th>Site</th><th>First choice</th><th>Alternatives</th></tr></thead><tbody>
<tr><td>Volta hub</td><td>volta.football or voltagroup.co.uk</td><td>volta-group.com · wearevolta.com</td></tr>
<tr><td>Team Volta</td><td>teamvolta.co.uk</td><td>team.volta.football · teamvolta.com</td></tr>
<tr><td>Volta Management</td><td>voltamanagement.co.uk</td><td>management.volta.football</td></tr>
<tr><td>Volta Consultancy</td><td>voltaconsultancy.co.uk</td><td>consultancy.volta.football</td></tr>
<tr><td>Volta Intelligence</td><td>voltaintelligence.com</td><td>intelligence.volta.football · volta-intel.com</td></tr>
<tr><td>Volta Africa</td><td>voltaafrica.com</td><td>africa.volta.football · volta.africa</td></tr>
</tbody></table>
<div class="grid">
<div class="cell"><h3>Technical checklist to public launch</h3><ul class="check">
<li class="done">Six Vercel projects, one GitHub repo, auto-deploy on push</li>
<li class="done">Public preview links, no Vercel login wall</li>
<li class="done">SEO meta, schema, sitemaps, robots, security headers</li>
<li class="done">Cross-links on every site, ecosystem section and footer</li>
<li>Custom domains connected and HTTPS verified</li>
<li>Enquiry forms wired to a Volta inbox or CRM</li>
<li>Social preview images (og.png) per site</li>
<li>Google Analytics 4 and Search Console on all six</li>
<li>Final vector logos and photography added</li>
<li>Privacy policy and cookie notice pages</li>
</ul></div>
<div class="cell"><h3>Why static sites now</h3><p>Partners judge the vision, not the stack. Static pages are the fastest to share, impossible to take down by a bug, cheap to host and the easiest for Google to crawl. When Volta Intelligence ships its product, the marketing site stays and the app lives at app.&lt;domain&gt;, exactly as Prime Origins does.</p>
<h3 style="margin-top:10pt">Hosting and cost</h3><p>Vercel hosting for six static sites sits within the existing plan. Domains are the only new cost: typically £10 to £40 a year each, more for premium names such as volta.football.</p></div>
</div>
<p class="mute" style="margin-top:12pt">Source: Volta Logo Evolution Brief, Volta Ecosystem 1-2, Unlocking African Football Talent, Volta Media Engine and Volta Intelligence (all October 2026). Preview links generated 19 October 2026.</p>
</section>
</body></html>"""

out = os.path.join(os.path.dirname(__file__), "..", "roadmap.html")
open(out, "w").write(html)
print(out)
