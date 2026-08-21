---
title: Esvaziar
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cc2c5555723ecfe77475fef9e7a2090cdf760204
source_lang: en
---
# Esvaziar

Esvaziar cria uma casca oca a partir de um objeto sólido, deslocando a superfície para dentro. O resultado é uma versão de paredes finas da forma original.

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## Como Utilizar

1. Selecione um objeto sólido
2. Aplique a operação **Esvaziar** a partir do menu Remodelar
3. Defina a espessura de parede pretendida

## Parâmetros

- **Distância** - A espessura da parede em milímetros (predefinição: 2 mm). Corresponde à espessura que a casca resultante terá.
- **Nº de células** - Resolução do algoritmo de esvaziamento (predefinição: 64). Valores mais altos criam superfícies internas mais suaves, mas demoram mais tempo a calcular.

## Dicas

- Esvaziar é útil para criar caixas, recipientes, vasos e peças leves
- Uma espessura de parede de 1-2 mm é típica para a maioria das peças impressas em 3D
- Aumente o Nº de células se a superfície interna parecer rugosa ou facetada
- O esvaziamento cria um fundo aberto -- combine com um [Cubo](../../primitives/cube.md) se precisar de uma base fechada
- Em formas complexas, o cálculo pode demorar alguns segundos

## Relacionado

- [Corte por Plano](plane-cut.md) - Recortar um objeto a uma altura específica
- [Subtrair](../boolean/subtract.md) - Remover material manualmente
