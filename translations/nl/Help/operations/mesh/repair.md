---
title: Repareren
articleKey: RepairObject3D_2
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: f637470dee4f722b595f07d2da9dcdaac5e8da72
source_lang: en
---
# Repareren

Repareren verhelpt veelvoorkomende problemen in mesh-geometrie, waaronder niet-manifold randen, gaten, inconsistente vlakoriëntatie en bijna samenvallende hoekpunten. Dit is vooral handig voor geïmporteerde STL- en OBJ-bestanden die fouten kunnen bevatten.

![20260324 080517 paste 20260324 080517](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080517-paste-20260324-080517.jpg)


## Gebruik

1. Selecteer een object met mesh-problemen
2. Pas de bewerking **Repareren** toe via het Mesh-menu
3. Bekijk de statistieken van vóór en na om te zien wat er is hersteld

## Statistieken (alleen-lezen)

- **Beginhoekpunten / Uiteindelijke hoekpunten** - Aantal hoekpunten vóór en na het repareren
- **Beginvlakken / Uiteindelijke vlakken** - Aantal vlakken vóór en na het repareren
- **Begin niet-manifold randen / Uiteindelijke niet-manifold randen** - Aantal probleemranden vóór en na

### Geavanceerde opties

Schakel de modus **Geavanceerd** in voor nauwkeurige controle:

- **Vertices samenvoegen** - Bijna samenvallende hoekpunten samenvoegen (standaard: aan)
- **Samenvoegtolerantie** - Hoe dicht hoekpunten bij elkaar moeten liggen om samengevoegd te worden
- **Vlakoriëntatie** - Binnenstebuiten gekeerde shells de juiste kant op draaien, zodat elk lichaam als massief wordt gelezen. Elke shell wordt afzonderlijk beoordeeld, zodat een hol model zijn holtes behoudt in plaats van dat deze worden opgevuld. Shells waarvan de eigen vlakken onderling niet overeenkomen, worden met rust gelaten in plaats van dat er een gok wordt gedaan, en modellen die niet waterdicht zijn vallen terug op een toleranter herstel - voer eerst **Gaten vullen** uit als oriëntatie alleen ze niet verhelpt.
- **Randen samenvoegen** - Kleine scheuren en slechte naden herstellen
- **Gaten vullen** - Openingen in het meshoppervlak vullen
- **Verwijdermodus** - Interne of verdekte geometrie verwijderen:
  - **Geen** - Alle geometrie behouden
  - **Binnenkant** - Interne lichamen verwijderen die in de hoofdvorm verborgen zitten
  - **Verdekt** - Vlakken verwijderen die van buitenaf niet zichtbaar zijn

## Tips

- Probeer eerst Repareren als booleaanse bewerkingen (Combineren, Aftrekken) onverwachte resultaten geven op geïmporteerde modellen
- De standaardinstellingen (Vertices samenvoegen aan, al het overige uit) verhelpen de meest voorkomende problemen
- Schakel Gaten vullen in als u door openingen in het model heen kunt kijken
- Gebruik de Verwijdermodus Binnenkant om modellen op te schonen die verborgen geometrie bevatten

## Gerelateerd

- [Decimeren](decimate.md) - Het aantal polygonen verkleinen
- [Bestaande objecten toevoegen](../../getting-started/adding-existing-objects.md) - Modellen importeren die mogelijk gerepareerd moeten worden
