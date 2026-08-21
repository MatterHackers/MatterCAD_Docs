---
title: Oprettelse af nye objekter
parent: "Getting Started"
nav_order: 2
source_hash: 3eccb5aac5bb6f4d88f1ca3583eedd2f70384eeb
source_lang: en
---
# Oprettelse af nye objekter

MatterCAD indeholder et righoldigt sæt værktøjer til at oprette 3D-objekter. Du kan starte med primitive former, bruge specialiserede værktøjer som tekst og QR-koder eller opbygge komplekse former ved hjælp af booleske handlinger og arrays.

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## Tilføjelse af primitiver

Den hurtigste måde at begynde et design på er ved at tilføje primitive former. Åbn panelet Primitiver i biblioteket, og klik på en vilkårlig form for at føje den til dit arbejdsområde. Tilgængelige primitiver omfatter:

- **Grundlæggende former** - Terning, Cylinder, Kugle, Kegle, Torus, Ring, Pyramide, Kile og deres halve varianter
- **Tekst og specialformer** - Tekst, Braille, QR-kode, Billedobjekt, SVG-objekt

Hvert primitiv har parametre, som du kan justere i panelet Egenskaber, når du har valgt det. En Terning har for eksempel kontrollerne Bredde, Dybde og Højde. Se [Primitiver](../primitives/index.md) for detaljer om hver enkelt form.

## Værktøjslinjen med handlinger

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

Værktøjslinjen øverst i visningen giver dig hurtig adgang til almindelige handlinger:

- **Fortryd / Gentag** - Omgør eller gentag ændringer. Du kan også bruge **Ctrl+Z** til at fortryde og **Ctrl+Y** til at gentage
- **Gruppér / Opdel gruppe** - Kombinér valgte objekter til en gruppe, der flyttes og behandles som én enhed, eller bryd en gruppe op
- **Kopiér / Slet** - Duplikér eller fjern valgte objekter. Standardgenvejene **Ctrl+C**, **Ctrl+X** og **Ctrl+V** virker også
- **Justér** - Placér flere objekter i forhold til hinanden
- **Booleske handlinger** - [Kombinér](../operations/boolean/combine.md), [Træk fra](../operations/boolean/subtract.md), [Skær](../operations/boolean/intersect.md) og [Træk fra og erstat](../operations/boolean/subtract-and-replace.md)
- **Arrays** - Opret [lineære, radiale, kurve- og transformationsmønstre](../operations/array/array.md) af duplikerede objekter
- **Transformationer** - Anvend [Roter](../operations/transform/rotate.md), [Skalér](../operations/transform/scale.md), [Spejl](../operations/transform/mirror.md) og andre ændringer

## Opbygning af komplekse former

De fleste designs i MatterCAD bygges ved at kombinere enkle former:

1. **Start med primitiver** - Tilføj de grundlæggende former, du har brug for
2. **Placér dem** - Flyt og roter objekterne, så de overlapper, hvor du ønsker det
3. **Anvend booleske handlinger** - Brug [Kombinér](../operations/boolean/combine.md) til at smelte former sammen, eller [Træk fra](../operations/boolean/subtract.md) til at skære én form ud af en anden
4. **Forfin** - Brug handlinger under [Omform](../operations/reshape/index.md) som Fas, Kurve eller Vrid til at tilføje detaljer

## Relateret

- [Primitiver](../primitives/index.md) - Fuld reference for alle primitive former
- [Tilføjelse af eksisterende objekter](adding-existing-objects.md) - Importer filer i stedet for at oprette fra bunden
- [Booleske handlinger](../operations/boolean/index.md) - Kombinér former til komplekse figurer
- [Redigering af objekter](editing-objects.md) - Flyt, roter og skalér objekter, efter du har oprettet dem
