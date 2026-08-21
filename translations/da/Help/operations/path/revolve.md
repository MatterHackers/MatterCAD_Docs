---
title: Roter profil
articleKey: RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: a63ebb08d982178e0e59f0b9f07c3c0dca53148b
source_lang: en
---
# Roter profil

Roter profil drejer en 2D-sti omkring en akse for at skabe et 3D-omdrejningslegeme. Sådan laver du vaser, skåle, hjul og andre rotationssymmetriske objekter.

<!--  Before and after showing a profile path being revolved into a vase shape -->
![20260506 102004 paste 20260506 102004](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-102004-paste-20260506-102004.jpg)


## Sådan bruges den

1. Vælg en 2D-sti
2. Anvend **Roter profil** fra menuen med Sti-operationer
3. Justér rotationsområdet, akseposition og antal sider

## Parametre

- **Rotation** - Samlet rotationsvinkel for omdrejningen (standard: 0, interval: 0-360). Sæt til 360 for en komplet omdrejning.
- **Akseposition** - Rotationsaksens forskydning fra stiens centrum (standard: 0, interval: -30 til 30). Positiv flytter aksen væk fra stien, hvilket giver en større åbning.
- **Startvinkel** - Hvor omdrejningen begynder (standard: 0)
- **Slutvinkel** - Hvor omdrejningen slutter (standard: 45). Sæt til 360 for en fuld omdrejning.
- **Sider** - Antal segmenter rundt om omdrejningen (standard: 30). Flere = glattere overflade.

## Tips

- Brug Akseposition til at styre den indvendige diameter på den roterede form
- Sæt Startvinkel og Slutvinkel til mindre end 360 for at skabe delvise omdrejninger (buer, tagrender)
- Tegn en profilsti af din vase- eller skålform, og roter den derefter for perfekt symmetri
- En [Cirkel-sti](../../2d-paths/circle-path.md), der roteres, danner en torus

## Relateret

- [Lineær ekstrudering](linear-extrude.md) - Ekstrudér lige op i stedet for at rotere
- [2D-stier](../../2d-paths/index.md) - Opret profilstier til rotation
- [Torus](../../primitives/torus.md) - En færdiglavet roteret ringform
