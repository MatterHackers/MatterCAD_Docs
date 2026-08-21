---
title: Texto
articleKey: TextObject3D_2
parent: "Primitives"
nav_order: 16
source_hash: 526f3190c7b2150243499b5874ac455d74810bb2
source_lang: en
---
# Texto

Crea texto 3D extruido con contenido, fuente, tamaño y altura personalizables. Los objetos de texto son ideales para etiquetas, letreros, placas de nombre y letras decorativas.

<!--  Screenshot of a 3D Text object on the workspace showing extruded letters -->
![20260318 184207 paste 20260318 184207](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184207-paste-20260318-184207.jpg)


## Cómo usarlo

1. Agrega una primitiva de **Texto** desde el panel Primitivas
2. Escribe tu texto en el campo **Nombre** del panel Propiedades
3. Ajusta la fuente, el tamaño y la altura de extrusión según sea necesario

## Parámetros

- **Nombre** - El contenido de texto que se mostrará
- **Tamaño del punto** - El tamaño de la fuente. Es preciso en relación con el tamaño de impresión estándar: un tamaño de 12 puntos en MatterCAD coincide con una letra de 12 puntos en una impresora 2D
- **Altura** - La altura de extrusión (cuánto sobresale el texto de la superficie)
- **Fuente** - Selecciona entre las fuentes disponibles del sistema

## Consejos

- Usa [Restar](../operations/boolean/subtract.md) para grabar el texto en una superficie en lugar de que sobresalga
- Para textos muy pequeños, aumenta el Tamaño del punto y luego [Escalar](../operations/transform/scale.md) el objeto completo a un tamaño menor para obtener mejor detalle
- Cada letra del texto es una trayectoria independiente que se extruye en conjunto

## Relacionado

- [Braille](braille.md) - Genera texto en Braille imprimible en 3D
- [Código QR](qr-code.md) - Genera un código QR como objeto 3D
- [Objeto de imagen](image-object.md) - Convierte imágenes a 3D
