---
title: Seleccionar trayectorias
articleKey: SelectPathsObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: f7df7bb24841030643e4634febedcfce6e92ada9
source_lang: en
---
# Seleccionar trayectorias

Seleccionar trayectorias filtra qué subtrayectorias de un objeto de trayectoria compleja se conservan. Resulta especialmente útil al trabajar con fuentes decorativas o de varias partes en las que necesitas las formas exteriores de las letras y las formas recortadas interiores como piezas separadas; por ejemplo, para imprimirlas en 3D en dos colores distintos.

<!--  Screenshot showing Select Paths applied to decorative text with outer paths highlighted -->
![20260506 154655 paste 20260506 154655](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154655-paste-20260506-154655.jpg)

## Cómo funciona la profundidad de trayectoria

Cuando un objeto de trayectoria contiene formas con áreas cerradas (como el interior de la letra "O" o el hueco de una espiral decorativa), esas áreas cerradas son **agujeros** con profundidad 1. El contorno exterior de cada letra o forma está en la **profundidad 0**.

```
Depth 0 — outer contour of each letter or shape
Depth 1 — first level of enclosed holes (inside an "O", "A", etc.)
Depth 2 — shapes nested inside a hole (rarely used)
```

## Preajustes de filtro

### Todo
Incluye todas las trayectorias sin cambios. Es el valor predeterminado y equivale a no aplicar Seleccionar trayectorias en absoluto.

### Solo trayectorias exteriores
Conserva únicamente el contorno exterior de cada forma (profundidad == 0). Úsalo para obtener solo los contornos de las letras de una fuente decorativa, sin las áreas recortadas interiores.

### Solo agujeros
Conserva únicamente los agujeros cerrados (profundidad > 0). Úsalo para obtener solo las áreas de corte interiores de letras y formas.

### Por índice de grupo
Conserva únicamente las trayectorias que pertenecen a una forma inconexa. El grupo 0 es la primera forma, el grupo 1 es la segunda, y así sucesivamente. Úsalo para aislar un solo carácter de una palabra.

### Personalizado
Escribe una expresión que se evalúa para cada trayectoria. La trayectoria se **incluye** cuando la expresión es distinta de cero y se **excluye** cuando es cero.

Las expresiones deben comenzar con `=` para habilitar la sustitución de variables. Sin `=`, el valor se trata como un número simple (por ejemplo, `1` siempre incluye, `0` siempre excluye).

## Ejemplos de expresiones personalizadas

| Expresión | Efecto |
|------------|--------|
| `=PathDepth==0` | Solo contornos exteriores (igual que Solo trayectorias exteriores) |
| `=PathDepth>0` | Solo agujeros (igual que Solo agujeros) |
| `=GroupIndex==0` | Solo la primera forma inconexa |
| `=PathArea>100` | Formas con un área mayor que 100 mm² |
| `=PathLength>50` | Formas con un perímetro mayor que 50 mm |

## Variables de expresiones personalizadas

| Variable | Significado |
|----------|---------|
| `PathDepth` | 0 = contorno exterior; 1+ = agujero o forma anidada |
| `GroupIndex` | Índice de la forma inconexa (0, 1, 2…) |
| `GroupOuterArea` | Área de la trayectoria exterior de este grupo |
| `GroupOuterLength` | Perímetro de la trayectoria exterior de este grupo |
| `ChildCount` | Número de agujeros dentro de la trayectoria exterior de este grupo |
| `PathIndex` | Índice secuencial de esta trayectoria dentro de su grupo |
| `PathArea` | Área de esta trayectoria individual |
| `PathLength` | Perímetro de esta trayectoria individual |

## Ejemplo: impresión multicolor con una fuente navideña

Un uso habitual de Seleccionar trayectorias es imprimir texto decorativo en el que las letras tienen formas recortadas interiores. Para imprimir las letras exteriores en un color y los cortes interiores en un segundo color:

1. Agrega un objeto de **Texto** y configúralo con **salida 2D**
2. Aplica **Seleccionar trayectorias** → establece el preajuste en **Solo trayectorias exteriores**
3. Aplica **Extrusión lineal** para darle altura → asigna tu primer color de filamento
4. Vuelve al objeto de texto original
5. Aplica una segunda vez **Seleccionar trayectorias** → establece el preajuste en **Solo agujeros**
6. Aplica **Extrusión lineal** con la misma altura → asigna tu segundo color de filamento
7. Coloca un objeto extruido encima del otro; los dos colores se alinean perfectamente

## Relacionado

- [Extrusión lineal](linear-extrude.md) — Da altura a las trayectorias filtradas para crear un objeto 3D
- [Revolución](revolve.md) — Gira las trayectorias filtradas alrededor de un eje
- [Objeto SVG](../../primitives/svg-object.md) — Importa trayectorias vectoriales que pueden contener varias subtrayectorias
- [Texto](../../primitives/text.md) — Los objetos de texto en modo 2D producen una salida de varias trayectorias
