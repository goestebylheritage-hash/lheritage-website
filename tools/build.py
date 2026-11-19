#!/usr/bin/env python3
"""Genereert index.html, fr/index.html en en/index.html voor l'Heritage."""
import json, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.lheritage.be'
CUBILIS = 'https://reservations.cubilis.eu/b-and-b-lheritage-reninge'
GOESTE = 'https://goestepoperinge.be'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Dorpplaats+15+8647+Reninge'

ROOMS = [
    ('verm', 'Vermillion', 'kamer-vermillion', 1),
    ('oran', 'Orange', 'kamer-orange', 1),
    ('bgris', 'Bleu gris', 'kamer-bleu-blanc', 1),
    ('bblanc', 'Bleu blanc', 'kamer-bleu-gris', 2),
    ('vert', 'Vert', 'kamer-vert', 2),
]

T = {
'nl': dict(
    path='/', htmllang='nl-BE',
    title="l'Heritage · B&B en tearoom in Reninge",
    desc="Bed & breakfast in de oude kapelanij van Reninge, tussen Ieper, Poperinge en Diksmuide. Vijf kamers met ontbijt met streekproducten, vanaf €80 per nacht.",
    nav=['Verblijf', 'Kamers', 'Tearoom', 'De streek', 'Contact'], navbook='Boek een kamer', menu='Hoofdmenu', langlabel='Taal',
    eyebrow='Bed &amp; breakfast in de Westhoek',
    h1='Slapen in de oude kapelanij van Reninge',
    lead='Vijf kamers met elk hun eigen kleur, een uitgebreid ontbijt met streekproducten en de weidse IJzerbroeken vlak achter het dorp.',
    cta1='Bekijk beschikbaarheid', cta2='Wat je mag verwachten',
    pricenote='<strong>€80</strong> per nacht voor 1 persoon · <strong>€115</strong> voor 2 personen · ontbijt inbegrepen',
    slides=["De oude kapelanij van l'Heritage aan de Dorpplaats in Reninge", 'Het terras en de tuin met buxushagen en hortensia\'s', 'De ontbijtzaal met rode wanden, kroonluchter en gedekte tafels', 'Kamer Vermillion met rode wand en bloemetjesdekbed', 'Ontbijt van bovenaf: broodjes, kaas, fruit en koffie', 'De tearoom met stenen bar en kroonluchter'],
    slidelabel='Foto', slidenav='Kies een foto',
    heroalt="De oude kapelanij van l'Heritage aan de Dorpplaats in Reninge",
    stay_eyebrow='Jullie verblijf', stay_h='Een rustige uitvalsbasis tussen Ieper, Poperinge en Diksmuide',
    stay_p=["l'Heritage is een familiehuis aan de Dorpplaats van Reninge, in de vroegere kapelanij naast de kerk. Je slaapt in een klein, persoonlijk huis waar je 's avonds de stilte van de polder hoort en 's ochtends aanschuift aan een gedekte ontbijttafel.",
            "Van hieruit wandel of fiets je zo de IJzerbroeken in, en ben je in een kwartier in Ieper, Poperinge of Diksmuide."],
    breakfastalt='Gedekte ontbijttafel met fruit, kaas, croissants en bloemetjesporselein',
    expect=[('Ontbijt met streekproducten', 'Elke ochtend tussen 8 en 10 uur. Vroeger vertrekken kan, laat het ons gewoon weten.'),
            ('Rekening met je dieet', 'Suikervrij, glutenvrij of andere wensen? Vermeld het bij je boeking.'),
            ('Eigen badkamer', 'Elke kamer heeft een eigen badkamertje met douche, toilet en lavabo.'),
            ('Welkom voor fietsers en wandelaars', 'Het fietsknooppuntennetwerk en de wandelroutes van de Westhoek vertrekken vlak bij de deur.')],
    rooms_eyebrow='Kamers', rooms_h='Kies je kleur',
    rooms_p=['Elke kamer draagt de naam van haar kleur. Elke kamer heeft een eigen badkamertje met douche, toilet en lavabo. Het ontbijt is altijd inbegrepen, de prijs hangt alleen af van het aantal personen.',
             'Binnen vind je hoge plafonds, oude deuren, een kroonluchter hier en daar en behang met karakter. Een huis met een verleden, waar je meteen thuiskomt.'],
    gangalt="Een jonge gast met een oude koffer in de gang van l'Heritage",
    floor=['1e verdieping', '2e verdieping'], roomword='Kamer',
    rooms=['Uitzicht op de kerktoren, twee eenpersoonsbedden.', 'Op het oosten, met de zonsopgang boven de IJzervlakte.',
           'Aan de achterkant van het huis, de rustigste plek.', 'Knus, met dakkapel en zicht over de IJzerbroeken.', 'Een stille kamer onder het dak.'],
    prices_label='Prijzen', p1='1 persoon', p2='2 personen', pernight='per nacht, ontbijt inbegrepen',
    tea_eyebrow='Tearoom', tea_h='Koffie en pannenkoeken in de tearoom',
    tea_p='Ook wie niet blijft slapen is welkom. Op het zonnige terras of bij de open haard bakken we verse pannenkoeken volgens het familierecept, en schenken we koffie voor fietsers en wandelaars die even willen uitblazen.',
    tealt='De tearoom met stenen bar, kroonluchter en hoge ramen', seasons=[('Zomer', 'van Pasen tot ons verlof eind september', 'woensdag tot zaterdag'), ('Winter', 'van begin oktober tot Pasen', 'vrijdag en zaterdag')],
    holiday='Een tussentijds verlof wordt steeds op voorhand aangekondigd in de zaak.',
    area_eyebrow='De streek', area_h='Wat je vanuit Reninge kunt ontdekken',
    area_lead='De Westhoek is vlak, groen en vol verhalen. Een paar tips van ons, op fiets- of korte autoafstand.',
    places=[('Vlak bij huis', 'IJzerbroeken &amp; De Blankaart', 'Natte weilanden langs de IJzer, met in de winter duizenden ganzen. Ideaal om te wandelen en vogels te kijken.'),
            ('± 15 min', 'Ieper', 'De Lakenhalle, het In Flanders Fields Museum en elke avond om 20 uur de Last Post onder de Menenpoort.'),
            ('± 15 min', 'Poperinge', 'Hopstad met het Hopmuseum en Talbot House. Proef er de streek bij Goeste.'),
            ('± 15 min', 'Diksmuide', 'De IJzertoren en de Dodengang, een van de best bewaarde loopgraven van de Eerste Wereldoorlog.'),
            ('± 10 min', 'Westvleteren', 'De abdij Sint-Sixtus en het bezoekerscentrum In de Vrede, bekend om het trappistenbier.'),
            ('± 30 min', 'De kust', 'Nieuwpoort en De Panne voor een dag zee en strand.')],
    book_eyebrow='Boeken en contact', book_h='Boek je kamer',
    book_lead='Bekijk de vrije data en boek meteen online, rechtstreeks bij ons. Liever eerst iets vragen? Bel of mail ons gerust.',
    book_btn='Boek rechtstreeks', call='Bel ons', route='Route',
    contact=['Adres', 'Telefoon', 'E-mail', 'Ontbijt', 'Tearoom'], teatime='zomer wo–za, winter vr–za, 14:00 – 18:00',
    foot='B&amp;B en tearoom · Dorpplaats 15, 8647 Reninge',
    goeste1="Zin in l'Heritage-ijs of streekproducten?",
    goeste2=f"Die vind je niet in Reninge, maar in ons restaurant en streekwinkel <a href=\"{GOESTE}\">Goeste in Poperinge</a>, op een kwartiertje rijden.",
),
'fr': dict(
    path='/fr/', htmllang='fr-BE',
    title="l'Heritage · Chambres d'hôtes et salon de thé à Reninge",
    desc="Chambres d'hôtes dans l'ancienne maison du chapelain de Reninge, entre Ypres, Poperinge et Dixmude. Cinq chambres, petit-déjeuner aux produits du terroir, à partir de 80 € la nuit.",
    nav=['Séjour', 'Chambres', 'Salon de thé', 'La région', 'Contact'], navbook='Réserver', menu='Menu principal', langlabel='Langue',
    eyebrow="Chambres d'hôtes dans le Westhoek",
    h1="Dormir dans l'ancienne maison du chapelain de Reninge",
    lead="Cinq chambres, chacune avec sa propre couleur, un copieux petit-déjeuner aux produits du terroir et les vastes prairies de l'Yser juste derrière le village.",
    cta1='Voir les disponibilités', cta2='À quoi vous attendre',
    pricenote='<strong>80 €</strong> la nuit pour 1 personne · <strong>115 €</strong> pour 2 personnes · petit-déjeuner compris',
    slides=["L'ancienne maison du chapelain, l'Heritage, sur la Dorpplaats de Reninge", 'La terrasse et le jardin avec haies de buis et hortensias', 'La salle du petit-déjeuner aux murs rouges, avec lustre et tables dressées', 'La chambre Vermillion avec son mur rouge et sa couette fleurie', 'Le petit-déjeuner vu du dessus : petits pains, fromages, fruits et café', 'Le salon de thé avec son bar en pierre et son lustre'],
    slidelabel='Photo', slidenav='Choisir une photo',
    heroalt="L'ancienne maison du chapelain, l'Heritage, sur la Dorpplaats de Reninge",
    stay_eyebrow='Votre séjour', stay_h='Un point de chute paisible entre Ypres, Poperinge et Dixmude',
    stay_p=["l'Heritage est une maison familiale sur la place du village de Reninge, dans l'ancienne maison du chapelain à côté de l'église. Vous logez dans une petite maison chaleureuse où l'on entend le soir le calme des polders, et où une table dressée vous attend le matin.",
            "D'ici, vous partez à pied ou à vélo dans les prairies de l'Yser, et vous êtes en un quart d'heure à Ypres, Poperinge ou Dixmude."],
    breakfastalt='Table de petit-déjeuner avec fruits, fromages, croissants et porcelaine fleurie',
    expect=[('Petit-déjeuner du terroir', "Chaque matin entre 8 et 10 heures. Vous partez plus tôt ? Il suffit de nous le dire."),
            ('Régimes respectés', 'Sans sucre, sans gluten ou autre souhait ? Indiquez-le lors de la réservation.'),
            ('Salle de bain privée', 'Chaque chambre dispose de sa propre petite salle de bain avec douche, toilettes et lavabo.'),
            ('Cyclistes et randonneurs bienvenus', 'Le réseau de points-nœuds cyclables et les promenades du Westhoek partent tout près de la porte.')],
    rooms_eyebrow='Chambres', rooms_h='Choisissez votre couleur',
    rooms_p=['Chaque chambre porte le nom de sa couleur. Chacune a sa propre petite salle de bain avec douche, toilettes et lavabo. Le petit-déjeuner est toujours compris, le prix dépend seulement du nombre de personnes.',
             "À l'intérieur : hauts plafonds, portes anciennes, un lustre ici et là et des papiers peints pleins de caractère. Une maison chargée d'histoire où l'on se sent tout de suite chez soi."],
    gangalt="Un jeune hôte avec une vieille valise dans le couloir de l'Heritage",
    floor=['1er étage', '2e étage'], roomword='Chambre',
    rooms=["Vue sur le clocher, deux lits simples.", "Orientée à l'est, avec le lever du soleil sur la plaine de l'Yser.",
           "À l'arrière de la maison, la plus calme.", "Douillette, avec lucarne et vue sur les prairies de l'Yser.", 'Une chambre paisible sous le toit.'],
    prices_label='Tarifs', p1='1 personne', p2='2 personnes', pernight='par nuit, petit-déjeuner compris',
    tea_eyebrow='Salon de thé', tea_h='Café et crêpes au salon de thé',
    tea_p="Même sans y dormir, vous êtes le bienvenu. Sur la terrasse ensoleillée ou au coin du feu, nous préparons des crêpes selon la recette de famille et servons un café aux cyclistes et promeneurs qui veulent souffler un moment.",
    tealt='Le salon de thé avec son bar en pierre, son lustre et ses hautes fenêtres', seasons=[('Été', "de Pâques jusqu'à nos congés fin septembre", 'du mercredi au samedi'), ('Hiver', 'de début octobre à Pâques', 'vendredi et samedi')],
    holiday="Une fermeture pour congés en cours de saison est toujours annoncée à l'avance au salon de thé.",
    area_eyebrow='La région', area_h='À découvrir depuis Reninge',
    area_lead="Le Westhoek est plat, vert et plein d'histoires. Quelques conseils, à vélo ou à quelques minutes en voiture.",
    places=[('Tout près', "Prairies de l'Yser &amp; De Blankaart", "Prairies humides le long de l'Yser, avec des milliers d'oies en hiver. Idéal pour marcher et observer les oiseaux."),
            ('± 15 min', 'Ypres', 'La Halle aux draps, le musée In Flanders Fields et, chaque soir à 20 heures, le Last Post sous la Porte de Menin.'),
            ('± 15 min', 'Poperinge', 'La ville du houblon, avec son musée du houblon et Talbot House. Goûtez la région chez Goeste.'),
            ('± 15 min', 'Dixmude', "La Tour de l'Yser et le Boyau de la Mort, l'une des tranchées de la Première Guerre mondiale les mieux conservées."),
            ('± 10 min', 'Westvleteren', "L'abbaye Saint-Sixte et le centre d'accueil In de Vrede, connu pour sa bière trappiste."),
            ('± 30 min', 'La côte', 'Nieuport et La Panne pour une journée de mer et de plage.')],
    book_eyebrow='Réservation et contact', book_h='Réservez votre chambre',
    book_lead='Consultez les dates libres et réservez directement chez nous. Une question ? Appelez-nous ou envoyez-nous un e-mail.',
    book_btn='Réserver en direct', call='Nous appeler', route='Itinéraire',
    contact=['Adresse', 'Téléphone', 'E-mail', 'Petit-déjeuner', 'Salon de thé'], teatime='été mer.–sam., hiver ven.–sam., 14h00 – 18h00',
    foot="Chambres d'hôtes et salon de thé · Dorpplaats 15, 8647 Reninge",
    goeste1="Envie de glace l'Heritage ou de produits régionaux ?",
    goeste2=f"Vous ne les trouverez pas à Reninge, mais dans notre restaurant et épicerie régionale <a href=\"{GOESTE}\">Goeste à Poperinge</a>, à un quart d'heure en voiture.",
),
'en': dict(
    path='/en/', htmllang='en',
    title="l'Heritage · B&B and tearoom in Reninge, Belgium",
    desc="Bed & breakfast in the old chaplain's house in Reninge, between Ypres, Poperinge and Diksmuide. Five rooms, breakfast with local produce, from €80 a night.",
    nav=['Your stay', 'Rooms', 'Tearoom', 'The area', 'Contact'], navbook='Book a room', menu='Main menu', langlabel='Language',
    eyebrow='Bed &amp; breakfast in Flanders Fields',
    h1="Stay in the old chaplain's house of Reninge",
    lead='Five rooms, each with its own colour, a generous breakfast with local produce and the wide Yser meadows just beyond the village.',
    cta1='Check availability', cta2='What to expect',
    pricenote='<strong>€80</strong> a night for 1 person · <strong>€115</strong> for 2 people · breakfast included',
    slides=["l'Heritage, the old chaplain's house on the village square of Reninge", 'The terrace and garden with box hedges and hydrangeas', 'The breakfast room with red walls, chandelier and laid tables', 'The Vermillion room with its red wall and floral duvet', 'Breakfast from above: rolls, cheese, fruit and coffee', 'The tearoom with its stone bar and chandelier'],
    slidelabel='Photo', slidenav='Choose a photo',
    heroalt="l'Heritage, the old chaplain's house on the village square of Reninge",
    stay_eyebrow='Your stay', stay_h='A quiet base between Ypres, Poperinge and Diksmuide',
    stay_p=["l'Heritage is a family home on the village square of Reninge, in the former chaplain's house next to the church. You stay in a small, personal house where evenings are as quiet as the polders and breakfast is waiting on a laid table in the morning.",
            "From here you can walk or cycle straight into the Yser meadows, and Ypres, Poperinge and Diksmuide are each about fifteen minutes away."],
    breakfastalt='Breakfast table with fruit, cheese, croissants and floral china',
    expect=[('Breakfast with local produce', 'Every morning between 8 and 10. Leaving early? Just let us know.'),
            ('Dietary needs', 'Sugar-free, gluten-free or something else? Mention it when you book.'),
            ('Private bathroom', 'Every room has its own small bathroom with shower, toilet and washbasin.'),
            ('Cyclists and walkers welcome', 'The cycle network and walking routes of the Westhoek start right outside the door.')],
    rooms_eyebrow='Rooms', rooms_h='Pick your colour',
    rooms_p=['Each room is named after its colour. Each has its own small bathroom with shower, toilet and washbasin. Breakfast is always included and the price depends only on the number of guests.',
             'Inside you will find high ceilings, old doors, the odd chandelier and wallpaper with character. A house with a past, where you feel at home straight away.'],
    gangalt="A young guest with an old suitcase in the hallway of l'Heritage",
    floor=['1st floor', '2nd floor'], roomword='Room',
    rooms=['View of the church tower, two single beds.', 'Facing east, with sunrise over the Yser plain.',
           'At the back of the house, the quietest spot.', 'Cosy, with a dormer window overlooking the Yser meadows.', 'A peaceful room under the roof.'],
    prices_label='Prices', p1='1 person', p2='2 people', pernight='per night, breakfast included',
    tea_eyebrow='Tearoom', tea_h='Coffee and pancakes in the tearoom',
    tea_p="You are welcome even if you are not staying the night. On the sunny terrace or by the fireplace we bake fresh pancakes from the family recipe and pour coffee for cyclists and walkers taking a break.",
    tealt='The tearoom with its stone bar, chandelier and tall windows', seasons=[('Summer', 'from Easter until our holiday at the end of September', 'Wednesday to Saturday'), ('Winter', 'from early October until Easter', 'Friday and Saturday')],
    holiday='Any closure for holidays during the season is always announced in advance at the tearoom.',
    area_eyebrow='The area', area_h='What to discover from Reninge',
    area_lead='The Westhoek is flat, green and full of stories. A few tips from us, by bike or a short drive away.',
    places=[('On the doorstep', 'Yser meadows &amp; De Blankaart', 'Wet meadows along the Yser, with thousands of geese in winter. Perfect for walking and birdwatching.'),
            ('± 15 min', 'Ypres (Ieper)', 'The Cloth Hall, the In Flanders Fields Museum and, every evening at 8 pm, the Last Post at the Menin Gate.'),
            ('± 15 min', 'Poperinge', 'The hop town, with its Hop Museum and Talbot House. Taste the region at Goeste.'),
            ('± 15 min', 'Diksmuide', 'The Yser Tower and the Trench of Death, one of the best-preserved trenches of the First World War.'),
            ('± 10 min', 'Westvleteren', 'Saint Sixtus Abbey and the In de Vrede visitor centre, known for its Trappist beer.'),
            ('± 30 min', 'The coast', 'Nieuwpoort and De Panne for a day by the sea.')],
    book_eyebrow='Booking and contact', book_h='Book your room',
    book_lead='See which dates are free and book online, directly with us. Questions first? Call or email us.',
    book_btn='Book direct', call='Call us', route='Directions',
    contact=['Address', 'Phone', 'Email', 'Breakfast', 'Tearoom'], teatime='summer Wed–Sat, winter Fri–Sat, 14:00 – 18:00',
    foot='B&amp;B and tearoom · Dorpplaats 15, 8647 Reninge, Belgium',
    goeste1="Fancy l'Heritage ice cream or local produce?",
    goeste2=f"You will not find them in Reninge, but at our restaurant and regional shop <a href=\"{GOESTE}\">Goeste in Poperinge</a>, a fifteen-minute drive away.",
),
}

