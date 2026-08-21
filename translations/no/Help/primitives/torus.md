---
title: Torus
articleKey: TorusObject3D
parent: "Primitives"
nav_order: 17
source_hash: aaec1652de4d6713bd01a707964cf4985d3fb5f6
source_lang: en
---
# Torus

En smultringformet ring med uavhengig kontroll over den totale størrelsen og tykkelsen på ringens tverrsnitt.

<!--  Screenshot of a Torus primitive on the workspace -->
![20260318 184240 paste 20260318 184240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184240-paste-20260318-184240.jpg)


## Parametere

- **Ytre diameter** - Den totale bredden tvers over torusen (standard: 20mm)
- **Innvendig diameter** - Diameteren på hullet i midten (standard: 10mm)
- **Sider** - Antall segmenter rundt hovedringen (standard: 40)

### Avanserte parametere

Aktiver **Avansert**-modus for flere kontroller:

- **Startvinkel** - Vinkelen der torusen begynner (standard: 0)
- **Sluttvinkel** - Vinkelen der torusen slutter (standard: 360). Sett den lavere enn 360 for å få en åpen ring eller bue
- **Ringsider** - Antall segmenter rundt ringens tverrsnitt (standard: 15). Flere = jevnere rørprofil
- **Ringfasevinkel** - Roterer tverrsnittsprofilen (standard: 0)

## Tips

- Tykkelsen på ringrøret bestemmes av differansen mellom Ytre diameter og Innvendig diameter
- Bruk Startvinkel og Sluttvinkel til å lage åpne ringsegmenter, buer eller C-former
- Nyttig for å lage O-ringer, håndtak, dekorative ringer og rørbøyer

## Relatert

- [Ring](ring.md) - En hul sylinder med rette vegger (rør)
- [Kule](sphere.md) - En massiv kuleform
- [Halvkule](half-sphere.md) - En kuppelform
