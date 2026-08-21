---
title: Variabelenblad
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
source_hash: 3137a4da2b9d2086d4dcace156435caca288dd79
source_lang: en
---
# Variabelenblad

Het Variabelenblad bewaart gedeelde waarden voor een ontwerp. Gebruik het wanneer meerdere objecten dezelfde afmetingen, aantallen, labels of formules moeten gebruiken. Als je een waarde in het blad wijzigt, worden de afhankelijke objecten opnieuw berekend, zodat parametrische ontwerpen consistent blijven zonder dat je elk object afzonderlijk hoeft te bewerken.

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## Een Variabelenblad toevoegen

1. Open de bibliotheek en voeg **Variabelenblad** toe aan de scène.
2. Selecteer het Variabelenblad-object om de bladeditor te tonen.
3. Selecteer een cel en voer vervolgens een **Naam** en een waarde of formule in.
4. Gebruik de celnaam in andere velden in het ontwerp die expressies ondersteunen.

## Cellen bewerken

Elke cel heeft twee bewerkbare delen:

- **Naam** - Een optionele variabelenaam voor de cel. Namen zijn niet hoofdlettergevoelig, spaties worden omgezet naar liggende streepjes en dubbele namen worden automatisch aangepast.
- **Expressie** - De celwaarde. Platte tekst of getallen worden rechtstreeks opgeslagen. Formules beginnen met `=`.

Naar cellen kan ook worden verwezen via hun adres, zoals `A1` of `B2`. Benoemde cellen zijn meestal duidelijker voor ontwerpparameters omdat ze de bedoeling beschrijven, zoals `wall_thickness`, `outer_diameter` of `hole_count`.

## Formules

Begin een formule met `=` om deze in het blad te laten berekenen:

- `=20 + 5` geeft `25`
- `=pi * 10` geeft `31.41592653589793`
- `=A1 * 2` verwijst naar een andere cel via het adres
- `=wall_thickness + 4` verwijst naar een benoemde cel

Het blad ondersteunt rekenkundige bewerkingen, haakjes, vergelijkingsoperatoren, gangbare `Math`-functies zoals `sin`, `cos`, `sqrt` en `round`, en constanten waaronder `pi`, `tau` en `e`.

## Bladwaarden gebruiken in objecten

De meeste numerieke velden in MatterCAD ondersteunen expressies. Om een bladwaarde in een objectparameter te gebruiken, zet je `=` voor de verwijzing:

- Stel de **Breedte** van een Kubus in op `=case_width`.
- Stel het **Aantal** van een Reeks in op `=hole_count`.
- Stel een **Offset**-waarde van Verplaatsen in op `=wall_thickness * 2`.

Wanneer het blad verandert, berekent MatterCAD de objecten die ervan afhangen opnieuw.

## Tekst- en hulpfuncties

Cellen van het Variabelenblad kunnen zowel tekst als getallen bevatten. Tekstwaarden zijn handig voor gegenereerde labels, onderdeelnummers, geïmporteerde gegevens en aangepaste ontwerp-apps.

Nuttige hulpfuncties zijn onder andere:

- `concat()` of `strcat()` - Tekst of waarden samenvoegen.
- `substring()` - Een deel van een tekstwaarde uitnemen.
- `split()` - Tekst splitsen en één item teruggeven.
- `count()` - Door scheidingstekens gescheiden items in tekst tellen.
- `substitute()` - Tekst vervangen.
- `rand(seed)` - Een deterministische willekeurige waarde genereren wanneer een seed wordt opgegeven.
- `importdata()` - Een waarde inlezen vanaf een URL of een lokaal bestandspad.

## Tips

- Gebruik liever beschrijvende namen dan celadressen voor waarden die door andere objecten worden gebruikt.
- Houd de belangrijkste afmetingen linksboven in het blad, zodat ze gemakkelijk te vinden zijn.
- Gebruik formules voor afgeleide waarden, zoals `inner_diameter = outer_diameter - wall_thickness * 2`.
- Vermijd gereserveerde woorden zoals `pi`, `e`, `true`, `false` of functienamen als celnamen.
- Als een formule niet kan worden geïnterpreteerd, behoudt MatterCAD de oorspronkelijke invoer als tekst.

## Gerelateerd

- [Expressies](expressions.md) - Expressies gebruiken in objectparameters
- [Componenten](components.md) - Herbruikbare geparametriseerde ontwerpen maken
- [Reeks](../operations/array/array.md) - Herhaalde patronen maken die door bladwaarden worden aangestuurd
