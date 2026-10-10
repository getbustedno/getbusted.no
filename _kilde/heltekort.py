"""Heltekortet i hero (midtkortet i kortviften) på getbusted.no.

Kortet er ekte HTML/CSS (stiler i style.css, .hk-*). Første kortet i listen står server-rendret i HTML
(vises uten JS). En liten inline-JS velger ett kort tilfeldig (Math.random) ved hver sidelasting.
Ingen cookies, ingen localStorage, ingen sporing, ingen ekstern kode.

Bytt kort ved å endre KORT under og kjøre: python3 _kilde/heltekort.py
Teksten ligger mellom <!--heltekort--> og <!--/heltekort--> i index.html og skrives om hver gang.

KORT-ID-ER (til regelvakt, ordrett fra getbusted-merge/src/data/cards.json, lang no):
  GB094 GB539 GB542 GB1167 GB051 GB261 GB1783 GB125
Valgt etter: pekeleken eller drikk_om, spice 1-2, ikke minPlayers, ingen {spiller}, ingen alkohol-, drikke-,
skole-, sex- eller kjendisord, ikke på listen over kort uten markedsføring i regelvakt.md, ikke GB013.
Overskrifter og bunntekst følger appen i alkoholfri modus (HEADERS sober i engine.ts, SOBER_RULES i i18n.ts).
"""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[1]
LANG = 'no'

# (id, type, tekst). type: 'pek' = pekeleken, 'drikk' = drikk_om. Tekst ordrett fra cards.json.
KORT = [
    ('GB094', 'pek', 'har sjekket om eksen har sett storyen deres i dag'),
    ('GB539', 'pek', 'har dyrest fjellutstyr og kortest turer'),
    ('GB542', 'pek', 'snorker så høyt at noen flytter ut i bilen'),
    ('GB1167', 'pek', 'sier de skal være offline på hytta og legger ut story tre ganger'),
    ('GB051', 'drikk', 'sagt «i like måte» da servitøren sa «god appetitt»'),
    ('GB261', 'drikk', 'tapt Whamageddon før desember var halvveis'),
    ('GB1783', 'drikk', 'blitt spurt «hva er du utkledd som?» uten å være utkledd'),
    ('GB125', 'pek', 'har den mest pinlige Spotify Wrapped'),
]

# Alkoholfri tone, som appen skriver det (engine.ts HEADERS sober, i18n.ts footers.pek + SOBER_RULES).
HEAD = {
    'no': {'pek': 'På tre - pek på den som', 'drikk': 'Poeng om du har'},
    'sv': {'pek': 'På tre - peka på den som', 'drikk': 'Ta en poäng om du har'},
    'da': {'pek': 'På tre - peg på den der', 'drikk': 'Point hvis du har'},
    'en': {'pek': 'On three, point at the one who', 'drikk': 'Points if you have'},
}
FOOT = {
    'no': 'Flest pekere får 2 poeng',
    'sv': 'Den med flest pekningar får 2 poäng',
    'da': 'Den, flest peger på, får 2 point',
    'en': 'Whoever gets the most fingers gets 2 points',
}
HANDLE = {l: '@getbusted.no' for l in HEAD}  # samme som i de gamle kortbildene


def storrelse(tekst):
    """Startstørrelse på brødteksten i cqw (prosent av kortbredden), etter lengde og lengste ord.
    JS finjusterer etterpå hvis noe likevel flyter ut."""
    n = len(tekst)
    s = 14 if n <= 30 else 12.5 if n <= 60 else 11 if n <= 75 else 9.5 if n <= 95 else 8.5
    lengste = max(len(w) for w in re.split(r'[\s-]+', tekst))
    return round(min(s, 84 / (lengste * 0.58)), 1)


def kort_data(lang, kort):
    return [{'h': HEAD[lang][t], 'b': tekst, 'f': FOOT[lang] if t == 'pek' else '', 's': storrelse(tekst)}
            for _id, t, tekst in kort]


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def kort_html(lang, kort):
    data = kort_data(lang, kort)
    d0 = data[0]
    js_data = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    foot = f'<p class="hk-f">{esc(d0["f"])}</p>' if d0['f'] else '<p class="hk-f" hidden></p>'
    return (
        '<div class="card hk" data-hk>'
        '<div class="hk-in">'
        f'<p class="hk-h">{esc(d0["h"])}</p>'
        f'<p class="hk-b" style="--fs:{d0["s"]}cqw">{esc(d0["b"])}</p>'
        f'{foot}'
        '</div>'
        f'<p class="hk-t">{esc(HANDLE[lang])}</p>'
        '</div>\n'
        '<script>\n'
        '(function(){var c=document.querySelector("[data-hk]");if(!c)return;var K=' + js_data + ';'
        'var k=K[Math.floor(Math.random()*K.length)];'
        'var i=c.querySelector(".hk-in"),h=c.querySelector(".hk-h"),b=c.querySelector(".hk-b"),f=c.querySelector(".hk-f");'
        'h.textContent=k.h;b.textContent=k.b;f.textContent=k.f;f.hidden=!k.f;'
        'function fit(){var s=k.s;b.style.setProperty("--fs",s+"cqw");'
        'while(s>5&&(i.scrollHeight>i.clientHeight+1||b.scrollWidth>b.clientWidth+1)){s-=.5;b.style.setProperty("--fs",s+"cqw")}}'
        'fit();if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fit)})();\n'
        '</script>'
    )


def main():
    p = ROOT / 'index.html'
    s = p.read_text(encoding='utf-8')
    blokk = '<!--heltekort-->' + kort_html(LANG, KORT) + '<!--/heltekort-->'
    if '<!--heltekort-->' in s:
        s2 = re.sub(r'<!--heltekort-->.*?<!--/heltekort-->', lambda m: blokk, s, count=1, flags=re.S)
    else:
        s2 = re.sub(r'<picture class="card">.*?</picture>', lambda m: blokk, s, count=1, flags=re.S)
    assert s2 != s or '<!--heltekort-->' in s, 'fant ikke heltekortet i index.html'
    if s2 != s:
        p.write_text(s2, encoding='utf-8')
        print('skrev heltekort', len(KORT), 'kort')
    else:
        print('uendret')


if __name__ == '__main__':
    main()
