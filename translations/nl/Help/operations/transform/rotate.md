---
title: Roteren
articleKey: RotateObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 9bdc210c5c375fe3179050e8a8916d895455ce5f
source_lang: en
---
# Roteren

Roteren draait een object om een opgegeven as over een bepaalde hoek. Je kunt om elke asrichting roteren en het middelpunt van de rotatie kiezen.

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## Gebruik

1. Selecteer een object
2. Pas de bewerking **Roteren** toe via het menu Transformeren
3. Stel de rotatiehoek en de as in in het paneel Eigenschappen

Je kunt objecten ook rechtstreeks in de viewport roteren door op de rotatiegrepen in de hoeken van een geselecteerd object te klikken. Wanneer je de muis over de hoekindicatoren beweegt, wordt er gesprongen in stappen van 45 graden.

## Parameters

- **Hoek** - De rotatiehoek in graden (bereik: 3-360). Ondersteunt [expressies](../../workspace/expressions.md).
- **Roteren om** - Bepaalt de rotatieas en het oorsprongspunt. Je kunt om de X-, Y- of Z-as roteren, of een aangepaste richting opgeven.

## Tips

- De rotatie wordt standaard gecentreerd op het midden van de bounding box van het object
- Voor rotaties van 90 graden maken de snap-indicatoren het eenvoudig om exacte waarden te krijgen
- Gebruik de bewerking Roteren (in plaats van de bediening in de viewport) wanneer je een nauwkeurige hoek nodig hebt die geen veelvoud van 45 graden is
- Je kunt de rotatieas na het toepassen van de bewerking wijzigen door de eigenschap Roteren om te bewerken

## Gerelateerd

- [Verplaatsen](translate.md) - Een object over een bepaalde afstand verplaatsen
- [Schalen](scale.md) - De grootte van een object aanpassen
- [Spiegelen](mirror.md) - Een gespiegelde weergave maken
