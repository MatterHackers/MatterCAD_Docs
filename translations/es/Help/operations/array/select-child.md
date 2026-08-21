---
title: Seleccionar hijo
articleKey: SelectChildObject3D
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: f6f71d2b457b82126f272ea9354f877c36570df0
source_lang: en
---
# Seleccionar hijo

Seleccionar hijo elige un hijo de un grupo de objetos según un número de índice o un nombre. Esto resulta especialmente útil en diseños con scripts y paramétricos en los que quieres elegir dinámicamente qué objeto se muestra.

<!-- IMAGE: Screenshot showing Select Child operation with multiple children and one selected by index -->
![20260506 080526 paste 20260506 080526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080526-paste-20260506-080526.jpg)


## Cómo se usa

1. Selecciona dos o más objetos
2. Aplica la operación **Seleccionar hijo** desde el menú Duplicación
3. Elige **Por índice** o **Por nombre** para controlar cómo se selecciona el hijo
4. Establece el número de índice o el nombre que debe coincidir

## Parámetros

- **Método de selección** - Elige entre **Por índice** (seleccionar por posición) o **Por nombre** (seleccionar por el nombre del objeto). Se muestra como botones.
- **Índice secundario** - El índice de base cero del hijo que se va a seleccionar (se muestra al usar Por índice). Admite [expresiones](../../workspace/expressions.md).
- **Nombre secundario** - El nombre del hijo que se va a seleccionar (se muestra al usar Por nombre). Admite [expresiones](../../workspace/expressions.md).

Si el índice está fuera de rango o el nombre no coincide con ningún hijo, se devuelve el primer hijo como alternativa. Si no hay hijos, no se devuelve nada.

## Uso en scripts

Seleccionar hijo está pensado para funcionar con expresiones y la función `rand()` para crear diseños dinámicos y basados en datos. Por ejemplo, puedes construir una escena con varios objetos variantes como hijos y usar una expresión como `rand(42)` como semilla del índice para elegir uno al azar.

**Ejemplo: atrezo de libros aleatorios para un espectáculo teatral**

1. Importa 5 mallas de libros diferentes como hijos de una operación Seleccionar hijo
2. Establece el Método de selección en **Por índice**
3. Usa una expresión para el Índice secundario, como `floor(rand(seed) * 5)`, donde `seed` es una variable de hoja
4. Duplica la operación Seleccionar hijo varias veces, cada una con un valor de semilla distinto
5. Cada instancia elige al azar un libro diferente del conjunto

Este patrón sirve para cualquier situación en la que necesites elegir dentro de un conjunto de variantes: muebles, decoración, elementos arquitectónicos o cualquier colección de piezas intercambiables.

## Consejos

- Combínalo con [Matriz](array.md) para crear patrones variados en los que cada copia seleccione un hijo diferente
- Usa variables de hoja para el índice o el nombre y controlar la selección desde una hoja de cálculo
- El comportamiento de recurrir al primer hijo hace que tu diseño nunca se rompa aunque el índice o el nombre sean incorrectos

## Relacionado

- [Matriz](array.md) - Duplica objetos en patrones lineales, radiales, sobre curva y de transformación
