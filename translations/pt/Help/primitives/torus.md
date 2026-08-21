---
title: Toro
articleKey: TorusObject3D
parent: "Primitives"
nav_order: 17
source_hash: aaec1652de4d6713bd01a707964cf4985d3fb5f6
source_lang: en
---
# Toro

Um anel em formato de rosquinha com controle independente sobre o tamanho geral e a espessura da seção transversal do anel.

<!--  Screenshot of a Torus primitive on the workspace -->
![20260318 184240 paste 20260318 184240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184240-paste-20260318-184240.jpg)


## Parâmetros

- **Diâmetro externo** - A largura total do toro (padrão: 20mm)
- **Diâmetro Interno** - O diâmetro do furo central (padrão: 10mm)
- **Lados** - Número de segmentos ao redor do anel principal (padrão: 40)

### Parâmetros Avançados

Ative o modo **Avançado** para obter controles adicionais:

- **Ângulo Inicial** - Ângulo onde o toro começa (padrão: 0)
- **Ângulo Final** - Ângulo onde o toro termina (padrão: 360). Defina um valor menor que 360 para obter um anel aberto ou um arco
- **Lados do Anel** - Número de segmentos ao redor da seção transversal do anel (padrão: 15). Mais = perfil de tubo mais suave
- **Ângulo de Fase do Anel** - Rotaciona o perfil da seção transversal (padrão: 0)

## Dicas

- A espessura do tubo do anel é determinada pela diferença entre o Diâmetro externo e o Diâmetro Interno
- Use o Ângulo Inicial e o Ângulo Final para criar segmentos de anel abertos, arcos ou formas em C
- Útil para criar anéis de vedação (O-rings), alças, anéis decorativos e curvas de tubulação

## Relacionados

- [Anel](ring.md) - Um cilindro oco de paredes retas (tubo)
- [Esfera](sphere.md) - Uma bola sólida
- [Meia Esfera](half-sphere.md) - Um formato de cúpula
