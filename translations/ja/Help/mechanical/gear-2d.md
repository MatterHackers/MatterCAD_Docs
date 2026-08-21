---
title: Gear 2D
articleKey: Gear2D
parent: "Mechanical Parts"
nav_order: 1
source_hash: aa16d8f12f5342e41cfbfa852b1e8a02cfc82a7d
source_lang: en
---
# Gear 2D

ギアの歯形だけを平面パスとして作成する2Dギアパスです。[直線押し出し](../operations/path/linear-extrude.md) や [回転体](../operations/path/revolve.md) と組み合わせて使用すると、ギアを3D形状に仕上げる方法をより細かく制御できます。

<!-- AUTO_IMAGE: type=from_thumbnail item=gear_2d file=mechanical_gear_2d -->
![mechanical_gear_2d](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_gear_2d.png)

## 使い方

1. メカニカルツールから **Gear 2D** を追加します
2. 歯のパラメータを設定します
3. [直線押し出し](../operations/path/linear-extrude.md) を適用して高さを与えます

## ヒント

- 押し出す前にギアの輪郭を他のパス操作と組み合わせたい場合は Gear 2D を使用してください
- そのまま使える3Dギアが必要な場合は、代わりに [ギア](gears.md) を参照してください
- かみ合いのルールは同じです。互いにかみ合わせるギアでは円ピッチと圧力角を一致させてください

## 関連項目

- [ギア](gears.md) - そのまま使える3Dギア
- [星パス](../2d-paths/star-path.md) - よりシンプルな歯形形状
- [直線押し出し](../operations/path/linear-extrude.md) - ギアパスに高さを与えます
