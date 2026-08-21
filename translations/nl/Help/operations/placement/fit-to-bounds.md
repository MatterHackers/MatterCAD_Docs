---
title: Passend maken aan grenzen
articleKey: FitToBoundsObject3D_4
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 91b9c917cb636f28403c291a4d56f22bf6758b70
source_lang: en
---
# Passend maken aan grenzen

Passend maken aan grenzen schaalt een object zodat het binnen opgegeven afmetingen voor breedte, diepte en hoogte past. Je kunt bepalen hoe het object zich uitrekt en uitlijnt binnen de doelgrenzen.

<!--  Screenshot showing an object being fit to specific bounding dimensions -->
![20260506 154930 paste 20260506 154930](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154930-paste-20260506-154930.jpg)

## Gebruik

1. Selecteer een object
2. Pas de bewerking **Passend maken aan grenzen** toe via het menu Plaatsing
3. Voer de gewenste afmetingen in
4. Kies de vergrendeling van de verhouding en het uitrekgedrag

## Parameters

- **Verhouding vergrendelen** - Hoe de verhoudingen worden beperkt:
  - **Geen** - Elke as kan afzonderlijk worden ingesteld
  - **X & Y** - Breedte en diepte zijn aan elkaar gekoppeld
  - **X, Y & Z** - Uniforme schaling op alle assen
- **Breedte** - Gewenste breedte (X-afmeting)
- **Diepte** - Gewenste diepte (Y-afmeting)
- **Hoogte** - Gewenste hoogte (Z-afmeting)

### Wanneer Verhouding vergrendelen op X & Y of X, Y & Z staat

- **Uitrekken** - Hoe het object wordt ingepast:
  - **Binnen** - Verkleinen zodat het volledig binnen de grenzen past (kan ruimte overlaten)
  - **Uitvouwen** - Vergroten om de grenzen te vullen (kan in sommige afmetingen buiten de grenzen vallen)

### Wanneer Verhouding vergrendelen op Geen staat

Elke as heeft een eigen:

- **Uitrekken** - Binnen of Uitvouwen per as
- **Uitlijnen** - Waar het object binnen de grenzen wordt geplaatst (Min, Midden, Max)

## Tips

- Gebruik dit om geïmporteerde modellen naar exacte doelafmetingen te schalen
- Vergrendel alle verhoudingen voor uniforme schaling waarbij de oorspronkelijke vorm behouden blijft
- Gebruik de instelling per as wanneer je een specifieke breedte nodig hebt maar de andere afmetingen er niet toe doen

## Gerelateerd

- [Schalen](../transform/scale.md) - Schalen op verhouding of percentage in plaats van op doelafmeting
- [Passend maken aan cilinder](fit-to-cylinder.md) - Inpassen binnen een cilindrische begrenzing
- [Uitlijnen](align.md) - Objecten ten opzichte van elkaar positioneren
