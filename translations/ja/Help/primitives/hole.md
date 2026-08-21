---
title: 穴
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# 穴

ブーリアン減算ツールとして動作するようにあらかじめ設定された立方体形状のオブジェクトです。[結合](../operations/boolean/combine.md) を使用すると、穴オブジェクトは他の形状に加算されるのではなく、自動的に減算されます。

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## 動作の仕組み

穴プリミティブは [立方体](cube.md) と同じように動作しますが、出力タイプが「穴」に設定されています。穴を含むオブジェクトを結合すると、穴の体積が結果から削除されます。

## パラメータ

[立方体](cube.md) と同じです:

- **幅** - X 軸方向のサイズ
- **深さ** - Y 軸方向のサイズ
- **高さ** - Z 軸方向のサイズ

## ヒント

- 切り取りたいオブジェクトと重なるように穴の位置を合わせます
- 貫通穴にしたい場合は、穴が対象オブジェクトを完全に貫くように伸ばします
- 通常の形状を [減算](../operations/boolean/subtract.md) で使っても同じ効果が得られますが、穴は [結合](../operations/boolean/combine.md) で自動的に機能するため便利です
- 丸い穴には、代わりに [円柱](cylinder.md) と減算を使用してください

## 関連項目

- [立方体](cube.md) - 穴の動作を持たない同じ形状
- [結合](../operations/boolean/combine.md) - 形状を結合し、穴を自動的に減算します
- [減算](../operations/boolean/subtract.md) - 任意の形状を他の形状から手動で減算します
