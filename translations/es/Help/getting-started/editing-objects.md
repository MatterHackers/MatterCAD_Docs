---
title: Editar objetos
parent: "Getting Started"
nav_order: 3
source_hash: 5190f3e59be7ea02497903b15c1956ed68b4d270
source_lang: en
---
# Editar objetos

MatterCAD ofrece controles intuitivos integrados directamente en la vista 3D para mover, rotar y escalar sus objetos. También puede editar los parámetros del objeto en el panel Propiedades.

## Mover piezas


- **Arrastrar sobre la base** - Haga clic y arrastre cualquier objeto para deslizarlo por la superficie del espacio de trabajo
- **Mover arriba y abajo** - Utilice el control de flecha vertical situado en la parte superior de un objeto seleccionado para ajustar su altura (posición Z)
- Para un posicionamiento preciso, utilice la operación [Trasladar](../operations/transform/translate.md) o escriba valores exactos en el panel Propiedades

## Rotar piezas

![20260324 080843 paste 20260324 080843](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080843-paste-20260324-080843.jpg)

Haga clic en cualquiera de los **controles de rotación de las esquinas** que aparecen al seleccionar un objeto. Estos le permiten rotar el objeto en el plano de ese control.

- Mueva el ratón sobre uno de los indicadores de ángulo para ajustar la rotación a **incrementos de 45 grados**
- Para una rotación precisa, utilice la operación [Rotar](../operations/transform/rotate.md) e introduzca un ángulo exacto

## Escalar piezas

![20260324 080819 paste 20260324 080819](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080819-paste-20260324-080819.jpg)


Haga clic en cualquiera de los **controles de escalado de las esquinas** para cambiar el tamaño de su pieza en el espacio de trabajo.

- Arrastre una esquina para escalar proporcionalmente
- Para un dimensionado preciso o un escalado no uniforme, utilice la operación [Escalar](../operations/transform/scale.md), donde puede establecer dimensiones exactas o escalar cada eje de forma independiente

## Editar parámetros

Al seleccionar un objeto, sus parámetros aparecen en el panel Propiedades, en el lado derecho de la pantalla. Por ejemplo:

- Un **Cubo** muestra Anchura, Profundidad, Altura y los controles opcionales de Redondear
- Un **Cilindro** muestra Diámetro, Altura y Lados
- Un objeto de **Texto** muestra el contenido del texto, la fuente, el tamaño y la altura

Puede escribir los valores directamente, usar los deslizadores o introducir [expresiones](../workspace/expressions.md) para establecer relaciones paramétricas.

## Menú contextual

Haga clic derecho sobre cualquier objeto para acceder a opciones adicionales, entre ellas:

- Copiar, Cortar, Eliminar
- Agrupar / Desagrupar
- Operaciones disponibles para el objeto seleccionado
- Ayuda para ese tipo de objeto concreto (cuando esté disponible)

## Consejos

- Mantenga pulsada la tecla **Shift** mientras hace clic para seleccionar varios objetos y luego moverlos u operar sobre ellos en conjunto
- Pulse **Ctrl+Z** para deshacer cualquier cambio que realice
- Utilice [Alinear](../operations/placement/align.md) para posicionar con precisión varios objetos unos respecto a otros
- Pulse **Espacio** para deshacer la selección

## Relacionado

- [Navegación por la vista](viewport-navigation.md) - Cómo rotar, encuadrar y hacer zoom en la vista
- [Selección](../workspace/selection.md) - Comportamiento detallado de la selección
- [Operaciones de Transformar](../operations/transform/index.md) - Controles de transformación precisos
- [Atajos de teclado](../workspace/keyboard-shortcuts.md) - Todos los atajos disponibles
