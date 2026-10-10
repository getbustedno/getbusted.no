# Landingssider per anledning for getbusted.no (SEO og AI-søk). Kjør: python3 _kilde/landingssider.py
# Regler: ingen alkoholord (alkoholloven § 9-2), bare oppdiktede navn, kortene hentet fra appen (test-bygg, okt 2026).
import html, json, pathlib
E = html.escape
ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://getbusted.no'
P = 'På tre - pek på den som'

PAGES = [
 dict(slug='julebord', color='#E0473E', cover='cover_jul', pack='Jul', status='Ute nå',
  title='Festspill til julebordet - Get Busted',
  desc='Festspill til julebordet med kollegaene? Get Busted har kort om sjefen, talene og mandagen etter. For voksne 18+, én telefon, 2-30 spillere.',
  h1=('Festspill til ', 'julebordet'),
  lead='Julebordet er kveldens store sjanse til å bli kjent med kollegaene. Get Busted gjør jobben for dere: én telefon, ett kort om gangen, og alle blir dratt inn.',
  why=[('Kort om det dere faktisk kjenner igjen', 'Sjefens favoritt, talen ingen ba om og den som forsvinner ut «en tur». Jul-pakka er skrevet for norske julebord, ikke oversatt.'),
       ('Funker for store bord', 'Fra 2 til 30 spillere. Store grupper får flere kort som gjelder alle samtidig, og med lagspill kan avdelingene spille mot hverandre.'),
       ('Alle kan være med', 'Alkoholfri modus gjør alt om til poeng, og det er alltid lov å hoppe over et kort.')],
  cards=[(P, 'er sjefens favoritt på julebordet'), (P, 'blir DJ på julebordet uten å bli spurt'), (P, 'holder tale på julebordet uten å bli spurt'),
         (P, 'legger ut bilde fra julebordet på LinkedIn'), (P, 'er den alle snakker om mandagen etter julebordet'),
         (P, 'går ut for «en røyk» på julebordet og kommer tilbake etter 40 minutter uten å røyke'),
         ('Sannhet', 'Brage: hva er det dummeste du har sagt til en sjef på et julebord?'),
         ('Sannhet', 'Oddny: hvilken kollega ville du aldri sittet ved siden av på julebordet?')],
  tips=['Velg Jul og Original, og nivå Mild eller Frekk hvis sjefen sitter ved bordet.', 'Slå på lag og la avdelingene spille Rød mot Blå.', 'Bytt leser for hvert kapittel av kvelden, så slipper én person å lese alt.'],
  faq=[('Passer det for et julebord med kollegaer?', 'Ja. Velg nivå Mild eller Frekk, så holder kortene seg på riktig side av HR. Get Fu**ed er for vennegjengen.'),
       ('Hvor mange kan spille?', 'Fra 2 til 30. På et stort bord får dere flere kort som gjelder alle samtidig.'),
       ('Hva koster Jul-pakka?', '49 kr som engangskjøp. Du kan prøve 5 kort gratis først, og Original har 50 gratis kort hver kveld.')]),
 dict(slug='hyttetur', color='#C7864A', cover='cover_hytta', pack='Hytta', status='Ute nå',
  title='Spill til hytteturen - Get Busted',
  desc='Spill til hytteturen med vennegjengen: kort om badstua, gruppechatten og den som aldri tar oppvasken. Get Busted - festspill for voksne 18+, funker uten dekning.',
  h1=('Spill til ', 'hytteturen'),
  lead='Regnværsdag, null dekning og en hel kveld foran dere. Get Busted gjør hytteturen til den dere snakker om resten av året.',
  why=[('Skrevet for norske hytter', 'Hytta-pakka handler om badstua, utedoen, peisen som ikke vil tenne og gruppechatten før turen.'),
       ('Ingen dekning? Ingen problem', 'Kortene ligger i appen, så dere kan spille uten nett når appen først er lastet ned.'),
       ('Én telefon holder', 'Én leser holder telefonen og leser høyt. Resten ser på hverandre, ikke på en skjerm.')],
  cards=[(P, 'tar aldri oppvasken på hytta'), (P, 'sier de skal være offline på hytta og legger ut story tre ganger'),
         (P, 'snorker så høyt at noen flytter ut i bilen'),
         (P, 'skriver 40 meldinger i hyttegruppechatten før turen, men svarer bare «ok» når Vipps-kravet kommer'),
         (P, 'tror de er friluftsmenneske, men trenger hjelp til å tenne i peisen'), (P, 'jukser i Alias og nekter for det'),
         ('Sannhet', 'Eskil: hva er det ekleste du har gjort på hytta fordi det ikke var innlagt vann?'),
         ('Sannhet', 'Ragna: hvem ringer du først hvis dekningen kommer tilbake klokka tre i natt?')],
  tips=['Last ned appen og pakkene før dere drar, så funker alt uten dekning.', 'Velg Hytta og Original. Ta Get Fu**ed-nivået når klokka har passert midnatt.', 'Spill i duoer, så blir det lag for resten av helga.'],
  faq=[('Funker appen uten nett?', 'Ja, kortene ligger i appen. Last ned appen og pakkene du vil bruke før dere drar.'),
       ('Hvor mange kan være med?', 'Fra 2 til 30 spillere, og dere kan legge til eller fjerne folk underveis.'),
       ('Hva koster Hytta-pakka?', '49 kr som engangskjøp. Prøv 5 kort gratis først.')]),
 dict(slug='utdrikningslag', color='#E94B8A', cover='cover_utdrikning', pack='Utdrikningslag', status='Kommer 19. november',
  title='Leker til utdrikningslag - Get Busted',
  desc='Leker og spill til utdrikningslaget: kort om forloveren, talen og bryllupet. Get Busted - festspill for voksne 18+ på én telefon. Utdrikningslag-pakka kommer 19. november.',
  h1=('Leker til ', 'utdrikningslaget'),
  lead='Én av dere skal gifte seg, resten skal sørge for at kvelden blir husket. Utdrikningslag-pakka er laget for akkurat det.',
  why=[('Handler om den som skal gifte seg', 'Kort om forloveren, talen, eksene på gjestelista og hvor lenge ekteskapet holder.'),
       ('Dere trenger bare én telefon', 'Én leser, ett kort om gangen. Ingen rekvisitter, ingen forberedelser.'),
       ('Alle nivåer', 'Mild for svigerfamilien, Frekk for vennegjengen og Get Fu**ed når hovedpersonen tåler det.')],
  cards=[(P, 'gråter av sin egen tale'), (P, 'stjeler mikrofonen i bryllupet'), (P, 'har allerede planlagt sitt eget bryllup på Pinterest'),
         (P, 'velter kaken i bryllupet'), (P, 'tror de er best egnet som forlover, men ville mistet ringen før kirka'),
         (P, 'har allerede stalket hele brudefølget på Insta'),
         ('Sannhet', 'Vetle: hvem i rommet ville du IKKE hatt som forlover, og hvorfor?'),
         ('Sannhet', 'Signy: hvor mange år gir du dette ekteskapet? Du må svare seriøst.')],
  tips=['Sett hovedpersonen som leser den første runden.', 'Kombiner Utdrikningslag med Original for variasjon.', 'Bruk hemmelige oppdrag: telefonen går til én, som får et oppdrag bare hen vet om.'],
  faq=[('Når kommer Utdrikningslag-pakka?', '19. november. Fram til da kan dere spille Original, Jul, Nach, Hytta og Halloween.'),
       ('Passer det for både utdrikningslag for gutter og jenter?', 'Ja. Kortene handler om bryllupet og hovedpersonen, ikke om kjønn.'),
       ('Hva koster det?', '49 kr for pakka som engangskjøp, eller Busted+ for alt.')]),
 dict(slug='halloween', color='#FF8A1F', cover='cover_halloween', pack='Halloween', status='Ute nå',
  title='Festspill til halloweenfesten - Get Busted',
  desc='Festspill til halloweenfesten: kort om kostymer, skrekkfilmer og den som ville dødd først. Get Busted - for voksne 18+, én telefon, 2-30 spillere.',
  h1=('Festspill til ', 'halloween'),
  lead='Kostymene er på, skrekkfilmen er valgt. Halloween-pakka avslører hvem som ville overlevd, og hvem som kjøpte kostymet i dag.',
  why=[('Kort om kostymer og skrekk', 'Hvem ville dødd først, hvem ville solgt gjengen og hvem har det verste kostymet i rommet.'),
       ('Klar på 20 sekunder', 'Skriv inn navnene, velg Halloween og start. Appen setter navnene inn på kortene.'),
       ('Med eller uten', 'Alkoholfri modus er alltid med, og alle kort kan hoppes over.')],
  cards=[(P, 'ville gitt barna på døra rosiner og gode råd'), (P, 'kjøpte kostymet sitt i dag'), (P, 'er skumlest klokka sju om morgenen'),
         (P, 'ville solgt resten av gjengen til en seriemorder for å overleve'),
         (P, 'ville dødd først i en skrekkfilm fordi de sier «vi deler oss» for å få være alene med crushen'),
         (P, 'bruker kostymebildet fra i fjor som profilbilde på datingappen fordi det er det eneste de ser bra ut på'),
         ('Sannhet', 'Torgeir: hvilket kostyme angrer du mest på? Beskriv det i detalj.'),
         ('Sannhet', 'Åsne: hvem i rommet har det beste kostymet i kveld, og hvem har det verste?')],
  tips=['Spill Halloween-pakka mens dere venter på at filmen skal starte.', 'Bruk lagspill med kostymelag mot kostymelag.', 'Ta Get Fu**ed-nivået når de siste gjestene har kommet.'],
  faq=[('Er Halloween-pakka ute?', 'Ja, den er med fra start.'),
       ('Hvor mange kort er det?', 'Over 150 kort på norsk, fordelt på Mild, Frekk og Get Fu**ed.'),
       ('Hva koster den?', '49 kr som engangskjøp. Prøv 5 kort gratis først.')]),
]

