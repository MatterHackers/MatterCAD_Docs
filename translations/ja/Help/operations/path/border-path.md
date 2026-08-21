---
title: 境界パス
articleKey: BorderPathObject3D_2
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 2f2c0a540f69eddb0996a21cb6d8716a93287b5d
source_lang: en
---
# 境界パス

境界パスは、既存のパスの周囲に境界オフセットを追加し、元の形状を囲む一回り大きい形状を作成します。

<!--  Before and after showing a path with a border added -->
![20260506 100533 paste 20260506 100533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100533-paste-20260506-100533.jpg)


## 使い方

1. 2D パスを選択します
2. パス操作メニューから **境界パス** を適用します
3. 境界の幅を調整します

## ヒント

- 形状の周囲にマージンやパディングを作成する際に使用します
- 元のパスと [減算](../boolean/subtract.md) を組み合わせて、フレーム形状を作成できます
- [パスを膨張](inflate-path.md) に似ていますが、境界の生成専用に設計されています

## 関連項目

- [パスを膨張](inflate-path.md) - パスを外側に展開します
- [アウトラインパス](outline-path.md) - 塗りつぶしパスからアウトラインを作成します
- [直線押し出し](linear-extrude.md) - 境界を付けたパスに高さを与えます
