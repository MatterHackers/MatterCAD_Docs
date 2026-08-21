---
title: Texto
articleKey: TextObject3D_2
parent: "Primitives"
nav_order: 16
source_hash: 526f3190c7b2150243499b5874ac455d74810bb2
source_lang: en
---
# Texto

Crie texto 3D extrudado com conteúdo, fonte, tamanho e altura personalizáveis. Os objetos de texto são ótimos para etiquetas, placas, plaquetas de identificação e letras decorativas.

<!--  Screenshot of a 3D Text object on the workspace showing extruded letters -->
![20260318 184207 paste 20260318 184207](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184207-paste-20260318-184207.jpg)


## Como Usar

1. Adicione uma primitiva **Texto** no painel Primitivas
2. Digite seu texto no campo **Nome** no painel Propriedades
3. Ajuste a fonte, o tamanho e a altura de extrusão conforme necessário

## Parâmetros

- **Nome** - O conteúdo de texto a ser exibido
- **Tamanho do Ponto** - O tamanho da fonte. Isso é preciso em relação ao dimensionamento de impressão padrão -- um tamanho de 12 pontos no MatterCAD corresponde a um tipo de 12 pontos em uma impressora 2D
- **Altura** - A altura de extrusão (o quanto o texto se eleva acima da superfície)
- **Fonte** - Selecione entre as fontes disponíveis no sistema

## Dicas

- Use [Subtrair](../operations/boolean/subtract.md) para gravar o texto em uma superfície em vez de elevá-lo
- Para textos muito pequenos, aumente o Tamanho do Ponto e depois reduza a [Escala](../operations/transform/scale.md) de todo o objeto para obter melhores detalhes
- Cada letra do texto é um caminho separado que é extrudado em conjunto

## Relacionados

- [Braille](braille.md) - Gerar texto em Braille imprimível em 3D
- [Código QR](qr-code.md) - Gerar um código QR como objeto 3D
- [Objeto de Imagem](image-object.md) - Converter imagens em 3D
