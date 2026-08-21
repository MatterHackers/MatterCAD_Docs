---
title: Expresiones
parent: "Workspace"
nav_order: 2
source_hash: 79a2f2c42d81f7fca56a87ad89f69e4303ed0ae5
source_lang: en
---
# Expresiones

Muchos parámetros de MatterCAD aceptan expresiones matemáticas en lugar de números simples. Esto permite el diseño paramétrico, en el que al cambiar un valor se actualizan automáticamente las cotas relacionadas.

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)


## Cómo se usa

En lugar de escribir un número simple en un campo de parámetro, puedes escribir una expresión matemática. Por ejemplo:

- `20 + 5` se evalúa como 25
- `pi * 10` se evalúa como 31,416
- `width * 2` hace referencia a otro parámetro llamado "width"

## Constantes disponibles

- **pi** - 3,14159... (la relación entre la circunferencia y el diámetro)
- **tau** - 6,28318... (2 * pi, una revolución completa en radianes)

## Operaciones admitidas

- Suma: `+`
- Resta: `-`
- Multiplicación: `*`
- División: `/`
- Paréntesis: `(` y `)` para agrupar

## Consejos

- Las expresiones se admiten en cualquier campo que muestre `DoubleOrExpression`, `IntOrExpression` o `StringOrExpression` en el código; en la práctica, la mayoría de los campos numéricos de las herramientas de diseño las aceptan
- Usa expresiones para crear relaciones entre parámetros; por ejemplo, define el diámetro de un agujero como `outer_diameter - 4` para que siempre tenga paredes de 2 mm
- Las expresiones se actualizan automáticamente cuando cambian los valores a los que hacen referencia
- Usa una [Hoja de variables](variable-sheet.md) cuando varios objetos deban compartir los mismos valores con nombre o las mismas fórmulas
- Puedes usar expresiones en operaciones de [Matriz](../operations/array/index.md) para crear patrones paramétricos

## Relacionado

- [Componentes](components.md) - Crear diseños parametrizados reutilizables
- [Hoja de variables](variable-sheet.md) - Almacena valores y fórmulas compartidos para un diseño
- [Editar objetos](../getting-started/editing-objects.md) - Trabajar con los parámetros de los objetos
