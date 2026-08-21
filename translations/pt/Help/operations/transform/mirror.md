---
title: Espelhar
articleKey: MirrorObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 8a8de28f5e429177d4b0092d0756387eb6b83a70
source_lang: en
---
# Espelhar

Espelhar cria uma cópia refletida de um objeto em relação a um dos três eixos principais. O resultado é uma versão espelhada da forma original.

<!--  Before and after showing an object mirrored across the X axis -->
![20260506 160651 paste 20260506 160651](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160651-paste-20260506-160651.jpg)


## Como usar

1. Selecione um objeto
2. Aplique a operação **Espelhar** no menu Transformar
3. Escolha em qual eixo espelhar

## Parâmetros

- **Espelhamento ativado** - O eixo em relação ao qual espelhar:
  - **Eixo X** - Inverte o objeto da esquerda para a direita
  - **Eixo Y** - Inverte o objeto da frente para trás
  - **Eixo Z** - Inverte o objeto de cima para baixo

## Dicas

- O espelhamento é centralizado na caixa delimitadora do objeto, portanto o resultado espelhado ocupa o mesmo espaço que o original
- As normais das faces são corrigidas automaticamente após o espelhamento para manter a renderização correta
- Use Espelhar para criar designs simétricos -- modele uma metade, depois espelhe-a e use [Combinar](../boolean/combine.md) com o original
- Espelhar é não destrutivo: você pode alterar o eixo de espelhamento a qualquer momento

## Relacionados

- [Rotacionar](rotate.md) - Rotacione um objeto em vez de espelhá-lo
- [Escala](scale.md) - Redimensione um objeto
- [Combinar](../boolean/combine.md) - Mescle o original e a cópia espelhada em um único objeto
