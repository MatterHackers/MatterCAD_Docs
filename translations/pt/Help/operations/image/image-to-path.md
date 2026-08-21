---
title: Imagem para Caminho
articleKey: ImageToPathObject3D_2
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 0145587f635ede68bfc1df37b4f0d366a03d3a6c
source_lang: en
---
# Imagem para Caminho

A operação Imagem para Caminho traça os contornos de uma imagem para criar caminhos 2D. Esses caminhos podem então ser extrudados, revolucionados ou usados com qualquer outra operação de caminho. É ideal para converter logotipos, silhuetas e gráficos simples em objetos 3D.

![20260324 075521 paste 20260324 075521](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-075521-paste-20260324-075521.jpg)


## Como Usar

1. Selecione um objeto de imagem no seu espaço de trabalho
2. Aplique **Imagem para Caminho** no menu de operações de Imagem
3. Escolha o tipo de análise e ajuste o intervalo de seleção

## Parâmetros

- **Tipo de Análise** - Como a imagem é analisada para o traçado:
  - **Transparência** - Traça com base em áreas transparentes vs. opacas (melhor para PNGs com fundos transparentes)
  - **Cores** - Traça com base em regiões de cor
  - **Intensidade** - Traça com base nos níveis de brilho (melhor para a maioria das imagens)
- **Selecionar intervalo** - Um controle de histograma para selecionar quais valores de brilho/cor incluir no traçado
- **Área Mínima de Superfície** - Área mínima para que um laço de caminho seja incluído. Aumente para filtrar pequenos artefatos de ruído

## Dicas

- Imagens limpas, de alto contraste e com formas simples funcionam melhor
- Use o modo Transparência para imagens PNG com fundos transparentes
- Use o modo Intensidade para fotografias e imagens sem transparência
- Após traçar, aplique [Extrusão Linear](../path/linear-extrude.md) para dar altura ao caminho
- Aumente a Área Mínima de Superfície para remover pequenos detalhes indesejados do traçado

## Relacionados

- [Conversor de Imagem](image-converter.md) - Crie relevo por mapa de altura em vez de caminhos planos
- [Litofania](lithophane.md) - Crie exibições de imagem retroiluminadas
- [Objeto SVG](../../primitives/svg-object.md) - Importe gráficos vetoriais diretamente (sem necessidade de traçado)
- [Extrusão Linear](../path/linear-extrude.md) - Dê altura ao caminho traçado
