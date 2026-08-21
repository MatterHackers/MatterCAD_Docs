---
title: Subtrair
articleKey: SubtractObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 59685bd0a635b70d7f938780f71e90be595dd993
source_lang: en
---
# Subtrair

Subtrair recorta as peças que você escolhe das peças que você não escolheu. Use **Peça(s) a Subtrair** para selecionar as formas de corte; todo o restante é a base que será cortada.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->
![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)

[Combinar](combine.md), Subtrair, [Intersectar](intersect.md) e [Subtrair e Substituir](subtract-and-replace.md) são todos executados por um único objeto booleano -- o botão da barra de ferramentas o cria já com Subtrair selecionado, e você pode alternar para qualquer uma das outras três operações a qualquer momento na linha de ícones **Operação**, no topo do painel Propriedades.

Subtrair funciona com sólidos e com caminhos 2D. Ele analisa o que você forneceu e executa o tipo correto de operação, de modo que subtrair um caminho de outro produz um caminho, e subtrair uma malha de outra produz um sólido.

## Como Usar

1. Selecione dois ou mais objetos
2. Clique em **Subtrair** na barra de ferramentas -- uma peça padrão a ser recortada é escolhida automaticamente, para que algo aconteça imediatamente
3. Use **Peça(s) a Subtrair** para escolher quais filhos são as formas de corte
4. Mude de ideia a qualquer momento clicando em um ícone diferente na linha **Operação**, no topo do painel Propriedades -- a forma é reconstruída com a nova operação

## Parâmetros

- **Operação** - Qual booleano executar. Exibida como uma linha de ícones no topo do painel
- **Peça(s) a Subtrair** - Quais filhos são as formas de corte
- **Manter Peças Subtraídas** - Deixa na cena as peças que foram recortadas, em vez de descartá-las
- **Manter Geometria Invertida** - Trata uma casca invertida como material sólido, em vez de deixá-la anular o volume ao seu redor. Ative esta opção quando um modelo que deveria ser sólido retornar com partes faltando. Isso força o uso do mecanismo booleano exato, que é mais lento
- **Reparar Ordem de Enrolamento** - Reinverte as cascas invertidas de cada peça antes de executar o booleano. Isso corrige a geometria de uma vez, em vez de alterar o que cada operação posterior considera sólido, e costuma ser a melhor das duas soluções para um modelo invertido

## Dicas

- Os objetos precisam se sobrepor para que Subtrair produza algum efeito
- Para criar um furo passante, certifique-se de que o objeto de corte atravesse completamente a base
- Para um furo simples, a primitiva [Furo](../../primitives/hole.md) já vem configurada para subtrair
- Os objetos de corte permanecem na árvore do projeto, então você pode movê-los ou redimensioná-los e o corte é atualizado
- Se um resultado parecer errado, verifique se os objetos de origem são estanques. **Reparar Ordem de Enrolamento** corrige cascas invertidas; [Reparar](../mesh/repair.md) corrige danos mais amplos em modelos importados

## Relacionados

- [Combinar](combine.md) - Mescla vários objetos em uma única forma sólida
- [Intersectar](intersect.md) - Mantém apenas o volume onde os objetos se sobrepõem
- [Subtrair e Substituir](subtract-and-replace.md) - Subtrai uma forma e mantém a peça que foi recortada
- [Corte por Plano](../reshape/plane-cut.md) - Corta com um plano em vez de outra forma
- [Furo](../../primitives/hole.md) - Um cubo pré-configurado para subtrair
- [Reparar](../mesh/repair.md) - Corrige malhas importadas danificadas antes de um booleano

Esta página também abrange os objetos Subtrair mais antigos, ainda encontrados em projetos salvos antes de as operações serem mescladas. Eles continuam funcionando exatamente como antes; novos projetos usam o objeto booleano compartilhado com a operação Subtrair selecionada.
