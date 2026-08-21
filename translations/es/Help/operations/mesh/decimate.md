---
title: Reducir
articleKey: DecimateObject3D
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 58a2573b968808e98203832142fa8bacf7a9cf99
source_lang: en
---
# Reducir (Decimar)

Reducir disminuye el recuento de polígonos de una malla conservando la forma general. Resulta útil para simplificar modelos con mucho detalle, reducir el tamaño del archivo y acelerar las operaciones sobre geometría compleja.

![20260324 080430 paste 20260324 080430](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080430-paste-20260324-080430.jpg)


## Cómo se usa

1. Selecciona un objeto
2. Aplica la operación **Reducir** desde el menú Malla
3. Elige tu objetivo (cantidad o porcentaje) y ajústalo

## Parámetros

- **Modo** - Elige cómo especificar el objetivo:
  - **Porcentaje** - Conserva un porcentaje de los polígonos originales (predeterminado: 50 %)
  - **Cantidad** - Apunta a un recuento de polígonos concreto
- **Recuento de polígonos de origen** - Número original de polígonos (solo lectura)
- **Porcentaje objetivo** - Porcentaje de polígonos que se conservan (visible en el modo Porcentaje)
- **Recuento objetivo** - Número exacto de polígonos que se conservan (visible en el modo Cantidad)
- **Cantidad después de la reducción por porcentaje** - Recuento final de polígonos tras la reducción por porcentaje (solo lectura)
- **Mantener superficie** - Proyecta los vértices de vuelta sobre la superficie original para lograr mayor precisión (más lento, pero más fiel a la forma original)

## Consejos

- Una reducción del 50 % suele conservar bien la calidad visual
- Activa Mantener superficie cuando la precisión importe más que la velocidad
- Reducir el recuento de polígonos acelera las operaciones booleanas en modelos importados complejos
- Un recuento de polígonos muy bajo degradará la forma de manera visible: revisa el resultado antes de confirmarlo

## Relacionado

- [Reparar](repair.md) - Corrige problemas de la malla
