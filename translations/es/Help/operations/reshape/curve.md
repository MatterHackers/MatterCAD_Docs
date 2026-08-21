---
title: Curva
articleKey: CurveObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 6adde5da3bb469384f59eb5e9dfe5cb642b3eec5
source_lang: en
---
# Curva

Curva dobla un objeto recto para darle forma de arco o de círculo. Puedes controlar el doblado especificando un ángulo o un diámetro alrededor del cual envolver el objeto.

<!--  Before and after showing a straight bar being curved into an arc -->
![20260506 155243 paste 20260506 155243](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155243-paste-20260506-155243.jpg)

## Cómo se usa

1. Selecciona un objeto
2. Aplica la operación **Curva** desde el menú Remodelar
3. Elige entre el tipo de doblado por Ángulo o por Diámetro
4. Ajusta los parámetros para obtener la curvatura deseada

## Parámetros

- **Tipo de doblado** - Elige entre:
  - **Ángulo** - Especifica directamente el ángulo de doblado (1-360 grados)
  - **Diámetro** - Especifica el diámetro del círculo alrededor del cual se envuelve la pieza
- **Dirección de doblado** - Doblar hacia arriba o Doblar hacia abajo
- **Porcentaje inicial** - Punto a lo largo del objeto donde comienza el doblado (0-100 %)
- **Dividir malla** - Divide la malla para obtener curvas suaves (predeterminado: activado)
- **Lados mín. por revolución** - Número mínimo de segmentos de malla por revolución completa. Valores más altos = curvas más suaves

### Parámetros avanzados

- **Porcentaje de curvatura inicial** - Porcentaje desde la izquierda donde comienza el doblado
- **Porcentaje de curvatura final** - Porcentaje desde la izquierda donde termina el doblado

## Consejos

- Usa Curva para crear arcos, anillos y soportes doblados a partir de formas rectas
- Ajustar el ángulo a 360 envuelve el objeto formando un anillo completo
- Aumenta Lados mín. por revolución para obtener resultados más suaves en doblados cerrados
- El objeto se dobla a lo largo de su longitud (eje X)

## Relacionado

- [Torsión](twist.md) - Rota a lo largo de la altura en lugar de doblar
- [Toro](../../primitives/torus.md) - Una forma de anillo ya preparada
