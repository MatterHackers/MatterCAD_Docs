---
title: Engranajes
articleKey: GearObject3D
parent: "Mechanical Parts"
nav_order: 2
source_hash: 23098f94da8cd032e0617fbf346621504446347f
source_lang: en
---
# Engranajes

Cree engranajes 3D con una geometría de dientes totalmente configurable. MatterCAD genera perfiles de engranaje de evolvente correctos que engranan adecuadamente con otros engranajes del mismo módulo y ángulo de presión.

<!-- AUTO_IMAGE: type=from_thumbnail item=gear file=mechanical_gears -->
![mechanical_gears](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_gears.png)

## Cómo se usa

1. Agregue un **Engranaje** desde las herramientas de Mecánico o el panel Primitivas
2. Establezca el número de dientes y los demás parámetros
3. El perfil del engranaje se genera automáticamente

## Parámetros

### Características

- **Tipo de engranaje** - Engranaje Externo o Cremallera (barra recta con dientes)
- **Altura** - Espesor del engranaje (altura de extrusión)
- **Número de dientes** - Cantidad de dientes alrededor del engranaje (predeterminado: 30, rango: 4-60)
- **Paso circular** - La distancia de arco entre dientes a lo largo de la circunferencia primitiva (rango: 3-30). Determina el tamaño general.
- **Diámetro del agujero central** - Diámetro del agujero central del eje (predeterminado: 4mm, establezca 0 para no tener agujero). Solo para engranajes externos.
- **Ancho del borde exterior** - Anchura del borde situado fuera de los dientes interiores
- **Número de dientes del engranaje interior** - Número de dientes del engranaje interno acoplado

### Avanzado

- **Ángulo de presión** - El ángulo de la superficie de contacto del diente (valores habituales: 14,5, 20 o 25 grados). Todos los engranajes que engranan entre sí deben usar el mismo ángulo de presión.
- **Holgura** - Separación mínima entre la punta del diente y el fondo del diente acoplado
- **Holgura** - Separación mínima entre los dientes de los engranajes acoplados para evitar agarrotamientos

### Datos del engranaje (solo lectura)

- **Radio primitivo** - El radio en el que los engranajes engranan entre sí
- **Diámetro exterior** - El diámetro total hasta la punta de los dientes

## Consejos

- Dos engranajes engranarán correctamente cuando tengan el mismo Paso circular y el mismo Ángulo de presión
- Utilice los valores de Radio primitivo para espaciar correctamente los engranajes acoplados: la distancia entre los centros de los engranajes debe ser igual a la suma de sus radios primitivos
- Agregue Holgura en los engranajes impresos en 3D para tener en cuenta las tolerancias de impresión
- Para perfiles de engranaje 2D (para usar con Extruir), consulte [Engranaje 2D](gear-2d.md)

## Relacionado

- [Engranaje 2D](gear-2d.md) - Trayectoria de engranaje 2D para operaciones con trayectorias
- [Roscas](threads.md) - Crear características roscadas
