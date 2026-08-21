---
title: Anillo
articleKey: RingObject3D
parent: "Primitives"
nav_order: 13
source_hash: fd16c400f3d8c8af13416ab57ddd8407e761d93a
source_lang: en
---
# Anillo

Un cilindro hueco (tubo) con diámetros interior y exterior independientes y una altura especificada. También conocido como forma de tubería o tubo.

<!--  Screenshot of a Ring primitive on the workspace -->
![20260318 183848 paste 20260318 183848](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183848-paste-20260318-183848.jpg)


## Parámetros

- **Diámetro exterior** - El ancho exterior del anillo (predeterminado: 20mm)
- **Diámetro interior** - El diámetro del centro hueco (predeterminado: 15mm)
- **Altura** - La altura del anillo (predeterminado: 5mm)
- **Lados** - Número de segmentos alrededor del perímetro (predeterminado: 40)

### Parámetros avanzados

Activa el modo **Avanzado** para acceder a controles adicionales:

- **Ángulo inicial** - Ángulo donde comienza el anillo (predeterminado: 0)
- **Ángulo final** - Ángulo donde termina el anillo (predeterminado: 360). Usa un valor menor que 360 para obtener un anillo parcial
- **Redondear** - Agrega redondeo a los bordes (Ninguno, Arriba o Abajo)
- **Dirección** - Redondea hacia el borde interior o exterior (visible cuando Redondear está activado)
- **Segmentos de redondeo** - Suavidad del redondeo (visible cuando Redondear está activado)

## Consejos

- El espesor de pared equivale a (Diámetro exterior - Diámetro interior) / 2
- Usa esta forma para arandelas, separadores, casquillos y elementos tubulares
- Define una altura grande para tuberías o pequeña para arandelas planas
- Usa el Ángulo inicial y el Ángulo final para formas de anillo parcial, como clips en C

## Relacionado

- [Torus](torus.md) - Un anillo con forma de dona y sección transversal redonda
- [Cilindro](cylinder.md) - Una columna redonda sólida (sin centro hueco)
