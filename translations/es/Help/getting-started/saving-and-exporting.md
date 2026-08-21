---
title: Guardando y Exportando
parent: "Getting Started"
nav_order: 4
source_hash: 020d4bf43f07d3ab7dbd7d585e13c99309f0c0b8
source_lang: en
---
# Guardando y Exportando

MatterCAD admite varios formatos de archivo para guardar y exportar sus diseños. El formato que elija depende de cómo planee usar el archivo.

## Formatos para guardar

### MCX (formato nativo)

MCX es el formato de archivo nativo de MatterCAD y la mejor opción para los diseños que desea seguir editando más adelante. Conserva:

- El árbol de diseño completo con todos los objetos y su jerarquía
- Todos los parámetros y ajustes de cada objeto
- Operaciones booleanas, matrices y otras operaciones en forma editable
- Las relaciones entre componentes

**Use MCX cuando:** desee guardar su trabajo y continuar editándolo más adelante.

### STL

STL es el formato más utilizado para la impresión 3D. Contiene únicamente la geometría final de malla triangular, sin historial de diseño ni parámetros.

**Use STL cuando:** desee imprimir su diseño en 3D o compartirlo con alguien que no use MatterCAD.

### OBJ

OBJ (Wavefront) es un formato 3D común compatible con la mayoría del software 3D. Al igual que STL, contiene solo la geometría de malla.

**Use OBJ cuando:** necesite abrir su diseño en otro software 3D como Blender o un motor de videojuegos.

### SVG

La exportación a SVG crea un archivo vectorial 2D a partir de la vista superior de su diseño. Esto resulta útil para el corte láser o el fresado CNC.

**Use SVG cuando:** necesite un contorno 2D de su diseño para corte láser o grabado.

## Cómo guardar

![20260324 080726 paste 20260324 080726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080726-paste-20260324-080726.jpg)

1. Abra el **menú de marca** (el logotipo de MatterCAD en la esquina superior izquierda)
2. Seleccione **Guardar como** para elegir una ubicación y un formato
3. Seleccione el formato de archivo en el menú desplegable de formatos
4. Elija dónde guardar el archivo y haga clic en **Guardar**

Su diseño también se guarda automáticamente mientras trabaja, por lo que no perderá los cambios si cierra la aplicación.

## Consejos

- Guarde siempre una copia MCX de su diseño antes de exportarlo a STL u OBJ, para poder hacer cambios más adelante
- Al exportar a STL, todos los objetos de la escena se combinan en una sola malla
- Si necesita compartir un diseño con alguien que usa MatterCAD, envíe el archivo MCX para conservar la editabilidad completa
- También puede guardar diseños en su [Biblioteca en la nube](../library/cloud-library.md) para acceder a ellos desde cualquier equipo

## Relacionado

- [Agregar objetos existentes](adding-existing-objects.md) - Importar archivos a MatterCAD
- [Biblioteca](../library/index.md) - Organice sus diseños guardados
- [Biblioteca en la nube](../library/cloud-library.md) - Guarde diseños en la nube
