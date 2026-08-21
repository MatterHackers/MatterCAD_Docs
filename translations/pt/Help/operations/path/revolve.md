---
title: Revolucionar
articleKey: RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: a63ebb08d982178e0e59f0b9f07c3c0dca53148b
source_lang: en
---
# Revolucionar

Revolucionar gira um caminho 2D em torno de um eixo para criar um sólido de revolução 3D. É assim que você cria vasos, tigelas, rodas e outros objetos com simetria de rotação.

<!--  Before and after showing a profile path being revolved into a vase shape -->
![20260506 102004 paste 20260506 102004](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-102004-paste-20260506-102004.jpg)


## Como Usar

1. Selecione um caminho 2D
2. Aplique **Revolucionar** no menu de operações de Caminho
3. Ajuste o intervalo de rotação, a posição do eixo e o número de lados

## Parâmetros

- **Rotação** - Ângulo total de rotação da revolução (padrão: 0, intervalo: 0-360). Defina como 360 para uma revolução completa.
- **Posição do Eixo** - Deslocamento do eixo de rotação em relação ao centro do caminho (padrão: 0, intervalo: -30 a 30). Valores positivos afastam o eixo do caminho, criando uma abertura maior.
- **Ângulo Inicial** - Onde a revolução começa (padrão: 0)
- **Ângulo Final** - Onde a revolução termina (padrão: 45). Defina como 360 para uma revolução completa.
- **Lados** - Número de segmentos ao longo da revolução (padrão: 30). Mais = superfície mais suave.

## Dicas

- Use a Posição do Eixo para controlar o diâmetro interno da forma revolucionada
- Defina o Ângulo Inicial e o Ângulo Final com valores menores que 360 para criar revoluções parciais (arcos, calhas)
- Desenhe um caminho de perfil do seu vaso ou tigela e depois revolucione-o para obter uma simetria perfeita
- Um [Caminho de Círculo](../../2d-paths/circle-path.md) revolucionado cria um toro

## Relacionados

- [Extrusão Linear](linear-extrude.md) - Extrude em linha reta para cima em vez de revolucionar
- [Caminhos 2D](../../2d-paths/index.md) - Crie caminhos de perfil para revolucionar
- [Toro](../../primitives/torus.md) - Uma forma de anel revolucionada já pronta
