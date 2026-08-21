---
title: Trasladar
articleKey: TranslateObject3D
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c05550dee2397bdb58dc2e247a068a544233a71d
source_lang: en
---
# Trasladar

Trasladar mueve un objeto una distancia específica a lo largo de los ejes X, Y y/o Z. A diferencia de arrastrar un objeto con el ratón, Trasladar permite introducir valores de desplazamiento exactos.

<!--  Screenshot showing the Translate operation properties with X, Y, Z offset fields -->
![20260506 160828 paste 20260506 160828](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160828-paste-20260506-160828.jpg)


## Cómo se usa

1. Seleccione un objeto
2. Aplique la operación **Trasladar** desde el menú Transformar
3. Introduzca los valores de desplazamiento deseados para X, Y y Z en el panel Propiedades

## Parámetros

- **X, Y, Z** (Traslación) - La distancia que se moverá el objeto a lo largo de cada eje, en milímetros. Admite [expresiones](../../workspace/expressions.md) para valores calculados.

## Consejos

- Use Trasladar cuando necesite un posicionamiento preciso y repetible que pueda ajustar más adelante
- Los valores de traslación son relativos a la posición actual del objeto: introducir 10 en X lo mueve 10 mm hacia la derecha desde donde está
- Para reposicionar rápidamente, también puede arrastrar los objetos directamente en la ventana gráfica. Consulte [Edición de objetos](../../getting-started/editing-objects.md)

## Relacionado

- [Rotar](rotate.md) - Rota un objeto un ángulo específico
- [Escalar](scale.md) - Cambia el tamaño de un objeto con precisión
- [Alinear](../placement/align.md) - Posiciona los objetos unos respecto a otros
