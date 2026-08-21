---
title: Roscas
articleKey: ThreadsObject3D_2
parent: "Mechanical Parts"
nav_order: 3
source_hash: 7d881b3293a508e102d3a4b845cdfd4eb9c34fa8
source_lang: en
---
# Roscas

Crea roscas de tornillo con diámetro, paso y perfil de rosca configurables. Las roscas se pueden usar como pernos/tornillos independientes o restarse de otros objetos para crear agujeros roscados.

<!-- AUTO_IMAGE: type=from_thumbnail item=threads file=mechanical_threads -->
![mechanical_threads](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_threads.png)

## Cómo se usa

1. Agrega **Roscas** desde las herramientas de Mecánico o el panel Primitivas
2. Define el diámetro, el paso y el número de rotaciones
3. Opcionalmente, activa "Usar como agujero" para crear agujeros roscados

## Parámetros

### Uso

- **Usar como agujero** - Cuando está activado, las roscas se dimensionan con tolerancia adicional para usarse como agujero restado (predeterminado: desactivado)
- **Tolerancia** - Holgura adicional para el ajuste cuando se usa como agujero (predeterminado: 0.2mm, visible cuando Usar como agujero está activado)

### Atributos

- **Diámetro** - El diámetro exterior de la sección roscada (predeterminado: 10mm)
- **Paso** - Distancia entre cada vuelta de la rosca (predeterminado: 2mm). Un paso menor = roscas más finas
- **Escala de rosca** - Anchura de las roscas como proporción del paso (predeterminado: 1.0, rango: 0.1-1.0)
- **Rotaciones** - Número de vueltas completas de la rosca (predeterminado: 10)

### Geometría

- **Lados** - Número de segmentos alrededor del perímetro (predeterminado: 40). Más = más suave

### Puntas (extremos de la rosca)

- **Escala de punta** - Cuánto se afinan los extremos de la rosca (predeterminado: 0, rango: 0-1). Ajusta un valor mayor que 0 para crear una entrada cónica en los extremos
- **Ángulo de punta** - El ángulo a lo largo del cual se afinan las puntas (predeterminado: 90 grados)

## Consejos

- Para crear un agujero roscado: activa "Usar como agujero", coloca las roscas y aplica [Restar](../operations/boolean/subtract.md) sobre tu objeto
- Agrega Tolerancia cuando lo uses como agujero para asegurar que las piezas impresas encajen entre sí
- Pasos de rosca métrica estándar: M3=0.5mm, M4=0.7mm, M5=0.8mm, M6=1.0mm, M8=1.25mm, M10=1.5mm
- Usa Escala de punta para crear una entrada que facilite el inicio del roscado

## Relacionado

- [Engranaje](gears.md) - Crea formas de engranaje mecánico
- [Cilindro](../primitives/cylinder.md) - Una columna redonda simple (sin roscas)
- [Restar](../operations/boolean/subtract.md) - Corta roscas en otros objetos para crear agujeros
