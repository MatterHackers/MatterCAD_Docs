---
title: Caminho Personalizado
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
source_hash: 3633c708477de3ac77d3547b730c33f7e4431cf6
source_lang: en
---
# Caminho Personalizado

Desenhe seu próprio caminho 2D com pontos de controle. Isso lhe dá total liberdade para criar qualquer forma 2D que possa depois ser extrudada ou revolucionada em um objeto 3D.

<!-- Screenshot showing a custom path being edited with control points -->
![20260506 080247 paste 20260506 080247](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080247-paste-20260506-080247.jpg)


## Como Usar

1. Adicione um **Caminho Personalizado** da biblioteca de Caminhos 2D
2. Edite os pontos de controle para definir sua forma
3. Aplique [Extrusão Linear](../operations/path/linear-extrude.md) ou outras operações de caminho para criar um objeto 3D

## Caminhos Abertos e Fechados

A caixa de seleção **Fechado** controla se o caminho une seu último ponto de volta ao primeiro.

- **Fechado** (o padrão) faz com que o caminho delimite uma região. É isso que a [Extrusão Linear](../operations/path/linear-extrude.md) e o [Revolucionar](../operations/path/revolve.md) preenchem.
- **Abrir** transforma o caminho em uma linha. Uma linha não delimita nada, então ela aparece na cena como uma fita fina ao longo de seu comprimento, e não como uma forma preenchida. Use [Inflar Caminho](../operations/path/inflate-path.md) para dar-lhe uma largura e transformá-la novamente em algo sólido.

Duas coisas a saber antes de desmarcar **Fechado**:

- **Fechar novamente não é um desfazer.** Abrir um caminho descarta seu segmento de fechamento. Se esse segmento era curvo, marcar **Fechado** de novo traz de volta uma linha reta, não a curva. Use Ctrl+Z em vez disso - desfazer restaura o caminho original exatamente.
- **Alguns contornos se recusam a abrir.** Um contorno que ficaria com menos de dois pontos - uma gota desenhada como um único ponto e uma curva que volta até ele - permanece fechado em vez de colapsar em algo que você não conseguiria mais ver ou clicar. O mesmo vale para um contorno que contenha uma curva quadrática, o que um SVG importado pode conter: abri-lo achataria a curva em um canto. A recusa é por contorno, portanto o restante do caminho ainda abre.

Se um caminho tem vários contornos e eles não concordam entre si, a caixa de seleção é exibida como aberta. Marcá-la alinha todos os contornos.

Operações que precisam de uma região fecharão um caminho aberto para você em vez de recusá-lo. Extrusão Linear, Revolucionar, Subtrair e as demais operações booleanas fazem isso, então um caminho aberto extruda para o mesmo sólido que sua versão fechada geraria.

## Dicas

- Use o Caminho Personalizado quando nenhuma das formas de caminho integradas corresponder ao que você precisa
- Para importar formas de editores vetoriais externos, veja [Objeto SVG](../primitives/svg-object.md)
- Para desenhar uma linha e transformá-la em uma peça, desmarque **Fechado**, aplique [Inflar Caminho](../operations/path/inflate-path.md) para dar-lhe espessura e depois [Extrusão Linear](../operations/path/linear-extrude.md) para dar-lhe altura

## Relacionados

- [Caminho de Círculo](circle-path.md) - Um círculo pronto
- [Caminho de Caixa](box-path.md) - Um retângulo pronto
- [Objeto SVG](../primitives/svg-object.md) - Importar caminhos vetoriais de arquivos SVG
- [Extrusão Linear](../operations/path/linear-extrude.md) - Dar altura aos caminhos
