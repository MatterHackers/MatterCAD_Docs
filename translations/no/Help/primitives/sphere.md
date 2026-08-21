---
title: Kule
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
source_hash: c227e98ac116c3481bb2af73c55801de84e70b1e
source_lang: en
---
# Kule

En rund kuleform med justerbar diameter og detaljnivå.

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## Parametere

- **Diameter** - Bredden tvers over kulen (standard: 20mm)
- **Sider** - Antall segmenter rundt omkretsen (standard: 40). Flere sider = jevnere overflate

### Avanserte parametere

Aktiver **Avansert**-modus for flere kontroller:

- **Startvinkel** - Vinkelen der kuleoverflaten begynner (standard: 0)
- **Sluttvinkel** - Vinkelen der kuleoverflaten slutter (standard: 360). Sett den lavere enn 360 for delvise kuleformer
- **Breddegradsider** - Antall segmenter fra topp til bunn (standard: 30). Flere = jevnere poler

## Tips

- For 3D-utskrift er 40 sider vanligvis tilstrekkelig. Høyere verdier gir jevnere overflater, men større filer
- Bruk Startvinkel og Sluttvinkel til å lage delvise kuleformer som boller eller kupler
- Kombiner med [Trekk fra](../operations/boolean/subtract.md) for å lage kuleformede hulrom

## Relatert

- [Halvkule](half-sphere.md) - Bare den øvre halvkulen
- [Torus](torus.md) - En smultringform
