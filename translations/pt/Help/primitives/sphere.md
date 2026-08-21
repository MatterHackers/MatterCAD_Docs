---
title: Esfera
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
source_hash: c227e98ac116c3481bb2af73c55801de84e70b1e
source_lang: en
---
# Esfera

Uma forma de bola redonda com diâmetro e nível de detalhe ajustáveis.

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## Parâmetros

- **Diâmetro** - A largura da esfera (padrão: 20mm)
- **Lados** - Número de segmentos ao redor do perímetro (padrão: 40). Mais lados = superfície mais suave

### Parâmetros Avançados

Ative o modo **Avançado** para obter controles adicionais:

- **Ângulo Inicial** - Ângulo onde a superfície da esfera começa (padrão: 0)
- **Ângulo Final** - Ângulo onde a superfície da esfera termina (padrão: 360). Defina um valor menor que 360 para obter formas de esfera parcial
- **Lados de Latitude** - Número de segmentos de cima para baixo (padrão: 30). Mais = polos mais suaves

## Dicas

- Para impressão 3D, 40 lados costumam ser suficientes. Valores maiores criam superfícies mais suaves, mas arquivos maiores
- Use o Ângulo Inicial e o Ângulo Final para criar formas de esfera parcial, como tigelas ou domos
- Combine com [Subtrair](../operations/boolean/subtract.md) para criar cavidades esféricas

## Relacionados

- [Meia Esfera](half-sphere.md) - Apenas o hemisfério superior
- [Torus](torus.md) - Uma forma de rosquinha
