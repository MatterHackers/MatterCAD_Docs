---
title: Sirkelbane
articleKey: CirclePathObject3D
parent: "2D Paths"
nav_order: 2
source_hash: 587edab627246f47731f9dbde2a13a00dd464807
source_lang: en
---
# Sirkelbane

En sirkulær 2D-bane. Brukes sammen med [Lineær ekstrudering](../operations/path/linear-extrude.md) for å lage sylindere, eller [Roter rundt akse](../operations/path/revolve.md) for å lage torusliknende former.

<!-- Screenshot of a Circle Path on the workspace -->
![20260506 080110 paste 20260506 080110](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080110-paste-20260506-080110.jpg)


## Parametere

- **Diameter** - Diameteren til sirkelen (standard: 20mm)
- **Segmenter** - Antall linjesegmenter som danner sirkelen. Flere = jevnere

## Tips

- En Sirkelbane kombinert med Lineær ekstrudering gir en sylinder, tilsvarende primitivet [Sylinder](../primitives/cylinder.md), men med større fleksibilitet i hvordan du bygger videre på den
- Bruk den som grunnlag for Roter rundt akse for å lage ringformer

## Relatert

- [Boksbane](box-path.md) - En rektangulær 2D-bane
- [Ringbane](ring-path.md) - En sirkel med hull
- [Lineær ekstrudering](../operations/path/linear-extrude.md) - Gi baner høyde
