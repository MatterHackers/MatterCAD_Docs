---
title: Caminho de Anel
articleKey: RingPathObject3D
parent: "2D Paths"
nav_order: 4
source_hash: 3ee3dd9ab102cfabf1e79d1093b237fb90f12aca
source_lang: en
---
# Caminho de Anel

Uma forma de anel 2D -- um círculo com um furo circular no centro. Use com [Extrusão Linear](../operations/path/linear-extrude.md) para criar formas de tubo ou arruela.

<!-- Screenshot of a Ring Path on the workspace -->
![20260506 080211 paste 20260506 080211](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080211-paste-20260506-080211.jpg)

## Parâmetros

- **Diâmetro externo** - O diâmetro externo do anel
- **Diâmetro Interno** - O diâmetro do furo no centro

## Dicas

- A espessura da parede do anel é (Diâmetro externo - Diâmetro Interno) / 2
- Extrudar um Caminho de Anel cria um tubo semelhante à primitiva [Anel](../primitives/ring.md)

## Relacionados

- [Caminho de Círculo](circle-path.md) - Um círculo sólido (sem furo)
- [Anel](../primitives/ring.md) - Uma forma 3D de tubo pronta para uso
- [Extrusão Linear](../operations/path/linear-extrude.md) - Dê altura aos caminhos
