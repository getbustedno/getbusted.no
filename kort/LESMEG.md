# Aktuelt-kort

`aktuelt.json` hentes av appen ved oppstart (https://getbusted.no/kort/aktuelt.json). Bytt fila en gang i måneden, push, så har alle de nye kortene innen en time. Ingen app-oppdatering trengs.

Regler:
- 10-20 kort. Minst 5, ellers vises ikke pakken.
- `id` må være unik (bruk ÅÅMM-nr, f.eks. 2612-01).
- `type`: drikk_om, pekeleken, navnekort, regel, duell, runde, sannhet, hemmelig, sang, quiz
- `spice`: 1 Mild, 2 Frekk, 3 Get Fu**ed
- `{spiller}` og `{spiller2}` byttes med navn.
- Ugyldige kort hoppes over, så en skrivefeil krasjer aldri appen.
- Vri på fenomenet, ikke på personer i straffesaker. Ingen navngitte privatpersoner.
