---
title: Inflar Caminho
articleKey: InflatePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: c0e11d3d24c5f832f797cde4d392e26a4694733d
source_lang: en
---
# Inflar Caminho

Inflar Caminho expande um caminho 2D para fora, tornando a forma maior e mantendo seu formato geral. Isso é semelhante a aplicar um deslocamento uniforme a todas as arestas.

<!--  Before and after showing a path inflated outward -->
![20260506 100652 paste 20260506 100652](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100652-paste-20260506-100652.jpg)


## Como Usar

1. Selecione um caminho 2D
2. Aplique **Inflar Caminho** a partir do menu de operações de Caminho
3. Ajuste a quantidade de inflação

## Inflando uma Linha Aberta

Inflar é a maneira de transformar uma linha em uma forma. Desmarque **Fechado** em um [Caminho Personalizado](../../2d-paths/custom-path.md) para desenhar uma linha aberta e, em seguida, infle-a: o resultado é uma faixa preenchida tão larga de cada lado da linha quanto a quantidade que você definir. A partir daí, ela é extrudada como qualquer outro caminho.

**Estilo** define como as duas extremidades da linha são fechadas, bem como a forma como seus cantos são unidos:

- **Plano** interrompe a faixa em esquadria em cada ponto final
- **Redondo** adiciona um semicírculo além de cada ponto final
- **Vivo** adiciona um quadrado além de cada ponto final

Uma linha aberta não tem interior para encolher, portanto uma quantidade zero ou negativa não deixaria absolutamente nada. Quando o caminho é *inteiramente* aberto, Inflar limita o valor a um pequeno número positivo e grava o número limitado de volta na caixa, para que você possa ver o que aconteceu.

Um caminho que mistura contornos abertos e fechados não é limitado: os contornos fechados encolhem normalmente e os abertos simplesmente desaparecem. Caminhos fechados continuam encolhendo com valores negativos exatamente como sempre fizeram.

## Dicas

- Use valores negativos para encolher o caminho para dentro em vez de expandi-lo
- Inflar é útil para criar deslocamentos de tolerância ao redor das formas
- Combine com [Caminho do contorno](outline-path.md) para criar bordas com larguras específicas

## Relacionados

- [Caminho do contorno](outline-path.md) - Crie um contorno a partir de um caminho
- [Caminho da Borda](border-path.md) - Adicione um deslocamento de borda
- [Suavizar Caminho](smooth-path.md) - Arredonde os cantos de um caminho
