---
title: Alinear
articleKey: AlignObject3D_3
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 1fadae72ba00cb06e36a21f0b96962dcff3f60ad
source_lang: en
---
# Alinear

Alinear posiciona con precisión varios objetos respecto a un objeto ancla. Úsalo para alinear bordes, centrar piezas entre sí, colocar un objeto encima de otro o crear pilas con espaciado uniforme.

<!--  Screenshot showing two objects being aligned with alignment options visible -->
![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)


## Cómo se usa

1. Selecciona dos o más objetos.
2. Aplica la operación **Alinear** desde el menú **Colocación**.
3. Elige el objeto **Ancla**. El ancla permanece en su lugar y los demás objetos se mueven.
4. Configura la alineación para los ejes X, Y y Z de forma independiente.
5. Usa **Aplicar** cuando quieras integrar las posiciones alineadas en el árbol de objetos.

## Parámetros

### Ancla

La lista **Ancla** selecciona el objeto hijo que se usa como referencia. El ancla no se mueve. Todos los demás hijos de la operación Alinear se reposicionan respecto al ancla, salvo que un eje esté usando el modo **Apilado**.

### Controles de eje

Cada eje tiene sus propios controles. Puedes alinear en un eje, en dos ejes o en los tres. Los bordes mínimo y máximo se nombran según el eje:

- **Eje X**: Mín es izquierda, Máx es derecha.
- **Eje Y**: Mín es delante, Máx es detrás.
- **Eje Z**: Mín es abajo, Máx es arriba.

Para cada eje:

- **Alinear**: elige el punto de referencia del ancla para ese eje. Usa **Ninguno** para dejar las posiciones sin cambios en ese eje.
- **Modo**: controla cómo se aplica la alineación seleccionada:
  - **Simple**: hace coincidir el borde, el centro o el origen correspondiente de cada objeto que se mueve con el del ancla. No se usa ningún desplazamiento.
  - **Desplazamiento**: elige qué parte del objeto que se mueve debe quedar sobre la referencia del ancla y luego añade separación con **Desplazamiento**.
  - **Apilado**: coloca los objetos uno tras otro a lo largo de ese eje, usando **Desplazamiento** como separación entre ellos.
- **Subalinear**: disponible en el modo **Desplazamiento**. Elige la parte del objeto que se mueve que se colocará sobre la referencia del ancla. Si **Subalinear** es **Ninguno**, Alinear usa el mismo borde, centro u origen seleccionado en **Alinear**.
- **Desplazamiento**: disponible en los modos **Desplazamiento** y **Apilado**. Añade distancia a lo largo de ese eje y admite [expresiones](../../workspace/expressions.md).

## Modos de alineación

### Simple

Usa **Simple** cuando quieras hacer coincidir posiciones equivalentes. Por ejemplo, **Alineación X: Centro** mueve todos los objetos que no son el ancla para que su centro en X coincida con el centro en X del ancla. **Alinear Z: Mín** mueve todos los objetos que no son el ancla para que su base quede a la altura de la base del ancla.

### Desplazamiento

Usa **Desplazamiento** cuando la parte del objeto que se mueve deba ser distinta de la referencia del ancla. Por ejemplo, para colocar un objeto encima del ancla:

1. Configura **Alinear Z** en **Máx** (arriba).
2. Configura **Modo Z** en **Desplazamiento**.
3. Configura **Subalinear Z** en **Inferior**.
4. Configura **Desplazamiento Z** con la separación deseada, o déjalo en `0` para que haya contacto directo.

Esto coloca la base del objeto que se mueve sobre la parte superior del ancla, con una separación opcional.

### Apilado

Usa **Apilado** para encadenar varios objetos a lo largo de un eje. Los objetos se procesan por nombre y luego por ID interno, así que nombrar los objetos con claridad da un orden de apilado predecible.

En el modo **Apilado**, cada objeto que se mueve se coloca contra la referencia anterior en ese eje:

- La alineación **Mín** apila hacia la dirección positiva, por ejemplo de izquierda a derecha en X o de abajo hacia arriba en Z.
- La alineación **Máx** apila hacia la dirección negativa, por ejemplo de derecha a izquierda en X o de arriba hacia abajo en Z.
- Las alineaciones **Centro** y **Origen** usan el desplazamiento entre el centro o el origen de cada objeto.

Usa **Desplazamiento** en el modo **Apilado** para establecer la separación entre objetos.

## Ejemplos

- **Centrar objetos sobre la superficie de la cama**: elige como **Ancla** el objeto que debe quedar fijo y luego configura **Alineación X** y **Alineación Y** en **Centro**.
- **Colocar un objeto encima de otro**: configura **Alinear Z** en **Máx** (arriba), **Modo Z** en **Desplazamiento** y **Subalinear Z** en **Inferior**.
- **Añadir una separación precisa desde un borde**: usa el modo **Desplazamiento**, elige el borde del objeto que se mueve con **Subalinear** y luego configura **Desplazamiento** con la separación que necesites.
- **Alinear varios objetos uno tras otro**: configura **Alineación X** en **Mín** (izquierda), **Modo X** en **Apilado** y usa **Desplazamiento X** para la separación.
- **Crear una pila vertical**: configura **Alinear Z** en **Mín** (abajo), **Modo Z** en **Apilado** y usa **Desplazamiento Z** para el espacio entre objetos.

## Consejos

- El objeto ancla permanece en su lugar; los demás objetos se mueven para alinearse con él.
- Puedes usar modos distintos en ejes distintos, como **Apilado** en X mientras usas **Centro** y **Simple** en Y.
- Usa los nombres de los objetos para controlar el orden **Apilado** cuando se alineen varios objetos a la vez.
- Alinear no es destructivo hasta que se aplica. Puedes cambiar los ajustes en cualquier momento para volver a alinear los hijos.
- Usa **Origen** cuando necesites alinear los orígenes de modelado en lugar de los bordes del cuadro delimitador.

## Relacionado

- [Ajustar a los límites](fit-to-bounds.md): escala un objeto para ajustarlo a dimensiones específicas
- [Trasladar](../transform/translate.md): mueve una distancia determinada
- [Agrupación](../../workspace/grouping.md): agrupa los objetos alineados para mantenerlos juntos
