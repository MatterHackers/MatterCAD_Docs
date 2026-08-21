---
title: Radiale knijp
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: 95ef5847767e5cfcdbae9df9aaa1cb1727da2f5e
source_lang: en
---
# Radiale knijp

Radiale knijp comprimeert een object naar binnen vanuit een middelpunt met een aanpasbare profielcurve. In tegenstelling tot de gewone [Knijpen](pinch.md), die van achter naar voren werkt, comprimeert Radiale knijp symmetrisch rond een middelas.

<!--  Before and after showing an object with radial pinch applied, creating a waisted shape -->
![20260506 155741 paste 20260506 155741](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155741-paste-20260506-155741.jpg)

## Gebruik

1. Selecteer een object
2. Pas de bewerking **Radiale knijp** toe via het menu Hervormen
3. Bewerk het padprofiel om te bepalen hoeveel knijping op elke hoogte wordt toegepast
4. Pas het aantal segmenten aan voor een vloeiender resultaat

## Parameters

- **Pad** - Een profielcurve-editor die de mate van knijping op elk hoogteniveau bepaalt. Bewerk de curve om aangepaste knijpprofielen te maken
- **Segmenten** - Aantal horizontale doorsneden voor een vloeiende knijping, gelijkmatig verdeeld over de hoogte van het onderdeel. Meer segmenten = vloeiender resultaat

### Geavanceerde parameters

- **Knijptype** - Richting van de compressie:
  - **Radiaal** - Comprimeer vanuit alle zijden gelijkmatig naar het midden
  - **X-as** - Comprimeer alleen langs de X-as
  - **Y-as** - Comprimeer alleen langs de Y-as
- **Rotatie-offset** - Verschuif het midden van het knijpeffect

## Tips

- Gebruik de padeditor om zandloper-, fles- of vaasachtige vormen te maken
- Radiale knijp is ideaal om organische, ronde vormen te maken van cilindrische objecten
- Verhoog Segmenten voor vloeiendere curves, vooral bij strakke knijpprofielen

## Gerelateerd

- [Knijpen](pinch.md) - Eenvoudige compressie van achter naar voren
- [Draaien](twist.md) - Spiraalvormige rotatie over de hoogte
- [Kromming](curve.md) - Buigen tot een boog
