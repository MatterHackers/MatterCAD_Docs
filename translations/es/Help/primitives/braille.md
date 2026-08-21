---
title: Braille
articleKey: BrailleObject3D
parent: "Primitives"
nav_order: 2
source_hash: d1d9d4aeb9b87efbe32045f2a96cfea49048f95f
source_lang: en
---
# Braille

Genere texto en braille imprimible en 3D a partir de texto estándar en inglés. La herramienta Braille admite la codificación braille de Grado 1 (letra por letra) y de Grado 2 (contraída).

<!-- Screenshot of a Braille object showing raised dots on the workspace -->
![20260318 182800 paste 20260318 182800](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-182800-paste-20260318-182800.jpg)


## Cómo se usa

1. Agregue una primitiva **Braille** desde el panel Primitivas
2. Escriba su texto en el campo **Texto a codificar**
3. La herramienta lo convierte automáticamente al patrón de puntos braille correcto

## Parámetros

- **Texto a codificar**: el texto en inglés que se convertirá a braille
- **Escalar**: ajusta el tamaño general del resultado en braille
- **Altura**: la altura de los puntos braille en relieve

## Consejos

- El braille de Grado 2 utiliza contracciones y abreviaturas para palabras y combinaciones de letras comunes, lo que lo hace más compacto
- Se emplean las dimensiones estándar de la celda braille para garantizar que el resultado sea legible
- Combine con una base plana de [Cubo](cube.md) para crear una etiqueta o un letrero braille completo
- Para tarjetas braille con una base integrada, consulte [Tarjeta braille](braille-card.md)

## Relacionado

- [Tarjeta braille](braille-card.md): braille con una base de tarjeta integrada
- [Texto](text.md): texto 3D estándar
