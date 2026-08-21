---
title: リングパス
articleKey: RingPathObject3D
parent: "2D Paths"
nav_order: 4
source_hash: 3ee3dd9ab102cfabf1e79d1093b237fb90f12aca
source_lang: en
---
# リングパス

2D のリング形状 — 中心に円形の穴が開いた円です。[直線押し出し](../operations/path/linear-extrude.md) と組み合わせて、チューブやワッシャーの形状を作成します。

<!-- Screenshot of a Ring Path on the workspace -->
![20260506 080211 paste 20260506 080211](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080211-paste-20260506-080211.jpg)

## パラメータ

- **外径** - リングの外側の直径
- **内径** - 中心にある穴の直径

## ヒント

- リングの肉厚は (外径 - 内径) / 2 になります
- リングパスを押し出すと、[リング](../primitives/ring.md) プリミティブと同様のチューブが作成されます

## 関連項目

- [円パス](circle-path.md) - 穴のない中実の円
- [リング](../primitives/ring.md) - あらかじめ用意された 3D のチューブ形状
- [直線押し出し](../operations/path/linear-extrude.md) - パスに高さを与える
