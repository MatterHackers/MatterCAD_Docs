---
title: Řez rovinou
articleKey: PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
source_hash: 64a9901bf54b71cd2ecc12c8db189b6e2fcde25e
source_lang: en
---
# Řez rovinou

Řez rovinou rozřízne objekt v zadané výšce vodorovnou rovinou a zachová pouze část pod řezem. Plocha řezu je uzavřena rovnou stěnou.

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## Použití

1. Vyberte objekt
2. Použijte operaci **Řez rovinou** z nabídky Přetvarovat
3. Nastavte výšku řezu

## Parametry

- **Výška řezu** – Výška Z, ve které se objekt rozřízne (výchozí: 10 mm, rozsah: 1–200 mm)

## Tipy

- Pomocí operace Řez rovinou zarovnáte horní část modelu do dané výšky
- Hodí se k ořezání importovaných modelů nebo k vytvoření rovných podstav
- Pro řez nerovinným tvarem použijte místo toho operaci [Odečíst](../boolean/subtract.md) s jiným objektem
- Pro řez skloněnou rovinou objekt nejprve otočte, použijte Řez rovinou a poté jej otočte zpět

## Související

- [Průnik](../boolean/intersect.md) – Zachová pouze místa, kde se objekty překrývají
- [Odečíst](../boolean/subtract.md) – Řez libovolným tvarem, nejen rovinou
- [Vydutit](hollow-out.md) – Vytvoří dutou skořepinu
