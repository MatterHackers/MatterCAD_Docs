---
title: Tilpasset sti
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
source_hash: 3633c708477de3ac77d3547b730c33f7e4431cf6
source_lang: en
---
# Tilpasset sti

Tegn din egen 2D-sti med kontrolpunkter. Det giver dig fuldstændig frihed til at oprette enhver 2D-form, som derefter kan ekstruderes eller roteres til et 3D-objekt.

<!-- Screenshot showing a custom path being edited with control points -->
![20260506 080247 paste 20260506 080247](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080247-paste-20260506-080247.jpg)


## Sådan bruges den

1. Tilføj en **Tilpasset sti** fra biblioteket med 2D-stier
2. Rediger kontrolpunkterne for at definere din form
3. Anvend [Lineær ekstrudering](../operations/path/linear-extrude.md) eller andre sti-handlinger for at oprette et 3D-objekt

## Åbne og lukkede stier

Afkrydsningsfeltet **Lukket** styrer, om stien forbinder sit sidste punkt tilbage til sit første.

- **Lukket** (standard) får stien til at afgrænse et område. Det er dette, [Lineær ekstrudering](../operations/path/linear-extrude.md) og [Roter profil](../operations/path/revolve.md) fylder ud.
- **Åbn** gør stien til en linje. En linje omslutter ingenting, så den vises i scenen som et tyndt bånd langs sin længde i stedet for som en udfyldt form. Brug [Udvid sti](../operations/path/inflate-path.md) til at give den en bredde og gøre den solid igen.

To ting, du bør vide, før du fjerner markeringen i **Lukket**:

- **At lukke igen er ikke det samme som at fortryde.** Når du åbner en sti, kasseres dens lukkende segment. Hvis det segment var en kurve, giver en ny markering af **Lukket** en lige linje tilbage, ikke kurven. Brug i stedet Ctrl+Z – fortryd gendanner den oprindelige sti nøjagtigt.
- **Nogle konturer nægter at åbne.** En kontur, der ville stå tilbage med færre end to punkter – en dråbeform tegnet som et enkelt punkt og en kurve, der løber tilbage til det – forbliver lukket i stedet for at kollapse til noget, du hverken kunne se eller klikke på. Det samme gælder en kontur med en kvadratisk kurve, som en importeret SVG kan indeholde: at åbne den ville flade kurven ud til et hjørne. Afvisningen gælder pr. kontur, så resten af stien åbnes stadig.

Hvis en sti har flere konturer, og de ikke stemmer overens, vises afkrydsningsfeltet som åbent. Når du markerer det, bringes alle konturer på linje.

Handlinger, der kræver et område, lukker en åben sti for dig i stedet for at afvise den. Lineær ekstrudering, Roter profil, Træk fra og de øvrige booleske handlinger gør alle dette, så en åben sti ekstruderes til det samme faste emne, som dens lukkede version ville give.

## Tips

- Brug Tilpasset sti, når ingen af de indbyggede stiformer passer til det, du har brug for
- Hvis du vil importere former fra eksterne vektorprogrammer, se [SVG-objekt](../primitives/svg-object.md)
- Hvis du vil tegne en linje og gøre den til en del, skal du fjerne markeringen i **Lukket**, anvende [Udvid sti](../operations/path/inflate-path.md) for at give den en tykkelse og derefter [Lineær ekstrudering](../operations/path/linear-extrude.md) for at give den højde

## Relateret

- [Cirkelsti](circle-path.md) – En færdiglavet cirkel
- [Kassesti](box-path.md) – Et færdiglavet rektangel
- [SVG-objekt](../primitives/svg-object.md) – Importer vektorstier fra SVG-filer
- [Lineær ekstrudering](../operations/path/linear-extrude.md) – Giv stier højde
