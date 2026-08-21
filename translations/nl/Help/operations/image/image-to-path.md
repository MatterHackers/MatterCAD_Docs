---
title: Afbeelding naar pad
articleKey: ImageToPathObject3D_2
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 0145587f635ede68bfc1df37b4f0d366a03d3a6c
source_lang: en
---
# Afbeelding naar pad

Afbeelding naar pad traceert de omtrekken van een afbeelding om 2D-paden te maken. Deze paden kunnen vervolgens worden geëxtrudeerd, gewenteld of gebruikt met elke andere padbewerking. Dit is ideaal om logo's, silhouetten en eenvoudige afbeeldingen om te zetten in 3D-objecten.

![20260324 075521 paste 20260324 075521](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-075521-paste-20260324-075521.jpg)


## Gebruik

1. Selecteer een afbeeldingsobject in je werkruimte
2. Pas **Afbeelding naar pad** toe vanuit het menu met Afbeelding-bewerkingen
3. Kies het analysetype en pas het geselecteerde bereik aan

## Parameters

- **Analysetype** - Hoe de afbeelding voor het traceren wordt geanalyseerd:
  - **Transparantie** - Traceren op basis van transparante versus ondoorzichtige gebieden (het beste voor PNG's met een transparante achtergrond)
  - **Kleuren** - Traceren op basis van kleurgebieden
  - **Intensiteit** - Traceren op basis van helderheidsniveaus (het beste voor de meeste afbeeldingen)
- **Bereik selecteren** - Een histogramregelaar om te selecteren welke helderheids-/kleurwaarden in de tracering worden meegenomen
- **Min. oppervlak** - Minimale oppervlakte waarbij een padlus wordt meegenomen. Verhoog deze waarde om kleine ruisartefacten uit te filteren

## Tips

- Schone, contrastrijke afbeeldingen met eenvoudige vormen werken het beste
- Gebruik de modus Transparantie voor PNG-afbeeldingen met een transparante achtergrond
- Gebruik de modus Intensiteit voor foto's en afbeeldingen zonder transparantie
- Pas na het traceren [Lineaire extrusie](../path/linear-extrude.md) toe om het pad hoogte te geven
- Verhoog Min. oppervlak om kleine ongewenste details uit de tracering te verwijderen

## Gerelateerd

- [Afbeeldingsconverter](image-converter.md) - Maak een reliëf op basis van een hoogtekaart in plaats van vlakke paden
- [Lithofaan](lithophane.md) - Maak achtergrondverlichte afbeeldingen
- [SVG-object](../../primitives/svg-object.md) - Importeer vectorafbeeldingen rechtstreeks (traceren niet nodig)
- [Lineaire extrusie](../path/linear-extrude.md) - Geef het getraceerde pad hoogte
