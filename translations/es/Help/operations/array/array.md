---
title: Matriz
articleKey: ArrayObject3D_2
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c547fa24e5f47e0d60f0cec0eac979700d946daf
source_lang: en
---
# Matriz

Matriz crea varias copias de un objeto dispuestas en un patrón. Selecciona un modo con los botones de la parte superior — **Lineal**, **Radial** o **Transformar** — para cambiar entre tipos de patrón.

<!--  Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->
![20260506 080647 paste 20260506 080647](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080647-paste-20260506-080647.jpg)


## Cómo se usa

1. Selecciona un objeto
2. Aplica la operación **Matriz** desde el menú Duplicación
3. Elige un modo (Lineal, Radial o Transformar)
4. Ajusta los parámetros del modo elegido

## Modo: Lineal

El modo Lineal coloca las copias a lo largo de una dirección con progresión opcional de rotación y escala.

**Cantidad** — Número de copias (entero o expresión). El objeto de origen es la primera copia; las copias adicionales se desplazan a partir de él.

**Método de desplazamiento** — Cómo se calcula el espaciado:
- **Relativo** — El desplazamiento se multiplica por el tamaño del cuadro delimitador del objeto. Un Desplazamiento relativo de (1, 0, 0) separa las copias exactamente el ancho de un objeto a lo largo de X.
- **Desplazamiento** — Distancia fija en el espacio del mundo, en mm, por copia.
- **Punto final** — Define la posición de la última copia; el espaciado se reparte de forma uniforme entre las copias.

**Desplazamiento relativo** / **Desplazamiento** / **Punto final** — El vector de espaciado, según el Método de desplazamiento seleccionado.

**Modo de rotación** — Cómo se acumula la rotación entre copias:
- **Local** — Cada copia rota sobre sí misma en su propio centro; la dirección del desplazamiento se mantiene en los ejes del mundo.
- **Combinación** — La rotación se acumula y orienta el desplazamiento, produciendo espirales, abanicos y hélices.

**Rotación** — Rotación por copia en grados en cada eje.

**Escalar** — Escala acumulativa por copia en cada eje. Los valores menores que 1 reducen las copias; los mayores que 1 las agrandan.

**La escala afecta al desplazamiento** — Cuando está activado, el espaciado entre copias también se escala en cada paso. Úsalo para espirales que se cierran y progresiones geométricas (conchas de nautilo, curvas de conchas apiladas).

## Modo: Radial

El modo Radial distribuye las copias uniformemente alrededor de un eje central a un radio fijo.

<!--  Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->
![20260506 092618 paste 20260506 092618](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-092618-paste-20260506-092618.jpg)


**Método de conteo** — Cómo se determina el número de copias:
- **Cantidad** — Número explícito de copias.
- **Distancia** — Separación angular entre copias en grados; la cantidad se calcula para rellenar el barrido.

**Cantidad** / **Distancia angular** — Número de copias (modo Cantidad) o espaciado angular en grados (modo Distancia). Admite expresiones.

**Eje central** — El eje alrededor del cual rotar (predeterminado: Z).

**Segmento de círculo** — Si las copias abarcan un círculo completo de 360° (**Completo**) o un arco parcial (**Arco**).

**Radio** — Distancia desde el eje central hasta cada copia.

**Ángulo de barrido** — Grados de arco que se van a rellenar (se muestra cuando Segmento de círculo es Arco). Admite expresiones.

**Alinear rotación** — Rota cada copia para que su eje frontal apunte hacia fuera desde el centro.

**Eje frontal** — Qué eje de la copia se considera «frontal» para la alineación (se muestra cuando Alinear rotación está activado).

## Modo: Transformar

El modo Transformar avanza las copias usando una transformación manual o siguiendo la transformación de otro objeto.

**Cantidad** — Número de copias (entero o expresión).

**Referencia de transformación** — De dónde procede la transformación de cada paso:
- **Entrada** — Especificas directamente la traslación, la rotación y la escala.
- **Objeto** — La transformación se lee de un objeto hermano indicado por su nombre.

**Traslación** — Desplazamiento por paso en el espacio del mundo, en mm (se muestra cuando la Referencia es Entrada).

**Rotación** — Rotación por paso en grados en cada eje (se muestra cuando la Referencia es Entrada).

**Escalar** / **Escalar ejes** — Escala uniforme y por eje aplicada en cada paso (se muestra cuando la Referencia es Entrada).

**Nombre de transformación** — Nombre del objeto hermano cuya transformación se usa como incremento en cada paso (se muestra cuando la Referencia es Objeto).

**Espacio relativo** — Cuando está activado, la transformación de cada copia se combina en el marco local de la copia anterior; cuando está desactivado, cada paso se aplica en el espacio del mundo (se muestra cuando la Referencia es Objeto).

## Aleatorizar

Activa **Aleatorizar** para añadir variación a todas las copias.

- **Desplazamiento aleatorio** — Desplazamiento de posición aleatorio máximo por eje, en mm.
- **Rotación aleatoria** — Rotación aleatoria máxima por eje, en grados.
- **Ejes de escala aleatoria** — Variación de escala aleatoria máxima por eje.
- **Excluir el primero** — Mantiene la primera copia en su posición calculada exacta (predeterminado: activado).
- **Excluir el último** — Mantiene la última copia en su posición calculada exacta.
- **Semilla aleatoria** — Cámbiala para obtener una disposición aleatoria distinta. Admite expresiones.

## Combinar

- **Crear malla única** — Combina todas las copias en un único objeto de malla fusionado.
- **Combinar vértices** — Suelda los vértices que estén dentro del umbral de distancia de combinación (se muestra cuando Crear malla única está activado).
- **Distancia** — Umbral de combinación en mm (se muestra cuando Combinar vértices está activado).

## Consejos

- Usa expresiones para Cantidad, Rotación o Punto final para crear patrones paramétricos
- Para patrones circulares, usa el modo Radial: ajusta el Radio para controlar el tamaño del círculo y activa Alinear rotación si las copias deben mirar hacia fuera
- La rotación de Combinación en el modo Lineal crea espirales y abanicos sin tener que calcular manualmente los desplazamientos angulares
- La escala afecta al desplazamiento genera de forma natural disposiciones tipo concha de nautilo y de progresión geométrica
- Combina Matriz con [Seleccionar hijo](select-child.md) para crear patrones en los que cada copia muestre una variante distinta

## Relacionado

- [Alinear](../placement/align.md) - Posiciona objetos unos respecto a otros
- [Seleccionar hijo](select-child.md) - Elige una copia concreta de una matriz por índice o por nombre
