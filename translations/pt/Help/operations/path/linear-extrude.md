---
title: Extrusão Linear
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cdfdb9cfe4c3339e70a23ddfb2f5071b1e8c5557
source_lang: en
---
# Extrusão Linear

A Extrusão Linear dá altura a um caminho 2D, transformando uma forma plana num sólido 3D. Esta é a principal maneira de converter caminhos em objetos 3D.

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## Como Utilizar

1. Selecione um caminho 2D ou um objeto baseado em caminho
2. Aplique **Extrusão Linear** a partir do menu de operações de Caminho
3. Defina a altura desejada

## Parâmetros

- **Altura** - Qual a altura da extrusão (predefinição: 5mm, intervalo: 0,1-50mm)
- **Chanfrar Topo** - Adiciona uma aresta chanfrada (arredondada) ao topo da extrusão (predefinição: desligado)

### Parâmetros de Chanfro (visíveis quando Chanfrar Topo está ativado)

- **Estilo** - O estilo do perfil do chanfro (Vivo ou arredondado)
- **Raio** - Qual a largura de extensão do chanfro (predefinição: 3mm)
- **Segmentos** - Suavidade da curva do chanfro (predefinição: 9)

## Dicas

- Isto funciona com qualquer caminho 2D: caminhos [Círculo](../../2d-paths/circle-path.md), [Caixa](../../2d-paths/box-path.md), [Estrela](../../2d-paths/star-path.md), [SVG](../../primitives/svg-object.md) e [Personalizado](../../2d-paths/custom-path.md)
- Ative Chanfrar Topo para um aspeto mais refinado e profissional
- Para revolucionar um caminho em torno de um eixo em vez de o extrudar a direito, consulte [Revolucionar](revolve.md)

## Relacionado

- [Revolucionar](revolve.md) - Gira um caminho em torno de um eixo
- [Caminhos 2D](../../2d-paths/index.md) - Formas de caminho disponíveis
- [Texto](../../primitives/text.md) - O texto é extrudado automaticamente
