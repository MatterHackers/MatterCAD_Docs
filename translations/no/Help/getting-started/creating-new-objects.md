---
title: Opprette nye objekter
parent: "Getting Started"
nav_order: 2
source_hash: 3eccb5aac5bb6f4d88f1ca3583eedd2f70384eeb
source_lang: en
---
# Opprette nye objekter

MatterCAD har et rikt sett med verktøy for å opprette 3D-objekter. Du kan starte med primitive former, bruke spesialiserte verktøy som tekst og QR-koder, eller bygge komplekse former ved hjelp av boolske operasjoner og matriser.

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## Legge til primitiver

Den raskeste måten å starte en design på er å legge til primitive former. Åpne panelet Primitiver i biblioteket og klikk på en form for å legge den til i arbeidsområdet. Tilgjengelige primitiver omfatter:

- **Grunnformer** - Kube, Sylinder, Kule, Kjegle, Torus, Ring, Pyramide, Kile og deres halvvarianter
- **Tekst og spesielle** - Tekst, Blindeskrift, QR-kode, Bildeobjekt, SVG-objekt

Hvert primitiv har parametere du kan justere i panelet Egenskaper etter at du har valgt det. En Kube har for eksempel kontrollene Bredde, Dybde og Høyde. Se [Primitiver](../primitives/index.md) for detaljer om hver form.

## Verktøylinjen for operasjoner

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

Verktøylinjen øverst i visningsområdet gir deg rask tilgang til vanlige operasjoner:

- **Angre / Gjør om** - Reverser eller gjenta endringer. Du kan også bruke **Ctrl+Z** for å angre og **Ctrl+Y** for å gjøre om
- **Grupper / Løs opp gruppe** - Slå sammen valgte objekter til en gruppe som flyttes og behandles som én enhet, eller bryt opp en gruppe
- **Kopier / Slett** - Dupliser eller fjern valgte objekter. Standardsnarveiene **Ctrl+C**, **Ctrl+X** og **Ctrl+V** fungerer også
- **Juster** - Plasser flere objekter i forhold til hverandre
- **Boolske operasjoner** - [Kombiner](../operations/boolean/combine.md), [Trekk fra](../operations/boolean/subtract.md), [Skjæring](../operations/boolean/intersect.md) og [Trekk fra og erstatt](../operations/boolean/subtract-and-replace.md)
- **Matriser** - Opprett [lineære, radiale, kurve- og transformermønstre](../operations/array/array.md) av dupliserte objekter
- **Transformeringer** - Bruk [Roter](../operations/transform/rotate.md), [Skaler](../operations/transform/scale.md), [Speil](../operations/transform/mirror.md) og andre endringer

## Bygge komplekse former

De fleste design i MatterCAD bygges ved å kombinere enkle former:

1. **Start med primitiver** - Legg til grunnformene du trenger
2. **Plasser dem** - Flytt og roter objektene slik at de overlapper der du ønsker
3. **Bruk boolske operasjoner** - Bruk [Kombiner](../operations/boolean/combine.md) for å slå sammen former, eller [Trekk fra](../operations/boolean/subtract.md) for å skjære én form ut av en annen
4. **Finpuss** - Bruk operasjoner under [Endre form](../operations/reshape/index.md) som Fas, Kurve eller Vri for å legge til detaljer

## Relatert

- [Primitiver](../primitives/index.md) - Fullstendig referanse for alle primitive former
- [Legge til eksisterende objekter](adding-existing-objects.md) - Importer filer i stedet for å lage fra bunnen av
- [Boolske operasjoner](../operations/boolean/index.md) - Kombiner former til komplekse figurer
- [Redigere objekter](editing-objects.md) - Flytt, roter og skaler objekter etter at du har opprettet dem
