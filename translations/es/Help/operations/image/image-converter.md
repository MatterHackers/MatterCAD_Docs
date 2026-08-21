---
title: Convertidor de imágenes
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c1a05f9688ebe115babfad5d63fc49445af7c449
source_lang: en
---
# Convertidor de imágenes

El Convertidor de imágenes transforma una imagen ráster en un relieve 3D donde el brillo de los píxeles determina la altura. Las zonas claras se elevan y las zonas oscuras quedan bajas (o al revés).

![20260323 210414 paste 20260323 210414](https://matterhackers.github.io/MatterCAD_Docs/assets/20260323-210414-paste-20260323-210414.jpg)


## Cómo usarlo

1. Agregue un Convertidor de imágenes desde el panel Primitivas, o arrastre un archivo de imagen al espacio de trabajo
2. La imagen se convierte en un mapa de alturas 3D
3. Ajuste la altura y los demás parámetros

## Consejos

- Las imágenes de alto contraste con formas definidas producen los mejores resultados
- Para trazar los contornos de una imagen como rutas planas en lugar de mapas de alturas, use [Imagen a trazado](image-to-path.md)
- Para crear visualizaciones de imágenes retroiluminadas, use [Litofanía](lithophane.md)
- Puede arrastrar imágenes directamente desde su escritorio al espacio de trabajo
- Agregue una base combinando el relieve de la imagen con un [Cubo](../../primitives/cube.md)

## Relacionado

- [Imagen a trazado](image-to-path.md) - Trazar contornos en lugar de crear un mapa de alturas
- [Litofanía](lithophane.md) - Crear visualizaciones de imágenes retroiluminadas
- [Objeto de imagen](../../primitives/image-object.md) - La versión primitiva de la importación de imágenes