HEAD_FOOT = (ROOT / 'hjelp/index.html').read_text(encoding='utf-8')
FOOTER = HEAD_FOOT[HEAD_FOOT.index('<footer>'):HEAD_FOOT.index('</footer>') + len('</footer>')]
NAV = '<header class="nav"><div class="wrap"><a class="brand" href="/"><img src="/img/logo.png" alt="">Get Busted</a><nav><a href="/#pakker">Pakker</a><a href="/#priser">Priser</a><a href="/hjelp/">Hjelp</a></nav></div></header>'

def others(cur):
    return ' · '.join(f'<a href="/{p["slug"]}/">{E(p["h1"][1].capitalize())}</a>' for p in PAGES if p['slug'] != cur)

HREF = {'julebord': ('/christmas-party/', '/se/julbord/', '/dk/julefrokost/'), 'hyttetur': ('/cabin-weekend/', '/se/stugan/', '/dk/sommerhus/'), 'utdrikningslag': ('/stag-and-hen/', '/se/svensexa-mohippa/', '/dk/polterabend/')}

def hreflang(slug, url):
    if slug not in HREF: return ''
    en, sv, da = HREF[slug]; o = 'https://getbusted.online'
    return (f'<link rel="alternate" hreflang="no" href="{url}">\n<link rel="alternate" hreflang="en" href="{o}{en}">\n'
            f'<link rel="alternate" hreflang="sv" href="{o}{sv}">\n<link rel="alternate" hreflang="da" href="{o}{da}">\n<link rel="alternate" hreflang="x-default" href="{o}{en}">\n')

