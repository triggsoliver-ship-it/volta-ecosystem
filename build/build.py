import os, sys, json, shutil
sys.path.insert(0, os.path.dirname(__file__))
from shared import *
from data import FIXTURES, TRACK, TEAM_JOURNEYS, MANAGEMENT_JOURNEYS, MEDIA_MIX

OUT = os.path.join(os.path.dirname(__file__), "..", "sites")
G, T, M, C, I, A = [SITES[k] for k in ORDER]
GROUP_URL = G["url"]
PARTNERS_URL = GROUP_URL + "/partners"

TEAM_DISCLAIMER = ("Team Volta operates as an independent player development and training organisation. "
                   "Participation does not guarantee professional opportunities or representation. Any introductions to "
                   "professional advisory or representation services are entirely optional, arranged separately and subject "
                   "to applicable regulations and necessary consents.")


def write(site_key, html, path="index.html", extra=None, protect=None):
    d = os.path.join(OUT, site_key)
    p = os.path.join(d, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(html)
    if path == "index.html":
        open(os.path.join(d, "sitemap.xml"), "w").write(sitemap(site_key))
        open(os.path.join(d, "robots.txt"), "w").write(robots(site_key))
        open(os.path.join(d, "vercel.json"), "w").write(VERCEL_JSON)
    if protect is not None:
        open(os.path.join(d, "middleware.js"), "w").write(middleware_js(protect))
        open(os.path.join(d, "package.json"), "w").write(PACKAGE_JSON)
    for name, content in (extra or {}).items():
        q = os.path.join(d, name)
        os.makedirs(os.path.dirname(q), exist_ok=True)
        open(q, "w").write(content)


def ribbon(items, sep="◆"):
    one = "".join(f"<span>{x}</span><i>{sep}</i>" for x in items)
    return f'<div class="ribbon" aria-hidden="true">{one * 3}</div>'


def stats(track, dark=False):
    cells = "".join(f'<div class="stat"><b>{n}</b><span>{l}</span></div>' for n, l in track)
    return f'<div class="grid g4">{cells}</div>'


def alloc_bar():
    cols = [T["accent"], "#121212", GOLD, "#6E6A62", "#14355E"]
    bar = "".join(f'<div style="width:{p}%;background:{c}">{p}%</div>' for (p, _), c in zip(MEDIA_MIX, cols))
    leg = "".join(f'<div><i style="background:{c}"></i>{l}</div>' for (_, l), c in zip(MEDIA_MIX, cols))
    return f'<div class="alloc">{bar}</div><div class="legend" style="grid-template-columns:repeat(5,1fr)">{leg}</div>'


def fixtures_archive():
    rows = ""
    for year in sorted(FIXTURES):
        chips = "".join(f'<span>{opp}<small>{when}</small></span>' for opp, when in FIXTURES[year])
        rows += f'<div class="yr"><b>{year}</b><div class="fx">{chips}</div></div>'
    return rows, sum(len(v) for v in FIXTURES.values())


def journeys(items, label):
    out = ""
    for it in items:
        steps = " → ".join(x for x in it[:3] if x)
        who = it[3] if len(it) > 3 else ""
        out += f'<div class="journey"><div class="path">{steps}</div><div class="who">{label}{" · " + who if who else ""}</div></div>'
    return f'<div class="grid g3">{out}</div>'


# =================================================================== VOLTA SPORTS (public front door)
def hub_public():
    k = "volta-group"
    links = [("#divisions", "Divisions"), ("#record", "Track record"), ("#values", "Values")]
    h = head(k, "Volta Sports | Player development, athlete management and football advisory",
             "Volta Sports brings together Team Volta player development and assessments, Volta Management athlete representation, and Volta Consultancy football investment advisory.")
    h += header(k, links)
    h += f"""<section class="hero"><div class="wrap">
<div><p class="kicker">Volta Sports</p>
<h1>Developed, not just discovered.</h1>
<p class="lede" style="margin-top:26px">Player development, athlete management and football advisory, built on results and word of mouth. Three specialist teams, one set of values.</p>
<div class="cta"><a class="btn" href="#divisions">Find the right team</a><a class="btn ghost" href="{SHOWCASE_APPLY}">Apply for an assessment</a></div></div>
{v_mark(G['accent'], 'mark', 300, 'big')}
</div></section>
{ribbon(["Development before exposure", "Resilience and character", "Personal responsibility", "The support system", "The right pathway", "Long-term relationships"])}
<section class="sec" id="divisions"><div class="wrap">
<div class="head"><p class="kicker">Divisions</p><h2>Three specialist teams. Choose the one that fits you.</h2></div>
<div class="grid g3">
<div class="cell" style="border-color:{T['accent']}"><h3>Team Volta</h3><p>Assessment camps, weekly training groups, showcase fixtures against professional academies, analysis and mentoring. For grassroots, academy and released players.</p><p style="margin-top:12px"><a href="{T['url']}/">Visit Team Volta ↗</a> · <a href="{SHOWCASE_APPLY}">Apply for a camp ↗</a></p></div>
<div class="cell" style="border-color:{M['accent']}"><h3>Volta Management</h3><p>Representation and long-term career management for professional and emerging players, with global reach and a full support team around each athlete.</p><p style="margin-top:12px"><a href="{M['url']}/">Visit Volta Management ↗</a></p></div>
<div class="cell" style="border-color:{C['accent']}"><h3>Volta Consultancy</h3><p>Club acquisitions, multi-club ownership, stakeholder management and academy solutions for qualified investors and ownership groups.</p><p style="margin-top:12px"><a href="{C['url']}/">Visit Volta Consultancy ↗</a></p></div>
</div>
<p class="mute" style="margin-top:26px">Each division operates separately. Training with Team Volta never requires or implies representation by Volta Management.</p>
</div></section>
<section class="sec dark" id="record"><div class="wrap">
<div class="head"><p class="kicker">Track record</p><h2>Real opportunities. Proven progression.</h2>
<p class="lede">Since 2020, Team Volta players have tested themselves against academy and club opposition across England.</p></div>
{stats(TRACK)}
</div></section>
<section class="sec" id="values"><div class="wrap"><div class="split">
<div><p class="kicker">Values</p><h2>What every part of Volta stands for.</h2>
<p class="lede">Volta grew from community football and education, including the Street to School charity in Ghana. The same values guide every session, every negotiation and every partnership.</p></div>
<div class="grid" style="gap:18px">
<div class="pitch"><h3>Development before exposure</h3><p class="mute">Make players better before presenting them.</p></div>
<div class="pitch"><h3>The support system</h3><p class="mute">Coaches, mentors, family and specialists each have a role.</p></div>
<div class="pitch"><h3>Long-term relationships</h3><p class="mute">Support is a continuing responsibility, not a transaction.</p></div>
</div></div></div></section>
"""
    h += ecosystem_section(k, title="Every Volta site, in one place.")
    h += contact_section(k, "Talk to Volta.", "For clubs, academies, partners and general enquiries. For assessments, use the Team Volta form or apply directly at showcasetrials.football.",
                         ["General enquiry", "Club or academy", "Partnership or sponsorship", "Media", "Other"])
    h += footer(k, links, "Volta Sports brings together player development, athlete management and football advisory under one set of values.")
    write(k, h, protect=["/partners", "/partners/:path*", "/api/:path*"])


# =================================================================== PARTNER HUB (private)
def hub_partners():
    k = "volta-group"
    links = [("#ecosystem", "Ecosystem"), ("#model", "How it connects"), ("#archive", "Showcase archive"), ("#players", "Player review"), ("#tools", "Tools")]
    h = head(k, "Volta partner hub | Strategy, ecosystem and roadmap", "Private partner hub for the Volta ecosystem.", path="/partners", noindex=True)
    h += header(k, links, home="/partners")
    _, n = fixtures_archive()
    h += f"""<section class="hero"><div class="wrap">
<div><p class="kicker">Partner hub · private</p>
<h1>The whole of Volta, for partners.</h1>
<p class="lede" style="margin-top:26px">The strategy, the full ecosystem, the showcase archive with footage, the player review and the enquiries inbox. Not linked from any public site and not indexed by search engines.</p>
<div class="cta"><a class="btn" href="/partners/inbox">Open the enquiries inbox</a><a class="btn ghost" href="#ecosystem">See all six sites</a></div></div>
{v_mark(G['accent'], 'mark', 300, 'big')}
</div></section>
"""
    h += ecosystem_section("partners", kicker="The Volta ecosystem", title="Six parts. Who sees what.",
                           intro="Public sites link only to what their audience needs. Team Volta stays separate from representation. Volta Intelligence is a partner preview and Volta Africa is password-protected until the Ghana pilot is agreed.",
                           keys=ORDER)
    h += f"""<section class="sec alt"><div class="wrap">
<div class="head"><p class="kicker">Access</p><h2>Public, preview and private.</h2></div>
<table><thead><tr><th>Site</th><th>Audience</th><th>Access now</th><th>Planned domain</th></tr></thead><tbody>
<tr><td>Volta Sports</td><td>Everyone: the front door</td><td>Public preview</td><td>voltasports.com (voltasports.co.uk redirects)</td></tr>
<tr><td>Partner hub</td><td>Volta partners only</td><td>Password</td><td>voltasports.com/partners</td></tr>
<tr><td>Team Volta</td><td>Players, parents, coaches</td><td>Public preview</td><td>showcasetrials.football (keeps every poster and QR code working)</td></tr>
<tr><td>Volta Management</td><td>Players, clubs, agents</td><td>Public preview</td><td>voltamanagement.co.uk</td></tr>
<tr><td>Volta Consultancy</td><td>Investors and advisers</td><td>Public preview</td><td>voltaconsultancy.co.uk (available to register)</td></tr>
<tr><td>Volta Intelligence</td><td>Partners, then clubs and agencies</td><td>Unlisted preview</td><td>voltaintelligence.ai or .co.uk (.com is taken)</td></tr>
<tr><td>Volta Africa</td><td>Partners only</td><td>Password</td><td>Decided when the pilot is agreed</td></tr>
</tbody></table></div></section>
<section class="sec dark" id="model"><div class="wrap">
<div class="head"><p class="kicker">How it connects</p><h2>Media finds the audience. Intelligence finds the opportunity.</h2>
<p class="lede">Two engines feed each other: Volta Media builds trust and demand; Volta Sports Tech turns validated football needs into software and mandate revenue.</p></div>
<div class="flow" style="border-color:#fff"><div class="on">Insight<small>Data and football stories</small></div><div style="border-color:#fff">Content<small>Trusted football media</small></div><div style="border-color:#fff">Audience<small>Players, agents, clubs, investors</small></div><div style="border-color:#fff">Demand<small>Qualified relationships</small></div><div class="on">Revenue<small>Mandates, subscriptions, services</small></div></div>
<div style="margin-top:44px"><h3 style="margin-bottom:14px">Revised media mix</h3>{alloc_bar()}</div>
</div></section>
<section class="sec" id="archive"><div class="wrap">
<div class="head"><p class="kicker">Showcase archive · footage</p><h2>{n} fixtures against academy and club opposition, 2020 to 2026.</h2>
<p class="lede">Fixtures with a ▶ open the full-match recording. Numbered links open separate recording parts. The public Team Volta site lists these fixtures without footage, because many recordings feature under-18 players.</p></div>
<div class="years" id="pfx"><p class="mute">Loading the footage archive…</p></div></div></section>
<section class="sec alt" id="players"><div class="wrap">
<div class="head"><p class="kicker">Player coaching and analysis · review copy 21 Oct 2026</p><h2>Seventeen player journeys, awaiting each player's consent.</h2>
<p class="lede">Public sites show club milestones only, with no names, until wording and consent are confirmed for each story.</p></div>
<div style="overflow-x:auto"><table><thead><tr><th>Player</th><th>Relationship to Volta</th><th>Club milestones</th><th>Coaching hours</th><th>Analysis hours</th></tr></thead><tbody id="pplayers"><tr><td colspan="5" class="mute">Loading…</td></tr></tbody></table></div>
<p class="mute" style="margin-top:14px">* Two coaching-hour figures differ between the source PDF and its workbook and are pending reconciliation.</p>
</div></section>
<section class="sec" id="tools"><div class="wrap">
<div class="head"><p class="kicker">Tools</p><h2>What partners can use today.</h2></div>
<div class="grid g3">
<div class="cell"><h3>Enquiries inbox</h3><p>Every enquiry from every Volta site, in one list, organised by division, with status, owner and notes.</p><p style="margin-top:12px"><a href="/partners/inbox">Open the inbox</a></p></div>
<div class="cell"><h3>Launch roadmap</h3><p>Roadmap v2 answers the October partner feedback and sets out the January mandate pilot. It is circulated to partners directly rather than hosted here.</p></div>
<div class="cell"><h3>Partner previews</h3><p><a href="{I['url']}/">Volta Intelligence ↗</a> (unlisted) and <a href="{A['url']}/">Volta Africa ↗</a> (same partner password).</p></div>
</div></div></section>
"""
    h += PARTNER_SCRIPT
    h += footer(k, links, "Private partner hub. Please don't forward the password outside the Volta partnership.", eco_keys=ORDER, home="/partners")
    h = h.replace('<a class="btn" href="#contact">Get in touch</a>', '<a class="btn" href="/partners/inbox">Inbox</a>').replace('<li><a href="#contact">Contact</a></li>', "")
    write(k, h, path="partners/index.html")


PARTNER_SCRIPT = """<script>
(function(){
function esc(s){return (s==null?'':String(s)).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
function safe(u){return /^https:\\/\\/www\\.dropbox\\.com\\//.test(u)?u:'#';}
fetch('/api/partner',{credentials:'same-origin'}).then(function(r){if(!r.ok)throw 0;return r.json();}).then(function(d){
 var fx=d.fixtures||{},html='';
 Object.keys(fx).sort().forEach(function(y){
  html+='<div class="yr"><b>'+esc(y)+'</b><div class="fx">'+fx[y].map(function(f){
   if(!f.links||!f.links.length)return '<span>'+esc(f.opp)+'<small>'+esc(f.when)+'</small></span>';
   if(f.links.length===1)return '<a href="'+safe(f.links[0])+'" target="_blank" rel="noopener">'+esc(f.opp)+'<small>'+esc(f.when)+' ▶</small></a>';
   return '<span>'+esc(f.opp)+'<small>'+esc(f.when)+' · parts</small> '+f.links.map(function(u,i){return '<a href="'+safe(u)+'" target="_blank" rel="noopener" style="padding:2px 6px">'+(i+1)+'</a>';}).join(' ')+'</span>';
  }).join('')+'</div></div>';
 });
 document.getElementById('pfx').innerHTML=html||'<p class="mute">No fixtures stored yet.</p>';
 document.getElementById('pplayers').innerHTML=(d.players||[]).map(function(p){return '<tr><td><b>'+esc(p.name)+'</b></td><td>'+esc(p.rel)+'</td><td>'+esc(p.milestones)+'</td><td>'+esc(p.hours)+'</td><td>To be confirmed</td></tr>';}).join('');
}).catch(function(){
 document.getElementById('pfx').innerHTML='<div class="notice"><b>The archive could not load.</b><p>Refresh the page. Footage and player details are held privately and load after sign-in.</p></div>';
 document.getElementById('pplayers').innerHTML='<tr><td colspan="5">Could not load. Refresh the page.</td></tr>';
});
})();
</script>
"""


def inbox_page():
    k = "volta-group"
    h = head(k, "Volta enquiries inbox", "Private inbox for Volta enquiries.", path="/partners/inbox", noindex=True)
    h += header(k, [("/partners", "Partner hub")], home="/partners").replace('<a class="btn" href="#contact">Get in touch</a>', "")
    divs = [("", "All divisions"), ("group", "Volta Sports"), ("team", "Team Volta"), ("showcase", "Showcases"), ("management", "Volta Management"),
            ("consultancy", "Volta Consultancy"), ("intelligence", "Volta Intelligence"), ("africa", "Volta Africa")]
    opts = "".join(f'<option value="{c}">{n}</option>' for c, n in divs)
    h += """<style>
.inbox{display:grid;gap:14px}.card{border:2px solid var(--ink);border-radius:6px;background:#fff;padding:18px}
.card header{display:flex;flex-wrap:wrap;gap:8px 16px;justify-content:space-between;align-items:baseline;margin-bottom:10px}
.tag{display:inline-block;border-radius:3px;padding:2px 8px;font-size:12px;font-weight:700;color:#fff;background:var(--ink)}
.st-new{background:#A51C24}.st-contacted{background:#14355E}.st-qualified{background:#C8541A}.st-won{background:#0F5F3C}.st-closed{background:#6E6A62}
.meta{font-size:14px;color:var(--ink-2)}.msg{white-space:pre-wrap;margin:10px 0 14px}
.tools{display:flex;flex-wrap:wrap;gap:10px;align-items:end;margin-bottom:22px}.tools label{font-size:13px}
.tools select{margin-top:4px;padding:9px 10px}.edit{display:grid;grid-template-columns:150px 160px 1fr auto;gap:10px;align-items:end}
@media (max-width:760px){.edit{grid-template-columns:1fr 1fr}}.edit input,.edit select{padding:9px 10px;margin-top:4px}
.edit .btn{padding:11px 14px}.counts{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px}.counts span{border:1.5px solid var(--ink);border-radius:999px;padding:4px 12px;font-size:13px;font-weight:600}
</style>
<section class="sec"><div class="wrap">
<div class="head"><p class="kicker">Enquiries inbox · private</p><h2>Every Volta enquiry, by division.</h2>
<p class="lede">New enquiries arrive here from every Volta site. Reply from the branded address shown on each card, then update the status so the team knows where it stands.</p></div>
<div class="tools"><label>Division<select id="fdiv">""" + opts + """</select></label>
<label>Status<select id="fst"><option value="">Any status</option><option>new</option><option>contacted</option><option>qualified</option><option>won</option><option>closed</option></select></label>
<button class="btn ghost" id="refresh" type="button">Refresh</button></div>
<div class="counts" id="counts"></div>
<div class="inbox" id="list"><p class="mute">Loading enquiries…</p></div>
</div></section>
<script>
var all=[];
function esc(s){return (s==null?'':String(s)).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
function render(){
 var d=document.getElementById('fdiv').value,s=document.getElementById('fst').value;
 var rows=all.filter(function(r){return (!d||r.division===d)&&(!s||r.status===s);});
 var c={};all.forEach(function(r){c[r.division_name]=(c[r.division_name]||0)+1;});
 document.getElementById('counts').innerHTML=Object.keys(c).map(function(k){return '<span>'+esc(k)+': '+c[k]+'</span>';}).join('')||'';
 var L=document.getElementById('list');
 if(!rows.length){L.innerHTML='<div class="notice"><b>No enquiries match.</b><p>New enquiries from any Volta site will appear here.</p></div>';return;}
 L.innerHTML=rows.map(function(r){
  var subj=encodeURIComponent('Re: your enquiry to '+r.division_name);
  return '<article class="card"><header><div><span class="tag st-'+esc(r.status)+'">'+esc(r.status)+'</span> <b>'+esc(r.name)+'</b> · '+esc(r.division_name)+'</div><span class="meta">'+new Date(r.created_at).toLocaleString('en-GB')+'</span></header>'
  +'<div class="meta">'+esc(r.enquiry_type||'')+(r.organisation?' · '+esc(r.organisation):'')+(r.age_group?' · '+esc(r.age_group):'')+(r.location?' · '+esc(r.location):'')+'</div>'
  +'<div class="msg">'+esc(r.message)+'</div>'
  +'<div class="meta">Email <a href="mailto:'+esc(r.email)+'?subject='+subj+'">'+esc(r.email)+'</a>'+(r.phone?' · Phone '+esc(r.phone):'')+' · Reply from <b>'+esc(r.reply_from)+'</b></div>'
  +'<form class="edit" data-id="'+r.id+'" style="margin-top:14px"><label>Status<select name="status">'+['new','contacted','qualified','won','closed'].map(function(x){return '<option'+(x===r.status?' selected':'')+'>'+x+'</option>';}).join('')+'</select></label>'
  +'<label>Owner<input name="owner" value="'+esc(r.owner)+'" maxlength="60"></label><label>Notes<input name="notes" value="'+esc(r.notes)+'" maxlength="1000"></label><button class="btn" type="submit">Save</button></form></article>';
 }).join('');
}
function load(){
 fetch('/api/inbox',{credentials:'same-origin'}).then(function(r){if(!r.ok)throw new Error(r.status);return r.json();})
 .then(function(j){all=j;render();})
 .catch(function(e){document.getElementById('list').innerHTML='<div class="notice"><b>The inbox could not load.</b><p>Refresh the page. If it keeps happening, the inbox key on Vercel may need resetting.</p></div>';});
}
document.getElementById('fdiv').onchange=render;document.getElementById('fst').onchange=render;document.getElementById('refresh').onclick=load;
document.addEventListener('submit',function(e){
 var f=e.target;if(!f.classList.contains('edit'))return;e.preventDefault();
 var b=f.querySelector('button');b.textContent='Saving…';
 fetch('/api/inbox',{method:'POST',credentials:'same-origin',headers:{'Content-Type':'application/json'},body:JSON.stringify({id:f.dataset.id,status:f.status.value,owner:f.owner.value,notes:f.notes.value})})
 .then(function(r){if(!r.ok)throw new Error();b.textContent='Saved';var row=all.find(function(x){return x.id===f.dataset.id;});row.status=f.status.value;row.owner=f.owner.value;row.notes=f.notes.value;setTimeout(render,700);})
 .catch(function(){b.textContent='Not saved, retry';});
});
load();
</script>
</body></html>"""
    write(k, h, path="partners/inbox/index.html")


API_INBOX = r"""// Private inbox API for the Volta partner hub. Protected by middleware.js (partner password).
// The database key never reaches the browser: it is the PARTNER_PASSWORD environment variable, checked by fingerprint in the database.
const URL_ = process.env.SUPABASE_URL;
const PUB = process.env.SUPABASE_PUBLISHABLE_KEY;
const KEY = process.env.PARTNER_PASSWORD; // same secret as the partner password gate

async function rpc(fn, body) {
  const r = await fetch(`${URL_}/rest/v1/rpc/${fn}`, {
    method: 'POST',
    headers: { apikey: PUB, 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  const text = await r.text();
  if (!r.ok) throw new Error(`database ${r.status}`);
  return text ? JSON.parse(text) : null;
}

const json = (data, status = 200) => new Response(JSON.stringify(data), {
  status, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' },
});

export async function GET() {
  try { return json(await rpc('partner_inbox_v2', { p_key: KEY })); }
  catch (e) { return json({ error: 'Inbox unavailable' }, 502); }
}

export async function POST(request) {
  let b;
  try { b = await request.json(); } catch (e) { return json({ error: 'Bad request' }, 400); }
  const statuses = ['new', 'contacted', 'qualified', 'won', 'closed'];
  if (!b || typeof b.id !== 'string' || !statuses.includes(b.status)) return json({ error: 'Bad request' }, 400);
  try {
    await rpc('partner_update', {
      p_key: KEY, p_id: b.id, p_status: b.status,
      p_owner: (b.owner || '').slice(0, 60) || null, p_notes: (b.notes || '').slice(0, 1000) || null,
    });
    return json({ ok: true });
  } catch (e) { return json({ error: 'Update failed' }, 502); }
}
"""


API_PARTNER = r"""// Partner-only content (player review, showcase footage links), held privately in the database.
// Protected by middleware.js; the database also checks the partner password fingerprint.
export async function GET() {
  try {
    const r = await fetch(`${process.env.SUPABASE_URL}/rest/v1/rpc/partner_content_v1`, {
      method: 'POST',
      headers: { apikey: process.env.SUPABASE_PUBLISHABLE_KEY, 'Content-Type': 'application/json' },
      body: JSON.stringify({ p_key: process.env.PARTNER_PASSWORD }),
    });
    if (!r.ok) throw new Error(String(r.status));
    return new Response(await r.text(), { headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' } });
  } catch (e) {
    return new Response(JSON.stringify({ error: 'Unavailable' }), { status: 502, headers: { 'Content-Type': 'application/json' } });
  }
}
"""


# =================================================================== TEAM VOLTA
def team():
    k = "team-volta"
    links = [("#camps", "Assessment camps"), ("#pathway", "Pathway"), ("#record", "Track record"), ("#archive", "Showcases"), ("#parents", "Parents")]
    h = head(k, "Team Volta | Developed Not Just Discovered — football assessments, training and showcases",
             "Team Volta assessment camps, weekly training and showcase fixtures against professional academies for grassroots, academy and released players. 40+ showcase fixtures, 100+ trials secured.")
    h += header(k, links)
    rows, n = fixtures_archive()
    h += f"""<section class="hero"><div class="wrap">
<div><p class="kicker">Team Volta · Developing excellence</p>
<h1>Developed Not Just Discovered</h1>
<p class="lede" style="margin-top:26px">We help players improve, get assessed fairly, prepare for the next opportunity and progress through the right pathway. Grassroots, academy and released players, with coaches and families alongside them.</p>
<div class="cta"><a class="btn" href="{SHOWCASE_APPLY}">Apply for an assessment camp</a><a class="btn ghost" href="#pathway">See the pathway</a></div></div>
{v_mark(T['accent'], 'player', 300, 'big')}
</div></section>
{ribbon(["Assessment", "Training", "Showcase", "Progression"], "›")}
<section class="sec" id="camps"><div class="wrap"><div class="split">
<div><p class="kicker">Assessment camps</p><h2>Where preparation meets opportunity.</h2>
<p class="lede">Two-day assessment camps run by UEFA-qualified coaches. Strong performers earn selection for a showcase fixture against a professional academy.</p>
<div class="cta"><a class="btn" href="{SHOWCASE_APPLY}">See dates and apply</a></div>
<p class="mute" style="margin-top:14px">Registration is handled at showcasetrials.football.</p></div>
<div class="grid g2" style="gap:18px">
<div class="journey"><div class="path">Southampton</div><div class="who">Two-day camp · <a href="{SHOWCASE_APPLY}?showcase-location=southampton">Apply ↗</a></div></div>
<div class="journey"><div class="path">Reading</div><div class="who">Two-day camp · <a href="{SHOWCASE_APPLY}?showcase-location=reading">Apply ↗</a></div></div>
<div class="notice" style="grid-column:1/-1"><b>New locations follow demand.</b><p>Tell us your town or postcode in the form below. Where interest clusters, we add camps.</p></div>
</div></div></div></section>
<section class="sec" id="pathway" style="padding-top:0"><div class="wrap">
<div class="head"><p class="kicker">The pathway</p><h2>An honest route forward.</h2>
<p class="lede">Opportunity follows preparation, growth and the right environment. Every player who comes to Volta gets structured feedback and a realistic next step, whatever the outcome.</p></div>
<div class="steps">
<div class="step"><div><h3>Assessment</h3><p>Regional assessment camps, identification events and referral assessments. Coaches record fair, structured development feedback for every player.</p></div></div>
<div class="step"><div><h3>Training</h3><p>Weekly training groups, individual technical sessions, strength and conditioning, osteopathy and recovery, training camps and position-specific guidance.</p></div></div>
<div class="step"><div><h3>Showcase</h3><p>Selection for showcase fixtures against professional academies, supported by match analysis, video and development plans.</p></div></div>
<div class="step"><div><h3>Progression</h3><p>As players continue to develop, Team Volta supports their progression towards suitable opportunities within the professional game. Where appropriate, players may also benefit from introductions to additional career development, advisory and professional support through our wider football network.</p></div></div>
</div>
<div class="notice" style="margin-top:28px"><b>Independent player development</b><p>{TEAM_DISCLAIMER}</p></div>
</div></section>
<section class="sec dark" id="record"><div class="wrap">
<div class="head"><p class="kicker">Track record</p><h2>Real opportunities. Proven progression.</h2></div>
{stats(TRACK)}
</div></section>
<section class="sec brandband" id="services"><div class="wrap">
<div class="head"><p class="kicker">What we do</p><h2>Everything around the player, not just the session.</h2></div>
<div class="grid g4">
<div class="cell" style="border-color:#fff"><h3>Training and identification</h3><ul style="color:#fff"><li>Assessment camps and ID events</li><li>Weekly training groups</li><li>Referral assessments</li><li>Showcase selection and fixtures</li></ul></div>
<div class="cell" style="border-color:#fff"><h3>Extra support</h3><ul style="color:#fff"><li>Strength and conditioning</li><li>Osteopathy and recovery</li><li>Individual technical sessions</li><li>Training camps</li></ul></div>
<div class="cell" style="border-color:#fff"><h3>Player analysis</h3><ul style="color:#fff"><li>Match and training analysis</li><li>Video clips and feedback</li><li>Position-specific guidance</li><li>Development plans</li></ul></div>
<div class="cell" style="border-color:#fff"><h3>Mentoring</h3><ul style="color:#fff"><li>Career and development guidance</li><li>Mindset and confidence</li><li>Trial and club transitions</li><li>Player and family support</li></ul></div>
</div></div></section>
<section class="sec" id="stories"><div class="wrap">
<div class="head"><span class="draft">Draft: names added once each player approves</span><p class="kicker">Player journeys</p><h2>The professionals' journeys were rarely straight lines either.</h2>
<p class="lede">Players coached by Volta staff have gone on to scholarships and professional contracts at home and abroad. Every journey started with preparation, setbacks and the right support.</p></div>
{journeys(TEAM_JOURNEYS, "Coached by Volta staff")}
<div style="margin-top:48px"><h3 style="margin-bottom:14px">How our media is balanced</h3>{alloc_bar()}</div>
</div></section>
<section class="sec alt" id="archive"><div class="wrap">
<div class="head"><p class="kicker">Showcase archive</p><h2>{n} showcase fixtures against academy and club opposition since 2020.</h2>
<p class="lede">The stage. The standard. The opportunity. Full-match recordings are available to clubs and partners on request.</p></div>
<div class="years">{rows}</div></div></section>
<section class="sec" id="parents"><div class="wrap"><div class="split">
<div><p class="kicker">For parents and guardians</p><h2>Safe, honest and worth your time.</h2>
<p class="lede">No guaranteed contracts. No false scarcity. No promises we cannot keep. Clear information, safeguarding and informed registration at every step.</p></div>
<div class="grid g2" style="gap:18px">
<div class="cell"><h3>Safeguarding first</h3><p>Consent, guardian involvement and limits on how young players' information and footage are used.</p></div>
<div class="cell"><h3>Structured feedback</h3><p>Every assessed player receives respectful feedback and realistic options.</p></div>
<div class="cell"><h3>Qualified people</h3><p>UEFA-qualified coaching and vetted specialists.</p></div>
<div class="cell"><h3>More than football</h3><p>Education, mentoring and community, including the Street to School charity in Ghana.</p></div>
</div></div></div></section>
"""
    h += ecosystem_section(k, title="Part of Volta Sports.", intro="Team Volta is the player development and training team within Volta Sports.")
    h += contact_section(k, "Take your next step.", "Tell us about the player, their age group and where you are. We will explain the camps and what happens next.",
                         ["Assessment camp enquiry", "Weekly training group", "Coach or specialist wanting to join", "Club or academy", "Parent or guardian question", "Other"],
                         "Send enquiry", player_fields=True)
    h += footer(k, links, "Team Volta develops grassroots, academy and released players through fair assessment, structured training and honest pathways.", disclaimer=TEAM_DISCLAIMER)
    write(k, h)


# =================================================================== MANAGEMENT
def management():
    k = "volta-management"
    links = [("#team", "One Player, One Team"), ("#record", "Track record"), ("#services", "Services"), ("#reach", "Global reach"), ("#how", "How we work")]
    h = head(k, "Volta Management | Athlete management and football representation with global reach",
             "Volta Management builds the team behind a player's career: contracts, global market access, performance development and long-term management. FIFA-licensed agent expertise. One Player, One Team.")
    h += header(k, links)
    h += f"""<section class="hero"><div class="wrap">
<div><p class="kicker">Volta Management</p>
<h1>Your career deserves more than representation.</h1>
<p class="lede" style="margin-top:26px">We build the team behind your progress. Coaching, analysis, performance specialists, management and family, coordinated around one athlete and one plan.</p>
<div class="cta"><a class="btn" href="#contact">Start a conversation</a><a class="btn ghost" href="#team">One Player, One Team</a></div></div>
{v_mark(M['accent'], 'star', 300, 'big')}
</div></section>
{ribbon(["One Player, One Team", "Contracts", "Global market access", "Performance development", "Long-term management"])}
<section class="sec" id="team"><div class="wrap"><div class="split">
<div><p class="kicker">Our philosophy</p><h2>One Player, One Team.</h2>
<p class="lede">Signing a player is the start. What matters is everything that follows: the decisions, the preparation, the people and the plan. Every Volta Management athlete gets a dedicated support team, not just an agent.</p></div>
<div class="steps">
<div class="step"><div><h3>The challenge</h3><p>A real career moment: a contract decision, a loan, a move abroad, a loss of form.</p></div></div>
<div class="step"><div><h3>The team</h3><p>Coaching, analysis, strength, recovery, mentoring and family, brought together and reviewed.</p></div></div>
<div class="step"><div><h3>The decisions</h3><p>Career planning with realistic options, not the biggest name on the list.</p></div></div>
<div class="step"><div><h3>The future</h3><p>Realistic next steps and a long-term responsibility to the athlete.</p></div></div>
</div></div></div></section>
<section class="sec alt" id="record"><div class="wrap">
<div class="head"><span class="draft">Draft: names, clubs and wording awaiting approval</span><p class="kicker">Track record</p><h2>Progression you can trace.</h2>
<p class="lede">Players coached and managed by Volta staff have signed professional contracts across England, Europe and the Middle East, and represented their country at youth level.</p></div>
{journeys(MANAGEMENT_JOURNEYS, "Coached and managed by Volta staff")}
</div></section>
<section class="sec dark" id="services"><div class="wrap">
<div class="head"><p class="kicker">Services</p><h2>Agency, advisory and athlete care in one place.</h2></div>
<div class="grid g3">
<div class="cell"><h3>Agency</h3><ul><li>Player intermediary</li><li>Club intermediary and recruitment mandates</li><li>Contract negotiation</li><li>International club introductions</li></ul></div>
<div class="cell"><h3>Player management and advisory</h3><ul><li>Long-term player support</li><li>Integrated performance services</li><li>Trial and club transitions</li><li>Player, family and club liaison</li></ul></div>
<div class="cell"><h3>Athlete care</h3><ul><li>Personal development plans</li><li>Commercial and image rights</li><li>Relocation and life administration</li><li>Education and mentoring</li></ul></div>
</div></div></section>
<section class="sec" id="reach"><div class="wrap">
<div class="head"><p class="kicker">Global reach</p><h2>Relationships on five continents.</h2>
<p class="lede">Volta Management works with clubs, agencies and decision-makers across Europe, Africa, Asia (including the Middle East), North America and South America.</p></div>
<div class="grid g4">
<div class="cell"><h3>Contracts</h3><p>Prepared, well-informed negotiation: structures, options, bonuses, sell-ons and the decisions behind them.</p></div>
<div class="cell"><h3>Market access</h3><p>Knowledge of clubs, pathways and transfer windows across five continents.</p></div>
<div class="cell"><h3>Performance development</h3><p>Technical, analytical, physical and recovery support brought together around the player.</p></div>
<div class="cell"><h3>Credentials</h3><p>FIFA-licensed agent expertise and UEFA-qualified coaching, operating within FIFA and national rules.</p></div>
</div></div></section>
<section class="sec alt" id="how"><div class="wrap"><div class="split">
<div><p class="kicker">How we work</p><h2>Professional, permissioned and separate.</h2>
<p class="lede">Volta Management is a separate representation service. Representation is only ever offered where it is appropriate, lawful and agreed in writing with the player and, for younger players, their family. Training with any Volta programme never requires or implies representation.</p></div>
<div class="grid" style="gap:18px">
<div class="pitch"><h3>No guaranteed outcomes</h3><p class="mute">We show the work, not a promise of a contract.</p></div>
<div class="pitch"><h3>Written agreements</h3><p class="mute">Scope, fees and conflicts set out before we act.</p></div>
<div class="pitch"><h3>Regulation first</h3><p class="mute">Licence, mandate, conflict and minors checks before any approach.</p></div>
<div class="pitch"><h3>Measurable support</h3><p class="mute">Before, during and after a contract or transfer.</p></div>
</div></div></div></section>
"""
    h += ecosystem_section(k, title="Part of Volta Sports.", intro="Volta Management is the representation and athlete-management team within Volta Sports.")
    h += contact_section(k, "Let's talk about your career.", "For players, families and clubs. Tell us where you are and what you are trying to achieve.",
                         ["Player enquiry", "Family or guardian", "Club: recruitment mandate", "Club: other", "Agent partnership", "Other"], "Start a conversation")
    h += footer(k, links, "Volta Management is the representation and athlete-management team within Volta Sports. We build the team behind your progress.")
    write(k, h)


# =================================================================== CONSULTANCY
def consultancy():
    k = "volta-consultancy"
    links = [("#services", "Services"), ("#engine", "How we find opportunities"), ("#process", "Process"), ("#who", "Who we work with")]
    h = head(k, "Volta Consultancy | Football club acquisitions, multi-club ownership and investment advisory",
             "Independent football-market expertise for qualified investors, family offices and ownership groups: club acquisitions, multi-club ownership, academy strategy and advisory mandates, backed by research-led investor and club intelligence.")
    h += header(k, links)
    h += f"""<section class="hero"><div class="wrap">
<div><p class="kicker">Volta Consultancy</p>
<h1>Identify the right capital. Build the right relationships.</h1>
<p class="lede" style="margin-top:26px">Independent football-market expertise for qualified investors and ownership groups: club evaluation, acquisition, multi-club structures and what happens after the deal.</p>
<div class="cta"><a class="btn" href="#contact">Request a private conversation</a><a class="btn ghost" href="#engine">How we find opportunities</a></div></div>
{v_mark(C['accent'], 'circle', 300, 'big')}
</div></section>
{ribbon(["Club acquisitions", "Multi-club ownership", "Stakeholder management", "Academy solutions"])}
<section class="sec" id="services"><div class="wrap">
<div class="head"><p class="kicker">Services</p><h2>From first thesis to post-acquisition operations.</h2></div>
<div class="grid g4">
<div class="cell"><h3>Club acquisitions</h3><p>Target identification, club evaluation, transaction stages, ownership structures and due diligence coordination.</p></div>
<div class="cell"><h3>Multi-club development</h3><p>Designing and operating multi-club structures with coherent sporting and commercial logic.</p></div>
<div class="cell"><h3>Stakeholder management</h3><p>Governing bodies, leagues, local authorities, supporters and existing owners, handled with discretion.</p></div>
<div class="cell"><h3>Academy and football business</h3><p>Academy strategy, recruitment operations and football business improvement after the deal.</p></div>
</div></div></section>
<section class="sec dark" id="engine"><div class="wrap">
<div class="head"><p class="kicker">How we find opportunities</p><h2>Research-led intelligence on investors and clubs.</h2>
<p class="lede">Volta Consultancy is supported by a research engine that tracks public signals of football investment interest and club ownership change, then turns them into short, evidence-backed briefings our advisers act on personally.</p></div>
<div class="grid g4">
<div class="cell"><h3>Signals</h3><p>Published ownership changes, club sale processes, investment announcements, minority stake activity and multi-club moves.</p></div>
<div class="cell"><h3>Profiles</h3><p>Investor and ownership-group profiles built from public sources: past football deals, stated interests and preferred markets.</p></div>
<div class="cell"><h3>Prioritisation</h3><p>Each opportunity scored for fit, timing and route of approach, with its sources shown.</p></div>
<div class="cell"><h3>Personal outreach</h3><p>Drafted introductions reviewed and sent by a Volta adviser. Never automated mass email.</p></div>
</div>
<p class="mute" style="margin-top:28px">We use only public or directly shared information and never infer private wealth. Investor relationships and mandates are held in a separate, access-controlled consultancy record.</p>
</div></section>
<section class="sec" id="process"><div class="wrap">
<div class="head"><p class="kicker">Process</p><h2>From credible signal to signed mandate.</h2></div>
<div class="steps">
<div class="step"><div><h3>Signal</h3><p>Public or directly disclosed interest in football ownership, with source and confidence.</p></div></div>
<div class="step"><div><h3>Research</h3><p>Investor profile, investment thesis and the appropriate professional route.</p></div></div>
<div class="step"><div><h3>Approach</h3><p>A bespoke, adviser-reviewed introduction.</p></div></div>
<div class="step"><div><h3>Qualify</h3><p>Objectives, funding parameters, preferred markets and timing.</p></div></div>
<div class="step"><div><h3>Mandate</h3><p>Scope, confidentiality, conflicts, engagement terms and fees.</p></div></div>
<div class="step"><div><h3>Source and execute</h3><p>Shortlist clubs or assets, coordinate advisers, support the transaction and what follows.</p></div></div>
</div></div></section>
<section class="sec alt" id="who"><div class="wrap">
<div class="head"><p class="kicker">Who we work with</p><h2>Qualified investors and the people who advise them.</h2></div>
<div class="grid g4">
<div class="cell"><h3>Individuals and family offices</h3><p>With publicly expressed or directly confirmed football investment ambitions.</p></div>
<div class="cell"><h3>Existing ownership groups</h3><p>Evaluating another club, an academy investment or a multi-club structure.</p></div>
<div class="cell"><h3>Strategic investors</h3><p>Considering football-related commercial or operational opportunities.</p></div>
<div class="cell"><h3>Professional advisers</h3><p>Lawyers, corporate finance, accountants and trusted intermediaries.</p></div>
</div></div></section>
"""
    h += ecosystem_section(k, title="Part of Volta Sports.", intro="Volta Consultancy is the investment and acquisition advisory team within Volta Sports.")
    h += contact_section(k, "A private, qualified conversation.", "If you are weighing a football investment, tell us the markets, structures and timing you have in mind. We reply directly and in confidence.",
                         ["Investor or family office", "Ownership group", "Professional adviser referral", "Club seeking investment", "Other"], "Request a conversation")
    h += footer(k, links, "Volta Consultancy provides independent football-market expertise for qualified investors and ownership groups.")
    write(k, h)


# =================================================================== INTELLIGENCE (unlisted partner preview)
def intelligence():
    k = "volta-intelligence"
    links = [("#pilot", "January pilot"), ("#usecase", "How a mandate works"), ("#modules", "Platform"), ("#data", "Data"), ("#trust", "Trust")]
    h = head(k, "Volta Intelligence | Football recruitment intelligence and mandate engine",
             "Volta Intelligence matches player data to clubs' positional needs and the decision-makers behind them, so Volta can open the right conversations and secure recruitment mandates.")
    h += header(k, links)
    h += f"""<section class="hero"><div class="wrap">
<div><p class="kicker">Volta Intelligence · partner preview</p>
<h1>Know who needs what. Know who fits. Know who to contact.</h1>
<p class="lede" style="margin-top:26px">A football intelligence and opportunity engine: player performance data, club needs and decision-makers in one place, turned into tailored introductions that win recruitment mandates.</p>
<div class="cta"><a class="btn" href="#pilot">The January pilot</a><a class="btn ghost" href="#usecase">How a mandate works</a></div></div>
{v_mark(I['accent'], 'node', 300, 'big')}
</div></section>
{ribbon(["Know", "Match", "Introduce", "Mandate", "Deal"], "›")}
<section class="sec" id="pilot"><div class="wrap"><div class="split">
<div><p class="kicker">January 2027 transfer window</p><h2>A working prototype, tested on real mandates.</h2>
<p class="lede">The first version is built to do one job well before the window opens: match the players Volta can place to clubs with a genuine positional need, and help the team open those conversations with the right person.</p>
<p class="mute">Club mandates typically carry a 5 to 10% fee. Several mandates in one window would validate the platform commercially before wider build.</p></div>
<div class="steps">
<div class="step"><div><h3>Player profiles</h3><p>Volta-supported players with licensed performance data: pressing, ball regains, final-third contribution and physical output, compared against league benchmarks.</p></div></div>
<div class="step"><div><h3>Club needs</h3><p>Squad depth, departures, contract expiries and recruitment briefs, with each fact's source and confidence.</p></div></div>
<div class="step"><div><h3>Decision-makers</h3><p>Sporting directors, heads of recruitment and chief scouts, with relationship history.</p></div></div>
<div class="step"><div><h3>Matched introductions</h3><p>A short, data-backed note for each club, reviewed and sent by Volta, offering to source for that position.</p></div></div>
<div class="step"><div><h3>Mandate tracking</h3><p>Replies, agreements, shortlists and fees tracked through to completion.</p></div></div>
</div></div></div></section>
<section class="sec alt" id="usecase"><div class="wrap">
<div class="head"><p class="kicker">How a mandate works</p><h2>A club loses its starting left-back. Here is what happens next.</h2></div>
<div class="steps">
<div class="step"><div><h3>Detect</h3><p>A confirmed departure updates the club's squad picture. Source and confidence shown.</p></div></div>
<div class="step"><div><h3>Assess</h3><p>The engine reviews available full-backs against the club's system, level and likely budget.</p></div></div>
<div class="step"><div><h3>Identify</h3><p>Find the recruitment decision-maker and any previous relationship with Volta.</p></div></div>
<div class="step"><div><h3>Approach</h3><p>Draft a tailored introduction offering to source left-back profiles. A Volta adviser approves before anything is sent.</p></div></div>
<div class="step"><div><h3>Authorise</h3><p>Record the club's agreement, scope and fee. Run licensing and conflict checks.</p></div></div>
<div class="step"><div><h3>Source and present</h3><p>Match candidates by role, level, feasibility and wage, find who represents them, and present a structured shortlist with video and data.</p></div></div>
<div class="step"><div><h3>Complete</h3><p>Track negotiation, milestones and fee entitlement to completion.</p></div></div>
</div></div></section>
<section class="sec dark" id="modules"><div class="wrap">
<div class="head"><p class="kicker">The platform</p><h2>Connected modules. One shared intelligence layer.</h2></div>
<div class="grid g3">
<div class="cell"><h3>Player intelligence</h3><p>Profile, eligibility, contract dates, performance and physical data, video and representation status.</p></div>
<div class="cell"><h3>Club intelligence and needs</h3><p>Squad depth, expiring deals, decision-makers, playing style and confirmed versus predicted needs.</p></div>
<div class="cell"><h3>Agent and agency intelligence</h3><p>Licensed agents, verified client lists, relationships and conflicts.</p></div>
<div class="cell"><h3>Player-to-club matching</h3><p>Recommendations that explain fit, cost, constraints and uncertainty.</p></div>
<div class="cell"><h3>Contract and transfer radar</h3><p>Expiry alerts at 3, 6 and 12 months, vacancies, staff changes and window deadlines.</p></div>
<div class="cell"><h3>Relationship CRM</h3><p>Every conversation, reply and agreement with clubs, agents and players.</p></div>
<div class="cell"><h3>Outreach and presentations</h3><p>Player dossiers and club-specific introductions, reviewed before sending.</p></div>
<div class="cell"><h3>Mandates and deals</h3><p>From first approach to signed mandate, shortlist and completed transfer.</p></div>
<div class="cell"><h3>Football assistant</h3><p>"Which clubs in League One need a left-footed centre-back in January, and who do we know there?"</p></div>
</div></div></section>
<section class="sec" id="data"><div class="wrap">
<div class="head"><p class="kicker">Data</p><h2>Built on the data clubs already use.</h2>
<p class="lede">Clubs judge players with professional event, video and physical data. Volta Intelligence is designed to work with licensed data from established providers, so the evidence we send is in the language recruitment teams trust. Provider selection is under way.</p></div>
<div class="grid g3">
<div class="cell"><h3>Event and video data</h3><p>Every on-ball action, linked to the clip, across professional and youth competitions.</p></div>
<div class="cell"><h3>Physical and off-ball data</h3><p>Speed, distance, high-intensity runs, pressing and positioning.</p></div>
<div class="cell"><h3>Comparison and fit</h3><p>Similar-player search and how a player's output translates to another league.</p></div>
</div></div></section>
<section class="sec alt" id="trust"><div class="wrap"><div class="split">
<div><p class="kicker">Trust by design</p><h2>Every recommendation shows its evidence.</h2>
<p class="lede">Facts are labelled confirmed, reported or predicted. External contact always passes a human. Representation rules, minors' protections and data-licence terms are built into the workflow.</p></div>
<div><table><thead><tr><th>Label</th><th>Meaning</th></tr></thead><tbody>
<tr><td><b>Confirmed</b></td><td>Official source or direct confirmation</td></tr>
<tr><td><b>Reported</b></td><td>Third-party information with a traceable source</td></tr>
<tr><td><b>Predicted</b></td><td>The engine's estimate, shown with its reasons</td></tr>
<tr><td><b>Unknown</b></td><td>Not available or not verified</td></tr>
</tbody></table></div>
</div></div></section>
"""
    h += ecosystem_section(k, kicker="Volta", title="Where to go next.", intro="Volta Intelligence is a partner preview within Volta Sports.")
    h += contact_section(k, "See it before you believe it.", "For clubs, agencies, scouting organisations, data and technology partners.",
                         ["Club or sporting director", "Agency", "Data or technology partner", "Investor", "Other"], "Request a conversation")
    h += footer(k, links, "Volta Intelligence: the football recruitment intelligence and mandate engine behind Volta Sports.")
    write(k, h)


# =================================================================== AFRICA (password-protected)
def africa_body():
    # Frozen v1 Volta Africa content (hero to community). Edit build/africa_body.html directly.
    return open(os.path.join(os.path.dirname(__file__), "africa_body.html")).read()


def africa():
    k = "volta-africa"
    links = [("#why", "Why Volta"), ("#products", "Products"), ("#ghana", "Ghana pilot"), ("#connect", "Connection to Intelligence"), ("#community", "Community")]
    h = head(k, "Volta Africa | Partner preview", "Private partner preview: African football scouting, development and recruitment intelligence, beginning in Ghana.", noindex=True)
    h += header(k, links)
    h += africa_body()
    h += f"""<section class="sec dark" id="connect"><div class="wrap">
<div class="head"><p class="kicker">Connection to Volta Intelligence</p><h2>African youth data becomes a lasting advantage.</h2>
<p class="lede">Once established, the Ghana data flows into Volta Intelligence. It gives Volta Africa the insight needed for a sustained edge in the African youth market and identifies future candidates for Volta Management.</p></div>
<div class="grid g3">
<div class="cell"><h3>Pilot first</h3><p>Collect and analyse meaningful footage and development data before any proposition goes to international clubs.</p></div>
<div class="cell"><h3>Then connect</h3><p>Longitudinal player records sit alongside professional player and club data in Volta Intelligence.</p></div>
<div class="cell"><h3>Then products</h3><p>Sports-tech products that connect the African youth network with the wider football industry.</p></div>
</div>
<p class="mute" style="margin-top:28px">Data protection, safeguarding, guardian consent and FIFA minor-player rules apply from day one.</p>
</div></section>
"""
    h += ecosystem_section(k, kicker="Partner preview", title="Where to go next.", intro="Volta Africa is private until the strategy and Ghana pilot are agreed.")
    h += contact_section(k, "Talk to us about the pilot.", "For partners discussing the Ghana pilot.",
                         ["Partner", "Club or recruitment team", "Academy or school partner", "Federation or public sector", "Other"], "Send")
    h += footer(k, links, "Volta Africa is the next phase of Volta: African football scouting, development and recruitment intelligence, beginning in Ghana.")
    write(k, h, protect=["/:path*"])


if __name__ == "__main__":
    shutil.rmtree(OUT, ignore_errors=True)
    hub_public(); hub_partners(); inbox_page()
    write("volta-group", "", path="api/.keep")
    open(os.path.join(OUT, "volta-group", "api", "inbox.js"), "w").write(API_INBOX)
    open(os.path.join(OUT, "volta-group", "api", "partner.js"), "w").write(API_PARTNER)
    os.remove(os.path.join(OUT, "volta-group", "api", ".keep"))
    team(); management(); consultancy(); intelligence(); africa()
    print("built")
