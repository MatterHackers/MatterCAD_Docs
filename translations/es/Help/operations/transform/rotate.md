---
title: Rotar
articleKey: RotateObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 9bdc210c5c375fe3179050e8a8916d895455ce5f
source_lang: en
---
# Rotar

Rotar gira un objeto alrededor de un eje especificado según un ángulo determinado. Puede rotar alrededor de cualquier dirección de eje y elegir el punto central de la rotación.

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## Cómo se usa

1. Seleccione un objeto
2. Aplique la operación **Rotar** desde el menú Transformar
3. Establezca el ángulo y el eje de rotación en el panel Propiedades

También puede rotar objetos directamente en la ventana gráfica haciendo clic en los controles de esquina de rotación de un objeto seleccionado. Al mover el ratón sobre los indicadores de ángulo, el giro se ajusta en incrementos de 45 grados.

## Parámetros

- **Ángulo** - El ángulo de rotación en grados (rango: 3-360). Admite [expresiones](../../workspace/expressions.md).
- **Rotar alrededor de** - Define el eje de rotación y el punto de origen. Puede rotar alrededor del eje X, Y o Z, o especificar una dirección personalizada.

## Consejos

- De forma predeterminada, la rotación se centra en el centro del cuadro delimitador del objeto
- Para rotaciones de 90 grados, los indicadores de ajuste facilitan obtener valores exactos
- Utilice la operación Rotar (en lugar de los controles de la ventana gráfica) cuando necesite un ángulo preciso que no sea múltiplo de 45 grados
- Puede cambiar el eje de rotación después de aplicar la operación editando la propiedad Rotar alrededor de

## Relacionado

- [Trasladar](translate.md) - Mover un objeto una distancia específica
- [Escalar](scale.md) - Cambiar el tamaño de un objeto
- [Simetría](mirror.md) - Crear un reflejo simétrico
