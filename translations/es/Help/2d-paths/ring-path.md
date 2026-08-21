---
title: Ruta de anillo
articleKey: RingPathObject3D
parent: "2D Paths"
nav_order: 4
source_hash: 3ee3dd9ab102cfabf1e79d1093b237fb90f12aca
source_lang: en
---
# Ruta de anillo

Una forma de anillo 2D: un círculo con un agujero circular en el centro. Úsala con [Extrusión lineal](../operations/path/linear-extrude.md) para crear formas de tubo o arandela.

<!-- Screenshot of a Ring Path on the workspace -->
![20260506 080211 paste 20260506 080211](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080211-paste-20260506-080211.jpg)

## Parámetros

- **Diámetro exterior**: el diámetro exterior del anillo
- **Diámetro interior**: el diámetro del agujero central

## Consejos

- El grosor de pared del anillo es (Diámetro exterior - Diámetro interior) / 2
- Extruir una Ruta de anillo crea un tubo similar a la primitiva [Anillo](../primitives/ring.md)

## Relacionado

- [Ruta de círculo](circle-path.md): un círculo macizo (sin agujero)
- [Anillo](../primitives/ring.md): una forma de tubo 3D ya preparada
- [Extrusión lineal](../operations/path/linear-extrude.md): da altura a las rutas
