---
title: Planilha de Variáveis
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
source_hash: 3137a4da2b9d2086d4dcace156435caca288dd79
source_lang: en
---
# Planilha de Variáveis

A Planilha de Variáveis armazena valores compartilhados de um projeto. Use-a quando vários objetos devem referenciar as mesmas dimensões, contagens, rótulos ou fórmulas. Alterar um valor na planilha recalcula os objetos dependentes, de modo que projetos paramétricos permanecem consistentes sem que você precise editar cada objeto individualmente.

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## Como adicionar uma Planilha de Variáveis

1. Abra a biblioteca e adicione **Planilha de Variáveis** à cena.
2. Selecione o objeto Planilha de Variáveis para exibir o editor da planilha.
3. Selecione uma célula e insira um **Nome** e um valor ou fórmula.
4. Use o nome da célula em outros campos do projeto que aceitam expressões.

## Editando células

Cada célula tem duas partes editáveis:

- **Nome** - Um nome de variável opcional para a célula. Os nomes não diferenciam maiúsculas de minúsculas, os espaços são convertidos em sublinhados e nomes duplicados são ajustados automaticamente.
- **Expressão** - O valor da célula. Texto simples ou números são armazenados diretamente. As fórmulas começam com `=`.

As células também podem ser referenciadas por endereço, como `A1` ou `B2`. Células nomeadas costumam ser mais claras para parâmetros de projeto porque descrevem a intenção, como `wall_thickness`, `outer_diameter` ou `hole_count`.

## Fórmulas

Inicie uma fórmula com `=` para que ela seja avaliada na planilha:

- `=20 + 5` retorna `25`
- `=pi * 10` retorna `31.41592653589793`
- `=A1 * 2` referencia outra célula por endereço
- `=wall_thickness + 4` referencia uma célula nomeada

A planilha oferece suporte a operações aritméticas, parênteses, operadores de comparação, funções `Math` comuns como `sin`, `cos`, `sqrt` e `round`, e constantes incluindo `pi`, `tau` e `e`.

## Usando valores da planilha em objetos

A maioria dos campos numéricos do MatterCAD aceita expressões. Para usar um valor da planilha em um parâmetro de objeto, coloque o prefixo `=` na referência:

- Defina a **Largura** de um Cubo como `=case_width`.
- Defina a **Contagem** de uma Matriz como `=hole_count`.
- Defina um valor de **Deslocamento** de Transladar como `=wall_thickness * 2`.

Quando a planilha muda, o MatterCAD recalcula os objetos que dependem dela.

## Texto e funções auxiliares

As células da Planilha de Variáveis podem conter texto além de números. Valores de texto são úteis para rótulos gerados, números de peça, dados importados e aplicativos de projeto personalizados.

Funções auxiliares úteis incluem:

- `concat()` ou `strcat()` - Une textos ou valores.
- `substring()` - Extrai parte de um valor de texto.
- `split()` - Divide o texto e retorna um item.
- `count()` - Conta itens delimitados em um texto.
- `substitute()` - Substitui texto.
- `rand(seed)` - Gera um valor aleatório determinístico quando uma semente é fornecida.
- `importdata()` - Lê um valor de uma URL ou de um caminho de arquivo local.

## Dicas

- Prefira nomes descritivos a endereços de célula para valores usados por outros objetos.
- Mantenha as dimensões principais próximas ao canto superior esquerdo da planilha para encontrá-las facilmente.
- Use fórmulas para valores derivados, como `inner_diameter = outer_diameter - wall_thickness * 2`.
- Evite usar palavras reservadas como `pi`, `e`, `true`, `false` ou nomes de funções como nomes de célula.
- Se uma fórmula não puder ser interpretada, o MatterCAD mantém a entrada original como texto.

## Relacionados

- [Expressões](expressions.md) - Use expressões em parâmetros de objetos
- [Componentes](components.md) - Crie projetos parametrizados reutilizáveis
- [Matriz](../operations/array/array.md) - Crie padrões repetidos controlados por valores da planilha
