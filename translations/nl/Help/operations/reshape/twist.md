---
title: Draaien
articleKey: TwistObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: 8ea8d2017c16f20dc42b433bcf91815262bb5380
source_lang: en
---
# Draaien

Draaien roteert de bovenkant van een object ten opzichte van de onderkant en creëert zo een spiraal- of draaieffect over de hoogte. Standaard verloopt de rotatie gelijkmatig van onder naar boven; onder Geavanceerd kun je tekenen waar over de hoogte de draaiing daadwerkelijk plaatsvindt.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## Gebruik

1. Selecteer een object
2. Pas de bewerking **Draaien** toe vanuit het menu Hervormen
3. Stel de draaihoek in en pas het aantal segmenten aan voor een vloeiend resultaat
4. Schakel **Geavanceerd** in als je wilt tekenen hoe de draaiing over het onderdeel wordt verdeeld

## Het Draaiprofiel

Onder Geavanceerd bepaalt de curve **Draaiprofiel** waar de draaiing plaatsvindt. De totale hoeveelheid draaiing wordt nog steeds ingesteld met de instelling Hoek (of Rotatieafstand) - de curve verdeelt die alleen:

- **Omhoog langs de curve** is de hoogte op het onderdeel in procenten - 0 onderaan, 100 bovenaan. Een hulplijn door de editor markeert 100 procent en is voorzien van de werkelijke hoogte van het onderdeel in mm.
- **Dwars over de curve** is het percentage van de totale draaiing dat op die hoogte is bereikt - 0 voor niets ervan, 100 voor de volledige draaiing.

Een nieuwe draaiing begint met een rechte diagonaal van 0 naar 100, wat precies de gelijkmatige draaiing is die je zonder Geavanceerd krijgt.

Een vlak stuk in de curve is een band van het onderdeel die niet draait. Waar de curve niet de volledige hoogte beslaat, wordt het dichtstbijzijnde uiteinde ervan aangehouden, zodat een curve die alleen tussen 40 en 60 procent is getekend het onderdeel eronder en erboven stijf laat - zo laat je een draaiing halverwege beginnen en stoppen.

Een stuk dat naar beneden loopt terwijl het omhoog gaat, draait terug: die band van het onderdeel draait de andere kant op, terug naar waar hij begon. Door het profiel voorbij 100 en daarna weer omlaag te tekenen, schiet je door het totaal heen en keer je er weer naar terug.

## Parameters

- **Rotatietype** - Kies tussen:
  - **Hoek** - Geef de totale draaihoek in graden op (3-360)
  - **Afstand** - Geef de draaiing op als een afstand langs de omtrek
- **Segmenten** - Aantal horizontale sneden dat wordt toegevoegd voor een vloeiende draaiing, gelijkmatig verdeeld over het onderdeel. Meer segmenten = vloeiendere draaiing
- **Minimum aantal zijden** - Het minimale aantal zijden dat het onderdeel rond de draai-as moet hebben. Een grove vorm zoals een kubus heeft rond zijn omtrek geen geometrie om de rotatie te dragen, waardoor de platte vlakken facetteren in plaats van te krommen; dit voegt verticale sneden door de draai-as toe zodat die vlakken de draaiing kunnen volgen. 0 (de standaard) laat het onderdeel ongemoeid
- **Rechts draaien** - Richting van de draaiing: rechts (met de klok mee) of links (tegen de klok in)
- **Voorkeursstraal** - Alleen-lezen: de straal die het onderdeel zelf opgeeft, of die door zijn vorm wordt geïmpliceerd, en waaromheen een draaiafstand wordt gemeten (alleen in de modus Afstand)
- **Straal bewerken** - Schakel de opgegeven straal uit zodat je een eigen straal kunt instellen (alleen in de modus Afstand, en alleen wanneer het onderdeel een straal opgeeft)
- **Straal overschrijven** - Aangepaste straal voor de draaiberekening (alleen in de modus Afstand)

### Geavanceerde parameters

- **Draaiprofiel** - De hierboven beschreven curve-editor: het percentage van de totale draaiing dat op elke hoogte in procenten is bereikt
- **Rotatie-offset** - Verschuif het middelpunt waaromheen het onderdeel wordt gedraaid, weg van het midden van het onderdeel

## Tips

- Hogere waarden voor Segmenten geven vloeiendere resultaten, maar genereren meer geometrie
- Als een gedraaide kubus of een andere vorm met platte zijden gefacetteerd in plaats van gekromd oogt, verhoog dan Minimum aantal zijden
- Teken het profiel onderaan vlak en daarna oplopend om een rechte basis onder een gedraaide kolom te houden
- Een draaiing van 90 graden op een vierkante kolom levert een elegant architectonisch effect op
- Teken twee vlakke stukken verbonden door een korte stijging om het midden van het onderdeel te draaien en beide uiteinden stijf te laten

## Gerelateerd

- [Krommen](curve.md) - Buig een object tot een boog
- [Knijpen](pinch.md) - Samendrukken richting het midden
- [Radiale knijp](radial-pinch.md) - Vorm het profiel op dezelfde manier met een curve
