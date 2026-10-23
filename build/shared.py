# Shared design system and components for the Volta ecosystem sites.
# v2 (23 Oct 2026): partner feedback applied — selective cross-linking, live enquiry forms
# into the central Volta CRM (Supabase), preview noindex, partner-only areas.

# While PREVIEW is True every site is marked noindex so Google does not index the
# vercel.app copies. Flip to False when the sites move onto their real domains.
PREVIEW = True

SUPABASE_URL = "https://fjbgdzwmsyawegpqfntb.supabase.co"
SUPABASE_PUBLISHABLE = "sb_publishable_CMG-DTPV9FknngASrsua4g_jSL43veV"

SHOWCASE_URL = "https://www.showcasetrials.football"
SHOWCASE_APPLY = "https://www.showcasetrials.football/apply"

SITES = {
    "volta-group": {
        "name": "Volta Sports", "short": "Volta", "sub": "Sports",
        "tag": "Development, representation, consultancy and intelligence in football",
        "url": "https://volta-group.vercel.app", "accent": "#C9A24B", "ink": "#121212",
        "symbol": "mark",
    },
    "team-volta": {
        "name": "Team Volta", "short": "Volta", "sub": "Training",
        "tag": "Player development, identification and pathways",
        "url": "https://team-volta.vercel.app", "accent": "#A51C24", "ink": "#121212",
        "symbol": "player",
    },
    "volta-management": {
        "name": "Volta Management", "short": "Volta", "sub": "Management",
        "tag": "Athlete management, representation and career advisory",
        "url": "https://volta-management.vercel.app", "accent": "#121212", "ink": "#121212",
        "symbol": "star",
    },
    "volta-consultancy": {
        "name": "Volta Consultancy", "short": "Volta", "sub": "Consultancy",
        "tag": "Club acquisitions, multi-club ownership and football investment advisory",
        "url": "https://volta-consultancy.vercel.app", "accent": "#0F5F3C", "ink": "#121212",
        "symbol": "circle",
    },
    "volta-intelligence": {
        "name": "Volta Intelligence", "short": "Volta", "sub": "Intelligence",
        "tag": "The global football CRM and opportunity engine",
        "url": "https://volta-intelligence.vercel.app", "accent": "#14355E", "ink": "#121212",
        "symbol": "node",
    },
    "volta-africa": {
        "name": "Volta Africa", "short": "Volta", "sub": "Africa",
        "tag": "African football scouting, development and recruitment intelligence",
        "url": "https://volta-africa.vercel.app", "accent": "#C8541A", "ink": "#121212",
        "symbol": "sun",
    },
}

ORDER = ["volta-group", "team-volta", "volta-management", "volta-consultancy", "volta-intelligence", "volta-africa"]

# Division code used by the central enquiries inbox, and the branded reply address.
DIVISION = {
    "volta-group": ("group", "enquiries@voltasports.com"),
    "team-volta": ("team", "enquiries@showcasetrials.football"),
    "volta-management": ("management", "enquiries@voltamanagement.co.uk"),
    "volta-consultancy": ("consultancy", "enquiries@voltaconsultancy.co.uk"),
    "volta-intelligence": ("intelligence", "enquiries@voltaintelligence.ai"),
    "volta-africa": ("africa", "enquiries@voltasports.com"),
}

# Selective cross-linking: each audience sees only the parts of Volta relevant to it.
# Training and representation are kept apart; Intelligence and Africa are partner-facing.
LINKS = {
    "volta-group": ["team-volta", "showcase", "volta-management", "volta-consultancy"],
    "team-volta": ["volta-group", "showcase"],
    "volta-management": ["volta-group", "volta-consultancy"],
    "volta-consultancy": ["volta-group", "volta-management"],
    "volta-intelligence": ["volta-group", "partners"],
    "volta-africa": ["partners", "volta-intelligence"],
    "partners": ORDER,
}
EXTRA = {
    "showcase": {"name": "Showcase Trials", "url": SHOWCASE_URL, "accent": "#A51C24", "symbol": "player",
                 "role": "Assessment camps, showcases and registration"},
    "partners": {"name": "Volta partner hub", "url": "https://volta-group.vercel.app/partners", "accent": "#C9A24B",
                 "symbol": "mark", "role": "Strategy, ecosystem and roadmap (partners only)"},
}

