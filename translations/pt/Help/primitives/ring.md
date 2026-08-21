---
title: Anel
articleKey: RingObject3D
parent: "Primitives"
nav_order: 13
source_hash: fd16c400f3d8c8af13416ab57ddd8407e761d93a
source_lang: en
---
# Anel

Um cilindro oco (tubo) com diâmetros interno e externo independentes e uma altura especificada. Também conhecido como formato de cano ou tubo.

<!--  Screenshot of a Ring primitive on the workspace -->
![20260318 183848 paste 20260318 183848](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183848-paste-20260318-183848.jpg)


## Parâmetros

- **Diâmetro externo** - A largura externa do anel (padrão: 20mm)
- **Diâmetro Interno** - O diâmetro do centro oco (padrão: 15mm)
- **Altura** - A altura do anel (padrão: 5mm)
- **Lados** - Número de segmentos ao redor do perímetro (padrão: 40)

### Parâmetros Avançados

Ative o modo **Avançado** para obter controles adicionais:

- **Ângulo Inicial** - Ângulo onde o anel começa (padrão: 0)
- **Ângulo Final** - Ângulo onde o anel termina (padrão: 360). Defina um valor menor que 360 para um anel parcial
- **Redondo** - Adiciona arredondamento às arestas (Nenhum, Cima ou Baixo)
- **Direção** - Arredonda em direção à aresta interna ou externa (visível quando Redondo está ativado)
- **Segmentos Arredondados** - Suavidade do arredondamento (visível quando Redondo está ativado)

## Dicas

- A espessura da parede equivale a (Diâmetro externo - Diâmetro Interno) / 2
- Use isto para arruelas, espaçadores, buchas e recursos em formato de tubo
- Defina uma altura grande para canos ou pequena para arruelas planas
- Use o Ângulo Inicial e o Ângulo Final para formatos de anel parcial, como clipes em C

## Relacionados

- [Torus](torus.md) - Um anel em formato de rosquinha com seção transversal redonda
- [Cilindro](cylinder.md) - Uma coluna redonda sólida (sem centro oco)
