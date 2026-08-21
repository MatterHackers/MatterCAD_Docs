---
title: Torcer
articleKey: TwistObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: 8ea8d2017c16f20dc42b433bcf91815262bb5380
source_lang: en
---
# Torcer

Torcer gira o topo de um objeto em relação à base, criando um efeito de espiral ou torção ao longo da altura. Por padrão, a rotação avança uniformemente de baixo para cima; em Avançado, você pode desenhar em que pontos da altura a rotação realmente acontece.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## Como Usar

1. Selecione um objeto
2. Aplique a operação **Torcer** no menu Remodelar
3. Defina o ângulo de torção e ajuste o fatiamento para obter suavidade
4. Ative **Avançado** se quiser desenhar como a torção é distribuída ao longo da peça

## O Perfil de Torção

Em Avançado, a curva do **Perfil de Torção** determina onde a torção acontece. A quantidade total de torção continua sendo definida pelo controle Ângulo (ou Distância de Rotação) — a curva apenas a distribui:

- **Ao longo da curva (vertical)** está a altura na peça em porcentagem — 0 na base, 100 no topo. Uma linha-guia no editor marca 100 por cento e é rotulada com a altura real da peça em mm.
- **Ao longo da curva (horizontal)** está a porcentagem da torção total alcançada naquela altura — 0 para nenhuma parte dela, 100 para toda ela.

Um novo Torcer começa com uma diagonal reta de 0 a 100, que é exatamente a torção uniforme simples obtida sem usar Avançado.

Um trecho plano na curva é uma faixa da peça que não se torce. Onde a curva não cobre toda a altura, a extremidade mais próxima dela é mantida, de modo que uma curva desenhada apenas entre 40 e 60 por cento deixa a peça rígida abaixo e acima desse intervalo — é assim que você inicia e interrompe uma torção no meio da altura.

Um trecho que recua conforme sobe desenrola: essa faixa da peça gira no sentido contrário, de volta para onde começou. Desenhar o perfil acima de 100 e depois trazê-lo de volta para baixo é a maneira de ultrapassar o total e retornar a ele.

## Parâmetros

- **Tipo de Rotação** - Escolha entre:
  - **Ângulo** - Especifique o ângulo total de torção em graus (3-360)
  - **Distância** - Especifique a torção como uma distância ao longo da circunferência
- **Fatias** - Número de cortes horizontais adicionados para uma torção suave, espaçados uniformemente ao longo da peça. Mais fatias = torção mais suave
- **Lados Mínimos** - O número mínimo de lados que a peça deve ter em torno do eixo de torção. Uma forma grosseira, como um cubo, não tem geometria ao longo do perímetro para acompanhar a rotação, então suas faces planas facetam em vez de se curvar; isso adiciona cortes verticais através do eixo de torção para que essas faces possam acompanhar a torção. 0 (o padrão) deixa a peça inalterada
- **Torcer à Direita** - Direção da torção: à direita (sentido horário) ou à esquerda (sentido anti-horário)
- **Raio Preferido** - Somente leitura: o raio que a própria peça informa, ou aquele implícito em sua forma, que é a referência em torno da qual a distância de torção é medida (somente no modo Distância)
- **Editar Raio** - Desative o raio informado para poder definir o seu próprio (somente no modo Distância e apenas quando a peça informa um)
- **Substituir Raio** - Raio personalizado para o cálculo da torção (somente no modo Distância)

### Parâmetros Avançados

- **Perfil de Torção** - O editor de curva descrito acima: a porcentagem da torção total alcançada em cada altura, em porcentagem
- **Deslocamento de Rotação** - Desloca o centro em torno do qual a peça é girada, afastando-o do meio da peça

## Dicas

- Valores mais altos de Fatias produzem resultados mais suaves, mas geram mais geometria
- Se um cubo torcido ou outra forma de faces planas parecer facetado em vez de curvo, aumente Lados Mínimos
- Desenhe o perfil plano na base e subindo a partir daí para deixar uma base reta sob uma coluna torcida
- Uma torção de 90 graus em uma coluna quadrada cria um elegante efeito arquitetônico
- Desenhe dois trechos planos unidos por uma subida curta para torcer o meio da peça e deixar ambas as extremidades rígidas

## Relacionados

- [Curva](curve.md) - Dobre um objeto em um arco
- [Estreitamento](pinch.md) - Comprima em direção ao centro
- [Estreitamento Radial](radial-pinch.md) - Modele o perfil com uma curva da mesma maneira
