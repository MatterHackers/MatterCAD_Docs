---
title: Agujero
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# Agujero

Un objeto con forma de cubo preconfigurado para actuar como herramienta de sustracción booleana. Cuando usas [Combinar](../operations/boolean/combine.md), los objetos Agujero se restan automáticamente de las demás formas en lugar de sumarse a ellas.

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## Cómo funciona

La primitiva Agujero funciona igual que un [Cubo](cube.md), pero con su tipo de salida establecido en «Agujero». Cuando combinas objetos que incluyen un Agujero, el volumen del Agujero se quita del resultado.

## Parámetros

Los mismos que los del [Cubo](cube.md):

- **Anchura** - Tamaño a lo largo del eje X
- **Profundidad** - Tamaño a lo largo del eje Y
- **Altura** - Tamaño a lo largo del eje Z

## Consejos

- Posiciona el Agujero de modo que se solape con el objeto que quieres cortar
- Haz que el Agujero atraviese por completo el objeto de destino si quieres un agujero pasante
- Puedes usar formas normales con [Restar](../operations/boolean/subtract.md) para lograr el mismo efecto, pero los Agujeros resultan cómodos porque funcionan automáticamente con [Combinar](../operations/boolean/combine.md)
- Para agujeros redondos, usa en su lugar un [Cilindro](cylinder.md) con Restar

## Relacionado

- [Cubo](cube.md) - La misma forma sin el comportamiento de agujero
- [Combinar](../operations/boolean/combine.md) - Combina formas y resta los Agujeros automáticamente
- [Restar](../operations/boolean/subtract.md) - Resta manualmente cualquier forma de otra
