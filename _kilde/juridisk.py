"""Juridiske sider for getbusted.no: personvern, bruksvilkår (/vilkar/), informasjonskapsler og kjøpsvilkår/refusjon (/kjop/), og felles bunntekst på alle sider.
Kjør fra roten av repoet: python3 _kilde/juridisk.py
Mappen _kilde publiseres ikke (GitHub Pages hopper over mapper som starter med _).
Engelsk, svensk og dansk versjon ligger på getbusted.online (build.py der).
"""
import datetime, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
OPPDATERT = '8. oktober 2026'
# Informasjonskapselsiden er ikke endret 8. oktober, så den beholder gammel dato.
OPPDATERT_SIDE = {'informasjonskapsler': '7. oktober 2026'}
FIRMA = 'Snikkerbua Holding AS'
ORGNR = '927 118 300'
ADRESSE = 'Voldgata 27, 2000 Lillestrøm'
EPOST = 'kontakt@getbusted.no'
MAIL = f'<a href="mailto:{EPOST}">{EPOST}</a>'

# ---------------------------------------------------------------------------
# PÅMINNELSE OM PRISENDRING (se også PAMINNELSER.md)
# Lanseringsprisen på Busted+ (249 kr) gjelder til og med 31. desember 2026.
# TODO 2027-01-01: sett LAUNCH_PRICE_ACTIVE = False (siden viser da bare 299 kr),
# sjekk at prisen i App Store og Google Play er endret til 299 kr samme dag, og oppdater getbusted.online/build.py likt.
# Generatoren stopper med feilmelding hvis den kjøres etter denne datoen mens lanseringsprisen fortsatt står.
PRICE_CHANGE_DATE = datetime.date(2027, 1, 1)
LAUNCH_PRICE_ACTIVE = True
if LAUNCH_PRICE_ACTIVE and datetime.date.today() >= PRICE_CHANGE_DATE:
    sys.exit('STOPP: Lanseringsprisen (249 kr) gjaldt til og med 31. desember 2026. Endre prisen på kjop-siden til 299 kr '
             '(sett LAUNCH_PRICE_ACTIVE = False i _kilde/juridisk.py), bekreft prisene i App Store og Google Play, og se PAMINNELSER.md.')
if LAUNCH_PRICE_ACTIVE:
    PRISTEKST = ('Busted+ koster 249 kr i lanseringsperioden til og med 31. desember 2026, og 299 kr fra 1. januar 2027. '
                 'Prisen du ser i butikken når du kjøper, er den som gjelder. Prisendringer påvirker ikke det du allerede har kjøpt.')
else:
    PRISTEKST = ('Busted+ koster 299 kr. Prisen du ser i butikken når du kjøper, er den som gjelder. '
                 'Prisendringer påvirker ikke det du allerede har kjøpt.')

FOOTER = f"""<footer>
  <div class="wrap">
    <div class="footer-links"><a href="/vilkar/">Bruksvilkår</a><a href="/personvern/">Personvern</a><a href="/informasjonskapsler/" data-samtykke>Informasjonskapsler</a><a href="/kjop/">Kjøp og refusjon</a><a href="/hjelp/">Hjelp</a><a href="mailto:{EPOST}">Kontakt</a><a href="https://www.instagram.com/getbusted.no/" rel="me">Instagram</a><a href="https://www.tiktok.com/@getbusted.no" rel="me">TikTok</a><a href="https://www.facebook.com/getbusted.no" rel="me">Facebook</a></div>
    <div class="footer-firma">© 2026 {FIRMA} · Org.nr. {ORGNR} · {ADRESSE} · For voksne over 18 år</div>
  </div>
</footer>"""


