---
title: Torus
articleKey: TorusObject3D
parent: "Primitives"
nav_order: 17
source_hash: aaec1652de4d6713bd01a707964cf4985d3fb5f6
source_lang: en
---
# Torus

En doughnutformet ring med uafhængig styring af den samlede størrelse og tykkelsen af ringens tværsnit.

<!--  Screenshot of a Torus primitive on the workspace -->
![20260318 184240 paste 20260318 184240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184240-paste-20260318-184240.jpg)


## Parametre

- **Ydre diameter** - Den samlede bredde tværs over torussen (standard: 20mm)
- **Indvendig diameter** - Diameteren på hullet i midten (standard: 10mm)
- **Sider** - Antal segmenter rundt om hovedringen (standard: 40)

### Avancerede parametre

Aktiver tilstanden **Avanceret** for yderligere kontrolmuligheder:

- **Startvinkel** - Vinklen hvor torussen begynder (standard: 0)
- **Slutvinkel** - Vinklen hvor torussen slutter (standard: 360). Sæt den til mindre end 360 for at få en åben ring eller bue
- **Ringsider** - Antal segmenter rundt om ringens tværsnit (standard: 15). Flere = glattere rørprofil
- **Ringfasevinkel** - Roterer tværsnitsprofilen (standard: 0)

## Tips

- Ringrørets tykkelse bestemmes af forskellen mellem ydre og indvendig diameter
- Brug start- og slutvinkler til at lave åbne ringsegmenter, buer eller C-former
- Nyttig til at lave O-ringe, håndtag, dekorative ringe og rørbøjninger

## Relateret

- [Ring](ring.md) - En hul cylinder med lige vægge (rør)
- [Kugle](sphere.md) - En massiv kugleform
- [Halv kugle](half-sphere.md) - En kuppelform
