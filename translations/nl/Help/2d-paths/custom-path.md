---
title: Aangepast pad
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
source_hash: 3633c708477de3ac77d3547b730c33f7e4431cf6
source_lang: en
---
# Aangepast pad

Teken je eigen 2D-pad met controlepunten. Dit geeft je volledige vrijheid om elke gewenste 2D-vorm te maken, die je vervolgens kunt extruderen of wentelen tot een 3D-object.

<!-- Screenshot showing a custom path being edited with control points -->
![20260506 080247 paste 20260506 080247](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080247-paste-20260506-080247.jpg)


## Gebruik

1. Voeg een **Aangepast pad** toe vanuit de bibliotheek met 2D-paden
2. Bewerk de controlepunten om je vorm te bepalen
3. Pas [Lineaire extrusie](../operations/path/linear-extrude.md) of andere padbewerkingen toe om een 3D-object te maken

## Open en gesloten paden

Het selectievakje **Gesloten** bepaalt of het pad zijn laatste punt weer met het eerste verbindt.

- **Gesloten** (de standaardinstelling) laat het pad een gebied omsluiten. Dat is wat [Lineaire extrusie](../operations/path/linear-extrude.md) en [Wentelen](../operations/path/revolve.md) opvullen.
- **Openen** maakt van het pad een lijn. Een lijn omsluit niets, dus die verschijnt in de scène als een dun lint over de lengte in plaats van als een gevulde vorm. Gebruik [Pad opblazen](../operations/path/inflate-path.md) om er breedte aan te geven en er weer iets massiefs van te maken.

Twee dingen om te weten voordat je **Gesloten** uitschakelt:

- **Opnieuw sluiten is geen ongedaan maken.** Bij het openen van een pad wordt het sluitende segment weggegooid. Als dat segment gebogen was, levert het opnieuw aanvinken van **Gesloten** een rechte lijn op, niet de curve. Gebruik in plaats daarvan Ctrl+Z - ongedaan maken herstelt het oorspronkelijke pad exact.
- **Sommige contouren laten zich niet openen.** Een contour die minder dan twee punten zou overhouden - een druppelvorm getekend als één punt met een curve die daarnaar terugloopt - blijft gesloten in plaats van in te klappen tot iets wat je niet meer kunt zien of aanklikken. Datzelfde geldt voor een contour met een kwadratische curve, zoals een geïmporteerde SVG die kan bevatten: openen zou de curve tot een hoek platslaan. De weigering geldt per contour, dus de rest van het pad gaat wel open.

Als een pad meerdere contouren heeft die het niet met elkaar eens zijn, staat het selectievakje op open. Door het aan te vinken breng je alle contouren op één lijn.

Bewerkingen die een gebied nodig hebben, sluiten een open pad voor je in plaats van het te weigeren. Lineaire extrusie, Wentelen, Aftrekken en de andere booleaanse bewerkingen doen dit allemaal, dus een open pad extrudeert tot hetzelfde volume als de gesloten versie.

## Tips

- Gebruik Aangepast pad wanneer geen van de ingebouwde padvormen past bij wat je nodig hebt
- Zie [SVG-object](../primitives/svg-object.md) voor het importeren van vormen uit externe vectorprogramma's
- Om een lijn te tekenen en er een onderdeel van te maken, schakel je **Gesloten** uit, pas je [Pad opblazen](../operations/path/inflate-path.md) toe om er dikte aan te geven en vervolgens [Lineaire extrusie](../operations/path/linear-extrude.md) om er hoogte aan te geven

## Gerelateerd

- [Cirkelpad](circle-path.md) - Een kant-en-klare cirkel
- [Kubuspad](box-path.md) - Een kant-en-klare rechthoek
- [SVG-object](../primitives/svg-object.md) - Vectorpaden uit SVG-bestanden importeren
- [Lineaire extrusie](../operations/path/linear-extrude.md) - Paden hoogte geven
