---
title: Cubo
articleKey: CubeObject3D
parent: "Primitives"
nav_order: 4
source_hash: a376a9c78d88d995f3c6ce21dd5098672d6c1dfb
source_lang: en
---
# Cubo

Uma forma de caixa retangular com largura, profundidade e altura ajustáveis e arestas arredondadas opcionais. O Cubo é uma das primitivas mais utilizadas para construir projetos.

<!--  Screenshot of a Cube primitive on the workspace -->
![20260318 183230 paste 20260318 183230](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183230-paste-20260318-183230.jpg)


## Parâmetros

- **Largura** - Tamanho ao longo do eixo X (padrão: 20mm)
- **Profundidade** - Tamanho ao longo do eixo Y (padrão: 20mm)
- **Altura** - Tamanho ao longo do eixo Z (padrão: 20mm)
- **Redondo** - Ativa as arestas arredondadas
- **Raio** - Tamanho do arredondamento (visível quando Redondo está ativado)
- **Segmentos Arredondados** - Suavidade do arredondamento; mais segmentos = curvas mais suaves (visível quando Redondo está ativado)

## Dicas

- Use um Cubo como ponto de partida para caixas, placas, suportes e invólucros
- Ative Redondo para obter arestas suaves e de aparência profissional
- O Raio não pode exceder metade da menor dimensão
- Combine um Cubo com [Subtrair](../operations/boolean/subtract.md) para criar recortes e rasgos retangulares

## Relacionados

- [Cilindro](cylinder.md) - Forma de coluna redonda
- [Pirâmide](pyramid.md) - Forma de quatro lados afunilada
- [Furo](hole.md) - Um cubo pré-configurado para subtração booleana
