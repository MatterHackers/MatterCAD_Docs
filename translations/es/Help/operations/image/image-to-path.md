---
title: Imagen a trazado
articleKey: ImageToPathObject3D_2
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 0145587f635ede68bfc1df37b4f0d366a03d3a6c
source_lang: en
---
# Imagen a trazado

Imagen a trazado traza los contornos de una imagen para crear rutas 2D. Estas rutas se pueden extruir, revolucionar o utilizar con cualquier otra operación de ruta. Es ideal para convertir logotipos, siluetas y gráficos sencillos en objetos 3D.

![20260324 075521 paste 20260324 075521](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-075521-paste-20260324-075521.jpg)


## Cómo se usa

1. Selecciona un objeto de imagen en tu espacio de trabajo
2. Aplica **Imagen a trazado** desde el menú de operaciones de Imagen
3. Elige el tipo de análisis y ajusta el intervalo de selección

## Parámetros

- **Tipo de análisis** - Cómo se analiza la imagen para el trazado:
  - **Transparencia** - Traza según las áreas transparentes frente a las opacas (ideal para PNG con fondos transparentes)
  - **Colores** - Traza según regiones de color
  - **Intensidad** - Traza según los niveles de brillo (ideal para la mayoría de las imágenes)
- **Seleccionar intervalo** - Un control de histograma para seleccionar qué valores de brillo/color se incluyen en el trazado
- **Área de superficie mín.** - Área mínima para que un bucle de ruta se incluya. Auméntala para filtrar pequeños artefactos de ruido

## Consejos

- Las imágenes limpias, de alto contraste y con formas sencillas dan los mejores resultados
- Usa el modo Transparencia para imágenes PNG con fondos transparentes
- Usa el modo Intensidad para fotografías e imágenes sin transparencia
- Después de trazar, aplica [Extrusión lineal](../path/linear-extrude.md) para dar altura a la ruta
- Aumenta el Área de superficie mín. para quitar del trazado pequeños detalles no deseados

## Relacionado

- [Convertidor de imágenes](image-converter.md) - Crea un relieve por mapa de alturas en lugar de rutas planas
- [Litofanía](lithophane.md) - Crea imágenes retroiluminadas
- [Objeto SVG](../../primitives/svg-object.md) - Importa gráficos vectoriales directamente (sin necesidad de trazar)
- [Extrusión lineal](../path/linear-extrude.md) - Da altura a la ruta trazada
