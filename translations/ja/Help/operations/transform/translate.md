---
title: 移動
articleKey: TranslateObject3D
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c05550dee2397bdb58dc2e247a068a544233a71d
source_lang: en
---
# 移動

移動は、オブジェクトを X、Y、Z 軸に沿って指定した距離だけ動かします。マウスでオブジェクトをドラッグする場合とは異なり、移動では正確なオフセット値を入力できます。

<!--  Screenshot showing the Translate operation properties with X, Y, Z offset fields -->
![20260506 160828 paste 20260506 160828](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160828-paste-20260506-160828.jpg)


## 使い方

1. オブジェクトを選択します
2. 変換メニューから **移動** 操作を適用します
3. プロパティパネルで X、Y、Z の希望するオフセット値を入力します

## パラメータ

- **X, Y, Z**（移動）- 各軸に沿ってオブジェクトを動かす距離（ミリメートル単位）。計算値には[式](../../workspace/expressions.md)を使用できます。

## ヒント

- 後から調整できる、正確で再現性のある位置決めが必要な場合は移動を使用します
- 移動の値はオブジェクトの現在の位置を基準とした相対値です。X に 10 を入力すると、現在の位置から右に 10mm 動きます
- すばやく位置を変えるには、ビューポート内でオブジェクトを直接ドラッグすることもできます。[オブジェクトの編集](../../getting-started/editing-objects.md)を参照してください

## 関連項目

- [回転](rotate.md) - オブジェクトを指定した角度だけ回転します
- [スケール](scale.md) - オブジェクトのサイズを正確に変更します
- [整列](../placement/align.md) - オブジェクト同士の相対的な位置を決めます
