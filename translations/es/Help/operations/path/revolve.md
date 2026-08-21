---
title: Revolución
articleKey: RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: a63ebb08d982178e0e59f0b9f07c3c0dca53148b
source_lang: en
---
# Revolución

La revolución gira una ruta 2D alrededor de un eje para crear un sólido de revolución 3D. Así es como se crean jarrones, cuencos, ruedas y otros objetos con simetría de rotación.

<!--  Before and after showing a profile path being revolved into a vase shape -->
![20260506 102004 paste 20260506 102004](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-102004-paste-20260506-102004.jpg)


## Cómo se usa

1. Seleccione una ruta 2D
2. Aplique **Revolución** desde el menú de operaciones de Ruta
3. Ajuste el rango de rotación, la posición del eje y el número de lados

## Parámetros

- **Rotación** - Ángulo de rotación total de la revolución (predeterminado: 0, rango: 0-360). Establézcalo en 360 para una revolución completa.
- **Posición del eje** - Desplazamiento del eje de rotación respecto al centro de la ruta (predeterminado: 0, rango: -30 a 30). Un valor positivo aleja el eje de la ruta, creando una abertura más grande.
- **Ángulo inicial** - Dónde comienza la revolución (predeterminado: 0)
- **Ángulo final** - Dónde termina la revolución (predeterminado: 45). Establézcalo en 360 para una revolución completa.
- **Lados** - Número de segmentos a lo largo de la revolución (predeterminado: 30). Más = superficie más suave.

## Consejos

- Use la Posición del eje para controlar el diámetro interior de la forma revolucionada
- Establezca el Ángulo inicial y el Ángulo final en menos de 360 para crear revoluciones parciales (arcos, canalones)
- Dibuje una ruta de perfil con la forma de su jarrón o cuenco y luego revoluciónela para obtener una simetría perfecta
- Una [Ruta de círculo](../../2d-paths/circle-path.md) revolucionada crea un toro

## Relacionado

- [Extrusión lineal](linear-extrude.md) - Extruye en línea recta hacia arriba en lugar de revolucionar
- [Rutas 2D](../../2d-paths/index.md) - Cree rutas de perfil para revolucionar
- [Toro](../../primitives/torus.md) - Una forma de anillo revolucionada ya lista
