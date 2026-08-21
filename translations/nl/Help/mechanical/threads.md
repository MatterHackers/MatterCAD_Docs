---
title: Draadgangen
articleKey: ThreadsObject3D_2
parent: "Mechanical Parts"
nav_order: 3
source_hash: 7d881b3293a508e102d3a4b845cdfd4eb9c34fa8
source_lang: en
---
# Draadgangen

Maak schroefdraad met instelbare diameter, steek en draadprofiel. Draadgangen kunnen worden gebruikt als losstaande bouten/schroeven of van andere objecten worden afgetrokken om draadgaten te maken.

<!-- AUTO_IMAGE: type=from_thumbnail item=threads file=mechanical_threads -->
![mechanical_threads](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_threads.png)

## Gebruik

1. Voeg **Draadgangen** toe via de Mechanisch-gereedschappen of het paneel Primitieven
2. Stel de diameter, de steek en het aantal rotaties in
3. Schakel eventueel "Gebruiken als gat" in om draadgaten te maken

## Parameters

### Gebruik

- **Gebruiken als gat** - Wanneer dit is ingeschakeld, krijgen de draadgangen extra tolerantie zodat ze als afgetrokken gat kunnen worden gebruikt (standaard: uit)
- **Tolerantie** - Extra speling voor de passing bij gebruik als gat (standaard: 0,2 mm, zichtbaar wanneer Gebruiken als gat aan staat)

### Eigenschappen

- **Diameter** - De buitendiameter van het deel met schroefdraad (standaard: 10 mm)
- **Steek** - Afstand tussen elke draadwinding (standaard: 2 mm). Kleinere steek = fijnere draad
- **Draadschaal** - Breedte van de draadgangen als verhouding van de steek (standaard: 1,0, bereik: 0,1-1,0)
- **Rotaties** - Aantal volledige draadwindingen (standaard: 10)

### Geometrie

- **Zijden** - Aantal segmenten rondom de omtrek (standaard: 40). Meer = gladder

### Punten (draaduiteinden)

- **Puntschaal** - Hoe sterk de draaduiteinden taps toelopen (standaard: 0, bereik: 0-1). Stel hoger dan 0 in om een taps toelopende aanloop aan de uiteinden te maken
- **Punthoek** - De hoek waarover de punten taps toelopen (standaard: 90 graden)

## Tips

- Een draadgat maken: schakel "Gebruiken als gat" in, plaats de draadgangen en [Aftrekken](../operations/boolean/subtract.md) van je object
- Voeg Tolerantie toe bij gebruik als gat, zodat de geprinte onderdelen goed in elkaar passen
- Standaard metrische draadsteken: M3=0,5 mm, M4=0,7 mm, M5=0,8 mm, M6=1,0 mm, M8=1,25 mm, M10=1,5 mm
- Gebruik Puntschaal om een aanloop te maken waarmee het draadaansnijden eenvoudiger wordt

## Gerelateerd

- [Tandwielen](gears.md) - Maak mechanische tandwielvormen
- [Cilinder](../primitives/cylinder.md) - Een gewone ronde kolom (zonder schroefdraad)
- [Aftrekken](../operations/boolean/subtract.md) - Snijd draadgangen uit andere objecten om gaten te maken