ROLES = {
    "volta-group": "Volta Sports: the divisions in one place",
    "team-volta": "Player development and identification",
    "volta-management": "Representation and athlete management",
    "volta-consultancy": "Investment and acquisition advisory",
    "volta-intelligence": "Football CRM and opportunity engine",
    "volta-africa": "African talent intelligence, Ghana first",
}

GOLD = "#C9A24B"
PAPER = "#F6F2EA"


def v_mark(accent, symbol="mark", size=120, cls=""):
    """The shared Volta V: heavy solid arms, tight opening, gold outline, secondary symbol below."""
    sym = ""
    if symbol == "star":
        sym = f'<path d="M60 128 l4.4 9.6 10.5 1.2-7.8 7.2 2.1 10.4-9.2-5.3-9.2 5.3 2.1-10.4-7.8-7.2 10.5-1.2z" fill="{GOLD}"/>'
    elif symbol == "circle":
        sym = f'<circle cx="60" cy="140" r="8" fill="{GOLD}"/>'
    elif symbol == "player":
        sym = (f'<g fill="{GOLD}"><circle cx="60" cy="124" r="4.5"/>'
               f'<path d="M57 130h6l3 14-4 1-2-7-1 12h-5l-1-12-2 7-4-1z"/>'
               f'<circle cx="69" cy="149" r="4"/></g>')
    elif symbol == "node":
        sym = (f'<g fill="none" stroke="{GOLD}" stroke-width="2.5"><circle cx="60" cy="140" r="5"/>'
               f'<circle cx="46" cy="150" r="3"/><circle cx="74" cy="150" r="3"/>'
               f'<path d="M56 143l-8 5M64 143l8 5"/></g>')
    elif symbol == "sun":
        sym = (f'<g fill="{GOLD}"><circle cx="60" cy="140" r="6"/>'
               f'<path d="M60 128v5M60 147v5M48 140h5M67 140h5M51 131l3.5 3.5M65.5 145.5l3.5 3.5M69 131l-3.5 3.5M54.5 145.5 51 149" stroke="{GOLD}" stroke-width="2.4" stroke-linecap="round"/></g>')
    else:
        sym = f'<rect x="52" y="132" width="16" height="16" fill="{GOLD}" transform="rotate(45 60 140)"/>'
    return (f'<svg class="vmark {cls}" width="{size}" height="{int(size*1.35)}" viewBox="0 0 120 162" '
            f'aria-hidden="true" focusable="false">'
            f'<path d="M8 6h34l18 70 18-70h34L78 116H42z" fill="{accent}" stroke="{GOLD}" stroke-width="6" stroke-linejoin="round"/>'
            f'{sym}</svg>')


def favicon(accent):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
           f'<rect width="64" height="64" rx="12" fill="{PAPER}"/>'
           f'<path d="M10 10h14l8 30 8-30h14L40 56H24z" fill="{accent}" stroke="{GOLD}" stroke-width="3" stroke-linejoin="round"/></svg>')
    import urllib.parse
    return "data:image/svg+xml," + urllib.parse.quote(svg)


