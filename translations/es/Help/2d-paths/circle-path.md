---
title: Ruta de círculo
articleKey: CirclePathObject3D
parent: "2D Paths"
nav_order: 2
source_hash: 587edab627246f47731f9dbde2a13a00dd464807
source_lang: en
---
# Ruta de círculo

Una ruta 2D circular. Úsala con [Extrusión lineal](../operations/path/linear-extrude.md) para crear cilindros, o con [Revolución](../operations/path/revolve.md) para crear formas similares a un toroide.

<!-- Screenshot of a Circle Path on the workspace -->
![20260506 080110 paste 20260506 080110](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080110-paste-20260506-080110.jpg)


## Parámetros

- **Diámetro** - El diámetro del círculo (predeterminado: 20mm)
- **Segmentos** - Número de segmentos de línea que forman el círculo. Más = más suave

## Consejos

- Una Ruta de círculo combinada con Extrusión lineal produce un cilindro, similar a la primitiva [Cilindro](../primitives/cylinder.md) pero con más flexibilidad para construir a partir de ella
- Úsala como base para Revolución y crear formas de anillo

## Relacionado

- [Ruta de caja](box-path.md) - Una ruta 2D rectangular
- [Ruta de anillo](ring-path.md) - Un círculo con un agujero
- [Extrusión lineal](../operations/path/linear-extrude.md) - Da altura a las rutas
