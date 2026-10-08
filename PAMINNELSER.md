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
