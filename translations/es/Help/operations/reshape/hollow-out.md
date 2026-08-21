---
title: Vaciar
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cc2c5555723ecfe77475fef9e7a2090cdf760204
source_lang: en
---
# Vaciar

Vaciar crea una carcasa hueca a partir de un objeto sólido desplazando la superficie hacia el interior. El resultado es una versión de pared delgada de la forma original.

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## Cómo se usa

1. Seleccione un objeto sólido
2. Aplique la operación **Vaciar** desde el menú Remodelar
3. Establezca el espesor de pared deseado

## Parámetros

- **Distancia**: el espesor de pared en milímetros (valor predeterminado: 2 mm). Es el grosor que tendrá la carcasa resultante.
- **Nº de celdas**: resolución del algoritmo de vaciado (valor predeterminado: 64). Los valores más altos generan superficies internas más suaves, pero tardan más en calcularse.

## Consejos

- Vaciar resulta útil para crear cajas, contenedores, jarrones y piezas ligeras
- Un espesor de pared de 1-2 mm es lo habitual en la mayoría de las piezas impresas en 3D
- Aumente el Nº de celdas si la superficie interna se ve rugosa o escalonada
- El vaciado deja la base abierta; combínelo con un [Cubo](../../primitives/cube.md) si necesita una base cerrada
- En formas complejas, el cálculo puede tardar unos segundos

## Relacionado

- [Corte por plano](plane-cut.md): corta un objeto a una altura determinada
- [Restar](../boolean/subtract.md): elimina material manualmente
