---
title: Escala
articleKey: ScaleObject3D_3
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b3b5419c3db29550b2544bb6aca91ca3ce6fa715
source_lang: en
---
# Escala

A Escala redimensiona um objeto com controle preciso sobre dimensões, proporções e conversão de unidades. Você pode escalar uniformemente, bloquear eixos específicos em conjunto ou redimensionar cada eixo de forma independente.

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## Como Usar

1. Selecione um objeto
2. Aplique a operação **Escala** no menu Transformar
3. Escolha o método de escala e insira os valores desejados

Você também pode escalar objetos na janela de visualização clicando e arrastando os controles de canto de escala em um objeto selecionado.

## Parâmetros

### Tipo de Escala

Escolha uma predefinição ou uma escala personalizada:

- **Personalizado** - Insira suas próprias dimensões ou porcentagens
- **Polegadas para mm** - Multiplica por 25,4 (converte imperial para métrico)
- **mm para polegadas** - Multiplica por 0,0393 (converte métrico para imperial)
- **mm para cm** - Multiplica por 0,1
- **cm para mm** - Multiplica por 10

### Método de escala (modo Personalizado)

- **Direto** - Insira a Largura, a Profundidade e a Altura desejadas em milímetros
- **Porcentagem** - Insira a Largura, a Profundidade e a Altura como porcentagens do tamanho original

### Bloquear Proporção

- **Nenhum (Escalar livremente)** - Cada eixo é escalado de forma independente
- **X e Y** - Largura e Profundidade ficam bloqueadas juntas; a Altura é escalada de forma independente
- **X, Y e Z** - Os três eixos são escalados uniformemente em conjunto

### Dimensões

- **Largura** - Tamanho ao longo do eixo X
- **Profundidade** - Tamanho ao longo do eixo Y
- **Altura** - Tamanho ao longo do eixo Z

## Dicas

- Use "Polegadas para mm" se você importou um arquivo STL projetado em polegadas e ele aparece pequeno demais
- Defina Bloquear Proporção como X, Y e Z para uma escala uniforme -- alterar qualquer dimensão atualiza todas elas
- A posição da base do objeto é mantida durante a escala, para que ele permaneça sobre a superfície do espaço de trabalho
- Você pode digitar valores exatos para um dimensionamento preciso ou usar os controles deslizantes para ajustes rápidos

## Relacionados

- [Transladar](translate.md) - Mover um objeto
- [Rotacionar](rotate.md) - Rotacionar um objeto
- [Ajustar aos Limites](../placement/fit-to-bounds.md) - Escalar para caber dentro de um tamanho específico
