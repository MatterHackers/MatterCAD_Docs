---
title: Objeto de imagen
articleKey: ImageObject3D
parent: "Primitives"
nav_order: 10
source_hash: 4c4cedd6b49be2fc75d0c9cd1d8d30fae679a74b
source_lang: en
---
# Objeto de imagen

Importa una imagen y conviértela en un objeto 3D en relieve donde los valores de brillo determinan la altura de cada píxel. Esto te permite convertir fotografías, logotipos y obras de arte en objetos imprimibles en 3D.

<!-- Screenshot showing an image converted to a 3D relief on the workspace -->
![20260318 183708 paste 20260318 183708](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183708-paste-20260318-183708.jpg)


## Cómo se usa

1. Agrega un **Convertidor de imágenes** desde el panel Primitivas, o arrastra un archivo de imagen directamente al espacio de trabajo
2. Selecciona o cambia la imagen mediante las propiedades
3. Ajusta la altura para controlar cuánto se elevan las zonas claras

## Parámetros

- **Altura** - Qué tan altas son las partes elevadas de la imagen
- La vista previa de la imagen se muestra en el panel Propiedades

## Consejos

- Las imágenes de alto contraste con formas nítidas dan los mejores resultados
- Puedes arrastrar imágenes directamente desde tu escritorio al espacio de trabajo de MatterCAD
- Usa las herramientas del menú adicional en una imagen importada para obtener más opciones de conversión
- Para obtener contornos basados en rutas a partir de imágenes, consulta [Imagen a trazado](../operations/image/image-to-path.md)
- Para visualizaciones de imágenes retroiluminadas, consulta [Litofanía](../operations/image/lithophane.md)
- Agrega una base combinando el objeto de imagen con un [Cubo](cube.md)

## Relacionado

- [Imagen a trazado](../operations/image/image-to-path.md) - Traza los contornos de una imagen como rutas 2D
- [Litofanía](../operations/image/lithophane.md) - Crea imágenes que aparecen al retroiluminarse
- [Objeto SVG](svg-object.md) - Importa gráficos vectoriales
