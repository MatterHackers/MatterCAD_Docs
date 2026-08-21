---
title: Cubo
articleKey: CubeObject3D
parent: "Primitives"
nav_order: 4
source_hash: a376a9c78d88d995f3c6ce21dd5098672d6c1dfb
source_lang: en
---
# Cubo

Una forma de caja rectangular con anchura, profundidad y altura ajustables, además de bordes redondeados opcionales. El Cubo es una de las primitivas más utilizadas para construir diseños.

<!--  Screenshot of a Cube primitive on the workspace -->
![20260318 183230 paste 20260318 183230](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183230-paste-20260318-183230.jpg)


## Parámetros

- **Anchura** - Tamaño a lo largo del eje X (predeterminado: 20mm)
- **Profundidad** - Tamaño a lo largo del eje Y (predeterminado: 20mm)
- **Altura** - Tamaño a lo largo del eje Z (predeterminado: 20mm)
- **Redondear** - Activa los bordes redondeados
- **Radio** - Tamaño del redondeo (visible cuando Redondear está activado)
- **Segmentos de redondeo** - Suavidad del redondeo; más segmentos = curvas más suaves (visible cuando Redondear está activado)

## Consejos

- Usa un Cubo como punto de partida para cajas, placas, soportes y carcasas
- Activa Redondear para obtener bordes suaves y de aspecto profesional
- El Radio no puede superar la mitad de la dimensión más pequeña
- Combina un Cubo con [Restar](../operations/boolean/subtract.md) para crear recortes y ranuras rectangulares

## Relacionado

- [Cilindro](cylinder.md) - Forma de columna redonda
- [Pirámide](pyramid.md) - Forma de cuatro caras que se estrecha
- [Agujero](hole.md) - Un cubo preconfigurado para la sustracción booleana