def page(slug, title, desc, body):
    return f"""<!doctype html>
<html lang="no">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} - Get Busted</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://getbusted.no/{slug}/">
<meta name="theme-color" content="#2B2B2B">
<link rel="icon" href="/img/favicon.png">
<link rel="preload" href="/fonts/bsc-900Black_Italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
<script src="/samtykke.js" defer></script>
</head>
<body>
<a class="skip" href="#innhold">Hopp til innholdet</a>
<header class="nav"><div class="wrap"><a class="brand" href="/"><img src="/img/logo.png" alt="">Get Busted</a><nav aria-label="Hovedmeny"><a href="/#pakker">Pakker</a><a href="/hjelp/">Hjelp</a></nav></div></header>
<main class="article" id="innhold">
<h1>{title}</h1>
<p class="meta">Sist oppdatert: {OPPDATERT_SIDE.get(slug, OPPDATERT)}</p>
{body.strip()}
</main>
{FOOTER}
</body>
</html>
"""


# Oppdatert 8. oktober 2026 etter Claude outputs/juridiske-sider/personvernerklaering.md (v0.2).
# JURIDISK USIKKERT: Rettslig grunnlag for RevenueCat-data (art. 6 nr. 1 b eller f), databehandleravtaler med RevenueCat, GitHub og Metricool,
#   om GitHub er databehandler eller egen behandlingsansvarlig, og DPF-status for GitHub og RevenueCat (ikke bekreftet mot dataprivacyframework.gov).
# JURIDISK USIKKERT: Lagringstider hos RevenueCat, Metricool og for e-post er ikke satt konkret. Innsyn uten navn (art. 11) og kravet om kvittering.
# JURIDISK USIKKERT: Om en enkel aldersbekreftelse (ja-knapp) er nok, og om spillernavn og historikk lagret lokalt gir oss noe ansvar (husholdningsunntaket).
# JURIDISK USIKKERT: Om bokføringsloven (5 år) gjelder opplysninger vi faktisk får fra butikkene.
PERSONVERN = f"""
<h2>Kort fortalt</h2>
<ul>
  <li>Appen har ingen brukerkontoer, ingen reklame og ingen analyseverktøy.</li>
  <li>Navnene dere skriver inn og innstillingene deres lagres bare på telefonen.</li>
  <li>Kjøp går gjennom Apple eller Google. Vi bruker RevenueCat til å holde styr på hvilke pakker du eier, med en tilfeldig ID uten navn.</li>
  <li>Nettsiden teller besøk med Metricool bare hvis du sier ja. Sier du nei, sendes ingenting.</li>
  <li>Appen er for voksne over 18 år.</li>
</ul>

<h2>Hvem er ansvarlig</h2>
<p>{FIRMA}, org.nr. {ORGNR}, {ADRESSE}, er behandlingsansvarlig for appen Get Busted og nettsidene getbusted.no og getbusted.online. Kontakt: {MAIL}.</p>

<h2>Appen</h2>
<h3>Det som lagres på telefonen din</h3>
<ul>
  <li>Innstillinger: språk, tørstenivå og alkoholfri modus.</li>
  <li>At du har bekreftet at du er over 18 år.</li>
  <li>Spillernavn og status for kvelden som pågår, så dere kan fortsette der dere slapp.</li>
  <li>Tidligere kvelder (dato, spillernavn, antall kort, hvem som ble mest busted og vinnerlag, maks 200 kvelder) som brukes til oppsummeringen «Wrapped».</li>
  <li>Hvilke kjøp du eier (en kopi, så appen virker uten nett), status på julekalender, om appen har bedt om vurdering og om du har slått på pakkevarsler.</li>
</ul>
<p>Dette sendes ikke til oss eller andre, og det slettes når du sletter appen. Bruk ikke fullt navn eller sensitive opplysninger om andre som spillernavn: fornavn eller kallenavn holder. Appen sender ikke spillernavn, kortinnhold eller spillhistorikk til noen. Den bruker ikke mikrofon, kamera, kontakter, posisjon eller helsedata, og annonse-ID (AD_ID på Android, IDFA på iOS) brukes ikke.</p>

<h3>Kjøp</h3>
<p>Kjøp gjøres i App Store eller Google Play. Apple og Google behandler betalingen og er selv ansvarlige for opplysningene de har om deg. Vi får aldri navnet ditt, e-postadressen din eller betalingsopplysningene dine.</p>
<p>For å vite hvilke pakker du eier, og for at du skal kunne gjenopprette kjøp på en ny telefon, bruker vi RevenueCat (RevenueCat, Inc., USA) som databehandler. RevenueCat mottar en tilfeldig app-bruker-ID som appen lager, kvitteringen for kjøpet fra Apple eller Google (hvilket produkt, når og transaksjons-ID) og teknisk informasjon som følger med forespørselen, blant annet IP-adresse, plattform, enhetstype, OS-versjon og appversjon. RevenueCat lagrer data i USA, og overføringen bygger på EUs standardkontrakter (SCC). Behandlingsgrunnlaget er at det er nødvendig for å levere det du har kjøpt (personvernforordningen art. 6 nr. 1 b). Opplysningene lagres så lenge du kan ha bruk for å gjenopprette kjøpene, eller til du ber oss slette dem.</p>

<h3>Nye kort fra nettet</h3>
<p>Appen henter en fil med aktuelle kort fra getbusted.no. Det sendes ingen opplysninger om deg, men som ved alle besøk på en nettside ser serveren (GitHub, se under) IP-adressen til telefonen.</p>

<h3>Varsler, deling og vurdering</h3>
<ul>
  <li>Varsler planlegges på telefonen. Det finnes ingen varselserver, og du kan slå dem av i appen eller i telefonens innstillinger.</li>
  <li>Når du deler et kort eller en oppsummering, bruker appen telefonens egen delingsmeny. Vi ser ikke hva du deler eller med hvem.</li>
  <li>Appen kan be Apple eller Google vise en dialog for vurdering i butikken. Vi får ikke vite hva du svarer.</li>
  <li>Sangkort kan ha en knapp som åpner Spotify. Da gjelder Spotifys vilkår og personvernerklæring.</li>
</ul>

<h2>Nettsidene</h2>
<h3>Drift</h3>
<p>Nettsidene ligger hos GitHub Pages (GitHub, Inc., USA). GitHub registrerer IP-adressen til besøkende av sikkerhetshensyn. GitHub er sertifisert under EU-US Data Privacy Framework. Behandlingsgrunnlaget er vår berettigede interesse i å levere nettsiden trygt (art. 6 nr. 1 f).</p>
<h3>Besøksstatistikk, bare med samtykke</h3>
<p>Hvis du trykker «Godta» i boksen om statistikk, teller vi besøk med Metricool (Metricool Software S.L., Madrid, Spania), som er databehandler for oss. Metricool mottar adressen til siden du ser på, siden du kom fra, størrelsen på nettleservinduet og teknisk informasjon som nettleseren sender med, blant annet IP-adresse og nettlesertype. Det settes ingen informasjonskapsler. Metricool lagrer data i EU/EØS. Behandlingsgrunnlaget er samtykket ditt (art. 6 nr. 1 a og ekomloven § 3-15). Du kan trekke samtykket når som helst via lenken «Informasjonskapsler» nederst på siden. Statistikken brukes bare til å se hvilke sider som blir lest, og ligger hos Metricool så lenge vi bruker tjenesten. Les mer på siden om <a href="/informasjonskapsler/">informasjonskapsler</a>.</p>
<h3>Skrift og lenker</h3>
<p>Skriften ligger på vår egen server, så ingenting sendes til Google eller andre når siden lastes. Lenkene til Instagram, TikTok og Facebook sender deg til disse tjenestene først når du trykker på dem.</p>

<h2>E-post til oss</h2>
<p>Skriver du til oss, bruker vi e-postadressen og det du skriver til å svare deg og følge opp saken. Behandlingsgrunnlaget er vår berettigede interesse i å svare på henvendelser (art. 6 nr. 1 f). E-posten slettes når saken er ferdig, med mindre vi må ta vare på den, for eksempel ved en klage.</p>

<h2>Hvor lenge vi lagrer</h2>
<ul>
  <li><b>På telefonen:</b> til du sletter appen. Avinstallerer du appen, slettes alt som er lagret lokalt.</li>
  <li><b>RevenueCat:</b> så lenge du kan ha behov for å gjenopprette kjøp, eller til du ber oss slette.</li>
  <li><b>Metricool (statistikk, bare med samtykke):</b> ligger hos Metricool så lenge vi bruker tjenesten. Trekker du samtykket, slutter vi å telle deg fra da.</li>
  <li><b>GitHub (IP-adresse i serverlogger):</b> GitHub styrer selv hvor lenge sikkerhetslogger lagres.</li>
  <li><b>E-post til oss:</b> slettes når saken er avsluttet, med mindre vi må ta vare på den, for eksempel ved klage.</li>
  <li><b>Regnskapsdata:</b> Apple og Google utbetaler til oss og er ansvarlige for kjøpsdata i sine systemer. Vi følger lovkrav om oppbevaring av regnskapsmateriale.</li>
</ul>

<h2>Hvem vi deler med</h2>
<ul>
  <li><b>RevenueCat, Inc.</b> (USA): databehandler for kjøp og eierskap.</li>
  <li><b>Apple Inc.</b> og <b>Google LLC / Google Ireland Ltd.</b>: butikkene der du kjøper. De er selv ansvarlige for opplysningene de har om deg.</li>
  <li><b>GitHub, Inc.</b> (GitHub Pages, USA): drift av nettsidene getbusted.no og getbusted.online.</li>
  <li><b>Metricool Software S.L.</b> (Madrid, Spania): databehandler for besøksstatistikk, bare hvis du har sagt ja.</li>
  <li>Offentlige myndigheter hvis loven krever det.</li>
</ul>
<p>Vi selger ikke personopplysninger.</p>

<h2>Overføring til land utenfor EØS</h2>
<p>RevenueCat lagrer data i USA, og overføringen bygger på EUs standardkontrakter (SCC). Nettsidene ligger hos GitHub Pages (USA), som er sertifisert under EU-US Data Privacy Framework. Apple og Google kan også behandle data i USA. Metricool lagrer data i EU/EØS. Du kan be om en kopi av garantiene ved å skrive til {MAIL}.</p>

<h2>Aldersgrense og barn</h2>
<p>Get Busted er kun for personer over 18 år. Appen ber deg bekrefte alderen ved første oppstart. Dette er en enkel bekreftelse, ikke en kontroll av alderen din. Vi samler ikke med vilje inn opplysninger om personer under 18 år. Oppdager vi det, sletter vi opplysningene. Er du forelder og tror barnet ditt har brukt appen, kontakt oss på {MAIL}.</p>

<h2>Sikkerhet</h2>
<p>Vi bruker leverandører som krypterer data under overføring, og vi lagrer så lite som mulig. Ingen løsning er helt sikker. Skjer det et brudd som gjelder deg, varsler vi Datatilsynet og deg etter reglene.</p>

<h2>Dine rettigheter</h2>
<p>Du har rett til innsyn i opplysningene vi har om deg, og til å få dem rettet eller slettet. Du kan også be om begrenset behandling, protestere mot behandling som bygger på berettiget interesse, få utlevert opplysninger du har gitt oss (dataportabilitet) og trekke tilbake samtykke. Skriv til {MAIL}. Vi svarer innen én måned.</p>
<p>Siden vi ikke har navnet ditt knyttet til kjøp, trenger vi kvitteringen eller ordrenummeret fra Apple eller Google for å finne riktige opplysninger hos RevenueCat. Data som bare ligger på telefonen din, har vi ikke tilgang til. Du sletter dem ved å avinstallere appen.</p>
<p>Mener du at vi behandler personopplysninger i strid med regelverket, kan du klage til <a href="https://www.datatilsynet.no/">Datatilsynet</a>. Vi setter pris på om du tar kontakt med oss først.</p>

<h2>Endringer</h2>
<p>Endrer vi hvordan appen eller nettsidene behandler personopplysninger, oppdaterer vi denne siden og datoen øverst. Samler vi inn mer data, for eksempel anonym måling av kort, oppdaterer vi erklæringen før det slås på. Ved vesentlige endringer i det du har samtykket til, spør vi på nytt.</p>
"""

