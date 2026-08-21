---
title: Doorsnijden
articleKey: IntersectionObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b997cfc4f6d2f02559346365311f217388a6a2da
source_lang: en
---
# Doorsnijden

Doorsnijden behoudt alleen het volume dat alle objecten gemeenschappelijk hebben en verwijdert de rest.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->
![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)

[Combineren](combine.md), [Aftrekken](subtract.md), Doorsnijden en [Aftrekken en vervangen](subtract-and-replace.md) worden allemaal uitgevoerd door één Booleaans object -- de werkbalkknop maakt het aan met Doorsnijden al geselecteerd, en je kunt op elk moment overschakelen naar een van de andere drie via de pictogramrij **Bewerking** boven aan het paneel Eigenschappen.

Doorsnijden werkt op solids en op 2D-paden. Het kijkt naar wat je aanlevert en voert het juiste soort bewerking uit: twee paden doorsnijden levert één pad op en twee meshes doorsnijden levert één solid op.

## Gebruik

1. Selecteer twee of meer objecten
2. Klik op **Doorsnijden** in de werkbalk
3. Bedenk je op elk moment door op een ander pictogram in de rij **Bewerking** boven aan het paneel Eigenschappen te klikken -- de vorm wordt opnieuw opgebouwd met de nieuwe bewerking

## Parameters

- **Bewerking** - Welke booleaanse bewerking wordt uitgevoerd. Weergegeven als een pictogramrij boven aan het paneel
- **Binnenstebuiten geometrie behouden** - Behandel een binnenstebuiten gekeerde schil als massief materiaal in plaats van het omringende volume te laten wegvallen. Schakel dit in wanneer een model dat massief zou moeten zijn met ontbrekende delen terugkomt. Dit forceert de tragere, exacte booleaanse engine
- **Wikkelrichting repareren** - Draai de binnenstebuiten gekeerde schillen van elk onderdeel om voordat de booleaanse bewerking wordt uitgevoerd. Dit repareert de geometrie eenmalig in plaats van te wijzigen wat elke latere bewerking als massief beschouwt, en is meestal de betere van de twee oplossingen voor een binnenstebuiten model

## Tips

- De objecten moeten elkaar overlappen. Als ze elkaar niet daadwerkelijk overlappen, is het resultaat leeg
- Bij meer dan twee objecten wordt de lijst afgewerkt: de eerste twee worden doorsneden, dat resultaat wordt vervolgens doorsneden met het derde, enzovoort
- Als een resultaat er verkeerd uitziet, controleer dan of de bronobjecten waterdicht zijn. **Wikkelrichting repareren** verhelpt binnenstebuiten gekeerde schillen; [Repareren](../mesh/repair.md) verhelpt bredere schade in geïmporteerde modellen

## Gerelateerd

- [Combineren](combine.md) - Meerdere objecten samenvoegen tot één massieve vorm
- [Aftrekken](subtract.md) - De ene vorm uit de andere snijden
- [Aftrekken en vervangen](subtract-and-replace.md) - Eén vorm aftrekken en het weggesneden deel behouden
- [Vlaksnede](../reshape/plane-cut.md) - Snijden met een plat vlak in plaats van met een andere vorm
- [Repareren](../mesh/repair.md) - Beschadigde geïmporteerde meshes herstellen vóór een booleaanse bewerking

Deze pagina behandelt ook de oudere Doorsnede-objecten die nog voorkomen in ontwerpen die zijn opgeslagen voordat de bewerkingen werden samengevoegd. Ze blijven precies zo werken als voorheen; nieuwe ontwerpen gebruiken het gedeelde Booleaanse object met de bewerking Doorsnijden geselecteerd.
