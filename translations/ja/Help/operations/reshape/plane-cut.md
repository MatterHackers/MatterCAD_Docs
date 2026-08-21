---
title: 平面カット
articleKey: PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
source_hash: 64a9901bf54b71cd2ecc12c8db189b6e2fcde25e
source_lang: en
---
# 平面カット

平面カットは、指定した高さで水平面によりオブジェクトをスライスし、カットより下の部分のみを残します。カット面は平らな面で塞がれます。

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## 使い方

1. オブジェクトを選択します
2. 形状変更メニューから **平面カット** 操作を適用します
3. カット高さを設定します

## パラメータ

- **カット高さ** - オブジェクトをスライスするZ高さ（既定値: 10mm、範囲: 1〜200mm）

## ヒント

- 平面カットを使用すると、モデルの上部を特定の高さで平らにできます
- インポートしたモデルのトリミングや、平らな底面の作成に便利です
- 平面以外の形状でカットする場合は、代わりに他のオブジェクトを使った [減算](../boolean/subtract.md) を使用してください
- 傾いた平面でカットする場合は、まずオブジェクトを回転させ、平面カットを適用してから、元に戻すように回転させます

## 関連項目

- [交差](../boolean/intersect.md) - オブジェクトが重なる部分のみを残します
- [減算](../boolean/subtract.md) - 平面だけでなく、任意の形状でカットします
- [中空化](hollow-out.md) - 中空のシェルを作成します
