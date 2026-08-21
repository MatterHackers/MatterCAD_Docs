---
title: Reduzir
articleKey: DecimateObject3D
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 58a2573b968808e98203832142fa8bacf7a9cf99
source_lang: en
---
# Reduzir (Decimar)

Reduzir diminui a contagem de polígonos de uma malha preservando a forma geral. Isso é útil para simplificar modelos com muitos detalhes, reduzir o tamanho do arquivo e acelerar operações em geometrias complexas.

![20260324 080430 paste 20260324 080430](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080430-paste-20260324-080430.jpg)


## Como Usar

1. Selecione um objeto
2. Aplique a operação **Reduzir** no menu Malha
3. Escolha o alvo (contagem ou porcentagem) e ajuste

## Parâmetros

- **Modo** - Escolha como especificar o alvo:
  - **Porcentagem** - Mantém uma porcentagem dos polígonos originais (padrão: 50%)
  - **Contagem** - Define uma contagem de polígonos específica como alvo
- **Contagem de Polígonos de Origem** - Número original de polígonos (somente leitura)
- **Percentagem Alvo** - Porcentagem de polígonos a manter (visível no modo Porcentagem)
- **Contagem Alvo** - Número exato de polígonos a manter (visível no modo Contagem)
- **Contagem Após Redução por Porcentagem** - Contagem final de polígonos após a redução percentual (somente leitura)
- **Manter Superfície** - Projeta os vértices de volta para a superfície original para maior precisão (mais lento, porém mais fiel à forma original)

## Dicas

- Uma redução de 50% geralmente preserva bem a qualidade visual
- Ative Manter Superfície quando a precisão for mais importante que a velocidade
- Reduzir a contagem de polígonos acelera as operações booleanas em modelos importados complexos
- Contagens de polígonos muito baixas degradam visivelmente a forma -- verifique o resultado antes de confirmar

## Relacionado

- [Reparar](repair.md) - Corrigir problemas na malha
