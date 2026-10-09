# Påminnelser

## 1. januar 2027: lanseringsprisen på Busted+ utløper

Siden /kjop/ sier at Busted+ koster 249 kr til og med 31. desember 2026 og 299 kr fra 1. januar 2027.

Gjør dette 1. januar 2027 (eller før):
1. Bekreft at prisen i App Store og Google Play er endret til 299 kr.
2. I `_kilde/juridisk.py`: sett `LAUNCH_PRICE_ACTIVE = False`. Siden viser da bare 299 kr.
3. Kjør `python3 _kilde/juridisk.py` og kontroller /kjop/.
4. Gjør tilsvarende i getbusted.online (`build.py`, samme konstanter).
5. Sjekk at forsiden, butikkoppføringene og SoMe ikke fortsatt sier 249 kr.

Generatoren stopper med en feilmelding hvis den kjøres 1. januar 2027 eller senere mens `LAUNCH_PRICE_ACTIVE = True`. Konstanten `PRICE_CHANGE_DATE` står øverst i `_kilde/juridisk.py`.

## Ved hvert pakkeslipp: oppdater kortantall og pakketall

Forsiden (index.html: meta description, og:description, ingress og tallboksene) sier «Over 1 000 kort i 5 pakker fra start og nye pakker utover høsten» (tallboksene: «1 000+ kort fra start», «5 pakker fra start, flere i høst»). Oppdater tallene hver gang en ny pakke slippes. Ikke lov «nye pakker hver uke». Gjør det samme på getbusted.online (COUNTS og «1 000+» / «5 pakker» i build.py). Bildet img/og.jpg har «Over 1 000 kort i 5 pakker» på seg og må lages på nytt når tallene endres (Pillow, Barlow Semi Condensed 800 Italic, 1200x630). getbusted.online har ingen tall om pakker i og_*-bildene.

## Fjernet i denne runden (kun-juridisk, oktober 2026)

- Løftet om prisavslag hvis en Busted+-pakke ikke kommer (/kjop/). Lovfestede rettigheter ved feil står igjen.
- All omtale av fysisk kortstokk/fysiske produkter (/kjop/, /vilkar/, forsiden: «Mer enn en kortstokk» er nå «Mer enn bare kort»).
- «Over 18 år» er byttet til «minst 18 år» (vilkår, kjøp, personvern, bunntekst, forsiden, hjelp).
- Prisene 249 kr (til og med 31. desember 2026) og 299 kr (fra 1. januar 2027) står som før på /kjop/.

## Før Sverige-lanseringen: personvernsidene på getbusted.online

Personvernsidene /privacy/, /se/integritet/ og /dk/privatliv/ på getbusted.online er ikke oppdatert til ny personvernerklæring ennå. Legg dem på listen og oppdater dem (samme innhold som /personvern/ her, på riktig språk) før Sverige-lanseringen.

## Ikke verifisert

Klageorganer og tilsyn. Ingen av disse er sjekket mot offisielle kilder (navn, hvem som er riktig organ for en nettbutikk/app, og at lenkene virker). Sjekk før lansering i hvert land.

Nevnt på getbusted.no (bruksvilkår, kjøp og personvern):
- Forbrukertilsynet (forbrukertilsynet.no) - IKKE VERIFISERT
- Forbrukerklageutvalget (forbrukerklageutvalget.no) - IKKE VERIFISERT
- Datatilsynet (datatilsynet.no) - IKKE VERIFISERT

Sverige (skal inn på /se/ på getbusted.online, ikke på denne siden):
- Allmänna reklamationsnämnden (ARN) - IKKE VERIFISERT
- Konsumentverket - IKKE VERIFISERT
- Integritetsskyddsmyndigheten (IMY) - IKKE VERIFISERT

Danmark (skal inn på /dk/ på getbusted.online, ikke på denne siden):
- Forbrugerklagenævnet - IKKE VERIFISERT
- Forbrugerombudsmanden - IKKE VERIFISERT
- Datatilsynet (Danmark) - IKKE VERIFISERT

Redaktørene for sv og da la inn noen forbehold som gjelder norsk side på samme måte (sjekkes sammen med jurist):
- At Apples og Googles kjøpsdialog innhenter uttrykkelig samtykke og bekreftelse på tapt angrerett (angrerettloven § 22 bokstav n) - IKKE VERIFISERT
- Om Snikkerbua Holding AS er selger overfor forbrukere i app-kjøp - IKKE VERIFISERT
- Lenkene til Apple og Google om refusjon (support.apple.com/no-no/118223, support.google.com/googleplay/answer/15574897) - IKKE VERIFISERT
- Org.nr og adresse mot Brønnøysundregistrene - IKKE VERIFISERT
