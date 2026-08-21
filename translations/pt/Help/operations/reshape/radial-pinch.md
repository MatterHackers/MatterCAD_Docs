---
title: Estreitamento Radial
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: 95ef5847767e5cfcdbae9df9aaa1cb1727da2f5e
source_lang: en
---
# Estreitamento Radial

O Estreitamento Radial comprime um objeto para dentro a partir de um ponto central, com uma curva de perfil personalizável. Ao contrário do [Estreitamento](pinch.md) comum, que atua de trás para a frente, o Estreitamento Radial comprime simetricamente em torno de um eixo central.

<!--  Before and after showing an object with radial pinch applied, creating a waisted shape -->
![20260506 155741 paste 20260506 155741](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155741-paste-20260506-155741.jpg)

## Como Usar

1. Selecione um objeto
2. Aplique a operação **Estreitamento Radial** no menu Remodelar
3. Edite o perfil do caminho para definir quanto estreitamento é aplicado em cada altura
4. Ajuste o número de fatias para obter mais suavidade

## Parâmetros

- **Caminho** - Um editor de curva de perfil que define a quantidade de estreitamento em cada nível de altura. Edite a curva para criar perfis de estreitamento personalizados
- **Fatias** - Número de cortes horizontais para um estreitamento suave, distribuídos uniformemente ao longo da peça. Mais fatias = resultados mais suaves

### Parâmetros Avançados

- **Tipo de Estreitamento** - Direção da compressão:
  - **Radial** - Comprime igualmente de todos os lados em direção ao centro
  - **Eixo X** - Comprime apenas ao longo do eixo X
  - **Eixo Y** - Comprime apenas ao longo do eixo Y
- **Deslocamento de Rotação** - Desloca o centro do efeito de estreitamento

## Dicas

- Use o editor de caminho para criar formas de ampulheta, garrafa ou vaso
- O estreitamento radial é ideal para criar formas orgânicas e arredondadas a partir de objetos cilíndricos
- Aumente as Fatias para obter curvas mais suaves, especialmente em perfis de estreitamento acentuados

## Relacionados

- [Estreitamento](pinch.md) - Compressão simples de trás para a frente
- [Torcer](twist.md) - Rotação em espiral ao longo da altura
- [Curva](curve.md) - Dobra em forma de arco
