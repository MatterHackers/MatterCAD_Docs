---
title: Litofania
articleKey: LithophaneObject3D
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 170d39ef48f6ac290e56917bcaebeb458d55777f
source_lang: en
---
# Litofania

Uma litofania é um painel 3D fino no qual uma imagem é codificada como variações de espessura. Quando iluminada por trás, as áreas mais finas deixam passar mais luz, revelando a imagem. Isso cria uma bela maneira de exibir fotografias e obras de arte.

![20260324 080310 paste 20260324 080310](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080310-paste-20260324-080310.jpg)


## Como Usar

1. Importe uma imagem ou selecione um objeto de imagem existente
2. Aplique a operação **Litofania**
3. Ajuste a resolução e as dimensões
4. Imprima o resultado em um material de cor clara e coloque-o diante de uma fonte de luz

## Parâmetros

- **Pixels Por mm** - Resolução da litofania (padrão: 1,5, intervalo: 0,5-3). Valores mais altos capturam mais detalhes, mas geram arquivos maiores
- **Altura** - Espessura máxima do painel da litofania (padrão: 2,5 mm, intervalo: 0,5-3 mm)
- **Largura** - Largura total da litofania em pixels (padrão: 150)
- **Inverter** - Inverte o mapeamento de claro/escuro (padrão: ativado). Normalmente mantido ativado para exibição correta quando iluminada por trás

## Dicas

- Imprima em material branco ou de cor clara para obter os melhores resultados
- Uma altura de 2-3 mm funciona bem para a maioria das litofanias
- Valores maiores de Pixels Por mm capturam mais detalhes, mas aumentam o tempo de impressão e o tamanho do arquivo
- Monte a impressão finalizada em uma moldura com iluminação traseira de LED para melhor visibilidade
- Fotos de retrato com bom contraste funcionam especialmente bem

## Relacionados

- [Conversor de Imagem](image-converter.md) - Crie um relevo elevado a partir de imagens
- [Imagem para Caminho](image-to-path.md) - Trace os contornos da imagem como caminhos
