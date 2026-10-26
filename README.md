# l'Heritage Reninge

Website van B&B en tearoom l'Heritage, Dorpplaats 15, 8647 Reninge: www.lheritage.be

Een eenvoudige statische site, zonder WordPress of database, in drie talen:

| Taal | Bestand | Adres |
|---|---|---|
| Nederlands | `index.html` | `/` |
| Frans | `fr/index.html` | `/fr/` |
| Engels | `en/index.html` | `/en/` |

## Teksten aanpassen

Alle teksten staan in `tools/build.py`. Pas ze daar aan en maak de pagina's opnieuw aan met:

```
python3 tools/build.py
```

Pas de HTML-bestanden dus niet rechtstreeks aan, want die worden overschreven.

Stijl en kleuren staan in `assets/css/style.css`, foto's in `assets/img/`.

## Boeken

Alle boekknoppen gaan naar Cubilis (rechtstreeks boeken, minder commissie dan Booking.com):
https://reservations.cubilis.eu/b-and-b-lheritage-reninge

## Online zetten (Cloudflare Pages)

1. Maak een gratis account op cloudflare.com.
2. Ga naar **Workers & Pages → Create → Pages → Connect to Git** en kies deze repository.
3. Laat "Build command" leeg en zet "Build output directory" op `/`.
4. Na de eerste deploy staat de site op een `*.pages.dev`-adres om te testen.
5. Voeg onder **Custom domains** `lheritage.be` en `www.lheritage.be` toe zodra het domein bij Cloudflare staat.

Elke wijziging op de `main`-branch komt daarna automatisch online.
