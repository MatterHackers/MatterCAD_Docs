---
title: Krommen
articleKey: CurveObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 6adde5da3bb469384f59eb5e9dfe5cb642b3eec5
source_lang: en
---
# Krommen

Krommen buigt een recht object tot een boog of cirkelvormige vorm. Je bepaalt de buiging door een hoek of een diameter op te geven waaromheen het object wordt gewikkeld.

<!--  Before and after showing a straight bar being curved into an arc -->
![20260506 155243 paste 20260506 155243](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155243-paste-20260506-155243.jpg)

## Gebruik

1. Selecteer een object
2. Pas de bewerking **Krommen** toe via het menu Hervormen
3. Kies tussen het buigtype Hoek of Diameter
4. Pas de parameters aan tot je de gewenste kromming krijgt

## Parameters

- **Buigtype** - Kies tussen:
  - **Hoek** - Geef de buighoek rechtstreeks op (1-360 graden)
  - **Diameter** - Geef de diameter op van de cirkel waaromheen het onderdeel wordt gewikkeld
- **Buigrichting** - Omhoog buigen of Omlaag buigen
- **Startpercentage** - Waar langs het object de buiging begint (0-100%)
- **Mesh splitsen** - Splits de mesh voor vloeiende krommingen (standaard: aan)
- **Min. zijden per rotatie** - Minimaal aantal meshsegmenten per volledige omwenteling. Hogere waarden = vloeiendere krommingen

### Geavanceerde parameters

- **Startbuigpercentage** - Percentage vanaf links waar de buiging begint
- **Eindbuigpercentage** - Percentage vanaf links waar de buiging eindigt

## Tips

- Gebruik Krommen om bogen, ringen en gebogen beugels te maken van rechte basisvormen
- Met een hoek van 360 wordt het object tot een volledige ring gewikkeld
- Verhoog Min. zijden per rotatie voor vloeiendere resultaten bij scherpe buigingen
- Het object wordt over zijn lengte (X-as) gebogen

## Gerelateerd

- [Draaien](twist.md) - Roteren over de hoogte in plaats van buigen
- [Torus](../../primitives/torus.md) - Een kant-en-klare ringvorm
