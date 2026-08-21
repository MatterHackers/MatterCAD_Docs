---
title: Rotacionar
articleKey: RotateObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 9bdc210c5c375fe3179050e8a8916d895455ce5f
source_lang: en
---
# Rotacionar

Rotacionar gira um objeto em torno de um eixo especificado por um determinado ângulo. Você pode rotacionar em torno de qualquer direção de eixo e escolher o ponto central da rotação.

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## Como Usar

1. Selecione um objeto
2. Aplique a operação **Rotacionar** no menu Transformar
3. Defina o ângulo e o eixo de rotação no painel Propriedades

Você também pode rotacionar objetos diretamente na viewport clicando nos controles de canto de rotação de um objeto selecionado. Mover o mouse sobre os indicadores de ângulo faz o encaixe em incrementos de 45 graus.

## Parâmetros

- **Ângulo** - O ângulo de rotação em graus (intervalo: 3-360). Suporta [expressões](../../workspace/expressions.md).
- **Rotacionar Em Torno De** - Define o eixo de rotação e o ponto de origem. Você pode rotacionar em torno do eixo X, Y ou Z, ou especificar uma direção personalizada.

## Dicas

- Por padrão, a rotação é centralizada no centro da caixa delimitadora do objeto
- Para rotações de 90 graus, os indicadores de encaixe facilitam a obtenção de valores exatos
- Use a operação Rotacionar (em vez dos controles da viewport) quando precisar de um ângulo preciso que não seja múltiplo de 45 graus
- Você pode alterar o eixo de rotação após aplicar a operação editando a propriedade Rotacionar Em Torno De

## Relacionados

- [Transladar](translate.md) - Mover um objeto por uma distância específica
- [Escala](scale.md) - Redimensionar um objeto
- [Espelhar](mirror.md) - Criar um reflexo espelhado