# Bruksvilkår (adressen /vilkar/ er beholdt). Kjøp, angrerett og refusjon ligger bare på /kjop/.
# JURIDISK USIKKERT: Oppdelingen bruksvilkår / salgsvilkår og forholdet mellom dem (punkt 11 i listen til advokat). Lovvalg og klageorganer (EU ODR er avviklet, Roma I).
VILKAR = f"""
<p>Disse vilkårene gjelder bruk av appen Get Busted og nettsidene getbusted.no og getbusted.online. Ved å laste ned eller bruke appen godtar du vilkårene. Kjøp av innhold, angrerett, refusjon og feil ved kjøp står på siden <a href="/kjop/">Kjøp og refusjon</a>. Vilkårene begrenser ikke rettighetene du har som forbruker etter loven.</p>

<h2>1. Hvem vi er</h2>
<p>Get Busted leveres av {FIRMA}, org.nr. {ORGNR}, {ADRESSE}. E-post: {MAIL}.</p>

<h2>2. For voksne over 18 år</h2>
<p>Get Busted er et festspill for voksne. Du må være over 18 år for å bruke appen. Spillet kan spilles med eller uten alkohol, og alkoholfri modus (poeng i stedet for slurker) er alltid tilgjengelig.</p>

<h2>3. Spill ansvarlig</h2>
<ul>
  <li>Alle bestemmer selv. Det er alltid lov å stå over et kort, uten å forklare hvorfor.</li>
  <li>Ingen skal presses til å drikke, gjøre utfordringer eller svare på spørsmål de ikke vil.</li>
  <li>Spill alkoholfritt hvis noen er gravide, tar medisiner som ikke tåler alkohol, skal kjøre eller av andre grunner ikke bør drikke.</li>
  <li>Følg loven og stedets regler. Gjør ingen utfordringer som kan skade deg selv, andre eller ting rundt dere.</li>
  <li>Del bare bilder, opptak eller oppsummeringer av andre hvis de har sagt ja.</li>
</ul>
<p>Du er selv ansvarlig for hvordan du og gruppen bruker spillet. Kortene er ment som humor og kan oppleves som frekke, særlig på nivået Get Fu**ed. Velg nivå og pakker som passer gruppen.</p>

<h2>4. Lisens til å bruke appen</h2>
<p>Appen er gratis å laste ned. Du får en personlig rett til å bruke appen og innholdet du har tilgang til på enhetene som er knyttet til samme Apple-ID eller Google-konto. Retten kan ikke selges eller overføres til andre. Bruken følger også Apples eller Googles vilkår for appen.</p>

<h2>5. Innhold og rettigheter</h2>
<p>Navnet Get Busted, logoen, kortene, tekstene, omslagene og resten av innholdet tilhører {FIRMA}. Du kan dele enkeltkort og oppsummeringer fra appen med delingsfunksjonen. Du kan ikke kopiere kortstokkene, selge innholdet videre, lage egne utgaver av spillet eller bruke innholdet kommersielt uten skriftlig samtykke.</p>

<h2>6. Endringer i appen</h2>
<p>Vi utvikler appen videre og kan legge til, endre eller ta bort kort, funksjoner og design. Vi tar ikke bort innhold du har betalt for, med mindre det er nødvendig, for eksempel fordi et kort viser seg å være krenkende eller i strid med loven. Da erstatter vi det med tilsvarende innhold. Oppdateringer kan være nødvendige for at appen skal virke.</p>

<h2>7. Tilgjengelighet og ansvar</h2>
<p>Vi gjør vårt beste for at appen skal virke, men kan ikke love at den alltid er feilfri eller tilgjengelig. Appen kan være utilgjengelig ved vedlikehold eller feil hos Apple, Google eller andre leverandører, og noen funksjoner krever internett.</p>
<p>Vi er ikke ansvarlige for skade eller tap som skyldes hvordan spillet blir brukt, for eksempel at noen drikker for mye eller gjør utfordringer som går galt. Dette gjelder ikke hvis skaden skyldes vår grove uaktsomhet eller forsett, eller hvis ansvarsfritak ikke er tillatt etter loven.</p>

<h2>8. Lenker til andre tjenester</h2>
<p>Appen og nettsidene kan lenke til Spotify, Instagram, TikTok, Facebook, App Store og Google Play. Disse tjenestene har egne vilkår, og vi er ikke ansvarlige for dem.</p>

<h2>9. Lovvalg og tvister</h2>
<p>Norsk lov gjelder. Bor du i et annet land i EU/EØS eller Storbritannia, beholder du forbrukervernet du har etter loven der du bor. Ta kontakt med oss først hvis du er misfornøyd. Finner vi ikke en løsning, kan du som forbruker i Norge klage til <a href="https://www.forbrukertilsynet.no/">Forbrukertilsynet</a> og <a href="https://www.forbrukerklageutvalget.no/">Forbrukerklageutvalget</a>, eller bringe saken inn for de alminnelige domstolene. Dette gjelder også klager på kjøp.</p>

<h2>10. Endringer i vilkårene</h2>
<p>Vi kan endre vilkårene, for eksempel når appen får nye funksjoner eller loven endres. Den gjeldende versjonen står alltid her, med dato øverst. Vesentlige endringer som er til ulempe for deg, gir vi beskjed om i appen eller på nettsiden før de gjelder.</p>
"""

