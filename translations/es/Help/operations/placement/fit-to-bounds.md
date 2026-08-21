---
title: Ajustar a los límites
articleKey: FitToBoundsObject3D_4
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 91b9c917cb636f28403c291a4d56f22bf6758b70
source_lang: en
---
# Ajustar a los límites

Ajustar a los límites escala un objeto para que quepa dentro de las dimensiones de anchura, profundidad y altura especificadas. Puedes controlar cómo se estira y se alinea el objeto dentro de los límites de destino.

<!--  Screenshot showing an object being fit to specific bounding dimensions -->
![20260506 154930 paste 20260506 154930](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154930-paste-20260506-154930.jpg)

## Cómo se usa

1. Selecciona un objeto
2. Aplica la operación **Ajustar a los límites** desde el menú Colocación
3. Introduce las dimensiones de destino
4. Elige el bloqueo de proporción y el comportamiento de estirado

## Parámetros

- **Bloquear proporción** - Cómo restringir las proporciones:
  - **Ninguno** - Cada eje se puede definir de forma independiente
  - **X e Y** - La anchura y la profundidad quedan bloqueadas juntas
  - **X, Y y Z** - Escalado uniforme en todos los ejes
- **Anchura** - Anchura de destino (dimensión X)
- **Profundidad** - Profundidad de destino (dimensión Y)
- **Altura** - Altura de destino (dimensión Z)

### Cuando Bloquear proporción es X e Y o X, Y y Z

- **Estirar** - Cómo se ajusta el objeto:
  - **Interior** - Reduce la escala para que quepa por completo dentro de los límites (puede dejar huecos)
  - **Expandir** - Aumenta la escala para llenar los límites (puede sobrepasarlos en algunas dimensiones)

### Cuando Bloquear proporción es Ninguno

Cada eje tiene el suyo propio:

- **Estirar** - Interior o Expandir por eje
- **Alinear** - Dónde colocarlo dentro de los límites (Mín, Centro, Máx)

## Consejos

- Utiliza esto para redimensionar modelos importados a dimensiones de destino exactas
- Bloquea todas las proporciones para lograr un escalado uniforme que mantenga la forma original
- Usa el control por eje cuando necesites ajustar una anchura concreta pero no te importen las demás dimensiones

## Relacionado

- [Escalar](../transform/scale.md) - Escala por proporción o porcentaje en lugar de por tamaño de destino
- [Ajustar a cilindro](fit-to-cylinder.md) - Ajusta dentro de un límite cilíndrico
- [Alinear](align.md) - Coloca objetos unos respecto a otros