def page(p):
    url = f'{SITE}/{p["slug"]}/'
    cards = ''.join(f"<figure class='sample' style='--c:{p['color']}'><figcaption>{E(p['pack'])}</figcaption><p class='sample-head'>{E(h)}</p><blockquote>{E(t)}</blockquote></figure>" for h, t in p['cards'])
    why = ''.join(f"<div class='feature'><h3>{E(h)}</h3><p>{E(t)}</p></div>" for h, t in p['why'])
    tips = ''.join(f'<li>{E(t)}</li>' for t in p['tips'])
    faq = ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in p['faq'])
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebPage', '@id': url, 'url': url, 'name': p['title'], 'description': p['desc'], 'inLanguage': 'no',
         'about': {'@id': 'https://getbusted.no/#app'}, 'isPartOf': {'@type': 'WebSite', 'url': SITE + '/', 'name': 'Get Busted'}},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Get Busted', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': p['h1'][0] + p['h1'][1], 'item': url}]},
        {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in p['faq']]}]}
    ldj = json.dumps(ld, ensure_ascii=False).replace('</', '<\\/')
    return f'''<!doctype html>
<html lang="no">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(p['title'])}</title>
<meta name="description" content="{E(p['desc'])}">
<link rel="canonical" href="{url}">
{hreflang(p["slug"], url)}<meta property="og:title" content="{E(p['title'])}">
<meta property="og:description" content="{E(p['desc'])}">
<meta property="og:image" content="{SITE}/img/og.jpg">
<meta property="og:url" content="{url}">
<meta name="theme-color" content="#191919">
<link rel="icon" href="/img/favicon.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preload" href="/fonts/bsc-900Black_Italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
<script src="/samtykke.js" defer></script>
<script type="application/ld+json">{ldj}</script>
</head>
<body>
<a class="skip" href="#innhold">Hopp til innholdet</a>
{NAV}
<main id="innhold">
<section class="hero lp">
  <div class="wrap">
    <div>
      <p class="kicker">{E(p['pack'])}-pakka · {E(p['status'])}</p>
      <h1>{E(p['h1'][0])}<em>{E(p['h1'][1])}</em></h1>
      <p class="lead">{E(p['lead'])}</p>
      <p class="note">For voksne, minst 18 år. Alkoholfri modus er alltid med. <a href="/">Les mer om Get Busted</a>.</p>
    </div>
    <div class="stage lp-stage" aria-hidden="true"><img class="cover" src="/img/{p['cover']}.jpg" alt="" style="--c:{p['color']}" width="360" height="503"></div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="kicker">Smakebiter</p>
    <h2>Kort fra <em>{E(p['pack'])}</em>-pakka</h2>
    <p class="lead">Et utvalg av kortene. Navnene byttes med gjengen deres.</p>
    <div class="samples">{cards}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="kicker">Hvorfor Get Busted</p>
    <h2>Laget for <em>kvelden</em></h2>
    <div class="features three">{why}</div>
    <div class="lp-tips"><h3>Slik får dere mest ut av det</h3><ul>{tips}</ul></div>
  </div>
</section>

<section class="alt">
  <div class="wrap" style="max-width:820px">
    <p class="kicker">Spørsmål</p>
    <h2>Ofte spurt</h2>
    {faq}
    <p class="lp-more">Flere anledninger: {others(p['slug'])}</p>
  </div>
</section>
</main>
{FOOTER}
</body>
</html>
'''

