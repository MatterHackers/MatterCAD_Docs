---
title: Matriz
articleKey: ArrayObject3D_2
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c547fa24e5f47e0d60f0cec0eac979700d946daf
source_lang: en
---
# Matriz

A Matriz cria várias cópias de um objeto dispostas num padrão. Selecione um modo nos botões no topo — **Linear**, **Radial** ou **Transformar** — para alternar entre tipos de padrão.

<!--  Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->
![20260506 080647 paste 20260506 080647](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080647-paste-20260506-080647.jpg)


## Como Utilizar

1. Selecione um objeto
2. Aplique a operação **Matriz** a partir do menu Duplicação
3. Escolha um modo (Linear, Radial ou Transformar)
4. Ajuste os parâmetros do modo escolhido

## Modo: Linear

O modo Linear coloca as cópias ao longo de uma direção, com progressão opcional de rotação e escala.

**Contagem** — Número de cópias (inteiro ou expressão). O objeto de origem é a primeira cópia; as cópias adicionais são deslocadas a partir dela.

**Método de Deslocamento** — Como o espaçamento é calculado:
- **Relativo** — O deslocamento é multiplicado pelo tamanho da caixa delimitadora do objeto. Um Deslocamento Relativo de (1, 0, 0) espaça as cópias exatamente à distância de uma largura de objeto ao longo de X.
- **Deslocamento** — Distância fixa em mm no espaço do mundo por cópia.
- **Ponto Final** — Define a posição da última cópia; o espaçamento é dividido uniformemente entre as cópias.

**Deslocamento Relativo** / **Deslocamento** / **Ponto Final** — O vetor de espaçamento, consoante o Método de Deslocamento selecionado.

**Modo de Rotação** — Como a rotação se acumula ao longo das cópias:
- **Local** — Cada cópia roda no seu lugar, em torno do próprio centro; a direção do deslocamento mantém-se nos eixos do mundo.
- **Composição** — A rotação acumula-se e orienta o deslocamento, produzindo espirais, leques e hélices.

**Rotação** — Rotação por cópia, em graus, em cada eixo.

**Escala** — Escala cumulativa por cópia em cada eixo. Valores inferiores a 1 reduzem as cópias; valores superiores a 1 aumentam-nas.

**Escala Afeta Deslocamento** — Quando ativado, o espaçamento entre cópias também é escalado a cada passo. Utilize esta opção para espirais que se apertam e progressões geométricas (conchas de náutilo, curvas de conchas empilhadas).

## Modo: Radial

O modo Radial distribui as cópias uniformemente em torno de um eixo central, a um raio fixo.

<!--  Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->
![20260506 092618 paste 20260506 092618](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-092618-paste-20260506-092618.jpg)


**Método de Contagem** — Como é determinado o número de cópias:
- **Contagem** — Número explícito de cópias.
- **Distância** — Intervalo angular entre cópias, em graus; a contagem é calculada para preencher o varrimento.

**Contagem** / **Distância Angular** — Número de cópias (modo Contagem) ou espaçamento angular em graus (modo Distância). Suporta expressões.

**Eixo Central** — O eixo em torno do qual rodar (predefinição: Z).

**Segmento de Círculo** — Se as cópias abrangem um círculo completo de 360° (**Completo**) ou um arco parcial (**Arco**).

**Raio** — Distância do eixo central a cada cópia.

**Ângulo de Varrimento** — Graus de arco a preencher (apresentado quando Segmento de Círculo é Arco). Suporta expressões.

**Alinhar Rotação** — Roda cada cópia para que o seu eixo frontal aponte para fora, a partir do centro.

**Eixo Frontal** — Qual o eixo da cópia tratado como "frontal" para o alinhamento (apresentado quando Alinhar Rotação está ativado).

## Modo: Transformar

O modo Transformar avança as cópias utilizando uma transformação manual ou seguindo a transformação de outro objeto.

**Contagem** — Número de cópias (inteiro ou expressão).

**Referência da Transformação** — De onde vem a transformação de cada passo:
- **Entrada** — Especifica diretamente a translação, a rotação e a escala.
- **Objeto** — A transformação é lida de um objeto irmão com um determinado nome.

**Translação** — Deslocamento por passo no espaço do mundo, em mm (apresentado quando a Referência é Entrada).

**Rotação** — Rotação por passo, em graus, por eixo (apresentado quando a Referência é Entrada).

**Escala** / **Eixos de Escala** — Escala uniforme e por eixo aplicada em cada passo (apresentado quando a Referência é Entrada).

**Nome da Transformação** — Nome do objeto irmão cuja transformação é utilizada como incremento por passo (apresentado quando a Referência é Objeto).

**Espaço Relativo** — Quando ativado, a transformação de cada cópia compõe-se no referencial local da cópia anterior; quando desativado, cada passo é aplicado no espaço do mundo (apresentado quando a Referência é Objeto).

## Aleatorizar

Ative **Aleatorizar** para adicionar variação a todas as cópias.

- **Deslocamento Aleatório** — Deslocamento máximo aleatório de posição por eixo, em mm.
- **Rotação Aleatória** — Rotação máxima aleatória por eixo, em graus.
- **Eixos de Escala Aleatória** — Variação máxima aleatória de escala por eixo.
- **Excluir Primeiro** — Mantém a primeira cópia na posição exata calculada (predefinição: ativado).
- **Excluir Último** — Mantém a última cópia na posição exata calculada.
- **Semente Aleatória** — Altere este valor para obter uma disposição aleatória diferente. Suporta expressões.

## Mesclar

- **Criar Malha Única** — Combina todas as cópias num único objeto de malha mesclada.
- **Mesclar Vértices** — Solda os vértices dentro do limiar de distância de mesclagem (apresentado quando Criar Malha Única está ativado).
- **Distância** — Limiar de mesclagem em mm (apresentado quando Mesclar Vértices está ativado).

## Dicas

- Utilize expressões em Contagem, Rotação ou Ponto Final para criar padrões paramétricos
- Para padrões circulares, utilize o modo Radial — defina o Raio para controlar o tamanho do círculo e ative Alinhar Rotação se as cópias devem ficar viradas para fora
- A rotação em Composição no modo Linear cria espirais e leques sem calcular manualmente os deslocamentos de ângulo
- Escala Afeta Deslocamento cria naturalmente disposições em concha de náutilo e em progressão geométrica
- Combine a Matriz com [Selecionar filho](select-child.md) para criar padrões em que cada cópia mostra uma variante diferente

## Relacionados

- [Alinhar](../placement/align.md) - Posicionar objetos uns em relação aos outros
- [Selecionar filho](select-child.md) - Escolher uma cópia específica de uma matriz por índice ou nome
