---
title: Cub
articleKey: CubeObject3D
parent: "Primitives"
nav_order: 4
source_hash: a376a9c78d88d995f3c6ce21dd5098672d6c1dfb
source_lang: en
---
# Cub

O formă de cutie dreptunghiulară cu lățime, adâncime și înălțime reglabile și muchii rotunjite opționale. Cubul este una dintre cele mai frecvent utilizate primitive pentru realizarea modelelor.

<!--  Screenshot of a Cube primitive on the workspace -->
![20260318 183230 paste 20260318 183230](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183230-paste-20260318-183230.jpg)


## Parametri

- **Lățime** - Dimensiunea pe axa X (implicit: 20mm)
- **Adâncime** - Dimensiunea pe axa Y (implicit: 20mm)
- **Înălțime** - Dimensiunea pe axa Z (implicit: 20mm)
- **Rotund** - Activează muchiile rotunjite
- **Rază** - Dimensiunea rotunjirii (vizibilă când Rotund este activat)
- **Segmente de rotunjire** - Netezimea rotunjirii, mai multe segmente = curbe mai netede (vizibilă când Rotund este activat)

## Sfaturi

- Folosiți un Cub ca punct de plecare pentru cutii, plăci, console și carcase
- Activați Rotund pentru muchii netede, cu aspect profesionist
- Raza nu poate depăși jumătate din cea mai mică dimensiune
- Combinați un Cub cu [Scădere](../operations/boolean/subtract.md) pentru a crea decupaje și canale dreptunghiulare

## Corelate

- [Cilindru](cylinder.md) - Formă de coloană rotundă
- [Piramidă](pyramid.md) - Formă cu patru laturi, îngustată spre vârf
- [Gaură](hole.md) - Un cub preconfigurat pentru scădere booleană
