---
title: Expressões
parent: "Workspace"
nav_order: 2
source_hash: 79a2f2c42d81f7fca56a87ad89f69e4303ed0ae5
source_lang: en
---
# Expressões

Muitos parâmetros no MatterCAD aceitam expressões matemáticas em vez de números simples. Isso possibilita o design paramétrico, no qual alterar um valor atualiza automaticamente as dimensões relacionadas.

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)


## Como Usar

Em vez de digitar um número simples em um campo de parâmetro, você pode digitar uma expressão matemática. Por exemplo:

- `20 + 5` resulta em 25
- `pi * 10` resulta em 31,416
- `width * 2` faz referência a outro parâmetro chamado "width"

## Constantes Disponíveis

- **pi** - 3,14159... (a razão entre a circunferência e o diâmetro)
- **tau** - 6,28318... (2 * pi, uma revolução completa em radianos)

## Operações Suportadas

- Adição: `+`
- Subtração: `-`
- Multiplicação: `*`
- Divisão: `/`
- Parênteses: `(` e `)` para agrupamento

## Dicas

- As expressões são suportadas em qualquer campo que mostre `DoubleOrExpression`, `IntOrExpression` ou `StringOrExpression` no código -- na prática, a maioria dos campos numéricos das ferramentas de design as aceita
- Use expressões para criar relações entre parâmetros -- por exemplo, defina o diâmetro de um furo como `outer_diameter - 4` para que ele sempre tenha paredes de 2 mm
- As expressões são atualizadas automaticamente quando os valores referenciados mudam
- Use uma [Planilha de Variáveis](variable-sheet.md) quando vários objetos devem compartilhar os mesmos valores nomeados ou fórmulas
- Você pode usar expressões em operações de [Matriz](../operations/array/index.md) para criar padrões paramétricos

## Relacionados

- [Componentes](components.md) - Criar designs parametrizados reutilizáveis
- [Planilha de Variáveis](variable-sheet.md) - Armazene valores e fórmulas compartilhados em um design
- [Editar Objetos](../getting-started/editing-objects.md) - Trabalhando com parâmetros de objetos
