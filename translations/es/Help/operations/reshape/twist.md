---
title: Torsión
articleKey: TwistObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: 8ea8d2017c16f20dc42b433bcf91815262bb5380
source_lang: en
---
# Torsión

La torsión gira la parte superior de un objeto respecto a la inferior, creando un efecto de espiral o retorcido a lo largo de la altura. De forma predeterminada, la rotación avanza de manera uniforme de abajo hacia arriba; en Avanzado puedes dibujar en qué punto de la altura se produce realmente el giro.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## Cómo se usa

1. Selecciona un objeto
2. Aplica la operación **Torsión** desde el menú Remodelar
3. Establece el ángulo de torsión y ajusta el laminado para obtener suavidad
4. Activa **Avanzado** si quieres dibujar cómo se reparte la torsión a lo largo de la pieza

## El Perfil de torsión

En Avanzado, la curva del **Perfil de torsión** determina dónde se produce la torsión. La cantidad total de torsión la sigue fijando el control Ángulo (o Distancia de rotación); la curva solo la reparte:

- **A lo largo de la curva** está la altura de la pieza en porcentaje: 0 abajo, 100 arriba. Una línea guía que cruza el editor marca el 100 por ciento y está etiquetada con la altura real de la pieza en mm.
- **A lo ancho de la curva** está el porcentaje de la torsión total alcanzado a esa altura: 0 para nada de ella, 100 para toda.

Una Torsión nueva comienza con una diagonal recta de 0 a 100, que es la torsión uniforme sencilla que obtienes sin usar Avanzado en absoluto.

Un tramo plano de la curva es una franja de la pieza que no se retuerce. Donde la curva no cubre toda la altura, se mantiene su extremo más cercano, de modo que una curva dibujada solo entre el 40 y el 60 por ciento deja la pieza rígida por debajo y por encima: así es como se inicia y se detiene una torsión a media altura.

Un tramo que retrocede a medida que sube desenrolla: esa franja de la pieza gira en sentido contrario, de vuelta hacia donde empezó. Dibujar el perfil por encima de 100 y luego de vuelta hacia abajo es la forma de sobrepasar el total y regresar a él.

## Parámetros

- **Tipo de rotación** - Elige entre:
  - **Ángulo** - Especifica el ángulo total de torsión en grados (3-360)
  - **Distancia** - Especifica la torsión como una distancia a lo largo de la circunferencia
- **Cortes** - Número de cortes horizontales añadidos para una torsión suave, espaciados uniformemente a lo largo de la pieza. Más cortes = torsión más suave
- **Lados mínimos** - El número mínimo de lados que debe tener la pieza alrededor del eje de torsión. Una forma tosca como un cubo no tiene geometría alrededor de su perímetro que soporte la rotación, por lo que sus caras planas se facetan en lugar de curvarse; esto añade cortes verticales a través del eje de torsión para que esas caras puedan seguir la torsión. 0 (el valor predeterminado) deja la pieza sin modificar
- **Torsión a la derecha** - Dirección de la torsión: derecha (sentido horario) o izquierda (sentido antihorario)
- **Radio preferido** - Solo lectura: el radio que la propia pieza informa, o el que implica su forma, que es alrededor del cual se mide una distancia de torsión (solo en el modo Distancia)
- **Editar radio** - Desactiva el radio informado para que puedas establecer el tuyo propio (solo en el modo Distancia, y solo cuando la pieza informa uno)
- **Anular radio** - Radio personalizado para el cálculo de la torsión (solo en el modo Distancia)

### Parámetros avanzados

- **Perfil de torsión** - El editor de curvas descrito arriba: el porcentaje de la torsión total alcanzado a cada altura en porcentaje
- **Desplazamiento de rotación** - Desplaza el centro alrededor del cual gira la pieza, apartándolo del medio de la pieza

## Consejos

- Valores más altos de Cortes producen resultados más suaves pero generan más geometría
- Si un cubo retorcido u otra forma de caras planas se ve facetada en lugar de curvada, aumenta Lados mínimos
- Dibuja el perfil plano en la parte inferior y ascendente después para dejar una base recta bajo una columna retorcida
- Una torsión de 90 grados en una columna cuadrada crea un elegante efecto arquitectónico
- Dibuja dos tramos planos unidos por una subida corta para retorcer el centro de la pieza y dejar rígidos ambos extremos

## Relacionado

- [Curva](curve.md) - Dobla un objeto formando un arco
- [Pellizco](pinch.md) - Comprime hacia el centro
- [Pinzamiento radial](radial-pinch.md) - Da forma al perfil con una curva de la misma manera
