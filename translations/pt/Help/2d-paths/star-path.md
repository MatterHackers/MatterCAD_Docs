---
title: Caminho de Estrela
articleKey: StarPathObject3D
parent: "2D Paths"
nav_order: 5
source_hash: 74d92e4171c452cd10069921636e45d7ef9dc70e
source_lang: en
---
# Caminho de Estrela

Um caminho 2D em forma de estrela com número de pontas e raio interno/externo configuráveis. Use com [Extrusão Linear](../operations/path/linear-extrude.md) para criar formas de estrela em 3D.

<!-- Screenshot of a Star Path on the workspace -->
![20260506 080319 paste 20260506 080319](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080319-paste-20260506-080319.jpg)


## Parâmetros

- **Pontos** - Número de pontas da estrela
- **Raio Externo** - Distância do centro até a ponta de cada vértice
- **Raio Interno** - Distância do centro até os vales entre as pontas

## Dicas

- A proporção entre o Raio Interno e o Raio Externo determina o quanto a estrela é "pontiaguda". Um Raio Interno pequeno cria pontas afiadas e pronunciadas.
- Defina Pontos como 5 para uma estrela clássica, 6 para uma Estrela de Davi ou valores maiores para formas semelhantes a engrenagens
- Use [Suavizar Caminho](../operations/path/smooth-path.md) em um Caminho de Estrela para criar formas de estrela arredondadas

## Relacionados

- [Caminho de Círculo](circle-path.md) - Um círculo suave
- [Engrenagem 2D](../mechanical/gear-2d.md) - Um perfil de engrenagem adequado
- [Extrusão Linear](../operations/path/linear-extrude.md) - Dá altura aos caminhos