# Kjøpsvilkår (salgsvilkår): kjøp, Busted+, pris, angrerett, refusjon og reklamasjon.
# Beslutning 12: «Pakker som kommer» bruker den snevre avgrensningen fra salgsvilkar.md til advokaten har sett på det.
# Beslutning 13: lanseringsprisen står (se PRISTEKST og PRICE_CHANGE_DATE øverst).
# Beslutning 14: «14 dager» som refusjonsløfte og Googles «48 timer» er fjernet. Angrerett står bare som forklaring av lovens hovedregel.
# JURIDISK USIKKERT: (1) Oppfyller Apples og Googles kjøpsdialog angrerettloven § 22 bokstav n (uttrykkelig samtykke, bekreftelse, varig medium), og hvem er selger?
# JURIDISK USIKKERT: (2) «så lenge vi tilbyr appen» og hva som skjer ved nedleggelse (avtaleloven § 36, markedsføringsloven).
# JURIDISK USIKKERT: (3) Om lanseringspris og senere prisøkning må merkes spesielt (prisopplysning, markedsføringsloven).
# JURIDISK USIKKERT: (4) Reklamasjonsfrist og kontaktpunkt for digitale ytelser (digitalytelsesloven).
KJOP = f"""
<p>Denne siden gjelder kjøp i appen Get Busted. Selger er {FIRMA}, org.nr. {ORGNR}, {ADRESSE}, {MAIL}. Du må være over 18 år. Regler for bruk av appen står i <a href="/vilkar/">Bruksvilkår</a>.</p>

<h2>Kort fortalt</h2>
<ul>
  <li>Alle kjøp er engangskjøp gjennom App Store eller Google Play. Ingen abonnement og ingen automatisk trekk.</li>
  <li>Apple og Google tar imot betalingen og behandler refusjon etter sine egne regler.</li>
  <li>Virker ikke noe du har kjøpt, retter vi feilen. Får vi det ikke til, har du krav på prisavslag eller pengene tilbake.</li>
</ul>

<h2>Hva du kjøper</h2>
<p>Appen er gratis å laste ned og gir 50 kort fra Original gratis hver kveld. Du kan kjøpe temapakker, Get Fu**ed-nivået, Kveldspakke (én pakke og Get Fu**ed-nivået) og Busted+ (alle pakker). Prisen står i butikken før du bekrefter kjøpet, og inkluderer merverdiavgift. Prisen kan variere mellom land. Kjøpet er bindende når du har bekreftet det i butikken. Innholdet låses opp med en gang kjøpet er bekreftet, og appen husker kjøpet slik at du kan spille uten nett. Hva du får bruke innholdet til, står under Lisens i <a href="/vilkar/">Bruksvilkår</a>.</p>

<h2>Busted+ og pakker som kommer</h2>
<p>Busted+ gir tilgang til alle pakker i appen, også nye kortpakker og nye nivåer som {FIRMA} selv slipper i Get Busted-appen, så lenge vi tilbyr appen. Du betaler ikke ekstra for nye pakker som er en del av appens vanlige pakkeutvalg. Det gjelder ikke:</p>
<ul>
  <li>en egen, separat app eller et annet spill</li>
  <li>fysiske produkter, for eksempel en kortstokk</li>
  <li>innhold laget sammen med eller solgt av en tredjepart, hvis det er tydelig merket at det ikke er med i Busted+</li>
  <li>tidsbegrenset innhold som vi uttrykkelig har sagt er ekstra</li>
</ul>
<p>Vi bestemmer selv hvor mange pakker som slippes og når. Busted+ er et engangskjøp. Vi trekker aldri penger automatisk.</p>
<p>Pakker med senere slippdato vises som «Kommer» og kan ikke kjøpes enkeltvis før de er sluppet. Busted+ låser dem opp automatisk på slippdatoen. Blir en pakke forsinket, låses den opp når den kommer. Har du kjøpt Busted+ og en varslet pakke ikke blir sluppet, kan du ta kontakt for et passende prisavslag.</p>

<h2>Pris og lanseringspris</h2>
<p>{PRISTEKST}</p>

<h2>Angrerett</h2>
<p>Etter angrerettloven har du som forbruker vanligvis 14 dagers angrerett. For digitalt innhold som leveres med en gang, bortfaller angreretten når leveringen er påbegynt etter at du uttrykkelig har samtykket til det og har bekreftet at angreretten da går tapt (angrerettloven § 22 bokstav n). Kjøp skjer i butikkens egen betalingsdialog, og innholdet leveres umiddelbart når kjøpet er bekreftet.</p>

<h2>Refusjon hos Apple og Google</h2>
<p>Apple og Google tar imot betalingen og behandler refusjon etter sine egne regler. Reglene kan endres, så sjekk alltid gjeldende regler hos butikken:</p>
<ul>
  <li><b>iPhone:</b> <a href="https://support.apple.com/no-no/118223">Apples side om refusjon</a>. Du ber om refusjon på <a href="https://reportaproblem.apple.com/">reportaproblem.apple.com</a> med Apple-ID-en du kjøpte med.</li>
  <li><b>Android:</b> <a href="https://support.google.com/googleplay/answer/15574897?hl=no">Googles side om refusjon i Google Play</a>.</li>
</ul>
<p>Har du kjøpt noe ved en feil, kan du kontakte oss på {MAIL} og sende kvitteringen eller ordrenummeret fra Apple eller Google. Vi hjelper deg så langt vi kan, men utbetalingen skjer hos Apple eller Google.</p>

<h2>Feil ved kjøp</h2>
<p>Innhold du har kjøpt, skal virke slik det er beskrevet. Er det feil, for eksempel at en pakke ikke låses opp eller ikke kan gjenopprettes, har du rettigheter etter digitalytelsesloven. Prøv først «Gjenopprett kjøp» i appen, med samme Apple-ID eller Google-konto som du kjøpte med. Virker det ikke, skriv til {MAIL} uten ugrunnet opphold og beskriv feilen, gjerne med kvittering, telefon og appversjon. Vi retter feilen så raskt vi kan, for eksempel med en oppdatering, og du kan måtte installere den. Klarer vi det ikke innen rimelig tid, har du krav på prisavslag eller å få pengene tilbake. Dette begrenser ikke rettighetene du har som forbruker etter loven.</p>

<h2>Spørsmål og klage</h2>
<p>Skriv til {MAIL}. Hvem du kan klage til hvis vi ikke blir enige, står under Lovvalg og tvister i <a href="/vilkar/">Bruksvilkår</a>. Hvordan vi behandler personopplysninger, står i <a href="/personvern/">personvernerklæringen</a>.</p>
"""

