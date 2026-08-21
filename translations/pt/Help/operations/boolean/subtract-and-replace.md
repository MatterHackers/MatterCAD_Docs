---
title: Subtrair e Substituir
articleKey: SubtractAndReplaceObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c1698bab75faca8046b23cc148803c8063ba0678
source_lang: en
---
# Subtrair e Substituir

Subtrair e Substituir subtrai as peças que você escolher das peças que não escolheu, mas mantém o pedaço que foi recortado como uma peça própria em vez de descartá-lo. Use **Peça(s) a Subtrair** para escolher as formas de corte; todo o restante é a base que será recortada.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->
![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)

[Combinar](combine.md), [Subtrair](subtract.md), [Intersectar](intersect.md) e Subtrair e Substituir são todas executadas por um único objeto booleano -- o botão da barra de ferramentas o cria já com Subtrair e Substituir selecionado, e você pode alternar para qualquer uma das outras três a qualquer momento na linha de ícones **Operação**, no topo do painel Propriedades.

Subtrair e Substituir não é oferecido para caminhos 2D -- uma região não tem volume removido para devolver.

## Como Usar

1. Selecione dois ou mais objetos
2. Clique em **Subtrair e Substituir** na barra de ferramentas
3. Use **Peça(s) a Subtrair** para escolher quais filhos são as formas de corte
4. Mude de ideia a qualquer momento clicando em um ícone diferente na linha **Operação**, no topo do painel Propriedades -- a forma é reconstruída com a nova operação

## Parâmetros

- **Operação** - Qual booleana executar. Exibida como uma linha de ícones no topo do painel
- **Peça(s) a Subtrair** - Quais filhos são as formas de corte
- **Manter Geometria Invertida** - Trata uma casca invertida como material sólido em vez de deixá-la anular o volume ao seu redor. Ative isto quando um modelo que deveria ser sólido retorna com partes faltando. Isso força o motor booleano exato, que é mais lento
- **Reparar Ordem de Enrolamento** - Reinverte as cascas invertidas de cada peça antes de a booleana ser executada. Isso corrige a geometria de uma vez, em vez de mudar o que cada operação posterior considera sólido, e normalmente é a melhor das duas respostas para um modelo invertido

## Dicas

- As duas peças se encaixam exatamente, porque saíram da mesma operação
- Use isto para projetos multicoloridos, montagens que se encaixam e embutidos
- Se um resultado parecer errado, verifique se os objetos de origem são estanques. **Reparar Ordem de Enrolamento** corrige cascas invertidas; [Reparar](../mesh/repair.md) corrige danos mais amplos em modelos importados

## Relacionados

- [Combinar](combine.md) - Mescla vários objetos em uma única forma sólida
- [Subtrair](subtract.md) - Recorta uma forma de dentro de outra
- [Intersectar](intersect.md) - Mantém apenas o volume onde os objetos se sobrepõem
- [Corte por Plano](../reshape/plane-cut.md) - Recorta com um plano em vez de outra forma
- [Reparar](../mesh/repair.md) - Corrige malhas importadas danificadas antes de uma booleana

Esta página também abrange os objetos Subtrair e Substituir mais antigos, ainda encontrados em projetos salvos antes de as operações serem mescladas. Eles continuam funcionando exatamente como antes; projetos novos usam o objeto booleano compartilhado com a operação Subtrair e Substituir selecionada.
