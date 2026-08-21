---
title: Combinar
articleKey: CombineObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: a3066faa634b5a88a2fe1650a4e2ac278ac50e24
source_lang: en
---
# Combinar

Combinar une tudo em um único sólido. As faces internas onde as formas se sobrepunham são removidas, de modo que o resultado é uma malha contínua em vez de cascas sobrepostas.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->
![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)

Combinar, [Subtrair](subtract.md), [Intersectar](intersect.md) e [Subtrair e Substituir](subtract-and-replace.md) são todas executadas por um único objeto booleano -- o botão da barra de ferramentas o cria já com Combinar selecionado, e você pode alternar para qualquer uma das outras três a qualquer momento na linha de ícones **Operação**, no topo do painel Propriedades.

Combinar funciona com sólidos e com caminhos 2D. Ele analisa o que você forneceu e executa o tipo correto de operação, de modo que combinar dois caminhos produz um caminho e combinar duas malhas produz um sólido.

## Como Usar

1. Selecione dois ou mais objetos
2. Clique em **Combinar** na barra de ferramentas
3. Mude de ideia a qualquer momento clicando em um ícone diferente na linha **Operação**, no topo do painel Propriedades -- a forma é reconstruída com a nova operação

## Parâmetros

- **Operação** - Qual operação booleana executar. Exibida como uma linha de ícones no topo do painel
- **Manter Geometria Invertida** - Trata uma casca invertida como material sólido em vez de deixá-la anular o volume ao seu redor. Ative esta opção quando um modelo que deveria ser sólido apresentar partes faltando. Isso força o uso do motor booleano exato, que é mais lento
- **Reparar Ordem de Enrolamento** - Reinverte as cascas invertidas de cada peça antes da execução da operação booleana. Isso corrige a geometria de uma vez, em vez de alterar o que cada operação posterior considera sólido, e normalmente é a melhor das duas respostas para um modelo invertido

## Dicas

- Combinar ainda unirá objetos que não se sobrepõem em uma única malha, mas eles permanecem visualmente separados
- Combinar trata os objetos Furo para você: tudo o que estiver marcado como furo é subtraído do resultado em vez de adicionado a ele
- Combinar transfere as cores por face dos objetos originais
- Se um resultado parecer errado, verifique se os objetos de origem são estanques. **Reparar Ordem de Enrolamento** corrige cascas invertidas; [Reparar](../mesh/repair.md) corrige danos mais amplos em modelos importados

## Relacionados

- [Subtrair](subtract.md) - Recorta uma forma de dentro de outra
- [Intersectar](intersect.md) - Mantém apenas o volume onde os objetos se sobrepõem
- [Subtrair e Substituir](subtract-and-replace.md) - Subtrai uma forma e mantém a peça que foi removida
- [Corte por Plano](../reshape/plane-cut.md) - Corta com um plano em vez de outra forma
- [Furo](../../primitives/hole.md) - Um cubo pré-configurado para subtrair
- [Reparar](../mesh/repair.md) - Corrige malhas importadas danificadas antes de uma operação booleana

Esta página também abrange os objetos Combinar mais antigos ainda encontrados em projetos salvos antes da unificação das operações. Eles continuam funcionando exatamente como antes; novos projetos usam o objeto booleano compartilhado com a operação Combinar selecionada.
