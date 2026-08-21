---
title: Roscas
articleKey: ThreadsObject3D_2
parent: "Mechanical Parts"
nav_order: 3
source_hash: 7d881b3293a508e102d3a4b845cdfd4eb9c34fa8
source_lang: en
---
# Roscas

Crie roscas de parafuso com diâmetro, passo e perfil de rosca configuráveis. As roscas podem ser usadas como parafusos independentes ou subtraídas de outros objetos para criar furos roscados.

<!-- AUTO_IMAGE: type=from_thumbnail item=threads file=mechanical_threads -->
![mechanical_threads](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_threads.png)

## Como Usar

1. Adicione **Roscas** a partir das ferramentas Mecânico ou do painel Primitivas
2. Defina o diâmetro, o passo e o número de rotações
3. Opcionalmente, ative "Usar como Furo" para criar furos roscados

## Parâmetros

### Uso

- **Usar como Furo** - Quando ativado, as roscas são dimensionadas com tolerância extra para uso como furo subtraído (padrão: desativado)
- **Tolerância** - Folga extra para o ajuste quando usado como furo (padrão: 0,2 mm, visível quando Usar como Furo está ativado)

### Atributos

- **Diâmetro** - O diâmetro externo da seção roscada (padrão: 10 mm)
- **Passo** - Distância entre cada volta da rosca (padrão: 2 mm). Passo menor = roscas mais finas
- **Escala da Rosca** - Largura das roscas como proporção do passo (padrão: 1.0, intervalo: 0.1-1.0)
- **Rotações** - Número de voltas completas da rosca (padrão: 10)

### Geometria

- **Lados** - Número de segmentos ao redor do perímetro (padrão: 40). Mais = mais suave

### Pontas (Extremidades da Rosca)

- **Escala da Ponta** - Quanto afunilar as extremidades da rosca (padrão: 0, intervalo: 0-1). Defina acima de 0 para criar uma entrada afunilada nas extremidades
- **Ângulo da Ponta** - O ângulo ao longo do qual as pontas são afuniladas (padrão: 90 graus)

## Dicas

- Para criar um furo roscado: ative "Usar como Furo", posicione as roscas e use [Subtrair](../operations/boolean/subtract.md) no seu objeto
- Adicione Tolerância ao usar como furo para garantir que as peças impressas se encaixem
- Passos de rosca métrica padrão: M3=0,5 mm, M4=0,7 mm, M5=0,8 mm, M6=1,0 mm, M8=1,25 mm, M10=1,5 mm
- Use a Escala da Ponta para criar uma entrada que facilite o início do rosqueamento

## Relacionados

- [Engrenagem](gears.md) - Crie formas de engrenagem mecânica
- [Cilindro](../primitives/cylinder.md) - Uma coluna redonda simples (sem roscas)
- [Subtrair](../operations/boolean/subtract.md) - Recorte roscas de outros objetos para criar furos
