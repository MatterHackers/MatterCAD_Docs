---
title: Esfera
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
source_hash: c227e98ac116c3481bb2af73c55801de84e70b1e
source_lang: en
---
# Esfera

Una forma de bola redonda con diámetro y nivel de detalle ajustables.

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## Parámetros

- **Diámetro** - El ancho de la esfera (predeterminado: 20mm)
- **Lados** - Número de segmentos alrededor del perímetro (predeterminado: 40). Más lados = superficie más suave

### Parámetros avanzados

Activa el modo **Avanzado** para acceder a controles adicionales:

- **Ángulo inicial** - Ángulo donde comienza la superficie de la esfera (predeterminado: 0)
- **Ángulo final** - Ángulo donde termina la superficie de la esfera (predeterminado: 360). Usa un valor menor que 360 para obtener formas de esfera parcial
- **Lados de latitud** - Número de segmentos de arriba a abajo (predeterminado: 30). Más = polos más suaves

## Consejos

- Para impresión 3D, 40 lados suele ser suficiente. Los valores más altos crean superficies más suaves, pero archivos más grandes
- Usa el Ángulo inicial y el Ángulo final para crear formas de esfera parcial como cuencos o cúpulas
- Combina con [Restar](../operations/boolean/subtract.md) para crear cavidades esféricas

## Relacionado

- [Media esfera](half-sphere.md) - Solo el hemisferio superior
- [Toro](torus.md) - Una forma de dona
