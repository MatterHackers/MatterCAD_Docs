---
title: Crear nuevos objetos
parent: "Getting Started"
nav_order: 2
source_hash: 3eccb5aac5bb6f4d88f1ca3583eedd2f70384eeb
source_lang: en
---
# Crear nuevos objetos

MatterCAD ofrece un amplio conjunto de herramientas para crear objetos 3D. Puede empezar con formas primitivas, usar herramientas especializadas como texto y códigos QR, o construir formas complejas mediante operaciones booleanas y matrices.

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## Agregar primitivas

La forma más rápida de comenzar un diseño es agregar formas primitivas. Abra el panel Primitivas en la biblioteca y haga clic en cualquier forma para agregarla a su espacio de trabajo. Las primitivas disponibles incluyen:

- **Formas básicas** - Cubo, Cilindro, Esfera, Cono, Toro, Anillo, Pirámide, Cuña y sus variantes de media forma
- **Texto y especiales** - Texto, Braille, Código QR, Objeto de imagen, Objeto SVG

Cada primitiva tiene parámetros que puede ajustar en el panel Propiedades después de seleccionarla. Por ejemplo, un Cubo tiene controles de Anchura, Profundidad y Altura. Consulte [Primitivas](../primitives/index.md) para obtener detalles sobre cada forma.

## La barra de herramientas de operaciones

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

La barra de herramientas situada en la parte superior de la vista le da acceso rápido a las operaciones más comunes:

- **Deshacer / Rehacer** - Revierta o vuelva a aplicar los cambios. También puede usar **Ctrl+Z** para deshacer y **Ctrl+Y** para rehacer
- **Agrupar / Desagrupar** - Combine los objetos seleccionados en un grupo que se mueve y opera como una sola unidad, o separe un grupo
- **Copiar / Eliminar** - Duplique o quite los objetos seleccionados. Los atajos estándar **Ctrl+C**, **Ctrl+X** y **Ctrl+V** también funcionan
- **Alinear** - Posicione varios objetos unos respecto a otros
- **Operaciones booleanas** - [Combinar](../operations/boolean/combine.md), [Restar](../operations/boolean/subtract.md), [Intersecar](../operations/boolean/intersect.md) y [Restar y reemplazar](../operations/boolean/subtract-and-replace.md)
- **Matrices** - Cree [patrones lineales, radiales, de curva y de transformación](../operations/array/array.md) de objetos duplicados
- **Transformaciones** - Aplique [Rotar](../operations/transform/rotate.md), [Escalar](../operations/transform/scale.md), [Simetría](../operations/transform/mirror.md) y otras modificaciones

## Construir formas complejas

La mayoría de los diseños en MatterCAD se construyen combinando formas simples:

1. **Empiece con primitivas** - Agregue las formas básicas que necesite
2. **Colóquelas** - Mueva y rote los objetos para que se solapen donde usted quiera
3. **Aplique operaciones booleanas** - Use [Combinar](../operations/boolean/combine.md) para fusionar formas entre sí, o [Restar](../operations/boolean/subtract.md) para recortar una forma de otra
4. **Refine** - Use operaciones de [Remodelar](../operations/reshape/index.md) como Bisel, Curva o Torsión para agregar detalle

## Relacionado

- [Primitivas](../primitives/index.md) - Referencia completa de todas las formas primitivas
- [Agregar objetos existentes](adding-existing-objects.md) - Importe archivos en lugar de crear desde cero
- [Operaciones booleanas](../operations/boolean/index.md) - Combine formas para obtener formas complejas
- [Editar objetos](editing-objects.md) - Mueva, rote y escale los objetos después de crearlos
