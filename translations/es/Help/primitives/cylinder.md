---
title: Cilindro
articleKey: CylinderObject3D
parent: "Primitives"
nav_order: 5
source_hash: ab8394a14de799f83dc9c39eb86b8eaf2aab37b7
source_lang: en
---
# Cilindro

Una forma de columna redonda con diámetro, altura y número de lados configurables. El Cilindro es esencial para crear pasadores, varillas, agujeros y elementos redondos.

<!--  Screenshot of a Cylinder primitive on the workspace -->
![20260318 183248 paste 20260318 183248](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183248-paste-20260318-183248.jpg)


## Parámetros

- **Diámetro** - El ancho de un extremo a otro del cilindro (predeterminado: 20mm)
- **Altura** - La altura del cilindro (predeterminado: 20mm)
- **Lados** - Número de segmentos alrededor del perímetro (predeterminado: 40). Los valores más bajos crean formas poligonales (por ejemplo, 6 para un hexágono)

### Parámetros avanzados

Activa el modo **Avanzado** para acceder a controles adicionales:

- **Diámetro superior** - Establece un diámetro distinto para la parte superior del cilindro y crea formas cónicas o de cono truncado (predeterminado: coincide con el Diámetro)
- **Ángulo inicial** - Ángulo donde comienza el cilindro (predeterminado: 0). Úsalo junto con el Ángulo final para crear cilindros parciales
- **Ángulo final** - Ángulo donde termina el cilindro (predeterminado: 360). Establece un valor menor que 360 para obtener formas de porción de tarta

## Consejos

- Establece Lados en un número bajo para crear polígonos regulares: 6 para hexágonos, 8 para octógonos, etc.
- Usa valores distintos de Diámetro y Diámetro superior para crear conos truncados y formas cónicas
- Establece el Ángulo inicial y el Ángulo final para crear formas de porción de tarta o de arco
- Los cilindros son excelentes herramientas de corte para crear agujeros redondos con [Restar](../operations/boolean/subtract.md)

## Relacionado

- [Cono](cone.md) - Un cilindro que se estrecha hasta terminar en punta
- [Medio cilindro](half-cylinder.md) - Un cilindro cortado por la mitad a lo largo
- [Anillo](ring.md) - Un cilindro hueco (tubo)
