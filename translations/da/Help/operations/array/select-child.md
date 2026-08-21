---
title: Vælg underelement
articleKey: SelectChildObject3D
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: f6f71d2b457b82126f272ea9354f877c36570df0
source_lang: en
---
# Vælg underelement

Vælg underelement udvælger ét underelement fra en gruppe af objekter ud fra enten et indeksnummer eller et navn. Det er især nyttigt i scriptede og parametriske designs, hvor du dynamisk vil vælge, hvilket objekt der skal vises.

<!-- IMAGE: Screenshot showing Select Child operation with multiple children and one selected by index -->
![20260506 080526 paste 20260506 080526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080526-paste-20260506-080526.jpg)


## Sådan bruges den

1. Markér to eller flere objekter
2. Anvend handlingen **Vælg underelement** fra menuen Duplikering
3. Vælg **Efter indeks** eller **Efter navn** for at styre, hvordan underelementet vælges
4. Angiv det indeksnummer eller navn, der skal matches

## Parametre

- **Markeringsmetode** – Vælg mellem **Efter indeks** (vælg efter position) eller **Efter navn** (vælg efter objektnavn). Vises som knapper.
- **Underordnet indeks** – Det nulbaserede indeks for det underelement, der skal vælges (vises ved brug af Efter indeks). Understøtter [udtryk](../../workspace/expressions.md).
- **Underordnet navn** – Navnet på det underelement, der skal vælges (vises ved brug af Efter navn). Understøtter [udtryk](../../workspace/expressions.md).

Hvis indekset er uden for området, eller navnet ikke matcher noget underelement, returneres det første underelement som reserveløsning. Hvis der ikke er nogen underelementer, returneres intet.

## Brug i scripting

Vælg underelement er designet til at fungere sammen med udtryk og funktionen `rand()` til at skabe dynamiske, datadrevne designs. Du kan for eksempel opbygge en scene med flere variantobjekter som underelementer og bruge et udtryk som `rand(42)` som indeks-seed til tilfældigt at vælge ét af dem.

**Eksempel: Tilfældige bogrekvisitter til en teaterforestilling**

1. Importer 5 forskellige bog-meshes som underelementer til en Vælg underelement-handling
2. Sæt Markeringsmetode til **Efter indeks**
3. Brug et udtryk til Underordnet indeks, f.eks. `floor(rand(seed) * 5)`, hvor `seed` er en arkvariabel
4. Duplikér Vælg underelement-handlingen flere gange, hver med en forskellig seed-værdi
5. Hver instans vælger tilfældigt en forskellig bog fra sættet

Dette mønster fungerer i alle situationer, hvor du skal vælge fra et sæt varianter: møbler, dekorationer, arkitektoniske elementer eller enhver samling af udskiftelige dele.

## Tips

- Kombinér med [Array](array.md) for at skabe varierede mønstre, hvor hver kopi vælger et forskelligt underelement
- Brug arkvariabler til indekset eller navnet for at styre markeringen fra et regneark
- Reserveløsningen med det første underelement betyder, at dit design aldrig går i stykker, heller ikke selvom indekset eller navnet er forkert

## Relateret

- [Array](array.md) – Duplikér objekter i lineære, radiale, kurve- og transformationsmønstre
