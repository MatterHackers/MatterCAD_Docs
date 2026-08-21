---
title: Nieuwe objecten maken
parent: "Getting Started"
nav_order: 2
source_hash: 3eccb5aac5bb6f4d88f1ca3583eedd2f70384eeb
source_lang: en
---
# Nieuwe objecten maken

MatterCAD biedt een uitgebreide set gereedschappen om 3D-objecten te maken. Je kunt beginnen met primitieve vormen, gespecialiseerde gereedschappen zoals tekst en QR-codes gebruiken, of complexe vormen bouwen met booleaanse bewerkingen en reeksen.

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## Primitieven toevoegen

De snelste manier om een ontwerp te beginnen is door primitieve vormen toe te voegen. Open het paneel Primitieven in de bibliotheek en klik op een willekeurige vorm om die aan je werkruimte toe te voegen. Beschikbare primitieven zijn onder meer:

- **Basisvormen** - Kubus, Cilinder, Bol, Kegel, Torus, Ring, Piramide, Wig en hun halve varianten
- **Tekst en speciaal** - Tekst, Braille, QR-code, Afbeeldingsobject, SVG-object

Elk primitief heeft parameters die je na selectie in het paneel Eigenschappen kunt aanpassen. Een Kubus heeft bijvoorbeeld regelaars voor Breedte, Diepte en Hoogte. Zie [Primitieven](../primitives/index.md) voor details over elke vorm.

## De werkbalk Bewerkingen

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

De werkbalk boven aan de viewport geeft je snel toegang tot veelgebruikte bewerkingen:

- **Ongedaan maken / Opnieuw uitvoeren** - Wijzigingen terugdraaien of opnieuw afspelen. Je kunt ook **Ctrl+Z** gebruiken om ongedaan te maken en **Ctrl+Y** om opnieuw uit te voeren
- **Groeperen / Groepering opheffen** - Combineer geselecteerde objecten tot een groep die als één geheel beweegt en werkt, of haal een groep uit elkaar
- **Kopiëren / Verwijderen** - Geselecteerde objecten dupliceren of verwijderen. De standaardsneltoetsen **Ctrl+C**, **Ctrl+X** en **Ctrl+V** werken ook
- **Uitlijnen** - Meerdere objecten ten opzichte van elkaar positioneren
- **Booleaanse bewerkingen** - [Combineren](../operations/boolean/combine.md), [Aftrekken](../operations/boolean/subtract.md), [Doorsnijden](../operations/boolean/intersect.md) en [Aftrekken en vervangen](../operations/boolean/subtract-and-replace.md)
- **Reeksen** - Maak [lineaire, radiale, kromme- en transformatiepatronen](../operations/array/array.md) van gedupliceerde objecten
- **Transformeren** - Pas [Roteren](../operations/transform/rotate.md), [Schalen](../operations/transform/scale.md), [Spiegelen](../operations/transform/mirror.md) en andere aanpassingen toe

## Complexe vormen bouwen

De meeste ontwerpen in MatterCAD worden gebouwd door eenvoudige vormen te combineren:

1. **Begin met primitieven** - Voeg de basisvormen toe die je nodig hebt
2. **Positioneer ze** - Verplaats en roteer objecten zodat ze elkaar overlappen waar jij dat wilt
3. **Pas booleaanse bewerkingen toe** - Gebruik [Combineren](../operations/boolean/combine.md) om vormen samen te voegen, of [Aftrekken](../operations/boolean/subtract.md) om de ene vorm uit de andere te snijden
4. **Verfijn** - Gebruik bewerkingen van [Hervormen](../operations/reshape/index.md) zoals Afschuining, Kromme of Draaien om detail toe te voegen

## Gerelateerd

- [Primitieven](../primitives/index.md) - Volledige referentie voor alle primitieve vormen
- [Bestaande objecten toevoegen](adding-existing-objects.md) - Importeer bestanden in plaats van vanaf nul te maken
- [Booleaanse bewerkingen](../operations/boolean/index.md) - Vormen combineren tot complexe vormen
- [Objecten bewerken](editing-objects.md) - Objecten verplaatsen, roteren en schalen nadat je ze hebt gemaakt