CSS = """
:root{--paper:#F6F2EA;--paper-2:#EFE9DD;--ink:#121212;--ink-2:#3A3732;--mute:#6E6A62;--line:#D9D2C3;--gold:#C9A24B;--gold-2:#A8853A;--accent:ACCENT;--on-accent:#FFFFFF;--maxw:1180px;--gutter:clamp(20px,4vw,56px)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{animation:none!important;transition:none!important}}
body{margin:0;background:var(--paper);color:var(--ink);font-family:"Archivo",system-ui,sans-serif;font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased}
img,svg{display:block;max-width:100%}
a{color:inherit}
h1,h2,h3,h4{margin:0;font-weight:800;line-height:1.02;letter-spacing:-.01em;text-wrap:balance}
h1{font-size:clamp(44px,7.2vw,104px);font-stretch:112%;text-transform:uppercase;letter-spacing:-.02em;line-height:.94}
h2{font-size:clamp(32px,4.6vw,60px);font-stretch:105%}
h3{font-size:clamp(21px,2.2vw,27px)}
p{margin:0 0 1em}
.lede{font-size:clamp(19px,1.6vw,23px);line-height:1.45;color:var(--ink-2);max-width:62ch}
.kicker{font-weight:700;color:var(--accent);margin:0 0 14px;font-size:17px}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 var(--gutter)}
.btn{display:inline-block;background:var(--accent);color:var(--on-accent);text-decoration:none;font-weight:700;padding:16px 24px;border:2px solid var(--accent);border-radius:4px;line-height:1}
.btn:hover{background:var(--ink);border-color:var(--ink);color:#fff}
.btn.ghost{background:transparent;color:var(--ink);border-color:var(--ink)}
.btn.ghost:hover{background:var(--ink);color:#fff}
.btn:focus-visible,a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{outline:3px solid var(--gold);outline-offset:3px}
/* header */
.top{position:sticky;top:0;z-index:50;background:rgba(246,242,234,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;height:74px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;font-weight:800;font-stretch:112%;text-transform:uppercase;letter-spacing:.04em;font-size:19px}
.brand .vmark{height:40px;width:auto}
.brand small{font-weight:600;letter-spacing:.14em;font-size:11px;color:var(--accent);display:block;line-height:1}
.nav{display:flex;gap:26px;align-items:center}
.nav a{text-decoration:none;font-weight:600;font-size:15px;color:var(--ink-2)}
.nav a:hover{color:var(--accent)}
.nav .btn{padding:11px 16px;font-size:14px}
.menu{display:none;background:none;border:2px solid var(--ink);border-radius:4px;padding:8px 10px;font:inherit;font-weight:700;cursor:pointer}
@media (max-width:860px){.nav{display:none;position:absolute;left:0;right:0;top:74px;background:var(--paper);border-bottom:1px solid var(--line);flex-direction:column;align-items:flex-start;padding:16px var(--gutter) 22px}.nav.open{display:flex}.menu{display:block}}
/* hero */
.hero{position:relative;overflow:hidden;padding:clamp(48px,8vw,110px) 0 clamp(40px,6vw,80px);border-bottom:6px solid var(--accent)}
.hero .wrap{display:grid;grid-template-columns:1fr auto;gap:40px;align-items:end}
.hero .big{width:clamp(160px,22vw,300px);height:auto;filter:drop-shadow(0 18px 30px rgba(0,0,0,.14))}
.hero .cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
@media (max-width:860px){.hero .wrap{grid-template-columns:1fr}.hero .big{width:140px;order:-1}}
.ribbon{background:var(--ink);color:#fff;overflow:hidden;white-space:nowrap;font-weight:700;font-stretch:112%;text-transform:uppercase;letter-spacing:.08em;font-size:14px;padding:14px 0}
.ribbon span{display:inline-block;padding-right:36px}
.ribbon i{color:var(--gold);font-style:normal;padding-right:36px}
/* sections */
.sec{padding:clamp(56px,8vw,112px) 0}
.sec.alt{background:var(--paper-2)}
.sec.dark{background:var(--ink);color:#fff}
.sec.dark .lede,.sec.dark .mute{color:#CFC9BC}
.sec.dark .kicker{color:var(--gold)}
.sec.brandband{background:var(--accent);color:var(--on-accent)}
.sec.brandband .kicker{color:#fff;opacity:.85}.sec.brandband .lede{color:#fff;opacity:.92}
.head{max-width:760px;margin-bottom:clamp(32px,4vw,56px)}
.grid{display:grid;gap:28px}
.g2{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}
@media (max-width:920px){.g3,.g4{grid-template-columns:repeat(2,1fr)}}
@media (max-width:600px){.g2,.g3,.g4{grid-template-columns:1fr}}
.cell{border-top:4px solid var(--accent);padding-top:18px}
.cell h3{margin-bottom:10px}.cell p{color:var(--ink-2);margin:0}
.sec.dark .cell p{color:#CFC9BC}.sec.dark .cell{border-color:var(--gold)}
.cell ul{margin:10px 0 0;padding-left:18px;color:var(--ink-2)}.sec.dark .cell ul{color:#CFC9BC}
.cell li{margin:4px 0}
.mute{color:var(--mute);font-size:15px}
/* pitch lines: the structural device */
.pitch{border-left:5px solid var(--accent);padding-left:22px}
.steps{counter-reset:s;display:grid;gap:0;border-top:2px solid var(--ink)}
.step{display:grid;grid-template-columns:72px 1fr;gap:18px;padding:22px 0;border-bottom:2px solid var(--ink);align-items:start}
.step::before{counter-increment:s;content:counter(s,decimal-leading-zero);font-weight:800;font-size:38px;line-height:1;color:var(--accent);font-stretch:112%}
.step h3{margin-bottom:6px}.step p{margin:0;color:var(--ink-2)}
.sec.dark .steps,.sec.dark .step{border-color:#fff}.sec.dark .step::before{color:var(--gold)}.sec.dark .step p{color:#CFC9BC}
.stat{border-top:6px solid var(--accent);padding-top:14px}
.stat b{display:block;font-size:clamp(40px,5vw,64px);font-weight:800;font-stretch:112%;line-height:1;letter-spacing:-.02em}
.stat span{display:block;color:var(--ink-2);margin-top:8px}.stat small{display:block;color:var(--mute);font-size:13px;margin-top:4px}
.sec.dark .stat{border-color:var(--gold)}.sec.dark .stat span{color:#CFC9BC}
.split{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center}
@media (max-width:860px){.split{grid-template-columns:1fr}}
.quote{font-size:clamp(26px,3.4vw,44px);font-weight:800;font-stretch:108%;line-height:1.08;letter-spacing:-.01em}
.flow{display:flex;flex-wrap:wrap;gap:0;border:2px solid var(--ink);border-radius:6px;overflow:hidden}
.flow div{flex:1 1 150px;padding:18px 16px;border-right:2px solid var(--ink);font-weight:700;font-stretch:108%;text-transform:uppercase;letter-spacing:.04em;font-size:14px;position:relative}
.flow div:last-child{border-right:0}
.flow div small{display:block;text-transform:none;letter-spacing:0;font-weight:500;color:var(--mute);margin-top:6px;font-size:13px}
.flow div.on{background:var(--accent);color:#fff}.flow div.on small{color:#fff;opacity:.85}
.pills{display:flex;flex-wrap:wrap;gap:10px}
.pills span{border:2px solid var(--ink);border-radius:999px;padding:8px 14px;font-weight:600;font-size:14px}
.sec.dark .pills span{border-color:#fff}
.alloc{display:flex;height:34px;border-radius:4px;overflow:hidden;border:2px solid var(--ink)}
.alloc div{display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:13px}
.legend{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:16px;font-size:14px}
@media (max-width:760px){.legend{grid-template-columns:1fr 1fr}}
.legend i{display:inline-block;width:12px;height:12px;border-radius:2px;margin-right:8px;vertical-align:-1px}
table{width:100%;border-collapse:collapse;font-size:15px}
th,td{text-align:left;padding:12px 12px 12px 0;border-bottom:1px solid var(--line);vertical-align:top}
th{font-weight:700;border-bottom:2px solid var(--ink)}
.sec.dark th,.sec.dark td{border-color:#4a463f}
/* ecosystem */
.eco{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
@media (max-width:900px){.eco{grid-template-columns:repeat(2,1fr)}}
@media (max-width:560px){.eco{grid-template-columns:1fr}}
.eco a{display:block;text-decoration:none;border:2px solid var(--ink);border-radius:6px;padding:22px;background:#fff;transition:transform .15s}
.eco a:hover{transform:translateY(-3px);border-color:var(--gold)}
.eco .vmark{height:56px;width:auto;margin-bottom:14px}
.eco h3{margin-bottom:6px}.eco p{color:var(--ink-2);margin:0 0 10px;font-size:15px}
.eco b{color:var(--accent);font-size:14px}
.eco a.here{background:var(--paper-2)}
/* forms */
form{display:grid;gap:14px;max-width:560px}
label{font-weight:600;font-size:14px}
input,select,textarea{width:100%;font:inherit;padding:13px 14px;border:2px solid var(--ink);border-radius:4px;background:#fff;margin-top:6px}
textarea{min-height:120px}
.note{font-size:13px;color:var(--mute)}
.ok{display:none;padding:18px;border:2px solid var(--accent);border-radius:6px;font-weight:600}
/* footer */
footer{background:var(--ink);color:#CFC9BC;padding:56px 0 30px;font-size:14px}
footer .cols{display:grid;grid-template-columns:1.2fr 1fr 1.4fr;gap:40px}
@media (max-width:860px){footer .cols{grid-template-columns:1fr}}
footer h4{color:#fff;margin-bottom:12px;font-size:15px}
footer a{color:#fff;text-decoration:none}footer a:hover{color:var(--gold)}
footer ul{list-style:none;margin:0;padding:0}footer li{margin:6px 0}
footer li small{display:block;color:#9B968B}
footer .fine{border-top:1px solid #3a3732;margin-top:40px;padding-top:20px;color:#9B968B;font-size:13px}
footer .brand{color:#fff}footer .brand small{color:var(--gold)}
footer .disc{border:1px solid #3a3732;border-radius:6px;padding:14px 16px;margin-top:28px;color:#CFC9BC;font-size:13px;line-height:1.5}
/* v2 */
.previewbar{background:var(--gold);color:#121212;font-size:13px;font-weight:600;text-align:center;padding:7px 16px}
.err{display:none;padding:14px;border:2px solid #A51C24;border-radius:6px;color:#A51C24;font-weight:600}
.hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:14px}@media (max-width:560px){.row2{grid-template-columns:1fr}}
.notice{border:2px solid var(--ink);border-radius:6px;padding:20px 22px;background:#fff}
.notice p{margin:0;color:var(--ink-2)}
.notice b{display:block;margin-bottom:6px}
.draft{display:inline-block;background:var(--gold);color:#121212;font-weight:700;font-size:12px;border-radius:3px;padding:3px 8px;margin-bottom:14px}
.years{display:grid;gap:0;border-top:2px solid var(--ink)}
.yr{display:grid;grid-template-columns:110px 1fr;gap:18px;padding:18px 0;border-bottom:1px solid var(--line)}
.yr>b{font-size:38px;font-weight:800;font-stretch:112%;line-height:1;color:var(--accent)}
.fx{display:flex;flex-wrap:wrap;gap:8px 10px;align-items:flex-start}
.fx span,.fx a{border:1.5px solid var(--ink);border-radius:4px;padding:7px 11px;font-size:14px;font-weight:600;text-decoration:none;background:#fff}
.fx small{font-weight:500;color:var(--mute);margin-left:6px}
.fx a{border-color:var(--accent)}.fx a:hover{background:var(--accent);color:#fff}.fx a:hover small{color:#fff}
@media (max-width:560px){.yr{grid-template-columns:1fr;gap:8px}.yr>b{font-size:30px}}
.journey{border:2px solid var(--ink);border-radius:6px;padding:18px;background:#fff}
.journey .path{font-weight:700;font-size:17px;line-height:1.3;margin-bottom:8px}
.journey .who{font-size:13px;color:var(--mute)}
"""


