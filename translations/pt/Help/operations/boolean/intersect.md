---
title: Intersectar
articleKey: IntersectionObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b997cfc4f6d2f02559346365311f217388a6a2da
source_lang: en
---
# Intersectar

Intersectar mantém apenas o volume que todos os objetos compartilham e descarta o restante.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->
![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)

[Combinar](combine.md), [Subtrair](subtract.md), Intersectar e [Subtrair e Substituir](subtract-and-replace.md) são todos realizados por um único objeto booleano -- o botão da barra de ferramentas o cria já com Intersectar selecionado, e você pode alternar para qualquer uma das outras três a qualquer momento na linha de ícones **Operação**, no topo do painel Propriedades.

Intersectar funciona com sólidos e com caminhos 2D. Ele analisa o que você forneceu e executa o tipo certo de operação, de modo que intersectar dois caminhos produz um caminho e intersectar duas malhas produz um sólido.

## Como Usar

1. Selecione dois ou mais objetos
2. Clique em **Intersectar** na barra de ferramentas
3. Mude de ideia a qualquer momento clicando em um ícone diferente na linha **Operação**, no topo do painel Propriedades -- a forma é reconstruída com a nova operação

## Parâmetros

- **Operação** - Qual booleana executar. Exibida como uma linha de ícones no topo do painel
- **Manter Geometria Invertida** - Trata uma casca invertida como material sólido em vez de deixá-la anular o volume ao seu redor. Ative isso quando um modelo que deveria ser sólido retornar com partes faltando. Isso força o mecanismo booleano exato, que é mais lento
- **Reparar Ordem de Enrolamento** - Reinverte as cascas invertidas de cada parte antes de a booleana ser executada. Isso corrige a geometria de uma vez, em vez de mudar o que cada operação posterior considera sólido, e costuma ser a melhor das duas respostas para um modelo invertido

## Dicas

- Os objetos precisam se sobrepor. Se eles não se sobrepuserem de fato, o resultado é vazio
- Com mais de dois objetos, o processo segue a lista: os dois primeiros são intersectados, depois esse resultado é intersectado com o terceiro, e assim por diante
- Se um resultado parecer errado, verifique se os objetos de origem são estanques. **Reparar Ordem de Enrolamento** corrige cascas invertidas; [Reparar](../mesh/repair.md) corrige danos mais amplos em modelos importados

## Relacionados

- [Combinar](combine.md) - Mescla vários objetos em uma única forma sólida
- [Subtrair](subtract.md) - Recorta uma forma de dentro de outra
- [Subtrair e Substituir](subtract-and-replace.md) - Subtrai uma forma e mantém a peça que foi removida
- [Corte por Plano](../reshape/plane-cut.md) - Corta com um plano em vez de outra forma
- [Reparar](../mesh/repair.md) - Corrige malhas importadas danificadas antes de uma booleana

Esta página também abrange os objetos Interseção mais antigos, ainda encontrados em projetos salvos antes de as operações serem mescladas. Eles continuam funcionando exatamente como antes; novos projetos usam o objeto booleano compartilhado com a operação Intersectar selecionada.
