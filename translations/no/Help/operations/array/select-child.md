---
title: Velg underobjekt
articleKey: SelectChildObject3D
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: f6f71d2b457b82126f272ea9354f877c36570df0
source_lang: en
---
# Velg underobjekt

Velg underobjekt plukker ut ett underobjekt fra en gruppe objekter basert på enten et indeksnummer eller et navn. Dette er spesielt nyttig i skriptbaserte og parametriske design der du vil velge dynamisk hvilket objekt som skal vises.

<!-- IMAGE: Screenshot showing Select Child operation with multiple children and one selected by index -->
![20260506 080526 paste 20260506 080526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080526-paste-20260506-080526.jpg)


## Slik bruker du den

1. Velg to eller flere objekter
2. Bruk operasjonen **Velg underobjekt** fra Duplisering-menyen
3. Velg **Etter indeks** eller **Etter navn** for å styre hvordan underobjektet velges
4. Angi indeksnummeret eller navnet det skal samsvare med

## Parametere

- **Utvalgsmetode** – Velg mellom **Etter indeks** (velg etter posisjon) eller **Etter navn** (velg etter objektnavn). Vises som knapper.
- **Underordnet indeks** – Den nullbaserte indeksen til underobjektet som skal velges (vises når Etter indeks brukes). Støtter [uttrykk](../../workspace/expressions.md).
- **Underordnet navn** – Navnet på underobjektet som skal velges (vises når Etter navn brukes). Støtter [uttrykk](../../workspace/expressions.md).

Hvis indeksen er utenfor gyldig område, eller navnet ikke samsvarer med noe underobjekt, returneres det første underobjektet som reserveløsning. Hvis det ikke finnes noen underobjekter, returneres ingenting.

## Bruk i Skripting

Velg underobjekt er laget for å fungere sammen med uttrykk og funksjonen `rand()` for å lage dynamiske, datadrevne design. Du kan for eksempel bygge en scene med flere variantobjekter som underobjekter og bruke et uttrykk som `rand(42)` som indeksfrø for å plukke ett tilfeldig.

**Eksempel: Tilfeldige bokrekvisitter til en sceneoppsetning**

1. Importer 5 forskjellige bok-mesher som underobjekter av en Velg underobjekt-operasjon
2. Sett Utvalgsmetode til **Etter indeks**
3. Bruk et uttrykk for Underordnet indeks, for eksempel `floor(rand(seed) * 5)` der `seed` er en arkvariabel
4. Dupliser Velg underobjekt-operasjonen flere ganger, hver med en ulik frøverdi
5. Hver forekomst plukker tilfeldig en annen bok fra settet

Dette mønsteret fungerer for alle situasjoner der du må velge fra et sett med varianter: møbler, dekorasjoner, arkitektoniske elementer eller enhver samling av utbyttbare deler.

## Tips

- Kombiner med [Matrise](array.md) for å lage varierte mønstre der hver kopi velger et annet underobjekt
- Bruk arkvariabler for indeksen eller navnet for å styre utvalget fra et regneark
- Reserveløsningen med å falle tilbake til det første underobjektet gjør at designet aldri blir ødelagt, selv om indeksen eller navnet er feil

## Relatert

- [Matrise](array.md) – Dupliser objekter i lineære, radiale, kurve- og transformasjonsmønstre