for p in PAGES:
    d = ROOT / p['slug']; d.mkdir(exist_ok=True)
    (d / 'index.html').write_text(page(p), encoding='utf-8')

# Sitemap: legg til sidene
sm = ROOT / 'sitemap.xml'; s = sm.read_text(encoding='utf-8')
for p in PAGES:
    loc = f'<url><loc>{SITE}/{p["slug"]}/</loc></url>'
    if loc not in s: s = s.replace('</urlset>', loc + '\n</urlset>')
sm.write_text(s, encoding='utf-8')

# CSS
css = ROOT / 'style.css'; c = css.read_text(encoding='utf-8')
if '.lp-stage' not in c:
    c += """
/* Landingssider per anledning */
.hero.lp .wrap{grid-template-columns:1.3fr .7fr}
.lp-stage{height:auto;min-height:0;display:flex;justify-content:center}
.lp-stage .cover{position:relative;top:0;width:240px;transform:rotate(3deg)}
.features.three{grid-template-columns:repeat(3,1fr)}
.lp-tips{margin-top:28px;background:var(--card2);border:1px solid var(--line);border-radius:var(--radius);padding:22px 26px}
.lp-tips h3{font-size:22px;margin-bottom:6px}.lp-tips li{color:var(--muted)}
.lp-more{margin-top:22px;color:var(--muted)}
@media (max-width:900px){.hero.lp .wrap{grid-template-columns:1fr}.features.three{grid-template-columns:1fr}.lp-stage .cover{width:180px}}
"""
    css.write_text(c, encoding='utf-8')
print('ok', [p['slug'] for p in PAGES])
