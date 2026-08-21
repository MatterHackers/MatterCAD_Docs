---
title: Intersecar
articleKey: IntersectionObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b997cfc4f6d2f02559346365311f217388a6a2da
source_lang: en
---
# Intersecar

Intersecar conserva únicamente el volumen que comparten todos los objetos y descarta el resto.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->
![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)

[Combinar](combine.md), [Restar](subtract.md), Intersecar y [Restar y Reemplazar](subtract-and-replace.md) se realizan mediante un mismo objeto booleano: el botón de la barra de herramientas lo crea con Intersecar ya seleccionado, y puede cambiar a cualquiera de las otras tres en cualquier momento desde la fila de iconos **Operación** situada en la parte superior del panel Propiedades.

Intersecar funciona con sólidos y con trayectorias 2D. Analiza lo que se le proporciona y realiza el tipo de operación adecuado, de modo que intersecar dos trayectorias produce una trayectoria e intersecar dos mallas produce un sólido.

## Cómo se usa

1. Seleccione dos o más objetos
2. Haga clic en **Intersecar** en la barra de herramientas
3. Cambie de idea en cualquier momento haciendo clic en un icono distinto de la fila **Operación** situada en la parte superior del panel Propiedades: la forma se reconstruye con la nueva operación

## Parámetros

- **Operación** - Qué operación booleana se realiza. Se muestra como una fila de iconos en la parte superior del panel
- **Mantener geometría invertida** - Trata un caparazón invertido como material sólido en lugar de dejar que anule el volumen que lo rodea. Active esta opción cuando un modelo que debería ser sólido aparezca con partes ausentes. Fuerza el uso del motor booleano exacto, que es más lento
- **Reparar orden de bobinado** - Corrige el bobinado de los caparazones invertidos de cada pieza antes de ejecutar la operación booleana. Esto repara la geometría una sola vez en lugar de cambiar lo que cada operación posterior considera sólido, y suele ser la mejor de las dos soluciones para un modelo invertido

## Consejos

- Los objetos deben solaparse. Si en realidad no se solapan, el resultado está vacío
- Con más de dos objetos, se procesa la lista en orden: se intersecan los dos primeros, luego ese resultado se interseca con el tercero, y así sucesivamente
- Si un resultado parece incorrecto, compruebe que los objetos de origen sean estancos. **Reparar orden de bobinado** corrige los caparazones invertidos; [Reparar](../mesh/repair.md) corrige daños más amplios en modelos importados

## Relacionado

- [Combinar](combine.md) - Combina varios objetos en una única forma sólida
- [Restar](subtract.md) - Corta una forma de otra
- [Restar y Reemplazar](subtract-and-replace.md) - Resta una forma y conserva la pieza que se ha recortado
- [Corte por plano](../reshape/plane-cut.md) - Corta con un plano en lugar de con otra forma
- [Reparar](../mesh/repair.md) - Repara mallas importadas dañadas antes de una operación booleana

Esta página también cubre los antiguos objetos de Intersección que todavía se encuentran en diseños guardados antes de que se unificaran las operaciones. Siguen funcionando exactamente igual que antes; los diseños nuevos utilizan el objeto booleano común con la operación Intersecar seleccionada.
