---
title: Tilføjelse af eksisterende objekter
parent: "Getting Started"
nav_order: 1
source_hash: e384a5c024336c3c58343d262d914fa40e0b0426
source_lang: en
---
# Tilføjelse af eksisterende objekter

Du kan hente eksisterende 3D-modeller ind i MatterCAD ved at importere filer fra din computer eller tilføje indhold fra det indbyggede bibliotek.

## Fra din computer

![20260324 081143 paste 20260324 081143](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081143-paste-20260324-081143.jpg)

![20260324 081240 paste 20260324 081240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081240-paste-20260324-081240.jpg)


Klik på knappen **Åbn** i værktøjslinjen for at gennemse og tilføje filer fra din computer. MatterCAD understøtter følgende importformater:

- **STL** (.stl) - Industristandard til 3D-modeller, meget udbredt til 3D-print
- **AMF** (.amf) - Avanceret format, der understøtter farver og objekter med flere materialer
- **OBJ** (.obj) - Wavefront 3D-grafikformat (kun mesh-geometri)
- **3MF** (.3mf) - 3D Manufacturing Format med omfattende understøttelse af metadata
- **MCX** (.mcx) - MatterCADs eget format, som bevarer alle designdata og parametre
- **SVG** (.svg) - Scalable Vector Graphics, importeres som 2D-baner
- **TTF / OTF** (.ttf, .otf) - Skrifttypefiler til brug med Tekst-værktøjet

## Træk og slip

Du kan også trække og slippe filer direkte fra dit skrivebord eller din filstifinder ind i MatterCAD-arbejdsområdet. Understøttede filtyper importeres automatisk.

![20260324 081416 paste 20260324 081416](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081416-paste-20260324-081416.jpg)

## Fra Bibliotek

### Bibliotekets sidepanel

Klik på knappen **Tilføj indhold** i værktøjslinjen for at åbne bibliotekspanelet. Herfra kan du:

- Gennemse dine gemte designs
- Navigere til biblioteket Primitiver for at finde indbyggede former
- Få adgang til dit Skybibliotek, hvis du er logget ind
- Trække og slippe et hvilket som helst element fra biblioteket direkte ind i dit arbejdsområde

![20260324 081446 paste 20260324 081446](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081446-paste-20260324-081446.jpg)

### Fanen Bibliotek

Du kan også bruge fanen Bibliotek til at gennemse dine samlinger. Højreklik på et objekt i biblioteket, og vælg **Tilføj til scene** for at importere det til dit aktuelle designarbejdsområde.

![20260324 081536 paste 20260324 081536](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081536-paste-20260324-081536.jpg)

## Tips

- MCX er det bedste format, hvis du vil redigere designs igen senere, da det bevarer alle parametre og designtræet
- STL-filer indeholder kun mesh-geometri. Hvis du importerer en STL-fil, kan du stadig anvende operationer på den, men du kan ikke redigere de oprindelige parametre
- Når du importerer flere filer, bliver hver enkelt et separat objekt i din scene. Brug [Gruppér](../workspace/grouping.md) til at organisere dem

## Relateret

- [Oprettelse af nye objekter](creating-new-objects.md) - Start et design fra bunden med primitiver
- [Gemmer og eksporterer](saving-and-exporting.md) - Gem og eksportér dine færdige designs
- [Bibliotek](../library/index.md) - Læs mere om, hvordan du organiserer dit designbibliotek