COOKIES = f"""
<h2>Kort fortalt</h2>
<p>getbusted.no bruker ingen informasjonskapsler (cookies). Nettleseren din lagrer bare valget ditt om statistikk. Besøksstatistikk med Metricool slås på bare hvis du trykker «Godta».</p>

<h2>Det som lagres i nettleseren din</h2>
<table class="tbl">
  <caption class="sr">Lagring i nettleseren på getbusted.no</caption>
  <thead><tr><th scope="col">Navn</th><th scope="col">Hva og hvorfor</th><th scope="col">Hvor lenge</th><th scope="col">Samtykke</th></tr></thead>
  <tbody>
    <tr><td data-l="Navn"><code>gb-samtykke</code></td><td data-l="Hva og hvorfor">Husker om du har sagt ja eller nei til statistikk, så vi ikke spør på hver side. Lagres i nettleserens lokale lagring (localStorage), sendes ikke til noen.</td><td data-l="Hvor lenge">Til du sletter nettleserdata eller endrer valget</td><td data-l="Samtykke">Nei, nødvendig</td></tr>
  </tbody>
</table>

<h2>Besøksstatistikk (Metricool)</h2>
<table class="tbl">
  <caption class="sr">Statistikkverktøy på getbusted.no</caption>
  <thead><tr><th scope="col">Tjeneste</th><th scope="col">Hva som sendes</th><th scope="col">Formål</th><th scope="col">Samtykke</th></tr></thead>
  <tbody>
    <tr><td data-l="Tjeneste">Metricool (Metricool Software S.L., Spania)</td><td data-l="Hva som sendes">Adressen til siden, siden du kom fra, størrelsen på nettleservinduet, IP-adresse og nettlesertype. Ingen informasjonskapsler.</td><td data-l="Formål">Telle besøk og se hvilke sider som blir lest</td><td data-l="Samtykke">Ja, lastes bare etter «Godta»</td></tr>
  </tbody>
</table>
<p>Selv om Metricool ikke setter informasjonskapsler, henter den informasjon fra nettleseren din. Derfor spør vi om samtykke etter ekomloven § 3-15.</p>

<h2>Endre eller trekke samtykket</h2>
<p><button type="button" class="btn-link" data-samtykke>Endre valget mitt om statistikk</button></p>
<p>Du kan også slette nettleserdata for getbusted.no i innstillingene i nettleseren. Da spør vi på nytt neste gang.</p>

<h2>Ingen andre tredjeparter</h2>
<p>Skriften ligger på vår egen server, og det finnes ingen innebygde videoer, kart, reklame eller sosiale medier-knapper som laster innhold fra andre. Lenkene til Instagram, TikTok og Facebook er vanlige lenker.</p>

<h2>getbusted.online</h2>
<p>Den engelske, svenske og danske nettsiden bruker ingen informasjonskapsler og ingen statistikk. Den husker bare språket du har valgt (<code>gb-lang</code> i localStorage), som er nødvendig for at siden skal vise riktig språk.</p>

<h2>Mer om personvern</h2>
<p>Les <a href="/personvern/">personvernerklæringen</a> for hvordan vi behandler personopplysninger i appen og på nettsidene. Spørsmål: {MAIL}.</p>
"""

