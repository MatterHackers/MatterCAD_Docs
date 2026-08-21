---
title: Aftrekken en vervangen
articleKey: SubtractAndReplaceObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c1698bab75faca8046b23cc148803c8063ba0678
source_lang: en
---
# Aftrekken en vervangen

Aftrekken en vervangen trekt de onderdelen die je kiest af van de onderdelen die je niet koos, maar behoudt het weggesneden stuk als een eigen onderdeel in plaats van het weg te gooien. Gebruik **Af te trekken onderdeel/onderdelen** om de snijvormen te kiezen; al het overige is de basis die gesneden wordt.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->
![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)

[Combineren](combine.md), [Aftrekken](subtract.md), [Doorsnijden](intersect.md) en Aftrekken en vervangen worden alle uitgevoerd door één booleaans object -- de werkbalkknop maakt het aan met Aftrekken en vervangen al geselecteerd, en je kunt op elk moment overschakelen naar een van de andere drie via de pictogrammenrij **Bewerking** boven aan het paneel Eigenschappen.

Aftrekken en vervangen wordt niet aangeboden voor 2D-paden -- een gebied heeft geen verwijderd volume om terug te geven.

## Gebruik

1. Selecteer twee of meer objecten
2. Klik op **Aftrekken en vervangen** in de werkbalk
3. Gebruik **Af te trekken onderdeel/onderdelen** om te kiezen welke onderliggende objecten de snijvormen zijn
4. Bedenk je je op elk moment door op een ander pictogram in de rij **Bewerking** boven aan het paneel Eigenschappen te klikken -- de vorm wordt opnieuw opgebouwd met de nieuwe bewerking

## Parameters

- **Bewerking** - Welke booleaanse bewerking wordt uitgevoerd. Weergegeven als een pictogrammenrij boven aan het paneel
- **Af te trekken onderdeel/onderdelen** - Welke onderliggende objecten de snijvormen zijn
- **Binnenstebuiten geometrie behouden** - Behandel een binnenstebuiten gekeerde schil als massief materiaal in plaats van het volume eromheen te laten wegvallen. Schakel dit in wanneer een model dat massief zou moeten zijn met ontbrekende delen terugkomt. Het forceert de tragere, exacte booleaanse engine
- **Wikkelrichting repareren** - Keer de binnenstebuiten gekeerde schillen van elk onderdeel om voordat de booleaanse bewerking wordt uitgevoerd. Dit herstelt de geometrie eenmalig in plaats van te wijzigen wat elke latere bewerking als massief beschouwt, en is meestal het beste van de twee antwoorden op een binnenstebuiten gekeerd model

## Tips

- De twee onderdelen passen exact op elkaar, omdat ze uit dezelfde bewerking komen
- Gebruik het voor ontwerpen in meerdere kleuren, in elkaar grijpende assemblages en inlegwerk
- Als een resultaat er verkeerd uitziet, controleer dan of de bronobjecten waterdicht zijn. **Wikkelrichting repareren** herstelt binnenstebuiten gekeerde schillen; [Repareren](../mesh/repair.md) verhelpt bredere schade in geïmporteerde modellen

## Gerelateerd

- [Combineren](combine.md) - Meerdere objecten samenvoegen tot één massieve vorm
- [Aftrekken](subtract.md) - De ene vorm uit de andere snijden
- [Doorsnijden](intersect.md) - Alleen het volume behouden waar objecten elkaar overlappen
- [Vlaksnede](../reshape/plane-cut.md) - Snijden met een plat vlak in plaats van met een andere vorm
- [Repareren](../mesh/repair.md) - Beschadigde geïmporteerde meshes herstellen vóór een booleaanse bewerking

Deze pagina behandelt ook de oudere objecten voor Aftrekken en vervangen die nog voorkomen in ontwerpen die zijn opgeslagen voordat de bewerkingen werden samengevoegd. Ze blijven precies zo werken als voorheen; nieuwe ontwerpen gebruiken het gedeelde booleaanse object met de bewerking Aftrekken en vervangen geselecteerd.
