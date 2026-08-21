---
title: Hoja de variables
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
source_hash: 3137a4da2b9d2086d4dcace156435caca288dd79
source_lang: en
---
# Hoja de variables

La Hoja de variables almacena valores compartidos para un diseño. Úsala cuando varios objetos deban hacer referencia a las mismas dimensiones, cantidades, etiquetas o fórmulas. Al cambiar un valor de la hoja se recalculan los objetos dependientes, de modo que los diseños paramétricos se mantienen coherentes sin tener que editar cada objeto uno por uno.

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## Cómo agregar una Hoja de variables

1. Abre la biblioteca y agrega **Hoja de variables** a la escena.
2. Selecciona el objeto Hoja de variables para mostrar el editor de la hoja.
3. Selecciona una celda y luego introduce un **Nombre** y un valor o una fórmula.
4. Usa el nombre de la celda desde otros campos del diseño que admitan expresiones.

## Edición de celdas

Cada celda tiene dos partes editables:

- **Nombre** - Un nombre de variable opcional para la celda. Los nombres no distinguen mayúsculas de minúsculas, los espacios se convierten en guiones bajos y los nombres duplicados se ajustan automáticamente.
- **Expresión** - El valor de la celda. El texto simple o los números se almacenan directamente. Las fórmulas comienzan con `=`.

También se puede hacer referencia a las celdas por su dirección, como `A1` o `B2`. Las celdas con nombre suelen ser más claras para los parámetros de diseño porque describen la intención, como `wall_thickness`, `outer_diameter` o `hole_count`.

## Fórmulas

Comienza una fórmula con `=` para evaluarla en la hoja:

- `=20 + 5` devuelve `25`
- `=pi * 10` devuelve `31.41592653589793`
- `=A1 * 2` hace referencia a otra celda por su dirección
- `=wall_thickness + 4` hace referencia a una celda con nombre

La hoja admite aritmética, paréntesis, operadores de comparación, funciones `Math` habituales como `sin`, `cos`, `sqrt` y `round`, y constantes como `pi`, `tau` y `e`.

## Uso de los valores de la hoja en objetos

La mayoría de los campos numéricos de MatterCAD admiten expresiones. Para usar un valor de la hoja en un parámetro de objeto, antepón `=` a la referencia:

- Establece la **Anchura** de un Cubo en `=case_width`.
- Establece la **Cantidad** de una Matriz en `=hole_count`.
- Establece un valor de **Desplazamiento** de Trasladar en `=wall_thickness * 2`.

Cuando la hoja cambia, MatterCAD recalcula los objetos que dependen de ella.

## Texto y funciones auxiliares

Las celdas de la Hoja de variables pueden contener texto además de números. Los valores de texto son útiles para etiquetas generadas, números de pieza, datos importados y aplicaciones de diseño personalizadas.

Entre las funciones auxiliares útiles se incluyen:

- `concat()` o `strcat()` - Une textos o valores.
- `substring()` - Extrae parte de un valor de texto.
- `split()` - Divide un texto y devuelve un elemento.
- `count()` - Cuenta los elementos delimitados de un texto.
- `substitute()` - Reemplaza texto.
- `rand(seed)` - Genera un valor aleatorio determinista cuando se proporciona una semilla.
- `importdata()` - Lee un valor desde una URL o una ruta de archivo local.

## Consejos

- Prefiere nombres descriptivos en lugar de direcciones de celda para los valores que usen otros objetos.
- Mantén las dimensiones principales cerca de la parte superior izquierda de la hoja para encontrarlas fácilmente.
- Usa fórmulas para los valores derivados, como `inner_diameter = outer_diameter - wall_thickness * 2`.
- Evita usar palabras reservadas como `pi`, `e`, `true`, `false` o nombres de funciones como nombres de celda.
- Si una fórmula no se puede analizar, MatterCAD conserva la entrada original como texto.

## Relacionado

- [Expresiones](expressions.md) - Usa expresiones en los parámetros de los objetos
- [Componentes](components.md) - Crea diseños parametrizados reutilizables
- [Matriz](../operations/array/array.md) - Crea patrones repetidos controlados por valores de la hoja
