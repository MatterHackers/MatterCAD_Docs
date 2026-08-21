---
title: Novedades
nav_order: 105
source_hash: 172343b8320204d2b0ec52419324f0efd2be95a1
source_lang: en
---
# MatterCAD 2.2026.8

# Novedades

* **Editar hijos**
  * Haga doble clic en cualquier objeto para entrar en él y editar las piezas que lo componen, directamente sobre la cama
  * Una ruta de navegación muestra dónde se encuentra: haga clic en cualquier nivel para integrar de nuevo sus ediciones
  * ![MatterCAD 2.2026.8](https://www.matterhackers.com/r/qgG4VA)

* **Una sola herramienta booleana**
  * Combinar, Restar, Intersecar y Restar y reemplazar son ahora una única operación: cambie de modo con un clic en lugar de eliminar y volver a aplicar
  <!-- Boolean property panel showing the four-icon operation row with Subtract selected. ~500x350px -->
  * ![One Boolean Tool](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)

* **Booleanas que simplemente funcionan**
  * Un nuevo motor es más rápido y tiene éxito con mallas que antes fallaban
  * Combinar repara automáticamente las piezas con agujeros e indica el nombre de todo lo que no pudo fusionar; Corte por plano deja ahora un sólido estanco e imprimible

* **Mejor edición de rutas 2D**
  * Modos de punto, simetría en vivo con Simetría, ajuste a la cuadrícula, selección por arrastre y Esc para cancelar un arrastre
  <!-- Turn on Mirror, drag a point and watch its partner follow, then drag it onto the axis to merge. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

## Mejoras

* **Navegación**: pulse Z con una ruta 2D seleccionada para obtener una vista de edición cenital
* **Texto más nítido**: la representación de texto con subpíxeles se activa ahora automáticamente cuando su pantalla lo admite
* **Modelado**: Extrusión lineal puede biselar el borde inferior con su propio estilo, radio y número de segmentos

## Principales correcciones de errores

* **Fiabilidad al guardar**: un guardado fallido ya no puede dañar el archivo que estaba reemplazando, y le avisa de que ha fallado
* **Biblioteca en la nube**: al guardar en disco un elemento de la nube se conserva el nombre de su pestaña, y la pestaña se mantiene tras reiniciar
* **Carga de archivos**: se ha corregido que se descartaran piezas 3MF de forma silenciosa al cargar
* **Edición de rutas**: se ha corregido un fallo al eliminar un punto de curva y que los puntos de costura revirtieran el modo elegido
* **Tareas en segundo plano**: el botón Detener de una tarea en ejecución ahora se puede pulsar y realmente cancela

## Puede consultar las notas de la versión completas [aquí](release-notes.md).
