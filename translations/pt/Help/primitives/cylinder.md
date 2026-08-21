---
title: Cilindro
articleKey: CylinderObject3D
parent: "Primitives"
nav_order: 5
source_hash: ab8394a14de799f83dc9c39eb86b8eaf2aab37b7
source_lang: en
---
# Cilindro

Uma forma de coluna redonda com diâmetro, altura e número de lados configuráveis. O Cilindro é essencial para criar pinos, hastes, furos e detalhes arredondados.

<!--  Screenshot of a Cylinder primitive on the workspace -->
![20260318 183248 paste 20260318 183248](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183248-paste-20260318-183248.jpg)


## Parâmetros

- **Diâmetro** - A largura ao longo do cilindro (padrão: 20mm)
- **Altura** - A altura do cilindro (padrão: 20mm)
- **Lados** - Número de segmentos ao redor do perímetro (padrão: 40). Valores menores criam formas poligonais (por exemplo, 6 para um hexágono)

### Parâmetros Avançados

Ative o modo **Avançado** para acessar controles adicionais:

- **Diâmetro Superior** - Defina um diâmetro diferente para o topo do cilindro e crie formas cônicas ou de cone truncado (padrão: igual ao Diâmetro)
- **Ângulo Inicial** - Ângulo onde o cilindro começa (padrão: 0). Use junto com o Ângulo Final para criar cilindros parciais
- **Ângulo Final** - Ângulo onde o cilindro termina (padrão: 360). Defina um valor menor que 360 para obter formas de fatia de pizza

## Dicas

- Defina Lados com um número baixo para criar polígonos regulares -- 6 para hexágonos, 8 para octógonos, etc.
- Use valores diferentes de Diâmetro e Diâmetro Superior para criar cones truncados e formas cônicas
- Defina o Ângulo Inicial e o Ângulo Final para criar formas de fatia de pizza ou de arco
- Cilindros são excelentes ferramentas de corte para criar furos redondos com [Subtrair](../operations/boolean/subtract.md)

## Relacionados

- [Cone](cone.md) - Um cilindro que afina até um ponto
- [Meio Cilindro](half-cylinder.md) - Um cilindro cortado ao meio no sentido do comprimento
- [Anel](ring.md) - Um cilindro oco (tubo)
