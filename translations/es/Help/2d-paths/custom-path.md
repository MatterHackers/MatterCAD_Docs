---
title: Ruta personalizada
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
source_hash: 3633c708477de3ac77d3547b730c33f7e4431cf6
source_lang: en
---
# Ruta personalizada

Dibuja tu propia ruta 2D con puntos de control. Esto te da total libertad para crear cualquier forma 2D que luego puede extruirse o revolucionarse para obtener un objeto 3D.

<!-- Screenshot showing a custom path being edited with control points -->
![20260506 080247 paste 20260506 080247](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080247-paste-20260506-080247.jpg)


## Cómo se usa

1. Agrega una **Ruta personalizada** desde la biblioteca de rutas 2D
2. Edita los puntos de control para definir tu forma
3. Aplica [Extrusión lineal](../operations/path/linear-extrude.md) u otras operaciones de ruta para crear un objeto 3D

## Rutas abiertas y cerradas

La casilla **Cerrado** controla si la ruta une su último punto con el primero.

- **Cerrado** (opción predeterminada) hace que la ruta delimite una región. Esto es lo que rellenan [Extrusión lineal](../operations/path/linear-extrude.md) y [Revolución](../operations/path/revolve.md).
- **Abrir** convierte la ruta en una línea. Una línea no encierra nada, por lo que se muestra en la escena como una cinta delgada a lo largo de su longitud en lugar de como una forma rellena. Usa [Inflar trayectoria](../operations/path/inflate-path.md) para darle un ancho y convertirla de nuevo en algo sólido.

Dos cosas que debes saber antes de desmarcar **Cerrado**:

- **Volver a cerrar no equivale a deshacer.** Al abrir una ruta se descarta su segmento de cierre. Si ese segmento era curvo, al marcar **Cerrado** de nuevo aparece una línea recta, no la curva. Usa Ctrl+Z en su lugar: deshacer restaura la ruta original exactamente.
- **Algunos contornos no se pueden abrir.** Un contorno que quedaría con menos de dos puntos —una lágrima dibujada como un solo punto y una curva que vuelve sobre él— permanece cerrado en lugar de colapsar en algo que ya no podrías ver ni seleccionar. Lo mismo ocurre con un contorno que contiene una curva cuadrática, algo que puede incluir un SVG importado: abrirlo aplanaría la curva convirtiéndola en una esquina. La negativa es por contorno, así que el resto de la ruta sí se abre.

Si una ruta tiene varios contornos y no coinciden entre sí, la casilla se muestra como abierta. Al marcarla, todos los contornos se alinean.

Las operaciones que necesitan una región cerrarán una ruta abierta por ti en lugar de rechazarla. Extrusión lineal, Revolución, Restar y las demás operaciones booleanas hacen esto, de modo que una ruta abierta se extruye al mismo sólido que produciría su versión cerrada.

## Consejos

- Usa Ruta personalizada cuando ninguna de las formas de ruta integradas se ajuste a lo que necesitas
- Para importar formas desde editores vectoriales externos, consulta [Objeto SVG](../primitives/svg-object.md)
- Para dibujar una línea y convertirla en una pieza, desmarca **Cerrado**, aplica [Inflar trayectoria](../operations/path/inflate-path.md) para darle grosor y luego [Extrusión lineal](../operations/path/linear-extrude.md) para darle altura

## Relacionado

- [Ruta de círculo](circle-path.md): un círculo predefinido
- [Ruta de caja](box-path.md): un rectángulo predefinido
- [Objeto SVG](../primitives/svg-object.md): importa rutas vectoriales desde archivos SVG
- [Extrusión lineal](../operations/path/linear-extrude.md): da altura a las rutas
