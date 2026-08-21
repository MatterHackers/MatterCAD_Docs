---
title: Notas de la versión
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8 (13 de agosto de 2026)
[Descarga para Windows](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## Nuevas características

* **Editar hijos**
  * Haz doble clic en un objeto de la cama o en el árbol de escena para entrar en él y editar las piezas con las que está construido: sin ventanas ni pestañas separadas
  * En operaciones como Restar, editas las piezas de origen y el resultado se reconstruye cuando sales
  * Una ruta de navegación en la parte superior del árbol de escena muestra el recorrido completo; al hacer clic en un nivel, tus ediciones se integran como un único paso deshacible, y cada nivel conserva su propio historial de deshacer
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **Una sola herramienta booleana**
  * Combinar, Restar, Intersecar y Restar y reemplazar son ahora una única operación con una fila de iconos en la parte superior de su panel: cambia de modo con un clic en lugar de eliminar y volver a aplicar
  * La misma operación funciona tanto con mallas 3D como con rutas 2D, y muestra el progreso mientras se ejecuta una booleana pesada
  * Los diseños guardados con los antiguos objetos booleanos independientes se siguen abriendo con normalidad
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **Booleanas que simplemente funcionan**
  * Las booleanas se ejecutan sobre un nuevo motor nativo que es más rápido y tiene éxito con mallas que antes fallaban
  * Combinar repara automáticamente las piezas con agujeros: las reparaciones limpias se suman a la unión, las piezas que no se pueden fusionar de forma segura se conservan al lado y se nombran por ti, y una pieza que no se ha podido reparar mantiene tu geometría original
  * Corte por plano es ahora una verdadera intersección sólida, así que el resultado es estanco e imprimible en lugar de una cáscara abierta
  * Nuevas opciones Mantener geometría invertida y Reparar orden de bobinado para mallas importadas problemáticas


## Mejoras

* **Editor de rutas 2D**
  * Cuatro modos de punto —Agudo, Simétrico, Alineado y Libre— aplicables con un clic, tanto en el editor 2D como en la vista 3D
  * Simetría es ahora un modo de simetría en vivo: las ediciones se reflejan a través del centro a medida que las haces, y arrastrar un par reflejado sobre el eje lo fusiona en un solo punto
  * Selecciona puntos arrastrando con un marco elástico, muévelos en grupo, ajústalos a la cuadrícula y pulsa Esc para cancelar un arrastre
  * Suavizar ajusta una curva a través de los puntos que has marcado en un solo paso
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **Visualización y navegación**
  * Pulsa Z con una ruta plana seleccionada para animar hacia una vista de edición en picado ajustada a la ruta
  * El renderizado de texto subpíxel se activa automáticamente cuando tu pantalla lo admite, y aún se puede activar o desactivar en los ajustes de Avanzado

* **Modelado**
  * Extrusión lineal puede biselar el borde inferior con su propio estilo, radio y número de segmentos
  * Los objetos exclusivos del editor (Curva 3D, Herramienta de medición, Descripción, Hoja) se siguen mostrando, pero quedan excluidos de la exportación

## Principales correcciones de errores

  * Un guardado que fallaba a medias podía truncar el archivo que estaba reemplazando e informar de éxito. Ahora los guardados se completan por entero y luego reemplazan el destino de forma atómica; la misma protección cubre los guardados en la biblioteca y las exportaciones
  * Un guardado fallido deja el diseño marcado como no guardado, así que cerrar la aplicación no puede descartar tu trabajo en silencio
  * Guardar en disco un elemento de la nube mantenía el nombre de pestaña antiguo y perdía la pestaña al reiniciar
  * Corregido que los submodelos 3MF se descartaran en silencio al cargar, y que los archivos 3MF cargados a la vez se contaminaran entre sí
  * Corregidos bloqueos, un filtro de histograma defectuoso y las copias de una pieza de imagen que no se mantenían sincronizadas con el original
  * Corregido un bloqueo al eliminar un punto de curva, y que los puntos en la costura de una ruta cerrada revirtieran el modo elegido
  * El botón Detener de una tarea en ejecución ahora se puede pulsar y realmente cancela

---

# MatterCAD 2.2026.5 (8 de mayo de 2026)
[Descarga para Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## Nuevas características

* **Herramienta de matriz rediseñada**
  * Una única operación de matriz unificada sustituye a las antiguas Matriz lineal, Matriz radial y Matriz avanzada
  * Modo **Lineal**: copias a lo largo de una dirección con rotación opcional y escala progresiva
  * Modo **Radial**: copias alrededor de un eje central con radio, ángulo de barrido y patrones de arco o círculo completo configurables
  * Modo **Transformar**: copias por pasos usando una transformación manual o la transformación de un objeto hermano con nombre
  * El modo de rotación Combinación en Lineal crea espirales, abanicos y hélices de forma natural
  * Opción La escala afecta al desplazamiento para disposiciones tipo concha de nautilo y de progresión geométrica
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **Favoritos de la biblioteca**
  * Marca con una estrella cualquier elemento de la biblioteca para añadirlo a una carpeta Favoritos persistente
  * Accede rápidamente desde un solo lugar a tus primitivas, generadores y piezas guardadas más usados
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## Mejoras

* **Alinear**
  * La alineación Apilado es ahora un botón de modo directo en lugar de una opción desplegable
  * Se han añadido modos más claros: Simple, Desplazamiento y Apilado, para alinear bordes, añadir separaciones precisas y construir pilas ordenadas
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **Compatibilidad de archivos**
  * Añadida compatibilidad con el formato de imagen WEBP en las operaciones basadas en imágenes
  * Mejorado el análisis de archivos SVG para importaciones más fiables

* **Fiabilidad**
  * Mejorada la velocidad y la fiabilidad de la carga de archivos 3MF
  * Mejor restauración de pestañas entre sesiones

## Principales correcciones de errores

* **Inicio de sesión y acceso a la Biblioteca en la nube**
  * Se han restaurado el inicio de sesión y el acceso a la Biblioteca en la nube después de que una actualización del servidor rompiera el acceso.
  * MatterCAD ahora te pide volver a iniciar sesión cuando el acceso a la nube encuentra credenciales caducadas o no válidas.

* **Selección en el árbol de escena**
  * Corregido el comportamiento inconsistente de la selección al elegir objetos en el árbol de escena.

* **Navegación por la ayuda**
  * Corregidos problemas de navegación en la ayuda incluida y en la documentación de versiones.

* **Clic derecho en la biblioteca**
  * Corregido el comportamiento del clic derecho en la vista de árbol de la biblioteca.

* **Hojas**
  * Corregido un bloqueo que podía producirse al trabajar con hojas.

---

# MatterCAD 2.2026.3 (12 de marzo de 2026)
[Descarga para Windows](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## Nuevas características

* **Nuevo motor de renderizado Direct3D 11**
  * Migración completa de OpenGL a Direct3D 11 para un rendimiento mucho mejor
  * Antialiasing FXAA para bordes nítidos y limpios
  * Doble depth peeling para una transparencia correcta independiente del orden
  * Sombras de la cama aceleradas por hardware
  * Contornos de objeto y elementos visuales de selección mejorados
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **Transparencia de objeto**
  * Ajusta el alfa/transparencia en cualquier objeto individual de la escena
  * Las mallas con color por cara admiten alfa sin dañar el color
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **Bloquear y ocultar objetos**
  * Bloquea objetos para evitar seleccionarlos o editarlos por accidente
  * Oculta objetos para reducir el desorden visual mientras trabajas en piezas concretas
  * Comandos Mostrar todo y Desbloquear todo para restaurar rápidamente la visibilidad
  * Los objetos bloqueados y ocultos quedan correctamente excluidos de la selección por rayo
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **Restar booleano mejorado**
  * Las operaciones de resta múltiple son mucho más fiables y precisas

## Mejoras

* **Manejo de archivos**
  * Los proyectos ahora se guardan como 3MF de forma predeterminada en lugar de STL, conservando colores, materiales e historial de diseño
  * Compatibilidad mejorada de arrastrar y soltar archivos y carpetas en la vista 3D

* **Flujo de trabajo**
  * Los diálogos Guardar como y Mover recuerdan la última ubicación de carpeta
  * Los campos de expresión ahora admiten `pi`, `tau`, `e` y `count`
  * La tecla Esc deshace en los contextos de edición de diseño
  * Los controles 3D permanecen visibles cuando el ratón sale de la escena

* **Rendimiento y estabilidad**
  * Corregidos bloqueos al inicio y problemas de carga recursiva
  * Corregidos errores de renderizado de iluminación y mipmapping
  * Mejoradas las actualizaciones de la vista de árbol de la biblioteca
  * Cálculo dinámico de los planos cercano/lejano para un mejor comportamiento del zoom
  * Actualizado a .NET 10

---

# MatterCAD 2.2025.6 (20 de junio de 2025)
[Descarga para Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## Nuevas características

* **Compatibilidad con Archivo SVG**  
  * Compatibilidad total de arrastrar y soltar para archivos SVG
  * Conversión directa de gráficos SVG a objetos 3D
  * Integración perfecta con los flujos de trabajo CAD existentes

* **Manejo avanzado de Archivo OBJ**  
  * Compatibilidad con la carga de materiales desde archivos ZIP
  * Análisis de archivos OBJ y manejo de materiales mejorados
  * Mejor compatibilidad con modelos 3D complejos con varios materiales

* **Sistema de gestión de pestañas mejorado**
  * Las pestañas de la biblioteca en la nube ahora persisten correctamente: tu trabajo se queda exactamente donde lo dejaste
  * Organización y navegación de pestañas mejoradas
  * Restauración automática de las pestañas abiertas entre sesiones

## Mejoras de la experiencia de usuario

* **Interfaz simplificada**
  * Menú Recientes reorganizado para un acceso más rápido
  * Mejor respuesta visual durante operaciones largas
  * Tiempo de inicio y capacidad de respuesta de la aplicación mejorados

* **Fiabilidad**
  * Corregidos bloqueos críticos en las interacciones con la escena 3D
  * Resueltos problemas de gestión de memoria
  * Estabilidad de la aplicación mejorada en todas las plataformas

---

# MatterCAD 2.21.5 (13 de febrero de 2025)

[Descarga para Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# Características existentes

*Las siguientes características representan la base sobre la que MatterCAD se apoya, heredada de MatterControl:*

* Añadida la característica Hueco  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* Añadido Reducir polígonos  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* Añadida la reparación de mallas  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* Incorporado el soporte totalmente automático (soporte heredado) como opción, además de la nueva opción de soporte manual
* Añadida compatibilidad con gsSlicer (nuevo motor de laminado experimental)
* Errores corregidos

## Cambios

* Mejorada la desagrupación de mallas (división en varias mallas)
    * Descarte de caras degeneradas
    * Descarte de características discretas microscópicas

## Cambios

* Añadida una barra de búsqueda para la aplicación
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* Mejorada la barra de herramientas de diseño
    * Añadida agrupación a algunos elementos
    * Añadido botón de alineación doble
    * Añadido botón Organizar todo
* Desplaza los elementos de la cama con las teclas de flecha
* La carpeta Descargas se ordena por fecha

## Cambios

* Mejoras en la interfaz
    * Actualizaciones más rápidas en las carpetas de la Biblioteca en la nube
    * Restauración de la interfaz al volver a abrir
    * Mejor compatibilidad con la navegación por teclado
* Nuevo sistema de detección de errores y avisos
    * Más errores de hardware gestionados
* Mejoras y optimizaciones de las herramientas de diseño
    * Nuevas herramientas de torsión
    * Herramienta de curva mejorada
    * Alinear mejorado


## Cambios

* Aplanado mejorado
* Compatibilidad con deshacer mejorada
* Historial de diseño mejorado

## Cambios
* Versionado: cambio a un número de versión (versión).(año).(mes). Más fácil de leer y más informativo.
* Nuevas operaciones Restar, Combinar e Intersección de última generación (solo en Windows)
* Ahora arrancamos con un «recorrido por las características» para ayudar a los nuevos usuarios a orientarse

## Cambios
* Herramientas de diseño: la capacidad de modelar en 3D con un conjunto completo de primitivas de modelado
* Usa una primitiva para crear tus propios soportes personalizados
* Aplicaciones de diseño: diseños sofisticados y personalizables
* Procesamiento de 64 bits
