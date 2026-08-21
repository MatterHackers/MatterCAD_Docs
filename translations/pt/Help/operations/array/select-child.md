---
title: Selecionar filho
articleKey: SelectChildObject3D
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: f6f71d2b457b82126f272ea9354f877c36570df0
source_lang: en
---
# Selecionar filho

Selecionar filho escolhe um filho de um grupo de objetos com base em um número de índice ou em um nome. Isso é especialmente útil em projetos com scripts e paramétricos, nos quais você deseja escolher dinamicamente qual objeto exibir.

<!-- IMAGE: Screenshot showing Select Child operation with multiple children and one selected by index -->
![20260506 080526 paste 20260506 080526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080526-paste-20260506-080526.jpg)


## Como usar

1. Selecione dois ou mais objetos
2. Aplique a operação **Selecionar filho** no menu Duplicação
3. Escolha **Por Índice** ou **Por Nome** para controlar como o filho é selecionado
4. Defina o número de índice ou o nome a ser correspondido

## Parâmetros

- **Método de seleção** - Escolha entre **Por Índice** (selecionar pela posição) ou **Por Nome** (selecionar pelo nome do objeto). Exibido como botões.
- **Índice Filho** - O índice de base zero do filho a ser selecionado (exibido ao usar Por Índice). Suporta [expressões](../../workspace/expressions.md).
- **Nome do Filho** - O nome do filho a ser selecionado (exibido ao usar Por Nome). Suporta [expressões](../../workspace/expressions.md).

Se o índice estiver fora do intervalo ou o nome não corresponder a nenhum filho, o primeiro filho é retornado como alternativa. Se não houver filhos, nada é retornado.

## Uso em Scripts

Selecionar filho foi projetado para funcionar com expressões e com a função `rand()` para criar projetos dinâmicos e orientados a dados. Por exemplo, você pode montar uma cena com vários objetos variantes como filhos e usar uma expressão como `rand(42)` como semente do índice para escolher um aleatoriamente.

**Exemplo: adereços de livros aleatórios para um espetáculo teatral**

1. Importe 5 malhas de livros diferentes como filhos de uma operação Selecionar filho
2. Defina o Método de seleção como **Por Índice**
3. Use uma expressão para o Índice Filho, como `floor(rand(seed) * 5)`, em que `seed` é uma variável de planilha
4. Duplique a operação Selecionar filho várias vezes, cada uma com um valor de semente diferente
5. Cada instância escolhe aleatoriamente um livro diferente do conjunto

Esse padrão funciona para qualquer cenário em que você precise escolher entre um conjunto de variantes: móveis, decorações, elementos arquitetônicos ou qualquer coleção de peças intercambiáveis.

## Dicas

- Combine com [Matriz](array.md) para criar padrões variados em que cada cópia seleciona um filho diferente
- Use variáveis de planilha para o índice ou o nome, para controlar a seleção a partir de uma planilha
- O comportamento de recorrer ao primeiro filho significa que seu projeto nunca quebra, mesmo que o índice ou o nome esteja errado

## Relacionados

- [Matriz](array.md) - Duplicar objetos em padrões lineares, radiais, por curva e por transformação
