---
title: Schalen
articleKey: ScaleObject3D_3
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b3b5419c3db29550b2544bb6aca91ca3ce6fa715
source_lang: en
---
# Schalen

Schalen wijzigt de grootte van een object met nauwkeurige controle over afmetingen, verhoudingen en eenheidsomrekening. Je kunt uniform schalen, specifieke assen aan elkaar koppelen of elke as onafhankelijk aanpassen.

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## Gebruik

1. Selecteer een object
2. Pas de bewerking **Schalen** toe via het menu Transformeren
3. Kies je schaalmethode en voer de gewenste waarden in

Je kunt objecten ook in de viewport schalen door op de schaalhoekgrepen van een geselecteerd object te klikken en te slepen.

## Parameters

### Schaaltype

Kies een voorinstelling of aangepaste schaling:

- **Aangepast** - Voer je eigen afmetingen of percentages in
- **Inches naar mm** - Vermenigvuldig met 25,4 (imperiaal naar metrisch omrekenen)
- **mm naar inches** - Vermenigvuldig met 0,0393 (metrisch naar imperiaal omrekenen)
- **mm naar cm** - Vermenigvuldig met 0,1
- **cm naar mm** - Vermenigvuldig met 10

### Schaalmethode (modus Aangepast)

- **Direct** - Voer de gewenste Breedte, Diepte en Hoogte in millimeters in
- **Percentage** - Voer Breedte, Diepte en Hoogte in als percentages van de oorspronkelijke grootte

### Verhouding vergrendelen

- **Geen (Vrij schalen)** - Elke as schaalt onafhankelijk
- **X & Y** - Breedte en Diepte zijn aan elkaar gekoppeld; Hoogte schaalt onafhankelijk
- **X, Y & Z** - Alle drie de assen schalen uniform mee

### Afmetingen

- **Breedte** - Grootte langs de X-as
- **Diepte** - Grootte langs de Y-as
- **Hoogte** - Grootte langs de Z-as

## Tips

- Gebruik "Inches naar mm" als je een STL-bestand hebt geïmporteerd dat in inches is ontworpen en te klein wordt weergegeven
- Zet Verhouding vergrendelen op X, Y & Z voor uniform schalen -- het wijzigen van één afmeting werkt ze allemaal bij
- De basispositie van het object blijft tijdens het schalen behouden, zodat het op het werkbladoppervlak blijft staan
- Je kunt exacte waarden typen voor nauwkeurige afmetingen of de schuifregelaars gebruiken voor snelle aanpassingen

## Gerelateerd

- [Verplaatsen](translate.md) - Een object verplaatsen
- [Roteren](rotate.md) - Een object roteren
- [Passend maken aan grenzen](../placement/fit-to-bounds.md) - Schalen zodat het binnen een specifieke grootte past
