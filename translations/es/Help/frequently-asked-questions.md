---
title: Preguntas frecuentes
nav_order: 101
source_hash: 929ea9e89d3f5008996615341418ba715d3f6075
source_lang: en
---
# ¿Por qué mis objetos tienen la escala incorrecta?
- Los archivos STL no almacenan información de unidades. MatterCAD espera dimensiones STL en milímetros, mientras que la mayoría del software CAD exporta en sus unidades nativas (normalmente pulgadas). Esto provoca discrepancias de escala al importar diseños.

- La mejor solución es configurar su software de diseño para que exporte los archivos STL en milímetros. Por ejemplo, en SolidWorks, use el botón Opciones del cuadro de diálogo Guardar como para definir los parámetros de exportación STL.

- Como alternativa, puede reescalar la pieza dentro de MatterCAD. En la Vista 3D, entre en el modo Editar y seleccione ESCALA en la barra de herramientas derecha. Use el menú desplegable para los factores de conversión habituales o introduzca dimensiones específicas en los campos de los ejes.

# ¿Cómo borro los datos de la aplicación?

- Si reinstalar no resuelve un problema, es posible que deba eliminar los datos almacenados de MatterCAD. Estos datos permanecen tras la desinstalación. Para restablecer por completo la configuración predeterminada, quite la carpeta de la aplicación. También puede cambiar temporalmente el nombre del archivo de base de datos SQLite (MatterCAD.db) para comprobar si la configuración es la causa de los problemas.
![20260318 194137 paste 20260318 194137](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194137-paste-20260318-194137.jpg)

![20260318 194200 paste 20260318 194200](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194200-paste-20260318-194200.jpg)

![20260318 194218 paste 20260318 194218](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194218-paste-20260318-194218.jpg)


- Windows
  - La biblioteca del usuario y la configuración se almacenan en C:\Users\{user}\AppData\Local\MatterCAD.
