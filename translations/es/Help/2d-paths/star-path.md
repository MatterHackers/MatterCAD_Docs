---
title: Ruta de estrella
articleKey: StarPathObject3D
parent: "2D Paths"
nav_order: 5
source_hash: 74d92e4171c452cd10069921636e45d7ef9dc70e
source_lang: en
---
# Ruta de estrella

Una ruta 2D con forma de estrella con un número de puntos y un radio interior/exterior configurables. Úsala con [Extrusión lineal](../operations/path/linear-extrude.md) para crear formas de estrella en 3D.

<!-- Screenshot of a Star Path on the workspace -->
![20260506 080319 paste 20260506 080319](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080319-paste-20260506-080319.jpg)


## Parámetros

- **Puntos** - Número de puntas de la estrella
- **Radio exterior** - Distancia desde el centro hasta el extremo de cada punta
- **Radio interior** - Distancia desde el centro hasta los valles entre las puntas

## Consejos

- La relación entre el Radio interior y el Radio exterior determina lo "puntiaguda" que es la estrella. Un Radio interior pequeño crea puntas afiladas y pronunciadas.
- Ajusta Puntos a 5 para una estrella clásica, a 6 para una estrella de David o a un valor mayor para formas similares a un engranaje
- Usa [Suavizar trayectoria](../operations/path/smooth-path.md) en una Ruta de estrella para crear formas de estrella redondeadas

## Relacionado

- [Ruta de círculo](circle-path.md) - Un círculo suave
- [Engranaje 2D](../mechanical/gear-2d.md) - Un perfil de engranaje real
- [Extrusión lineal](../operations/path/linear-extrude.md) - Da altura a las rutas
