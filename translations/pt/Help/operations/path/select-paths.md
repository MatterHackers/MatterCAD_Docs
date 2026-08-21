---
title: Selecionar caminhos
articleKey: SelectPathsObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: f7df7bb24841030643e4634febedcfce6e92ada9
source_lang: en
---
# Selecionar caminhos

O Selecionar caminhos filtra quais subcaminhos de um objeto de caminho complexo são mantidos. É especialmente útil ao trabalhar com fontes decorativas ou de várias partes, nas quais você precisa das formas externas das letras e das formas de recorte internas como peças separadas — por exemplo, para imprimi-las em 3D em duas cores diferentes.

<!--  Screenshot showing Select Paths applied to decorative text with outer paths highlighted -->
![20260506 154655 paste 20260506 154655](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154655-paste-20260506-154655.jpg)

## Como Funciona a Profundidade do Caminho

Quando um objeto de caminho contém formas com áreas fechadas (como o interior da letra "O" ou o vazio de uma espiral decorativa), essas áreas fechadas são **furos** na profundidade 1. O contorno externo de cada letra ou forma está na **profundidade 0**.

```
Depth 0 — outer contour of each letter or shape
Depth 1 — first level of enclosed holes (inside an "O", "A", etc.)
Depth 2 — shapes nested inside a hole (rarely used)
```

## Predefinições de Filtro

### Tudo
Inclui todos os caminhos sem alterações. Esta é a opção padrão e equivale a não aplicar o Selecionar caminhos.

### Apenas Caminhos Externos
Mantém somente o contorno externo de cada forma (profundidade == 0). Use isto para obter apenas os contornos das letras de uma fonte decorativa, sem as áreas de recorte internas.

### Apenas Furos
Mantém somente os furos fechados (profundidade > 0). Use isto para obter apenas as áreas de corte internas de letras e formas.

### Por Índice de Grupo
Mantém somente os caminhos pertencentes a uma forma desconectada. O grupo 0 é a primeira forma, o grupo 1 é a segunda, e assim por diante. Use isto para isolar um único caractere de uma palavra.

### Personalizado
Escreva uma expressão que é avaliada para cada caminho. O caminho é **incluído** quando a expressão é diferente de zero e **excluído** quando é zero.

As expressões devem começar com `=` para ativar a substituição de variáveis. Sem `=`, o valor é tratado como um número simples (por exemplo, `1` sempre inclui, `0` sempre exclui).

## Exemplos de Expressões Personalizadas

| Expressão | Efeito |
|------------|--------|
| `=PathDepth==0` | Apenas contornos externos (igual a Apenas Caminhos Externos) |
| `=PathDepth>0` | Apenas furos (igual a Apenas Furos) |
| `=GroupIndex==0` | Apenas a primeira forma desconectada |
| `=PathArea>100` | Formas com área maior que 100 mm² |
| `=PathLength>50` | Formas com perímetro maior que 50 mm |

## Variáveis de Expressões Personalizadas

| Variável | Significado |
|----------|---------|
| `PathDepth` | 0 = contorno externo; 1+ = furo ou forma aninhada |
| `GroupIndex` | Índice da forma desconectada (0, 1, 2…) |
| `GroupOuterArea` | Área do caminho externo deste grupo |
| `GroupOuterLength` | Perímetro do caminho externo deste grupo |
| `ChildCount` | Número de furos dentro do caminho externo deste grupo |
| `PathIndex` | Índice sequencial deste caminho dentro do seu grupo |
| `PathArea` | Área deste caminho individual |
| `PathLength` | Perímetro deste caminho individual |

## Exemplo: Impressão de Fonte Natalina Multicolorida

Um uso comum do Selecionar caminhos é imprimir textos decorativos em que as letras têm formas de recorte internas. Para imprimir as letras externas em uma cor e os recortes internos em uma segunda cor:

1. Adicione um objeto **Texto** e defina-o como **saída 2D**
2. Aplique **Selecionar caminhos** → defina a predefinição como **Apenas Caminhos Externos**
3. Aplique **Extrusão Linear** para dar altura a ele → atribua a cor do seu primeiro filamento
4. Volte ao objeto de texto original
5. Aplique um segundo **Selecionar caminhos** → defina a predefinição como **Apenas Furos**
6. Aplique **Extrusão Linear** com a mesma altura → atribua a cor do seu segundo filamento
7. Posicione um objeto extrudado sobre o outro — as duas cores se alinham perfeitamente

## Relacionados

- [Extrusão Linear](linear-extrude.md) — Dê altura aos caminhos filtrados para criar um objeto 3D
- [Revolucionar](revolve.md) — Gire os caminhos filtrados em torno de um eixo
- [Objeto SVG](../../primitives/svg-object.md) — Importe caminhos vetoriais que podem conter vários subcaminhos
- [Texto](../../primitives/text.md) — Objetos de texto no modo 2D produzem saída com múltiplos caminhos
