---
title: Combineren
articleKey: CombineObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: a3066faa634b5a88a2fe1650a4e2ac278ac50e24
source_lang: en
---
# Combineren

Combineren voegt alles samen tot één solide. Interne vlakken waar de vormen elkaar overlapten worden verwijderd, zodat het resultaat één doorlopende mesh is in plaats van overlappende schillen.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->
![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)

Combineren, [Aftrekken](subtract.md), [Doorsnijden](intersect.md) en [Aftrekken en vervangen](subtract-and-replace.md) worden allemaal uitgevoerd door één Booleaans object -- de werkbalkknop maakt het aan met Combineren al geselecteerd, en je kunt op elk moment overschakelen naar een van de andere drie via de icoonrij **Bewerking** bovenaan het Eigenschappen-paneel.

Combineren werkt op solides en op 2D-paden. Het kijkt naar wat je aanlevert en voert het juiste soort bewerking uit, dus het combineren van twee paden levert één pad op en het combineren van twee meshes levert één solide op.

## Gebruik

1. Selecteer twee of meer objecten
2. Klik op **Combineren** in de werkbalk
3. Verander op elk moment van gedachten door op een ander icoon in de rij **Bewerking** bovenaan het Eigenschappen-paneel te klikken -- de vorm wordt opnieuw opgebouwd met de nieuwe bewerking

## Parameters

- **Bewerking** - Welke booleaanse bewerking wordt uitgevoerd. Weergegeven als een icoonrij bovenaan het paneel
- **Binnenstebuiten geometrie behouden** - Behandel een binnenstebuiten schil als vast materiaal in plaats van het volume eromheen te laten opheffen. Zet dit aan wanneer een model dat solide zou moeten zijn met ontbrekende delen terugkomt. Het forceert de tragere, exacte booleaanse engine
- **Wikkelrichting repareren** - Draai de binnenstebuiten schillen van elk onderdeel terug voordat de booleaanse bewerking wordt uitgevoerd. Dit herstelt de geometrie eenmalig in plaats van te veranderen wat elke latere bewerking als solide beschouwt, en is meestal de beste van de twee oplossingen voor een binnenstebuiten model

## Tips

- Combineren voegt ook niet-overlappende objecten samen tot één mesh, maar ze blijven visueel gescheiden
- Combineren verwerkt Gat-objecten voor je: alles wat als gat is gemarkeerd wordt van het resultaat afgetrokken in plaats van eraan toegevoegd
- Combineren neemt de kleuren per vlak over van de oorspronkelijke objecten
- Als een resultaat er verkeerd uitziet, controleer dan of de bronobjecten waterdicht zijn. **Wikkelrichting repareren** herstelt binnenstebuiten schillen; [Repareren](../mesh/repair.md) herstelt bredere schade in geïmporteerde modellen

## Gerelateerd

- [Aftrekken](subtract.md) - Snijd de ene vorm uit de andere
- [Doorsnijden](intersect.md) - Behoud alleen het volume waar objecten overlappen
- [Aftrekken en vervangen](subtract-and-replace.md) - Trek één vorm af en behoud het weggesneden deel
- [Vlaksnede](../reshape/plane-cut.md) - Snijd met een vlak in plaats van met een andere vorm
- [Gat](../../primitives/hole.md) - Een kubus die vooraf is ingesteld om af te trekken
- [Repareren](../mesh/repair.md) - Herstel beschadigde geïmporteerde meshes vóór een booleaanse bewerking

Deze pagina behandelt ook de oudere Combineren-objecten die nog voorkomen in ontwerpen die zijn opgeslagen voordat de bewerkingen werden samengevoegd. Ze blijven precies zo werken als voorheen; nieuwe ontwerpen gebruiken het gedeelde Booleaanse object met de bewerking Combineren geselecteerd.
