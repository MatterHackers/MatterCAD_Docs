---
title: Conversor de Imagem
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c1a05f9688ebe115babfad5d63fc49445af7c449
source_lang: en
---
# Conversor de Imagem

O Conversor de Imagem transforma uma imagem raster em um relevo 3D no qual o brilho dos pixels determina a altura. As áreas claras tornam-se elevadas e as áreas escuras tornam-se baixas (ou vice-versa).

![20260323 210414 paste 20260323 210414](https://matterhackers.github.io/MatterCAD_Docs/assets/20260323-210414-paste-20260323-210414.jpg)


## Como Usar

1. Adicione um Conversor de Imagem a partir do painel Primitivas, ou arraste um arquivo de imagem para o espaço de trabalho
2. A imagem é convertida em um mapa de altura 3D
3. Ajuste a altura e os demais parâmetros

## Dicas

- Imagens de alto contraste com formas bem definidas produzem os melhores resultados
- Para traçar os contornos da imagem como caminhos planos em vez de mapas de altura, use [Imagem para Caminho](image-to-path.md)
- Para criar exibições de imagem retroiluminadas, use [Litofania](lithophane.md)
- Você pode arrastar imagens diretamente da sua área de trabalho para o espaço de trabalho
- Adicione uma base combinando o relevo da imagem com um [Cubo](../../primitives/cube.md)

## Relacionados

- [Imagem para Caminho](image-to-path.md) - Traçar contornos em vez de criar um mapa de altura
- [Litofania](lithophane.md) - Criar exibições de imagem retroiluminadas
- [Objeto Imagem](../../primitives/image-object.md) - A versão primitiva da importação de imagem
