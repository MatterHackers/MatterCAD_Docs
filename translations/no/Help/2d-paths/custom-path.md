---
title: Egendefinert bane
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
source_hash: 3633c708477de3ac77d3547b730c33f7e4431cf6
source_lang: en
---
# Egendefinert bane

Tegn din egen 2D-bane med kontrollpunkter. Dette gir deg full frihet til å lage en hvilken som helst 2D-form som deretter kan ekstruderes eller roteres til et 3D-objekt.

<!-- Screenshot showing a custom path being edited with control points -->
![20260506 080247 paste 20260506 080247](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080247-paste-20260506-080247.jpg)


## Slik bruker du den

1. Legg til en **Egendefinert bane** fra 2D-banebiblioteket
2. Rediger kontrollpunktene for å definere formen
3. Bruk [Lineær ekstrudering](../operations/path/linear-extrude.md) eller andre baneoperasjoner for å lage et 3D-objekt

## Åpne og lukkede baner

Avmerkingsboksen **Lukket** styrer om banen kobler det siste punktet tilbake til det første.

- **Lukket** (standard) gjør at banen omslutter et område. Det er dette [Lineær ekstrudering](../operations/path/linear-extrude.md) og [Roter rundt akse](../operations/path/revolve.md) fyller.
- **Åpne** gjør banen til en linje. En linje omslutter ingenting, så den vises i scenen som et tynt bånd langs lengden i stedet for som en fylt form. Bruk [Utvid bane](../operations/path/inflate-path.md) for å gi den bredde og gjøre den om til noe solid igjen.

To ting du bør vite før du fjerner avmerkingen for **Lukket**:

- **Å lukke på nytt er ikke det samme som å angre.** Når du åpner en bane, forkastes lukkesegmentet. Hvis det segmentet var buet, gir en ny avmerking av **Lukket** deg en rett linje tilbake, ikke kurven. Bruk Ctrl+Z i stedet – angring gjenoppretter den opprinnelige banen nøyaktig.
- **Noen konturer lar seg ikke åpne.** En kontur som ville stått igjen med færre enn to punkter – en dråpeform tegnet som ett enkelt punkt og en kurve som løper tilbake til det – forblir lukket i stedet for å kollapse til noe du ikke lenger kunne se eller klikke på. Det samme gjelder en kontur med en kvadratisk kurve, som en importert SVG kan inneholde: å åpne den ville flate ut kurven til et hjørne. Nektelsen gjelder per kontur, så resten av banen åpnes likevel.

Hvis en bane har flere konturer som ikke stemmer overens, vises avmerkingsboksen som åpen. Å merke av for den bringer alle konturene i samsvar.

Operasjoner som trenger et område, lukker en åpen bane for deg i stedet for å avvise den. Lineær ekstrudering, Roter rundt akse, Trekk fra og de andre boolske operasjonene gjør alle dette, så en åpen bane ekstruderes til samme solide objekt som den lukkede versjonen ville gitt.

## Tips

- Bruk Egendefinert bane når ingen av de innebygde baneformene passer til det du trenger
- For å importere former fra eksterne vektorprogrammer, se [SVG-objekt](../primitives/svg-object.md)
- For å tegne en linje og gjøre den om til en del: fjern avmerkingen for **Lukket**, bruk [Utvid bane](../operations/path/inflate-path.md) for å gi den tykkelse, og deretter [Lineær ekstrudering](../operations/path/linear-extrude.md) for å gi den høyde

## Relatert

- [Sirkelbane](circle-path.md) – En ferdig sirkel
- [Boksbane](box-path.md) – Et ferdig rektangel
- [SVG-objekt](../primitives/svg-object.md) – Importer vektorbaner fra SVG-filer
- [Lineær ekstrudering](../operations/path/linear-extrude.md) – Gi baner høyde
