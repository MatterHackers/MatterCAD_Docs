---
title: Simetría
articleKey: MirrorObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 8a8de28f5e429177d4b0092d0756387eb6b83a70
source_lang: en
---
# Simetría

La operación Simetría crea una copia reflejada de un objeto respecto a uno de los tres ejes principales. El resultado es una versión simétrica de la forma original.

<!--  Before and after showing an object mirrored across the X axis -->
![20260506 160651 paste 20260506 160651](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160651-paste-20260506-160651.jpg)


## Cómo se usa

1. Selecciona un objeto
2. Aplica la operación **Simetría** desde el menú Transformar
3. Elige el eje respecto al cual se hará la simetría

## Parámetros

- **Simetría activada** - El eje respecto al cual se aplica la simetría:
  - **Eje X** - Invierte el objeto de izquierda a derecha
  - **Eje Y** - Invierte el objeto de delante hacia atrás
  - **Eje Z** - Invierte el objeto de arriba hacia abajo

## Consejos

- La simetría se centra en el cuadro delimitador del objeto, por lo que el resultado simétrico ocupa el mismo espacio que el original
- Las normales de las caras se corrigen automáticamente tras aplicar la simetría para mantener una representación correcta
- Usa Simetría para crear diseños simétricos: modela una mitad, aplícale la simetría y luego usa [Combinar](../boolean/combine.md) con el original
- La simetría no es destructiva: puedes cambiar el eje de simetría en cualquier momento

## Relacionado

- [Rotar](rotate.md) - Rota un objeto en lugar de aplicarle simetría
- [Escalar](scale.md) - Cambia el tamaño de un objeto
- [Combinar](../boolean/combine.md) - Combina el original y la copia simétrica en un solo objeto
