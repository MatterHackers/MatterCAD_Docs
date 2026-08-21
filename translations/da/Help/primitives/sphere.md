---
title: Kugle
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
source_hash: c227e98ac116c3481bb2af73c55801de84e70b1e
source_lang: en
---
# Kugle

En rund kugleform med justerbar diameter og detaljeniveau.

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## Parametre

- **Diameter** - Bredden tværs over kuglen (standard: 20mm)
- **Sider** - Antal segmenter rundt om omkredsen (standard: 40). Flere sider = glattere overflade

### Avancerede parametre

Aktivér tilstanden **Avanceret** for yderligere kontrolmuligheder:

- **Startvinkel** - Vinklen hvor kuglens overflade begynder (standard: 0)
- **Slutvinkel** - Vinklen hvor kuglens overflade slutter (standard: 360). Sæt den til mindre end 360 for delvise kugleformer
- **Breddegradssider** - Antal segmenter fra top til bund (standard: 30). Flere = glattere poler

## Tips

- Til 3D-print er 40 sider som regel tilstrækkeligt. Højere værdier giver glattere overflader, men større filer
- Brug Startvinkel og Slutvinkel til at skabe delvise kugleformer som skåle eller kupler
- Kombinér med [Træk fra](../operations/boolean/subtract.md) for at skabe kugleformede hulrum

## Relateret

- [Halv kugle](half-sphere.md) - Kun den øverste halvkugle
- [Torus](torus.md) - En doughnutform
