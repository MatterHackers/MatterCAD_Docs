---
title: Tandwielen
articleKey: GearObject3D
parent: "Mechanical Parts"
nav_order: 2
source_hash: 23098f94da8cd032e0617fbf346621504446347f
source_lang: en
---
# Tandwielen

Maak 3D-tandwielen met volledig configureerbare tandgeometrie. MatterCAD genereert correcte evolvente tandprofielen die goed grijpen in andere tandwielen met dezelfde module en drukhoek.

<!-- AUTO_IMAGE: type=from_thumbnail item=gear file=mechanical_gears -->
![mechanical_gears](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_gears.png)

## Gebruik

1. Voeg een **Tandwiel** toe vanuit de Mechanisch-gereedschappen of het paneel Primitieven
2. Stel het aantal tanden en de overige parameters in
3. Het tandprofiel wordt automatisch gegenereerd

## Parameters

### Kenmerken

- **Tandwieltype** - Extern tandwiel of Heugel (rechte staaf met tanden)
- **Hoogte** - Dikte van het tandwiel (extrusiehoogte)
- **Aantal tanden** - Aantal tanden rondom het tandwiel (standaard: 30, bereik: 4-60)
- **Cirkelsteek** - De boogafstand tussen de tanden langs de steekcirkel (bereik: 3-30). Dit bepaalt de totale grootte.
- **Diameter middengat** - Diameter van het centrale asgat (standaard: 4mm, stel in op 0 voor geen gat). Alleen voor externe tandwielen.
- **Buitenrandbreedte** - Breedte van de rand buiten de binnentanden
- **Aantal tanden binnentandwiel** - Aantal tanden van het bijbehorende inwendige tandwiel

### Geavanceerd

- **Drukhoek** - De hoek van het tandcontactvlak (gebruikelijke waarden: 14,5, 20 of 25 graden). Alle in elkaar grijpende tandwielen moeten dezelfde drukhoek gebruiken.
- **Speling** - Minimale ruimte tussen de tandtop en de tanddal van het bijbehorende tandwiel
- **Speling** - Minimale ruimte tussen in elkaar grijpende tanden om vastlopen te voorkomen

### Tandwielgegevens (alleen-lezen)

- **Steekstraal** - De straal waarop tandwielen in elkaar grijpen
- **Buitendiameter** - De totale diameter tot aan de tandtoppen

## Tips

- Twee tandwielen grijpen correct in elkaar wanneer ze dezelfde Cirkelsteek en Drukhoek hebben
- Gebruik de waarden van de Steekstraal om in elkaar grijpende tandwielen correct te plaatsen -- de afstand tussen de tandwielmiddelpunten moet gelijk zijn aan de som van hun steekstralen
- Voeg Speling toe bij 3D-geprinte tandwielen om rekening te houden met printtoleranties
- Voor 2D-tandwielprofielen (voor gebruik met Extruderen), zie [Tandwiel 2D](gear-2d.md)

## Gerelateerd

- [Tandwiel 2D](gear-2d.md) - 2D-tandwielpad voor padbewerkingen
- [Draadgangen](threads.md) - Maak schroefdraadkenmerken