def head(site_key, title, desc, extra_jsonld="", path="/", noindex=False):
    s = SITES[site_key]
    canon = s["url"] + ("" if path == "/" else path)
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": s["name"],
        "url": s["url"],
        "description": desc,
        "parentOrganization": {"@type": "Organization", "name": "Volta Sports", "url": SITES["volta-group"]["url"]} if site_key != "volta-group" else None,
        "sameAs": [SITES[k]["url"] for k in LINKS.get(site_key, []) if k in SITES],
    }
    org = {k: v for k, v in org.items() if v is not None}
    import json
    jsonld = json.dumps(org, ensure_ascii=False)
    kws = ", ".join(["Volta", s["name"], "football", s["tag"]])
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kws}">
<meta name="robots" content="{'noindex,nofollow' if (PREVIEW or noindex) else 'index,follow,max-image-preview:large'}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{s['name']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{s['url']}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{s['url']}/og.png">
<meta name="theme-color" content="{s['accent']}">
<link rel="icon" href="{favicon(s['accent'])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&display=swap" rel="stylesheet">
<style>{CSS.replace('ACCENT', s['accent'])}</style>
<script type="application/ld+json">{jsonld}</script>
{extra_jsonld}
</head>
<body>
"""


PREVIEW_NOTE = "Partner preview. Wording, credentials and player stories are awaiting Volta approval before public launch."


def header(site_key, links, home="/"):
    s = SITES[site_key]
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in links)
    bar = f'<div class="previewbar" role="note">{PREVIEW_NOTE}</div>' if PREVIEW else ""
    return f"""{bar}<header class="top"><div class="wrap">
