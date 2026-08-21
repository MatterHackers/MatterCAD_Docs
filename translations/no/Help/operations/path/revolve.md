---
title: Roter rundt akse
articleKey: RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: a63ebb08d982178e0e59f0b9f07c3c0dca53148b
source_lang: en
---
# Roter rundt akse

Roter rundt akse dreier en 2D-bane rundt en akse for å lage et 3D-rotasjonslegeme. Slik lager du vaser, boller, hjul og andre rotasjonssymmetriske objekter.

<!--  Before and after showing a profile path being revolved into a vase shape -->
![20260506 102004 paste 20260506 102004](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-102004-paste-20260506-102004.jpg)


## Slik bruker du den

1. Velg en 2D-bane
2. Bruk **Roter rundt akse** fra menyen for Bane-operasjoner
3. Juster rotasjonsområdet, akseposisjonen og antall sider

## Parametere

- **Rotasjon** – Total rotasjonsvinkel for rotasjonen (standard: 0, område: 0–360). Sett til 360 for en fullstendig omdreining.
- **Akseposisjon** – Forskyvning av rotasjonsaksen fra banens senter (standard: 0, område: -30 til 30). Positiv flytter aksen bort fra banen og gir en større åpning.
- **Startvinkel** – Der omdreiningen begynner (standard: 0)
- **Sluttvinkel** – Der omdreiningen slutter (standard: 45). Sett til 360 for en full omdreining.
- **Sider** – Antall segmenter rundt omdreiningen (standard: 30). Flere = jevnere overflate.

## Tips

- Bruk Akseposisjon til å styre den indre diameteren på den roterte formen
- Sett Startvinkel og Sluttvinkel til mindre enn 360 for å lage delvise omdreininger (buer, renner)
- Tegn en profilbane av vase- eller bolleformen din, og roter den for perfekt symmetri
- En [Sirkel-bane](../../2d-paths/circle-path.md) som roteres, gir en torus

## Relatert

- [Lineær ekstrudering](linear-extrude.md) – Ekstruder rett opp i stedet for å rotere
- [2D-baner](../../2d-paths/index.md) – Opprett profilbaner å rotere
- [Torus](../../primitives/torus.md) – En ferdiglaget, rotert ringform
