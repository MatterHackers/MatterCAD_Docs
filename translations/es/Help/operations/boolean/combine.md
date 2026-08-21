---
title: Combinar
articleKey: CombineObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: a3066faa634b5a88a2fe1650a4e2ac278ac50e24
source_lang: en
---
# Combinar

Combinar fusiona todo en un único sólido. Las caras internas donde las formas se superponían se eliminan, de modo que el resultado es una malla continua en lugar de carcasas superpuestas.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->
![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)

Combinar, [Restar](subtract.md), [Intersecar](intersect.md) y [Restar y reemplazar](subtract-and-replace.md) los realiza todos un mismo objeto booleano: el botón de la barra de herramientas lo crea con Combinar ya seleccionado, y puedes cambiar a cualquiera de las otras tres en cualquier momento desde la fila de iconos **Operación** situada en la parte superior del panel Propiedades.

Combinar funciona con sólidos y con trayectorias 2D. Analiza lo que le has dado y realiza el tipo de operación adecuado, de modo que combinar dos trayectorias produce una trayectoria y combinar dos mallas produce un sólido.

## Cómo se usa

1. Selecciona dos o más objetos
2. Haz clic en **Combinar** en la barra de herramientas
3. Cambia de opinión en cualquier momento haciendo clic en un icono distinto de la fila **Operación** situada en la parte superior del panel Propiedades: la forma se reconstruye con la nueva operación

## Parámetros

- **Operación** - Qué operación booleana realizar. Se muestra como una fila de iconos en la parte superior del panel
- **Mantener geometría invertida** - Trata una carcasa invertida como material sólido en lugar de dejar que anule el volumen que la rodea. Activa esta opción cuando un modelo que debería ser sólido aparece con partes que faltan. Fuerza el uso del motor booleano exacto, más lento
- **Reparar orden de bobinado** - Reorienta las carcasas invertidas de cada pieza antes de ejecutar la operación booleana. Esto corrige la geometría de una vez en lugar de cambiar lo que cada operación posterior considera sólido, y suele ser la mejor de las dos respuestas ante un modelo invertido

## Consejos

- Combinar también unirá objetos que no se superponen en una sola malla, pero seguirán viéndose separados
- Combinar gestiona por ti los objetos Agujero: todo lo marcado como agujero se resta del resultado en lugar de sumarse
- Combinar conserva los colores por cara de los objetos originales
- Si un resultado se ve mal, comprueba que los objetos de origen sean estancos. **Reparar orden de bobinado** corrige las carcasas invertidas; [Reparar](../mesh/repair.md) corrige daños más amplios en modelos importados

## Relacionado

- [Restar](subtract.md) - Corta una forma de otra
- [Intersecar](intersect.md) - Conserva solo el volumen donde los objetos se superponen
- [Restar y reemplazar](subtract-and-replace.md) - Resta una forma y conserva la pieza que se ha recortado
- [Corte por plano](../reshape/plane-cut.md) - Corta con un plano en lugar de con otra forma
- [Agujero](../../primitives/hole.md) - Un cubo preconfigurado para restarse
- [Reparar](../mesh/repair.md) - Corrige mallas importadas dañadas antes de una operación booleana

Esta página cubre también los antiguos objetos Combinar que todavía se encuentran en diseños guardados antes de que se unificaran las operaciones. Siguen funcionando exactamente igual; los diseños nuevos usan el objeto booleano compartido con la operación Combinar seleccionada.
