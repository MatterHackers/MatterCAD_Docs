---
title: Aftrekken
articleKey: SubtractObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 59685bd0a635b70d7f938780f71e90be595dd993
source_lang: en
---
# Aftrekken

Aftrekken snijdt de onderdelen die u kiest uit de onderdelen die u niet kiest. Gebruik **Af te trekken onderdeel/onderdelen** om de snijvormen te kiezen; al het overige is de basis die wordt gesneden.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->
![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)

[Combineren](combine.md), Aftrekken, [Doorsnijden](intersect.md) en [Aftrekken en vervangen](subtract-and-replace.md) worden allemaal uitgevoerd door één booleaans object -- de werkbalkknop maakt het aan met Aftrekken al geselecteerd, en u kunt op elk moment overschakelen naar een van de andere drie via de pictogramrij **Bewerking** boven aan het paneel Eigenschappen.

Aftrekken werkt op vaste lichamen en op 2D-paden. Er wordt gekeken naar wat u aanlevert en de juiste soort bewerking wordt uitgevoerd: het aftrekken van het ene pad van het andere levert een pad op, en het aftrekken van de ene mesh van de andere levert een vast lichaam op.

## Gebruik

1. Selecteer twee of meer objecten
2. Klik op **Aftrekken** in de werkbalk -- er wordt automatisch een standaardonderdeel gekozen dat wordt weggesneden, zodat er meteen iets gebeurt
3. Gebruik **Af te trekken onderdeel/onderdelen** om te kiezen welke onderliggende objecten de snijvormen zijn
4. Bedenk u op elk moment door op een ander pictogram in de rij **Bewerking** boven aan het paneel Eigenschappen te klikken -- de vorm wordt opnieuw opgebouwd met de nieuwe bewerking

## Parameters

- **Bewerking** - Welke booleaanse bewerking wordt uitgevoerd. Weergegeven als een pictogramrij boven aan het paneel
- **Af te trekken onderdeel/onderdelen** - Welke onderliggende objecten de snijvormen zijn
- **Afgetrokken onderdelen behouden** - Laat de weggesneden onderdelen in de scène staan in plaats van ze te verwijderen
- **Binnenstebuiten geometrie behouden** - Behandel een binnenstebuiten gekeerde schaal als vast materiaal in plaats van het volume eromheen te laten opheffen. Schakel dit in wanneer een model dat massief hoort te zijn met ontbrekende delen terugkomt. Het forceert de tragere, exacte booleaanse engine
- **Wikkelrichting repareren** - Draai de binnenstebuiten gekeerde schalen van elk onderdeel om voordat de booleaanse bewerking wordt uitgevoerd. Dit herstelt de geometrie in één keer in plaats van te wijzigen wat elke latere bewerking als massief beschouwt, en is meestal de betere van de twee oplossingen voor een binnenstebuiten gekeerd model

## Tips

- Objecten moeten elkaar overlappen, anders doet Aftrekken niets
- Zorg er voor een doorlopend gat voor dat het snijdende object volledig door de basis heen steekt
- Voor een eenvoudig gat is de primitief [Gat](../../primitives/hole.md) al ingesteld om af te trekken
- De snijdende objecten blijven in de ontwerpboom staan, zodat u ze kunt verplaatsen of van formaat kunt veranderen waarna de snede wordt bijgewerkt
- Ziet een resultaat er verkeerd uit, controleer dan of de bronobjecten waterdicht zijn. **Wikkelrichting repareren** herstelt binnenstebuiten gekeerde schalen; [Repareren](../mesh/repair.md) herstelt bredere schade in geïmporteerde modellen

## Gerelateerd

- [Combineren](combine.md) - Meerdere objecten samenvoegen tot één vaste vorm
- [Doorsnijden](intersect.md) - Alleen het volume behouden waar objecten elkaar overlappen
- [Aftrekken en vervangen](subtract-and-replace.md) - Eén vorm aftrekken en het weggesneden stuk behouden
- [Vlaksnede](../reshape/plane-cut.md) - Snijden met een plat vlak in plaats van met een andere vorm
- [Gat](../../primitives/hole.md) - Een kubus die vooraf is ingesteld om af te trekken
- [Repareren](../mesh/repair.md) - Beschadigde geïmporteerde meshes herstellen vóór een booleaanse bewerking

Deze pagina behandelt ook de oudere Aftrekken-objecten die nog voorkomen in ontwerpen die zijn opgeslagen voordat de bewerkingen werden samengevoegd. Ze blijven precies zo werken als voorheen; nieuwe ontwerpen gebruiken het gedeelde booleaanse object met de bewerking Aftrekken geselecteerd.
