---
title: Restar
articleKey: SubtractObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 59685bd0a635b70d7f938780f71e90be595dd993
source_lang: en
---
# Restar

Restar recorta las piezas que elijas de las piezas que no elegiste. Usa **Pieza(s) a sustraer** para elegir las formas de corte; todo lo demás es la base que se corta.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->
![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)

[Combinar](combine.md), Restar, [Intersecar](intersect.md) y [Restar y reemplazar](subtract-and-replace.md) se realizan mediante un único objeto booleano: el botón de la barra de herramientas lo crea con Restar ya seleccionado, y puedes cambiar a cualquiera de las otras tres en cualquier momento desde la fila de iconos **Operación** situada en la parte superior del panel Propiedades.

Restar funciona con sólidos y con trazados 2D. Analiza lo que le has dado y realiza el tipo de operación adecuado, de modo que restar un trazado de otro produce un trazado y restar una malla de otra produce un sólido.

## Cómo se usa

1. Selecciona dos o más objetos
2. Haz clic en **Restar** en la barra de herramientas: se elige por ti una pieza de corte predeterminada para que haga algo de inmediato
3. Usa **Pieza(s) a sustraer** para elegir qué hijos son las formas de corte
4. Cambia de opinión en cualquier momento haciendo clic en un icono distinto de la fila **Operación** situada en la parte superior del panel Propiedades: la forma se reconstruye con la nueva operación

## Parámetros

- **Operación** - Qué booleana realizar. Se muestra como una fila de iconos en la parte superior del panel
- **Pieza(s) a sustraer** - Qué hijos son las formas de corte
- **Mantener piezas sustraídas** - Deja en la escena las piezas que se recortaron en lugar de descartarlas
- **Mantener geometría invertida** - Trata un caparazón invertido como material sólido en vez de dejar que anule el volumen que lo rodea. Activa esta opción cuando un modelo que debería ser sólido aparezca con partes que faltan. Fuerza el motor booleano exacto, que es más lento
- **Reparar orden de bobinado** - Reorienta los caparazones invertidos de cada pieza antes de ejecutar la booleana. Esto corrige la geometría una sola vez en lugar de cambiar lo que cada operación posterior considera sólido, y suele ser la mejor de las dos soluciones para un modelo invertido

## Consejos

- Los objetos deben solaparse para que Restar haga algo
- Para hacer un agujero pasante, asegúrate de que el objeto de corte atraviese completamente la base
- Para un agujero sencillo, la primitiva [Agujero](../../primitives/hole.md) ya está configurada para restar
- Los objetos de corte permanecen en el árbol de diseño, así que puedes moverlos o cambiar su tamaño y el corte se actualiza
- Si un resultado parece incorrecto, comprueba que los objetos de origen sean estancos. **Reparar orden de bobinado** corrige los caparazones invertidos; [Reparar](../mesh/repair.md) corrige daños más amplios en modelos importados

## Relacionado

- [Combinar](combine.md) - Combina varios objetos en una única forma sólida
- [Intersecar](intersect.md) - Conserva solo el volumen donde los objetos se solapan
- [Restar y reemplazar](subtract-and-replace.md) - Resta una forma y conserva la pieza que se recortó
- [Corte por plano](../reshape/plane-cut.md) - Corta con un plano en lugar de con otra forma
- [Agujero](../../primitives/hole.md) - Un cubo preconfigurado para restar
- [Reparar](../mesh/repair.md) - Corrige mallas importadas dañadas antes de una booleana

Esta página también cubre los antiguos objetos Restar que aún se encuentran en diseños guardados antes de que se unificaran las operaciones. Siguen funcionando exactamente igual que antes; los diseños nuevos usan el objeto booleano compartido con la operación Restar seleccionada.
