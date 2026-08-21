---
title: Agregar objetos existentes
parent: "Getting Started"
nav_order: 1
source_hash: e384a5c024336c3c58343d262d914fa40e0b0426
source_lang: en
---
# Agregar objetos existentes

Puede incorporar modelos 3D existentes a MatterCAD importando archivos desde su equipo o agregando contenido desde la biblioteca integrada.

## Desde su equipo

![20260324 081143 paste 20260324 081143](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081143-paste-20260324-081143.jpg)

![20260324 081240 paste 20260324 081240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081240-paste-20260324-081240.jpg)


Haga clic en el botón **Abrir** de la barra de herramientas para explorar y agregar archivos desde su equipo. MatterCAD admite los siguientes formatos de importación:

- **STL** (.stl) - Formato de modelo 3D estándar de la industria, muy utilizado en impresión 3D
- **AMF** (.amf) - Formato avanzado compatible con colores y objetos multimaterial
- **OBJ** (.obj) - Formato de gráficos 3D de Wavefront (solo geometría de malla)
- **3MF** (.3mf) - 3D Manufacturing Format con amplia compatibilidad de metadatos
- **MCX** (.mcx) - Formato nativo de MatterCAD, que conserva todos los datos y parámetros del diseño
- **SVG** (.svg) - Scalable Vector Graphics, importado como trayectorias 2D
- **TTF / OTF** (.ttf, .otf) - Archivos de fuente para usar con la herramienta **Texto**

## Arrastrar y soltar

También puede arrastrar y soltar archivos directamente desde el escritorio o el explorador de archivos al espacio de trabajo de MatterCAD. Los tipos de archivo compatibles se importarán automáticamente.

![20260324 081416 paste 20260324 081416](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081416-paste-20260324-081416.jpg)

## Desde la Biblioteca

### La Barra lateral de la Biblioteca

Haga clic en el botón **Agregar contenido** de la barra de herramientas para abrir el panel del explorador de la biblioteca. Desde aquí puede:

- Explorar sus diseños guardados
- Navegar a la biblioteca de Primitivas para acceder a las formas integradas
- Acceder a su Biblioteca en la nube si ha iniciado sesión
- Arrastrar y soltar cualquier elemento de la biblioteca directamente en su espacio de trabajo

![20260324 081446 paste 20260324 081446](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081446-paste-20260324-081446.jpg)

### La pestaña Biblioteca

También puede usar la pestaña Biblioteca para explorar sus colecciones. Haga clic derecho en cualquier objeto de la biblioteca y seleccione **Agregar a la escena** para importarlo a su espacio de trabajo de diseño actual.

![20260324 081536 paste 20260324 081536](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081536-paste-20260324-081536.jpg)

## Consejos

- MCX es el mejor formato para volver a editar diseños más adelante, ya que conserva todos los parámetros y el árbol de diseño
- Los archivos STL contienen únicamente geometría de malla. Si importa un STL, aún puede aplicarle operaciones, pero no puede editar los parámetros originales
- Al importar varios archivos, cada uno se convierte en un objeto independiente de la escena. Use [Agrupar](../workspace/grouping.md) para organizarlos

## Relacionado

- [Crear objetos nuevos](creating-new-objects.md) - Comience un diseño desde cero con primitivas
- [Guardando y exportando](saving-and-exporting.md) - Guarde y exporte sus diseños terminados
- [Biblioteca](../library/index.md) - Aprenda más sobre cómo organizar su biblioteca de diseños
