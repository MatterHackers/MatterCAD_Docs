---
title: Legge til eksisterende objekter
parent: "Getting Started"
nav_order: 1
source_hash: e384a5c024336c3c58343d262d914fa40e0b0426
source_lang: en
---
# Legge til eksisterende objekter

Du kan hente eksisterende 3D-modeller inn i MatterCAD ved å importere filer fra datamaskinen eller legge til innhold fra det innebygde biblioteket.

## Fra datamaskinen din

![20260324 081143 paste 20260324 081143](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081143-paste-20260324-081143.jpg)

![20260324 081240 paste 20260324 081240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081240-paste-20260324-081240.jpg)


Klikk på **Åpne**-knappen i verktøylinjen for å bla gjennom og legge til filer fra datamaskinen. MatterCAD støtter følgende importformater:

- **STL** (.stl) – Bransjestandard for 3D-modellformat, mye brukt til 3D-utskrift
- **AMF** (.amf) – Avansert format med støtte for farger og objekter med flere materialer
- **OBJ** (.obj) – Wavefront 3D-grafikkformat (kun mesh-geometri)
- **3MF** (.3mf) – 3D Manufacturing Format med rik støtte for metadata
- **MCX** (.mcx) – MatterCADs eget format, som bevarer alle designdata og parametere
- **SVG** (.svg) – Scalable Vector Graphics, importeres som 2D-baner
- **TTF / OTF** (.ttf, .otf) – Skriftfiler til bruk med Tekst-verktøyet

## Dra og slipp

Du kan også dra og slippe filer direkte fra skrivebordet eller filutforskeren inn i MatterCAD-arbeidsområdet. Støttede filtyper importeres automatisk.

![20260324 081416 paste 20260324 081416](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081416-paste-20260324-081416.jpg)

## Fra biblioteket

### Bibliotek-sidefeltet

Klikk på **Legg til innhold**-knappen i verktøylinjen for å åpne bibliotekpanelet. Herfra kan du:

- Bla gjennom de lagrede designene dine
- Navigere til Primitiver-biblioteket for innebygde former
- Få tilgang til Skybibliotek hvis du er logget inn
- Dra og slippe et hvilket som helst element fra biblioteket direkte inn i arbeidsområdet

![20260324 081446 paste 20260324 081446](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081446-paste-20260324-081446.jpg)

### Bibliotek-fanen

Du kan også bruke Bibliotek-fanen til å bla gjennom samlingene dine. Høyreklikk på et objekt i biblioteket og velg **Legg til i scene** for å importere det til det gjeldende designarbeidsområdet.

![20260324 081536 paste 20260324 081536](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081536-paste-20260324-081536.jpg)

## Tips

- MCX er det beste formatet for å redigere design på nytt senere, siden det bevarer alle parametere og designtreet
- STL-filer inneholder kun mesh-geometri. Hvis du importerer en STL, kan du fortsatt bruke operasjoner på den, men du kan ikke redigere de opprinnelige parameterne
- Når du importerer flere filer, blir hver av dem et separat objekt i scenen. Bruk [Grupper](../workspace/grouping.md) for å organisere dem

## Relatert

- [Opprette nye objekter](creating-new-objects.md) – Start et design fra bunnen av med primitiver
- [Lagrer og eksporterer](saving-and-exporting.md) – Lagre og eksporter de ferdige designene dine
- [Bibliotek](../library/index.md) – Lær mer om hvordan du organiserer designbiblioteket ditt
