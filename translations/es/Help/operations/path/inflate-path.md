---
title: Inflar trayectoria
articleKey: InflatePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: c0e11d3d24c5f832f797cde4d392e26a4694733d
source_lang: en
---
# Inflar trayectoria

Inflar trayectoria expande una trayectoria 2D hacia afuera, agrandando la forma sin alterar su aspecto general. Es similar a aplicar un desplazamiento uniforme a todas las aristas.

<!--  Before and after showing a path inflated outward -->
![20260506 100652 paste 20260506 100652](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100652-paste-20260506-100652.jpg)


## Cómo se usa

1. Seleccione una trayectoria 2D
2. Aplique **Inflar trayectoria** desde el menú de operaciones de Ruta
3. Ajuste la cantidad de inflado

## Inflar una línea abierta

Inflar es la manera de convertir una línea en una forma. Desmarque **Cerrado** en una [Ruta personalizada](../../2d-paths/custom-path.md) para dibujar una línea abierta y luego ínflela: el resultado es una cinta rellena, tan ancha a cada lado de la línea como la cantidad que haya definido. A partir de ahí se extruye como cualquier otra trayectoria.

**Estilo** determina cómo se rematan los dos extremos de la línea, así como la forma en que se unen sus esquinas:

- **Plano** corta la cinta en escuadra en cada punto final
- **Redondear** añade un semicírculo más allá de cada punto final
- **Agudo** añade un cuadrado más allá de cada punto final

Una línea abierta no tiene interior hacia el que encogerse, por lo que un valor de cero o negativo no dejaría nada. Cuando la trayectoria está *totalmente* abierta, Inflar limita el valor hasta un número positivo pequeño y escribe ese número limitado de nuevo en el cuadro para que pueda ver lo ocurrido.

Una trayectoria que mezcla contornos abiertos y cerrados no se limita: los contornos cerrados se encogen con normalidad y los abiertos simplemente desaparecen. Las trayectorias cerradas siguen encogiéndose con valores negativos exactamente igual que siempre.

## Consejos

- Use valores negativos para encoger la trayectoria hacia dentro en lugar de expandirla
- Inflar resulta útil para crear desplazamientos de tolerancia alrededor de las formas
- Combínelo con [Trazado del contorno](outline-path.md) para crear bordes con anchos específicos

## Relacionado

- [Trazado del contorno](outline-path.md) - Crear un contorno a partir de una trayectoria
- [Trayectoria del borde](border-path.md) - Agregar un desplazamiento de borde
- [Suavizar trayectoria](smooth-path.md) - Redondear las esquinas de una trayectoria
