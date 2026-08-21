---
title: Tekst
articleKey: TextObject3D_2
parent: "Primitives"
nav_order: 16
source_hash: 526f3190c7b2150243499b5874ac455d74810bb2
source_lang: en
---
# Tekst

Maak 3D-geëxtrudeerde tekst met aanpasbare inhoud, lettertype, grootte en hoogte. Tekstobjecten zijn ideaal voor labels, borden, naamplaatjes en decoratieve letters.

<!--  Screenshot of a 3D Text object on the workspace showing extruded letters -->
![20260318 184207 paste 20260318 184207](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184207-paste-20260318-184207.jpg)


## Gebruik

1. Voeg een **Tekst**-primitief toe vanuit het paneel Primitieven
2. Typ je tekst in het veld **Naam** in het paneel Eigenschappen
3. Pas het lettertype, de grootte en de extrusiehoogte naar wens aan

## Parameters

- **Naam** - De weer te geven tekstinhoud
- **Puntgrootte** - De lettergrootte. Deze komt nauwkeurig overeen met standaard drukwerkformaten -- een puntgrootte van 12 in MatterCAD komt overeen met 12-punts letters op een 2D-printer
- **Hoogte** - De extrusiehoogte (hoe ver de tekst boven het oppervlak uitsteekt)
- **Lettertype** - Kies uit de beschikbare systeemlettertypen

## Tips

- Gebruik [Aftrekken](../operations/boolean/subtract.md) om tekst in een oppervlak te graveren in plaats van deze te verhogen
- Verhoog bij zeer kleine tekst de Puntgrootte en [Schalen](../operations/transform/scale.md) vervolgens het hele object naar beneden voor meer detail
- Elke letter in de tekst is een apart pad dat samen wordt geëxtrudeerd

## Gerelateerd

- [Braille](braille.md) - Genereer 3D-printbare Braille-tekst
- [QR-code](qr-code.md) - Genereer een QR-code als 3D-object
- [Afbeeldingsobject](image-object.md) - Zet afbeeldingen om naar 3D