SLIDES = ['slide-gevel', 'slide-terras', 'slide-ontbijtzaal', 'slide-vermillion', 'slide-ontbijt', 'slide-tearoom']

# Uitsnede per foto aanpassen als het belangrijkste deel buiten beeld valt
SLIDE_POS = {'slide-terras': ' style="object-position:50% 30%"'}

HEART = '<svg viewBox="0 0 24 20" aria-hidden="true"><path d="M12 20C6 16 0 12 0 6.5 0 2.8 2.7 0 6 0c2.6 0 4.6 1.6 6 3.6C13.4 1.6 15.4 0 18 0c3.3 0 6 2.8 6 6.5C24 12 18 16 12 20z"/></svg>'
IDS = ['verblijf', 'kamers', 'tearoom', 'streek', 'boeken']


def page(lang):
    t = T[lang]
    pre = '' if lang == 'nl' else '../'
    img = lambda n: f'{pre}assets/img/{n}'
    ext = 'target="_blank" rel="noopener"'
    alts = '\n'.join(f'  <link rel="alternate" hreflang="{T[l]["htmllang"][:2]}" href="{SITE}{T[l]["path"]}">' for l in T)
    langs = ''.join(f'<a href="{pre}{T[l]["path"].lstrip("/")}"{" aria-current=\"page\"" if l == lang else ""} lang="{l}">{l.upper()}</a>' for l in T)
    ld = {
        "@context": "https://schema.org", "@type": "BedAndBreakfast", "name": "l'Heritage",
        "url": SITE + t['path'], "image": SITE + '/assets/img/slide-gevel.jpg', "telephone": "+32 497 42 16 94", "email": "info@lheritage.be",
        "priceRange": "€80 – €115",
        "address": {"@type": "PostalAddress", "streetAddress": "Dorpplaats 15", "postalCode": "8647", "addressLocality": "Reninge", "addressCountry": "BE"},
        "numberOfRooms": 5,
    }
    nav = ''.join(f'<a href="#{i}">{n}</a>\n      ' for i, n in zip(IDS, t['nav']))
    expect = ''.join(f'<li><b>{a}</b><span>{b}</span></li>\n          ' for a, b in t['expect'])
    rooms = ''
    for (c, name, f, fl), d in zip(ROOMS, t['rooms']):
        rooms += f'''<article class="room"><div class="chip" style="--c:var(--{c})"><img src="{img(f + '.jpg')}" alt="{t['roomword']} {name}" width="900" height="600" loading="lazy"><span>{t['floor'][fl - 1]}</span></div><div class="txt"><h3>{name}</h3><p>{d}</p></div></article>
        '''
    places = ''.join(f'<div class="place"><span class="dist">{a}</span><h3>{b}</h3><p>{c}</p></div>\n        ' for a, b, c in t['places'])
    stay_p = ''.join(f'<p>{p}</p>\n          ' for p in t['stay_p'])
    rooms_p = ''.join(f'<p class="lead">{p}</p>\n        ' for p in t['rooms_p'])
    hours = ''.join(f'<div><dt>{n}<small>{w}</small></dt><dd>{d}<br>14:00 – 18:00</dd></div>\n          ' for n, w, d in t['seasons'])
    slides = ''.join(
        f'<img class="slide{" is-active" if i == 0 else ""}"{SLIDE_POS.get(f, "")} src="{img(f + ".jpg")}" srcset="{img(f + "-1000.jpg")} 1000w, {img(f + ".jpg")} 1920w" sizes="100vw" alt="{a}" width="1920" height="1280"{" fetchpriority=\"high\"" if i == 0 else " loading=\"lazy\""}>\n      '
        for i, (f, a) in enumerate(zip(SLIDES, t['slides'])))
    dots = ''.join(f'<button type="button" aria-label="{t["slidelabel"]} {i + 1}"{" aria-current=\"true\"" if i == 0 else ""}></button>' for i in range(len(SLIDES)))
    ct = t['contact']
    return f'''<!doctype html>
<html lang="{t['htmllang']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{t['title']}</title>
  <meta name="description" content="{html.escape(t['desc'])}">
  <link rel="canonical" href="{SITE}{t['path']}">
{alts}
  <link rel="alternate" hreflang="x-default" href="{SITE}/">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{t['title']}">
  <meta property="og:description" content="{html.escape(t['desc'])}">
  <meta property="og:image" content="{SITE}/assets/img/og-image.jpg">
  <meta property="og:url" content="{SITE}{t['path']}">
  <meta name="theme-color" content="#ffffff">
  <link rel="icon" type="image/png" sizes="32x32" href="{img('favicon-32.png')}">
  <link rel="apple-touch-icon" href="{img('apple-touch-icon.png')}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Mulish:wght@400;600;700&display=swap">
  <link rel="stylesheet" href="{pre}assets/css/style.css">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header class="site">
  <div class="wrap">
    <a class="brand" href="#top"><img src="{img('logo.png')}" srcset="{img('logo.png')} 1x, {img('logo@2x.png')} 2x" alt="l'Heritage, smaakt naar meer" width="86" height="78"></a>
    <div class="header-right">
      <nav class="main" aria-label="{t['menu']}">
      {nav}<a class="btn" href="#boeken">{t['navbook']}</a>
      </nav>
      <nav class="lang" aria-label="{t['langlabel']}">{langs}</nav>
    </div>
  </div>
</header>

<main id="top">
  <div class="hero">
    <div class="hero-photo" data-slideshow>
      {slides}<div class="slide-dots" role="group" aria-label="{t['slidenav']}">{dots}</div>
    </div>
    <div class="wrap">
      <div class="hero-card">
        <span class="eyebrow">{t['eyebrow']}</span>
        <h1>{t['h1']}</h1>
        <p class="lead">{t['lead']}</p>
        <div class="actions">
          <a class="btn" href="{CUBILIS}" {ext}>{t['cta1']}</a>
          <a class="btn ghost" href="#verblijf">{t['cta2']}</a>
        </div>
        <p class="price-note">{t['pricenote']}</p>
      </div>
      <div class="horizon">{HEART}</div>
    </div>
  </div>

  <section id="verblijf">
    <div class="wrap split">
      <div class="stack">
        <span class="eyebrow">{t['stay_eyebrow']}</span>
        <h2>{t['stay_h']}</h2>
        <figure class="photo"><img src="{img('ontbijt.jpg')}" alt="{t['breakfastalt']}" width="1200" height="800" loading="lazy"></figure>
      </div>
      <div class="stack">
        <div class="prose">
          {stay_p}</div>
        <ul class="expect">
          {expect}</ul>
      </div>
    </div>
  </section>

  <section id="kamers">
    <div class="wrap">
      <div class="split rooms-intro">
      <div class="stack">
        <span class="eyebrow">{t['rooms_eyebrow']}</span>
        <h2>{t['rooms_h']}</h2>
        {rooms_p}</div>
      <figure class="photo wide"><img src="{img('gang.jpg')}" alt="{t['gangalt']}" width="1400" height="933" loading="lazy"></figure>
      </div>
      <div class="rooms">
        {rooms}</div>
      <div class="prices" aria-label="{t['prices_label']}">
        <div><span class="eyebrow">{t['p1']}</span><span class="amount">€80</span><small>{t['pernight']}</small></div>
        <div><span class="eyebrow">{t['p2']}</span><span class="amount">€115</span><small>{t['pernight']}</small></div>
      </div>
    </div>
  </section>

  <section id="tearoom" class="tearoom">
    <div class="wrap split">
      <div class="stack">
        <span class="eyebrow">{t['tea_eyebrow']}</span>
        <h2>{t['tea_h']}</h2>
        <figure class="photo"><img src="{img('tearoom.jpg')}" alt="{t['tealt']}" width="1200" height="801" loading="lazy"></figure>
      </div>
      <div class="stack">
        <div class="prose">
          <p>{t['tea_p']}</p>
        </div>
        <dl class="hours">
          {hours}</dl>
        <p class="hours-note">{t['holiday']}</p>
      </div>
    </div>
  </section>

  <section id="streek">
    <div class="wrap">
      <div class="stack">
        <span class="eyebrow">{t['area_eyebrow']}</span>
        <h2>{t['area_h']}</h2>
        <p class="lead">{t['area_lead']}</p>
      </div>
      <div class="places">
        {places}</div>
    </div>
  </section>

  <section id="boeken" class="book">
    <div class="wrap book-grid">
      <div class="stack">
        <span class="eyebrow" style="color:inherit;opacity:.8">{t['book_eyebrow']}</span>
        <h2>{t['book_h']}</h2>
        <p class="lead">{t['book_lead']}</p>
        <div class="actions">
          <a class="btn" href="{CUBILIS}" {ext}>{t['book_btn']}</a>
          <a class="btn ghost" href="tel:+32497421694">{t['call']}</a>
          <a class="btn ghost" href="{MAPS}" {ext}>{t['route']}</a>
        </div>
      </div>
      <div class="contact" id="contact">
        <dl>
          <dt>{ct[0]}</dt><dd>Dorpplaats 15, 8647 Reninge</dd>
          <dt>{ct[1]}</dt><dd><a href="tel:+32497421694">0497 42 16 94</a></dd>
          <dt>{ct[2]}</dt><dd><a href="mailto:info@lheritage.be">info@lheritage.be</a></dd>
          <dt>{ct[3]}</dt><dd>8:00 – 10:00</dd>
          <dt>{ct[4]}</dt><dd>{t['teatime']}</dd>
        </dl>
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <div class="stack" style="gap:6px">
      <img src="{img('logo.png')}" alt="l'Heritage" width="120" height="108" style="width:120px;height:auto" loading="lazy">
      <span>{t['foot']}</span>
    </div>
    <div class="goeste">
      <span>{t['goeste1']}</span>
      <span>{t['goeste2']}</span>
    </div>
  </div>
</footer>
<script src="{pre}assets/js/slideshow.js" defer></script>
</body>
</html>
'''


for lang, t in T.items():
    out = os.path.join(ROOT, t['path'].strip('/'), 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(page(lang))
    print('wrote', out)
