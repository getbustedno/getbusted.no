# Aktuelt-kort

`aktuelt.json` hentes av appen ved oppstart (https://getbusted.no/kort/aktuelt.json). Kortene blandes inn i pakken de hører til, tidlig i stokken, og merkes «AKTUELT». Bytt fila en gang i måneden, push, så har alle de nye kortene innen en time. Ingen app-oppdatering trengs.

Regler:
- `pack`: original, jul, nach, hytta, utdrikning, fotball, sport, reise, student (og nye pakker når de kommer). Mangler den, havner kortet i Original.
- 2-7 kort per pakke. Finn vinkelen for hver pakke: Fotball = fotballnyheter, Jul = julebord og jul, Reise = fly og ferie osv.
- Original er gratis for alle, så de beste kortene med bredest appell legges der.
- `id` må være unik (bruk ÅÅMM-nr, f.eks. 2612-01).
- `type`: drikk_om, pekeleken, navnekort, regel, duell, runde, sannhet, hemmelig, sang, quiz
- `spice`: 1 Mild, 2 Frekk, 3 Get Fu**ed
- `{spiller}` og `{spiller2}` byttes med navn.
- Ugyldige kort hoppes over, så en skrivefeil krasjer aldri appen.
- Vri på fenomenet, ikke på personer i straffesaker. Ingen navngitte privatpersoner.
