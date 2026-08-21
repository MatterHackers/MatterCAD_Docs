---
title: Objeto SVG
articleKey: SvgObject3D
parent: "Primitives"
nav_order: 15
source_hash: dab97cdde74d938b5612d959f83b54b4a04a49da
source_lang: en
---
# Objeto SVG

Importe arquivos SVG (Scalable Vector Graphics) e use-os como caminhos 2D no seu projeto. Os SVGs podem então ser extrudados em formas 3D usando [Extrusão Linear](../operations/path/linear-extrude.md) ou [Revolucionar](../operations/path/revolve.md).

<!--  Screenshot showing an imported SVG path being extruded into a 3D shape -->
![20260318 184807 paste 20260318 184807](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184807-paste-20260318-184807.jpg)



## Como Usar

1. Importe um arquivo SVG arrastando-o para a área de trabalho ou usando o botão Abrir
2. O SVG é importado como um caminho 2D
3. Aplique [Extrusão Linear](../operations/path/linear-extrude.md) para dar altura a ele, ou use outras [Operações de Caminho](../operations/path/index.md)

## Dicas

- Os arquivos SVG devem conter formas preenchidas ou caminhos fechados para obter melhores resultados
- SVGs complexos com muitos caminhos podem levar mais tempo para serem processados
- Use [Selecionar caminhos](../operations/path/select-paths.md) para trabalhar com partes específicas de um SVG com múltiplos caminhos
- Muitos arquivos SVG gratuitos estão disponíveis online para logotipos, ícones e padrões decorativos

## Relacionados

- [Imagem para Caminho](../operations/image/image-to-path.md) - Converta imagens raster em caminhos em vez de usar SVG
- [Texto](text.md) - Crie texto diretamente sem precisar de um SVG
- [Extrusão Linear](../operations/path/linear-extrude.md) - Dê altura a caminhos planos
- [Caminhos 2D](../2d-paths/index.md) - Primitivas de caminho integradas
