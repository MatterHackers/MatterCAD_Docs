---
title: Torus
articleKey: TorusObject3D
parent: "Primitives"
nav_order: 17
source_hash: aaec1652de4d6713bd01a707964cf4985d3fb5f6
source_lang: en
---
# Torus

Un anillo con forma de rosquilla que permite controlar de forma independiente el tamaño general y el grosor de la sección transversal del anillo.

<!--  Screenshot of a Torus primitive on the workspace -->
![20260318 184240 paste 20260318 184240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184240-paste-20260318-184240.jpg)


## Parámetros

- **Diámetro exterior** - El ancho total del toro (predeterminado: 20mm)
- **Diámetro interior** - El diámetro del orificio central (predeterminado: 10mm)
- **Lados** - Número de segmentos alrededor del anillo principal (predeterminado: 40)

### Parámetros avanzados

Activa el modo **Avanzado** para acceder a controles adicionales:

- **Ángulo inicial** - Ángulo donde comienza el toro (predeterminado: 0)
- **Ángulo final** - Ángulo donde termina el toro (predeterminado: 360). Usa un valor menor que 360 para obtener un anillo abierto o un arco
- **Lados del anillo** - Número de segmentos alrededor de la sección transversal del anillo (predeterminado: 15). Más = perfil del tubo más suave
- **Ángulo de fase del anillo** - Rota el perfil de la sección transversal (predeterminado: 0)

## Consejos

- El grosor del tubo del anillo se determina por la diferencia entre el Diámetro exterior y el Diámetro interior
- Usa el Ángulo inicial y el Ángulo final para crear segmentos de anillo abiertos, arcos o formas de C
- Útil para crear juntas tóricas, asas, anillos decorativos y curvas de tubería

## Relacionado

- [Anillo](ring.md) - Un cilindro hueco de paredes rectas (tubo)
- [Esfera](sphere.md) - Una bola sólida
- [Media esfera](half-sphere.md) - Una forma de cúpula
