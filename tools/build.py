#!/usr/bin/env python3
"""Genereert index.html, fr/index.html en en/index.html voor l'Heritage."""
import json, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.lheritage.be'
CUBILIS = 'https://reservations.cubilis.eu/b-and-b-lheritage-reninge'
GOESTE = 'https://goestepoperinge.be'
WALK_LINK = 'https://www.toerismewesthoek.be/en/hiking/walking-network'
BIKE_LINK = 'https://www.toerismewesthoek.be/nl/fietsen/routeplanner'
BIKE_ROUTE = 'https://www.lo-reninge.be/ijzerbroekenfietsroute'
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
    pricenote='Vanaf <strong>€80</strong> per nacht voor 1 persoon en <strong>€110</strong> voor 2 personen, ontbijt inbegrepen',
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
    rooms_p=['Elke kamer draagt de naam van haar kleur. Elke kamer heeft een eigen badkamertje met douche, toilet en lavabo. Het ontbijt is altijd inbegrepen; de prijs hangt af van het aantal personen en het aantal nachten.',
             'Binnen vind je hoge plafonds, oude deuren, een kroonluchter hier en daar en behang met karakter. Een huis met een verleden, waar je meteen thuiskomt.'],
    gangalt="Een jonge gast met een oude koffer in de gang van l'Heritage",
    floor=['1e verdieping', '2e verdieping'], roomword='Kamer',
    rooms=['Uitzicht op de kerktoren, twee eenpersoonsbedden.', 'Op het oosten, met de zonsopgang boven de IJzervlakte.',
           'Aan de achterkant van het huis, de rustigste plek.', 'Knus, met dakkapel en zicht over de IJzerbroeken.', 'Een stille kamer onder het dak.'],
    prices_label='Prijzen', p1='1 persoon', p2='2 personen', pernight='per nacht bij 2 nachten of meer', onenight='Eén nacht', pricenote2='Het ontbijt is altijd inbegrepen. Blijf je maar één nacht, dan komt er €5 (1 persoon) of €10 (2 personen) bij.',
    tea_eyebrow='Tearoom', tea_h='Koffie en pannenkoeken in de tearoom',
    tea_p='Ook wie niet blijft slapen is welkom. Op het zonnige terras of bij de open haard bakken we verse pannenkoeken volgens het familierecept, en schenken we koffie voor fietsers en wandelaars die even willen uitblazen.',
    tealt='De tearoom met stenen bar, kroonluchter en hoge ramen', seasons=[('Zomer', 'van Pasen tot ons verlof eind september', 'woensdag tot zaterdag'), ('Winter', 'van begin oktober tot Pasen', 'vrijdag en zaterdag')],
    holiday='Een tussentijds verlof wordt steeds op voorhand aangekondigd in de zaak.',
    area_eyebrow='De streek', area_h='Wat je vanuit Reninge kunt ontdekken',
    out_eyebrow='Wandelen en fietsen', out_h='Vanuit Reninge de polder in',
    out_lead='Officiële routes van Westtoer en Toerisme Westhoek, rond Reninge, langs de IJzer en door de natte weilanden van de IJzerbroeken.',
    walk_h='Wandelen', bike_h='Fietsen', see_h='Onderweg te zien',
    walks=[('± 10 km', 'Blankaartwandelroute', 'Vertrekt aan het bezoekerscentrum De Blankaart in Woumen. Onderweg zeven vogelkijkpunten en kijktorens over de natte weilanden.'),
           ('± 6,5 km', 'Drie Grachten', 'Een lus naar de plek waar drie waterlopen samenkomen, een belangrijke plek in de Eerste Wereldoorlog.'),
           ('± 8 km', 'Beverdijk', 'Een lus van het wandelnetwerk IJzervallei over de oude dijk langs de IJzer.'),
           ('± 110 km', 'Wandelnetwerk De Blankaart', 'Het wandelnetwerk van Westtoer rond De Blankaart en de IJzerbroeken. Met de knooppunten maak je zelf een wandeling op maat.')],
    bikes=[('49,7 km', 'IJzerbroekenfietsroute', 'Bewegwijzerde lus langs de IJzer, door Reninge, Lo, Fintele, Stavele en Alveringem. Volg de zeshoekige bordjes.'),
           ('Op maat', 'Fietsnetwerk Westhoek', 'Het fietsknooppuntennetwerk loopt door het dorp. Met de routeplanner van Toerisme Westhoek stippel je zelf een tocht uit.'),
           ('Kaart', 'Fietskaart Westhoek', 'De fietsnetwerkkaart koop je bij de Dienst Toerisme in Lo, Markt 11.')],
    sights=[('Lo, ± 5 km', 'Stadhuis met belfort', 'Uit 1565–1566, beschermd als UNESCO-werelderfgoed.'),
            ('Lo', 'Caesarsboom en stadsmuur', 'Een eeuwenoude taxus achter de middeleeuwse stadsmuur.'),
            ('Lo, sinds 2026', 'Uitkijkplatform Sint-Pieterskerk', '163 treden naar 31 meter hoogte, met uitzicht over de hele polder.'),
            ('Reninge', 'Sint-Rictrudiskerk', 'De dorpskerk, pal naast l\'Heritage.')],
    more_walk='Wandelnetwerken van Toerisme Westhoek', more_bike='Routeplanner van Toerisme Westhoek',
    out_note='Afstanden zijn bij benadering. Vraag ons gerust om tips als je aankomt.',
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
    pricenote='À partir de <strong>80 €</strong> la nuit pour 1 personne et <strong>110 €</strong> pour 2 personnes, petit-déjeuner compris',
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
    rooms_p=['Chaque chambre porte le nom de sa couleur. Chacune a sa propre petite salle de bain avec douche, toilettes et lavabo. Le petit-déjeuner est toujours compris ; le prix dépend du nombre de personnes et de nuits.',
             "À l'intérieur : hauts plafonds, portes anciennes, un lustre ici et là et des papiers peints pleins de caractère. Une maison chargée d'histoire où l'on se sent tout de suite chez soi."],
    gangalt="Un jeune hôte avec une vieille valise dans le couloir de l'Heritage",
    floor=['1er étage', '2e étage'], roomword='Chambre',
    rooms=["Vue sur le clocher, deux lits simples.", "Orientée à l'est, avec le lever du soleil sur la plaine de l'Yser.",
           "À l'arrière de la maison, la plus calme.", "Douillette, avec lucarne et vue sur les prairies de l'Yser.", 'Une chambre paisible sous le toit.'],
    prices_label='Tarifs', p1='1 personne', p2='2 personnes', pernight='par nuit à partir de 2 nuits', onenight='Une seule nuit', pricenote2="Le petit-déjeuner est toujours compris. Pour une seule nuit, comptez 5 € (1 personne) ou 10 € (2 personnes) de plus.",
    tea_eyebrow='Salon de thé', tea_h='Café et crêpes au salon de thé',
    tea_p="Même sans y dormir, vous êtes le bienvenu. Sur la terrasse ensoleillée ou au coin du feu, nous préparons des crêpes selon la recette de famille et servons un café aux cyclistes et promeneurs qui veulent souffler un moment.",
    tealt='Le salon de thé avec son bar en pierre, son lustre et ses hautes fenêtres', seasons=[('Été', "de Pâques jusqu'à nos congés fin septembre", 'du mercredi au samedi'), ('Hiver', 'de début octobre à Pâques', 'vendredi et samedi')],
    holiday="Une fermeture pour congés en cours de saison est toujours annoncée à l'avance au salon de thé.",
    area_eyebrow='La région', area_h='À découvrir depuis Reninge',
    out_eyebrow='Randonnées à pied et à vélo', out_h='Depuis Reninge, en pleine nature',
    out_lead="Des itinéraires officiels de Westtoer et Toerisme Westhoek, autour de Reninge, le long de l'Yser et à travers les prairies humides.",
    walk_h='À pied', bike_h='À vélo', see_h='À voir en chemin',
    walks=[('± 10 km', 'Promenade de la Blankaart', "Départ au centre d'accueil De Blankaart à Woumen. En chemin, sept observatoires et tours d'observation sur les prairies humides."),
           ('± 6,5 km', 'Drie Grachten', "Une boucle jusqu'au confluent de trois cours d'eau, un lieu marquant de la Première Guerre mondiale."),
           ('± 8 km', 'Beverdijk', "Une boucle du réseau de promenade de la vallée de l'Yser, sur l'ancienne digue."),
           ('± 110 km', 'Réseau de promenade De Blankaart', "Le réseau de Westtoer autour de la Blankaart et des prairies de l'Yser. Avec les points-nœuds, composez votre propre promenade.")],
    bikes=[('49,7 km', 'Itinéraire des prairies de l\'Yser', "Boucle balisée le long de l'Yser, par Reninge, Lo, Fintele, Stavele et Alveringem. Suivez les panneaux hexagonaux."),
           ('Sur mesure', 'Réseau cyclable du Westhoek', 'Le réseau à points-nœuds passe par le village. Planifiez votre balade avec le planificateur de Toerisme Westhoek.'),
           ('Carte', 'Carte vélo du Westhoek', "La carte du réseau est en vente à l'office du tourisme de Lo, Markt 11.")],
    sights=[('Lo, ± 5 km', 'Hôtel de ville et beffroi', 'Datant de 1565–1566, inscrit au patrimoine mondial de l\'UNESCO.'),
            ('Lo', 'Arbre de César et remparts', 'Un if plusieurs fois centenaire derrière les remparts médiévaux.'),
            ('Lo, depuis 2026', "Belvédère de l'église Saint-Pierre", '163 marches jusqu\'à 31 mètres, avec vue sur tout le polder.'),
            ('Reninge', 'Église Sainte-Rictrude', "L'église du village, juste à côté de l'Heritage.")],
    more_walk='Réseaux de promenade de Toerisme Westhoek', more_bike='Planificateur de Toerisme Westhoek',
    out_note="Les distances sont approximatives. N'hésitez pas à nous demander conseil à votre arrivée.",
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
    pricenote='From <strong>€80</strong> a night for 1 person and <strong>€110</strong> for 2 people, breakfast included',
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
    rooms_p=['Each room is named after its colour. Each has its own small bathroom with shower, toilet and washbasin. Breakfast is always included; the price depends on the number of guests and nights.',
             'Inside you will find high ceilings, old doors, the odd chandelier and wallpaper with character. A house with a past, where you feel at home straight away.'],
    gangalt="A young guest with an old suitcase in the hallway of l'Heritage",
    floor=['1st floor', '2nd floor'], roomword='Room',
    rooms=['View of the church tower, two single beds.', 'Facing east, with sunrise over the Yser plain.',
           'At the back of the house, the quietest spot.', 'Cosy, with a dormer window overlooking the Yser meadows.', 'A peaceful room under the roof.'],
    prices_label='Prices', p1='1 person', p2='2 people', pernight='per night for stays of 2 nights or more', onenight='One night', pricenote2='Breakfast is always included. For a one-night stay we add €5 (1 person) or €10 (2 people).',
    tea_eyebrow='Tearoom', tea_h='Coffee and pancakes in the tearoom',
    tea_p="You are welcome even if you are not staying the night. On the sunny terrace or by the fireplace we bake fresh pancakes from the family recipe and pour coffee for cyclists and walkers taking a break.",
    tealt='The tearoom with its stone bar, chandelier and tall windows', seasons=[('Summer', 'from Easter until our holiday at the end of September', 'Wednesday to Saturday'), ('Winter', 'from early October until Easter', 'Friday and Saturday')],
    holiday='Any closure for holidays during the season is always announced in advance at the tearoom.',
    area_eyebrow='The area', area_h='What to discover from Reninge',
    out_eyebrow='Walking and cycling', out_h='Straight from Reninge into the countryside',
    out_lead='Official routes from Westtoer and Toerisme Westhoek, around Reninge, along the Yser and through the wet meadows of the Yser floodplain.',
    walk_h='Walking', bike_h='Cycling', see_h='Worth a stop',
    walks=[('± 10 km', 'Blankaart walk', 'Starts at the De Blankaart visitor centre in Woumen. Along the way, seven birdwatching points and towers over the wet meadows.'),
           ('± 6.5 km', 'Drie Grachten', 'A loop to the point where three waterways meet, a key spot in the First World War.'),
           ('± 8 km', 'Beverdijk', 'A loop of the Yser valley walking network along the old Yser dyke.'),
           ('± 110 km', 'De Blankaart walking network', 'Westtoer\'s walking network around De Blankaart and the Yser meadows. Use the junctions to plan your own walk.')],
    bikes=[('49.7 km', 'IJzerbroeken cycle route', 'A signposted loop along the Yser, through Reninge, Lo, Fintele, Stavele and Alveringem. Follow the hexagonal signs.'),
           ('Your choice', 'Westhoek cycle network', 'The cycle node network runs through the village. Plan your own ride with the Toerisme Westhoek route planner.'),
           ('Map', 'Westhoek cycle map', 'Buy the network map at the tourist office in Lo, Markt 11.')],
    sights=[('Lo, ± 5 km', 'Town hall and belfry', 'Built in 1565–1566, a UNESCO World Heritage site.'),
            ('Lo', "Caesar's Tree and town wall", 'A centuries-old yew behind the medieval town wall.'),
            ('Lo, since 2026', 'Sint-Pieterskerk lookout', '163 steps up to 31 metres, with views over the whole polder.'),
            ('Reninge', 'Sint-Rictrudis church', "The village church, right next to l'Heritage.")],
    more_walk='Toerisme Westhoek walking networks', more_bike='Toerisme Westhoek route planner',
    out_note='Distances are approximate. Feel free to ask us for tips when you arrive.',
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
        "priceRange": "€80 – €120",
        "address": {"@type": "PostalAddress", "streetAddress": "Dorpplaats 15", "postalCode": "8647", "addressLocality": "Reninge", "addressCountry": "BE"},
        "numberOfRooms": 5,
    }
    nav = ''.join(f'<a href="#{i}">{n}</a>\n      ' for i, n in zip(IDS, t['nav']))
    expect = ''.join(f'<li><b>{a}</b><span>{b}</span></li>\n          ' for a, b in t['expect'])
    rooms = ''
    for (c, name, f, fl), d in zip(ROOMS, t['rooms']):
        rooms += f'''<article class="room"><div class="chip" style="--c:var(--{c})"><img src="{img(f + '.jpg')}" alt="{t['roomword']} {name}" width="900" height="600" loading="lazy"><span>{t['floor'][fl - 1]}</span></div><div class="txt"><h3>{name}</h3><p>{d}</p></div></article>
        '''
    route = lambda items: ''.join(f'<li><span class="dist">{a}</span><h4>{b}</h4><p>{c}</p></li>\n            ' for a, b, c in items)
    walks, bikes, sights = route(t['walks']), route(t['bikes']), route(t['sights'])
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
        <div><span class="eyebrow">{t['p1']}</span><span class="amount">€80</span><small>{t['pernight']}</small><span class="one-night">{t['onenight']}: <strong>€85</strong></span></div>
        <div><span class="eyebrow">{t['p2']}</span><span class="amount">€110</span><small>{t['pernight']}</small><span class="one-night">{t['onenight']}: <strong>€120</strong></span></div>
      </div>
      <p class="price-extra">{t['pricenote2']}</p>
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

  <section id="wandelen" class="outdoors">
    <div class="wrap">
      <div class="stack">
        <span class="eyebrow">{t['out_eyebrow']}</span>
        <h2>{t['out_h']}</h2>
        <p class="lead">{t['out_lead']}</p>
      </div>
      <div class="routes">
        <div class="route-col">
          <h3>{t['walk_h']}</h3>
          <ul>
            {walks}</ul>
          <a class="more" href="{WALK_LINK}" {ext}>{t['more_walk']} →</a>
        </div>
        <div class="route-col">
          <h3>{t['bike_h']}</h3>
          <ul>
            {bikes}</ul>
          <a class="more" href="{BIKE_LINK}" {ext}>{t['more_bike']} →</a>
          <a class="more" href="{BIKE_ROUTE}" {ext}>{t['bikes'][0][1]} →</a>
        </div>
        <div class="route-col">
          <h3>{t['see_h']}</h3>
          <ul>
            {sights}</ul>
        </div>
      </div>
      <p class="route-note">{t['out_note']}</p>
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