<a class="brand" href="{home}" aria-label="{s['name']} home">{v_mark(s['accent'], s['symbol'], 32)}<span>{s['short']}<small>{s['sub']}</small></span></a>
<button class="menu" aria-expanded="false" aria-controls="nav" onclick="var n=document.getElementById('nav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))">Menu</button>
<nav class="nav" id="nav" aria-label="Main">{nav}<a class="btn" href="#contact">Get in touch</a></nav>
</div></header>
"""


def _entry(k):
    if k in SITES:
        o = SITES[k]
        return o["name"], o["url"] + "/", o["accent"], o["symbol"], ROLES[k]
    o = EXTRA[k]
    return o["name"], o["url"], o["accent"], o["symbol"], o["role"]


def ecosystem_section(site_key, kicker="Part of Volta Sports", title=None, intro=None, keys=None):
    keys = keys if keys is not None else LINKS[site_key]
    title = title or "Where to go next."
    intro = intro or "Volta Sports brings together player development, representation and football advisory. Each part has its own site and its own team."
    cards = ""
    for k in keys:
        name, url, accent, symbol, role = _entry(k)
        here = k == site_key
        target = "" if here else ' target="_blank" rel="noopener"'
        cls = ' class="here"' if here else ""
        label = "You are here" if here else "Visit ↗"
        cards += (f'<a href="{url}"{cls}{target}>{v_mark(accent, symbol, 42)}'
                  f'<h3>{name}</h3><p>{role}</p><b>{label}</b></a>')
    return f"""<section class="sec" id="ecosystem"><div class="wrap">
