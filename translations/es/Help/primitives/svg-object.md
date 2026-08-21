---
title: Objeto SVG
articleKey: SvgObject3D
parent: "Primitives"
nav_order: 15
source_hash: dab97cdde74d938b5612d959f83b54b4a04a49da
source_lang: en
---
# Objeto SVG

Importa archivos SVG (Scalable Vector Graphics) y úsalos como trayectorias 2D en tu diseño. Después, los SVG se pueden extruir en formas 3D mediante [Extrusión lineal](../operations/path/linear-extrude.md) o [Revolución](../operations/path/revolve.md).

<!--  Screenshot showing an imported SVG path being extruded into a 3D shape -->
![20260318 184807 paste 20260318 184807](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184807-paste-20260318-184807.jpg)



## Cómo se usa

1. Importa un archivo SVG arrastrándolo al espacio de trabajo o mediante el botón Abrir
2. El SVG se importa como una trayectoria 2D
3. Aplica [Extrusión lineal](../operations/path/linear-extrude.md) para darle altura, o usa otras [Operaciones de trayectoria](../operations/path/index.md)

## Consejos

- Los archivos SVG deben contener formas rellenas o trayectorias cerradas para obtener mejores resultados
- Los SVG complejos con muchas trayectorias pueden tardar más en procesarse
- Usa [Seleccionar trayectorias](../operations/path/select-paths.md) para trabajar con partes específicas de un SVG de varias trayectorias
- Hay muchos archivos SVG gratuitos disponibles en línea para logotipos, iconos y patrones decorativos

## Relacionado

- [Imagen a trazado](../operations/image/image-to-path.md) - Convierte imágenes rasterizadas en trayectorias en lugar de usar SVG
- [Texto](text.md) - Crea texto directamente sin necesidad de un SVG
- [Extrusión lineal](../operations/path/linear-extrude.md) - Da altura a las trayectorias planas
- [Trayectorias 2D](../2d-paths/index.md) - Primitivas de trayectoria integradas
