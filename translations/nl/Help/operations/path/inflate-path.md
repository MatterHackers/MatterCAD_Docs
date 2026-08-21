---
title: Pad opblazen
articleKey: InflatePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: c0e11d3d24c5f832f797cde4d392e26a4694733d
source_lang: en
---
# Pad opblazen

Pad opblazen breidt een 2D-pad naar buiten uit, waardoor de vorm groter wordt terwijl de algehele vorm behouden blijft. Dit lijkt op het toepassen van een uniforme offset op alle randen.

<!--  Before and after showing a path inflated outward -->
![20260506 100652 paste 20260506 100652](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100652-paste-20260506-100652.jpg)


## Gebruik

1. Selecteer een 2D-pad
2. Pas **Pad opblazen** toe vanuit het menu met Pad-bewerkingen
3. Pas de mate van opblazen aan

## Een open lijn opblazen

Met Opblazen maak je van een lijn een vorm. Schakel **Gesloten** uit bij een [Aangepast pad](../../2d-paths/custom-path.md) om een open lijn te tekenen en blaas die vervolgens op: het resultaat is een gevulde band die aan weerszijden van de lijn zo breed is als de waarde die je instelt. Vanaf daar extrudeert hij net als elk ander pad.

**Stijl** bepaalt hoe de twee uiteinden van de lijn worden afgesloten en hoe de hoeken worden verbonden:

- **Vlak** laat de band recht eindigen bij elk eindpunt
- **Rond** voegt een halve cirkel toe voorbij elk eindpunt
- **Scherp** voegt een vierkant toe voorbij elk eindpunt

Een open lijn heeft geen binnenkant om naar te krimpen, dus bij een waarde van nul of een negatieve waarde zou er helemaal niets overblijven. Wanneer het pad *volledig* open is, begrenst Opblazen de waarde tot een klein positief getal en schrijft dat begrensde getal terug in het vak, zodat je kunt zien wat er is gebeurd.

Een pad dat open en gesloten contouren combineert, wordt niet begrensd: de gesloten contouren krimpen zoals gebruikelijk en de open contouren vallen simpelweg weg. Gesloten paden krimpen bij negatieve waarden nog steeds precies zoals altijd.

## Tips

- Gebruik negatieve waarden om het pad naar binnen te laten krimpen in plaats van uit te breiden
- Opblazen is handig voor het maken van tolerantie-offsets rond vormen
- Combineer met [Contourpad](outline-path.md) om randen met specifieke breedtes te maken

## Gerelateerd

- [Contourpad](outline-path.md) - Maak een contour van een pad
- [Randpad](border-path.md) - Voeg een randoffset toe
- [Pad gladmaken](smooth-path.md) - Rond de hoeken van een pad af