<div class="head"><p class="kicker">{kicker}</p><h2>{title}</h2><p class="lede">{intro}</p></div>
<div class="eco">{cards}</div>
</div></section>
"""


def contact_section(site_key, title, body, enquiry_types, button="Send enquiry", player_fields=False):
    code, reply = DIVISION[site_key]
    opts = "".join(f"<option>{o}</option>" for o in enquiry_types)
    extra = ""
    if player_fields:
        extra = """<div class="row2"><label>Player age group<select name="age_group"><option value="">Choose</option><option>Under 12</option><option>U12 to U14</option><option>U15 to U16</option><option>U17 to U18</option><option>U19 to U23</option><option>Senior (23+)</option></select></label>
<label>Town or postcode area<input name="location" maxlength="80" placeholder="e.g. Reading or RG30" autocomplete="postal-code"></label></div>"""
    return f"""<section class="sec alt" id="contact"><div class="wrap"><div class="split">
<div><p class="kicker">Contact</p><h2>{title}</h2><p class="lede">{body}</p>
<p class="mute">Prefer email? <a href="mailto:{reply}">{reply}</a>. Enquiries go to the Volta team and are never shared outside Volta.</p></div>
<div>
<form id="enq" novalidate>
<input type="hidden" name="division" value="{code}">
<div class="hp" aria-hidden="true"><label>Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label></div>
<div class="row2"><label>Your name<input name="name" required maxlength="120" autocomplete="name"></label>
<label>Email<input type="email" name="email" required maxlength="200" autocomplete="email"></label></div>
<div class="row2"><label>Phone (optional)<input name="phone" maxlength="40" autocomplete="tel"></label>
<label>Organisation (if any)<input name="organisation" maxlength="160" autocomplete="organization"></label></div>
{extra}
<label>Enquiry type<select name="enquiry_type">{opts}</select></label>
<label>Message<textarea name="message" required maxlength="4000"></textarea></label>
<button class="btn" type="submit">{button}</button>
</form>
<div class="ok" id="ok" role="status">Thank you. Your enquiry has been received and the Volta team will come back to you directly from {reply}.</div>
<div class="err" id="err" role="alert">Your enquiry did not send. Check your connection and try again, or email <a href="mailto:{reply}">{reply}</a>.</div>
</div>
</div></div></section>
<script>
(function(){{
var f=document.getElementById('enq');if(!f)return;
f.addEventListener('submit',function(e){{
e.preventDefault();
if(!f.reportValidity())return;
var d=Object.fromEntries(new FormData(f).entries());
if(d.website){{f.style.display='none';document.getElementById('ok').style.display='block';return;}}
delete d.website;
Object.keys(d).forEach(function(k){{if(d[k]==='')d[k]=null;}});
d.source_url=location.href.slice(0,400);
var b=f.querySelector('button');b.disabled=true;b.textContent='Sending…';
fetch('{SUPABASE_URL}/rest/v1/enquiries',{{method:'POST',headers:{{'apikey':'{SUPABASE_PUBLISHABLE}','Content-Type':'application/json','Prefer':'return=minimal'}},body:JSON.stringify(d)}})
.then(function(r){{if(!r.ok)throw new Error(r.status);f.style.display='none';document.getElementById('err').style.display='none';document.getElementById('ok').style.display='block';}})
.catch(function(){{b.disabled=false;b.textContent='Try again';document.getElementById('err').style.display='block';}});
}});
}})();
</script>
"""


def footer(site_key, links, blurb, disclaimer="", eco_keys=None, home="/"):
    s = SITES[site_key]
    eco = ""
    for k in (eco_keys if eco_keys is not None else LINKS[site_key]):
        name, url, _, _, role = _entry(k)
        if k == site_key:
            eco += f'<li><a href="{home}">{name} (this site)</a><small>{role}</small></li>'
        else:
            eco += f'<li><a href="{url}" target="_blank" rel="noopener">{name} ↗</a><small>{role}</small></li>'
    nav = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in links)
    disc = f'<div class="disc">{disclaimer}</div>' if disclaimer else ""
    return f"""<footer><div class="wrap">
