---
title: Curva
articleKey: CurveObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 6adde5da3bb469384f59eb5e9dfe5cb642b3eec5
source_lang: en
---
# Curva

A Curva dobra um objeto reto formando um arco ou uma forma circular. Você pode controlar a dobra especificando um ângulo ou um diâmetro ao redor do qual o objeto será envolvido.

<!--  Before and after showing a straight bar being curved into an arc -->
![20260506 155243 paste 20260506 155243](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155243-paste-20260506-155243.jpg)

## Como Usar

1. Selecione um objeto
2. Aplique a operação **Curva** a partir do menu Remodelar
3. Escolha entre o tipo de dobra Ângulo ou Diâmetro
4. Ajuste os parâmetros para obter a curvatura desejada

## Parâmetros

- **Tipo de Dobra** - Escolha entre:
  - **Ângulo** - Especifique diretamente o ângulo da dobra (1-360 graus)
  - **Diâmetro** - Especifique o diâmetro do círculo ao redor do qual a peça é envolvida
- **Direção da Dobra** - Dobrar para Cima ou Dobrar Para Baixo
- **Percentual Inicial** - Em que ponto ao longo do objeto a dobra começa (0-100%)
- **Dividir Malha** - Divide a malha para obter curvas suaves (padrão: ativado)
- **Mín. de Lados Por Rotação** - Número mínimo de segmentos da malha por revolução completa. Valores maiores = curvas mais suaves

### Parâmetros Avançados

- **Percentual Inicial de Curvatura** - Porcentagem a partir da esquerda onde a dobra começa
- **Percentual de Curvatura Final** - Porcentagem a partir da esquerda onde a dobra termina

## Dicas

- Use a Curva para criar arcos, anéis e suportes dobrados a partir de formas retas
- Definir o ângulo como 360 envolve o objeto formando um anel completo
- Aumente o Mín. de Lados Por Rotação para obter resultados mais suaves em dobras acentuadas
- O objeto é dobrado ao longo de seu comprimento (eixo X)

## Relacionados

- [Torcer](twist.md) - Rotaciona ao longo da altura em vez de dobrar
- [Toro](../../primitives/torus.md) - Uma forma de anel pronta
