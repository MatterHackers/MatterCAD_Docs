---
title: Engranaje 2D
articleKey: Gear2D
parent: "Mechanical Parts"
nav_order: 1
source_hash: aa16d8f12f5342e41cfbfa852b1e8a02cfc82a7d
source_lang: en
---
# Engranaje 2D

Una ruta de engranaje 2D que crea únicamente el perfil de los dientes como una ruta plana. Úsala con [Extrusión lineal](../operations/path/linear-extrude.md) o [Revolución](../operations/path/revolve.md) para tener más control sobre cómo se construye el engranaje en una forma 3D.

<!-- AUTO_IMAGE: type=from_thumbnail item=gear_2d file=mechanical_gear_2d -->
![mechanical_gear_2d](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_gear_2d.png)

## Cómo se usa

1. Agrega un **Engranaje 2D** desde las herramientas mecánicas
2. Configura los parámetros de los dientes
3. Aplica [Extrusión lineal](../operations/path/linear-extrude.md) para darle altura

## Consejos

- Usa Engranaje 2D cuando necesites combinar un perfil de engranaje con otras operaciones de ruta antes de extruirlo
- Para un engranaje 3D listo para usar, consulta [Engranajes](gears.md) en su lugar
- Se aplican las mismas reglas de engrane: el Paso circular y el Ángulo de presión deben coincidir para que los engranajes funcionen juntos

## Relacionado

- [Engranajes](gears.md) - Engranajes 3D listos para usar
- [Ruta de estrella](../2d-paths/star-path.md) - Una forma dentada más sencilla
- [Extrusión lineal](../operations/path/linear-extrude.md) - Dale altura a la ruta del engranaje