<div class="cols">
<div><a class="brand" href="{home}">{v_mark(s['accent'] if s['accent'] != '#121212' else '#2a2a2a', s['symbol'], 34)}<span>{s['short']}<small>{s['sub']}</small></span></a><p style="margin-top:16px;max-width:36ch">{blurb}</p></div>
<div><h4>Explore</h4><ul>{nav}<li><a href="#contact">Contact</a></li></ul></div>
<div><h4>Volta Sports</h4><ul>{eco}</ul></div>
</div>
{disc}
<div class="fine">© 2026 Volta Sports. Team Volta Ltd, 46 Cranbury Road, Reading, Berkshire RG30 2XD. The Volta names describe a public brand family, not a corporate structure. Nothing on this site is an offer of securities, a guarantee of any football outcome, or legal or financial advice.</div>
</div></footer>
</body></html>
"""


def sitemap(site_key, paths=("/",)):
    s = SITES[site_key]
    urls = "".join(f"<url><loc>{s['url']}{p if p != '/' else '/'}</loc><changefreq>weekly</changefreq><priority>{'1.0' if p == '/' else '0.8'}</priority></url>" for p in paths)
    return f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>'


def robots(site_key):
    if PREVIEW:
        return "# Partner preview: not for search indexing yet\nUser-agent: *\nDisallow: /\n"
    return f"User-agent: *\nAllow: /\nDisallow: /partners\nSitemap: {SITES[site_key]['url']}/sitemap.xml\n"


def vercel_json():
    hdrs = [
        {"key": "X-Content-Type-Options", "value": "nosniff"},
        {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
        {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
        {"key": "Cache-Control", "value": "public, max-age=0, must-revalidate"},
    ]
    if PREVIEW:
        hdrs.append({"key": "X-Robots-Tag", "value": "noindex, nofollow"})
    import json
    return json.dumps({"cleanUrls": True, "trailingSlash": False,
                       "headers": [{"source": "/(.*)", "headers": hdrs}]}, indent=2) + "\n"


VERCEL_JSON = vercel_json()

# Basic-auth gate for partner-only areas (Vercel Routing Middleware).
# The password lives in the PARTNER_PASSWORD environment variable on Vercel, never in the repo.
def middleware_js(matcher):
    import json
    return """import { next } from '@vercel/functions';

export const config = { matcher: %s };

function unauthorised() {
  return new Response('Volta partner area. Please sign in with the partner password.', {
    status: 401,
    headers: { 'WWW-Authenticate': 'Basic realm="Volta partners", charset="UTF-8"', 'Cache-Control': 'no-store' },
  });
}

export default function middleware(request) {
  const expected = process.env.PARTNER_PASSWORD;
  if (!expected) return unauthorised();
  const header = request.headers.get('authorization') || '';
  if (!header.startsWith('Basic ')) return unauthorised();
  let decoded = '';
  try { decoded = atob(header.slice(6)); } catch (e) { return unauthorised(); }
  const password = decoded.slice(decoded.indexOf(':') + 1);
  if (password.length !== expected.length) return unauthorised();
  let diff = 0;
  for (let i = 0; i < password.length; i++) diff |= password.charCodeAt(i) ^ expected.charCodeAt(i);
  if (diff !== 0) return unauthorised();
  return next({ headers: { 'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex, nofollow' } });
}
""" % json.dumps(matcher)


PACKAGE_JSON = """{
  "name": "volta-site",
  "private": true,
  "type": "module",
  "dependencies": { "@vercel/functions": "^3.10.0" }
}
"""
