---
title: Pinzamiento radial
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: 95ef5847767e5cfcdbae9df9aaa1cb1727da2f5e
source_lang: en
---
# Pinzamiento radial

Pinzamiento radial comprime un objeto hacia adentro desde un punto central con una curva de perfil personalizable. A diferencia del [Pellizco](pinch.md) normal, que actúa de atrás hacia adelante, Pinzamiento radial comprime simétricamente alrededor de un eje central.

<!--  Before and after showing an object with radial pinch applied, creating a waisted shape -->
![20260506 155741 paste 20260506 155741](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155741-paste-20260506-155741.jpg)

## Cómo se usa

1. Seleccione un objeto
2. Aplique la operación **Pinzamiento radial** desde el menú Remodelar
3. Edite el perfil de la ruta para definir cuánto pinzamiento se aplica a cada altura
4. Ajuste el número de cortes para obtener mayor suavidad

## Parámetros

- **Ruta** - Un editor de curva de perfil que define la cantidad de pinzamiento en cada nivel de altura. Edite la curva para crear perfiles de pinzamiento personalizados
- **Cortes** - Número de cortes horizontales para un pinzamiento suave, espaciados uniformemente a lo largo de la pieza. Más cortes = resultados más suaves

### Parámetros avanzados

- **Tipo de pinzamiento** - Dirección de la compresión:
  - **Radial** - Comprime por igual desde todos los lados hacia el centro
  - **Eje X** - Comprime únicamente a lo largo del eje X
  - **Eje Y** - Comprime únicamente a lo largo del eje Y
- **Desplazamiento de rotación** - Desplaza el centro del efecto de pinzamiento

## Consejos

- Use el editor de rutas para crear formas de reloj de arena, botella o jarrón
- El pinzamiento radial es ideal para crear formas orgánicas y redondeadas a partir de objetos cilíndricos
- Aumente los Cortes para obtener curvas más suaves, especialmente en perfiles de pinzamiento pronunciados

## Relacionado

- [Pellizco](pinch.md) - Compresión simple de atrás hacia adelante
- [Torsión](twist.md) - Rotación en espiral a lo largo de la altura
- [Curva](curve.md) - Doblar formando un arco
