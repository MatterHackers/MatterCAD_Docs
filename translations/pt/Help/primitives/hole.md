---
title: Furo
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# Furo

Um objeto em forma de cubo pré-configurado para atuar como ferramenta de subtração booleana. Ao usar [Combinar](../operations/boolean/combine.md), os objetos Furo são automaticamente subtraídos das outras formas em vez de serem somados a elas.

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## Como Funciona

A primitiva Furo funciona como um [Cubo](cube.md), mas tem seu tipo de saída definido como "Furo". Quando você combina objetos que incluem um Furo, o volume do Furo é removido do resultado.

## Parâmetros

Os mesmos do [Cubo](cube.md):

- **Largura** - Tamanho ao longo do eixo X
- **Profundidade** - Tamanho ao longo do eixo Y
- **Altura** - Tamanho ao longo do eixo Z

## Dicas

- Posicione o Furo de modo que ele se sobreponha ao objeto que você deseja cortar
- Faça o Furo atravessar completamente o objeto de destino se quiser um furo passante
- Você pode usar formas comuns com [Subtrair](../operations/boolean/subtract.md) para obter o mesmo efeito, mas os Furos são convenientes porque funcionam automaticamente com [Combinar](../operations/boolean/combine.md)
- Para furos redondos, use um [Cilindro](cylinder.md) com Subtrair

## Relacionados

- [Cubo](cube.md) - A mesma forma, sem o comportamento de furo
- [Combinar](../operations/boolean/combine.md) - Mescla formas e subtrai Furos automaticamente
- [Subtrair](../operations/boolean/subtract.md) - Subtraia manualmente qualquer forma de outra
