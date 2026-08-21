---
title: Extrusión lineal
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cdfdb9cfe4c3339e70a23ddfb2f5071b1e8c5557
source_lang: en
---
# Extrusión lineal

La Extrusión lineal da altura a una ruta 2D, convirtiendo una forma plana en un sólido 3D. Esta es la forma principal de convertir rutas en objetos 3D.

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## Cómo usarla

1. Seleccione una ruta 2D o un objeto basado en una ruta
2. Aplique **Extrusión lineal** desde el menú de operaciones de Ruta
3. Establezca la altura deseada

## Parámetros

- **Altura** - Qué tan alta es la extrusión (predeterminado: 5mm, rango: 0.1-50mm)
- **Biselar parte superior** - Agrega un borde biselado (redondeado) en la parte superior de la extrusión (predeterminado: desactivado)

### Parámetros del bisel (visibles cuando Biselar parte superior está activado)

- **Estilo** - El estilo del perfil del bisel (Agudo o redondeado)
- **Radio** - Qué tanto se extiende el bisel (predeterminado: 3mm)
- **Segmentos** - Suavidad de la curva del bisel (predeterminado: 9)

## Consejos

- Funciona con cualquier ruta 2D: rutas de [Círculo](../../2d-paths/circle-path.md), [Caja](../../2d-paths/box-path.md), [Estrella](../../2d-paths/star-path.md), [SVG](../../primitives/svg-object.md) y [Personalizado](../../2d-paths/custom-path.md)
- Active Biselar parte superior para lograr un aspecto más pulido y profesional
- Para girar una ruta alrededor de un eje en lugar de extruirla en línea recta hacia arriba, consulte [Revolución](revolve.md)

## Relacionado

- [Revolución](revolve.md) - Gira una ruta alrededor de un eje
- [Rutas 2D](../../2d-paths/index.md) - Formas de ruta disponibles
- [Texto](../../primitives/text.md) - El texto se extruye automáticamente
