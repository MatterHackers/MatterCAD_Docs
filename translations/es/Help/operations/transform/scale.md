---
title: Escalar
articleKey: ScaleObject3D_3
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b3b5419c3db29550b2544bb6aca91ca3ce6fa715
source_lang: en
---
# Escalar

Escalar redimensiona un objeto con un control preciso sobre las dimensiones, las proporciones y la conversión de unidades. Puede escalar de forma uniforme, bloquear ejes concretos entre sí o redimensionar cada eje de forma independiente.

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## Cómo se usa

1. Seleccione un objeto
2. Aplique la operación **Escalar** desde el menú Transformar
3. Elija el método de escala e introduzca los valores deseados

También puede escalar objetos en la ventana gráfica haciendo clic y arrastrando los controles de escala de las esquinas de un objeto seleccionado.

## Parámetros

### Tipo de escala

Elija un ajuste predefinido o una escala personalizada:

- **Personalizado** - Introduzca sus propias dimensiones o porcentajes
- **Pulgadas a mm** - Multiplica por 25,4 (convierte del sistema imperial al métrico)
- **mm a pulgadas** - Multiplica por 0,0393 (convierte del sistema métrico al imperial)
- **mm a cm** - Multiplica por 0,1
- **cm a mm** - Multiplica por 10

### Método de escala (modo Personalizado)

- **Directo** - Introduzca la Anchura, la Profundidad y la Altura deseadas en milímetros
- **Porcentaje** - Introduzca la Anchura, la Profundidad y la Altura como porcentajes del tamaño original

### Bloquear proporción

- **Ninguno (Escalar libremente)** - Cada eje se escala de forma independiente
- **X e Y** - La Anchura y la Profundidad quedan bloqueadas entre sí; la Altura se escala de forma independiente
- **X, Y y Z** - Los tres ejes se escalan juntos de forma uniforme

### Dimensiones

- **Anchura** - Tamaño a lo largo del eje X
- **Profundidad** - Tamaño a lo largo del eje Y
- **Altura** - Tamaño a lo largo del eje Z

## Consejos

- Use "Pulgadas a mm" si ha importado un archivo STL diseñado en pulgadas y se ve demasiado pequeño
- Ajuste Bloquear proporción a X, Y y Z para escalar de forma uniforme: al cambiar cualquier dimensión se actualizan todas
- La posición de la base del objeto se mantiene durante el escalado, de modo que permanece sobre la superficie del espacio de trabajo
- Puede escribir valores exactos para dimensionar con precisión o usar los deslizadores para hacer ajustes rápidos

## Relacionado

- [Trasladar](translate.md) - Mover un objeto
- [Rotar](rotate.md) - Rotar un objeto
- [Ajustar a los límites](../placement/fit-to-bounds.md) - Escalar para que quepa dentro de un tamaño concreto