PAGES = [
    ('personvern', 'Personvernerklæring', 'Hvordan Get Busted behandler personopplysninger i appen og på nettsidene.', PERSONVERN),
    ('vilkar', 'Bruksvilkår', 'Bruksvilkår for appen Get Busted og nettsidene getbusted.no og getbusted.online.', VILKAR),
    ('kjop', 'Kjøp, angrerett og refusjon', 'Slik fungerer kjøp i Get Busted, angrerett, refusjon og feil ved kjøp.', KJOP),
    ('informasjonskapsler', 'Informasjonskapsler og statistikk', 'Hva getbusted.no lagrer i nettleseren, og hvordan du endrer samtykket til statistikk.', COOKIES),
]

for slug, title, desc, body in PAGES:
    d = ROOT / slug
    d.mkdir(exist_ok=True)
    (d / 'index.html').write_text(page(slug, title, desc, body), encoding='utf-8')
    print('skrev', slug)

# Felles bunntekst og hopp-lenke på de andre sidene
for f in ['index.html', '404.html', 'hjelp/index.html']:
    p = ROOT / f
    s = p.read_text(encoding='utf-8')
    s2 = re.sub(r'<footer>.*?</footer>', FOOTER, s, count=1, flags=re.S)
    if '<a class="skip"' not in s2:
        s2 = s2.replace('<body>\n', '<body>\n<a class="skip" href="#innhold">Hopp til innholdet</a>\n', 1)
    if s2 != s:
        p.write_text(s2, encoding='utf-8'); print('bunntekst', f)
