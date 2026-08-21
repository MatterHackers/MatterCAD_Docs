---
title: Restar y reemplazar
articleKey: SubtractAndReplaceObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c1698bab75faca8046b23cc148803c8063ba0678
source_lang: en
---
# Restar y reemplazar

Restar y reemplazar sustrae las piezas que elijas de las piezas que no elegiste, pero conserva el trozo recortado como una pieza propia en lugar de descartarlo. Usa **Pieza(s) a sustraer** para elegir las formas de corte; todo lo demás es la base que se recorta.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->
![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)

[Combinar](combine.md), [Restar](subtract.md), [Intersecar](intersect.md) y Restar y reemplazar se realizan mediante un único objeto booleano: el botón de la barra de herramientas lo crea con Restar y reemplazar ya seleccionado, y puedes cambiar a cualquiera de las otras tres en cualquier momento desde la fila de iconos **Operación** situada en la parte superior del panel Propiedades.

Restar y reemplazar no está disponible para trayectorias 2D: una región no tiene volumen eliminado que devolver.

## Cómo se usa

1. Selecciona dos o más objetos
2. Haz clic en **Restar y reemplazar** en la barra de herramientas
3. Usa **Pieza(s) a sustraer** para elegir qué hijos son las formas de corte
4. Cambia de idea en cualquier momento haciendo clic en un icono distinto de la fila **Operación**, en la parte superior del panel Propiedades: la forma se reconstruye con la nueva operación

## Parámetros

- **Operación** - Qué booleano se realiza. Se muestra como una fila de iconos en la parte superior del panel
- **Pieza(s) a sustraer** - Qué hijos son las formas de corte
- **Mantener geometría invertida** - Trata un cascarón invertido como material sólido en lugar de dejar que anule el volumen que lo rodea. Activa esta opción cuando un modelo que debería ser sólido aparece con partes faltantes. Fuerza el uso del motor booleano exacto, que es más lento
- **Reparar orden de bobinado** - Reorienta los cascarones invertidos de cada pieza antes de ejecutar el booleano. Esto corrige la geometría una sola vez en lugar de cambiar lo que cada operación posterior considera sólido, y suele ser la mejor de las dos soluciones para un modelo invertido

## Consejos

- Las dos piezas encajan exactamente, porque proceden de la misma operación
- Úsalo para diseños multicolor, ensamblajes entrelazados e incrustaciones
- Si un resultado se ve mal, comprueba que los objetos de origen sean estancos. **Reparar orden de bobinado** corrige los cascarones invertidos; [Reparar](../mesh/repair.md) corrige daños más generales en modelos importados

## Relacionado

- [Combinar](combine.md) - Combinar varios objetos en una única forma sólida
- [Restar](subtract.md) - Recortar una forma de otra
- [Intersecar](intersect.md) - Conservar solo el volumen donde los objetos se solapan
- [Corte por plano](../reshape/plane-cut.md) - Cortar con un plano plano en lugar de con otra forma
- [Reparar](../mesh/repair.md) - Corregir mallas importadas dañadas antes de un booleano

Esta página también cubre los antiguos objetos Restar y reemplazar que todavía aparecen en diseños guardados antes de que las operaciones se unificaran. Siguen funcionando exactamente igual que antes; los diseños nuevos utilizan el objeto booleano compartido con la operación Restar y reemplazar seleccionada.
