---
title: 星パス
articleKey: StarPathObject3D
parent: "2D Paths"
nav_order: 5
source_hash: 74d92e4171c452cd10069921636e45d7ef9dc70e
source_lang: en
---
# 星パス

点の数と内側/外側の半径を設定できる星形の2Dパスです。[直線押し出し](../operations/path/linear-extrude.md) と組み合わせて3Dの星形状を作成できます。

<!-- Screenshot of a Star Path on the workspace -->
![20260506 080319 paste 20260506 080319](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080319-paste-20260506-080319.jpg)


## パラメータ

- **点** - 星の頂点の数
- **外側の半径** - 中心から各頂点の先端までの距離
- **内側の半径** - 中心から頂点間の谷までの距離

## ヒント

- 内側の半径と外側の半径の比率によって、星の「とがり具合」が決まります。内側の半径を小さくすると、鋭くはっきりした頂点になります。
- 点を5に設定すると一般的な星、6に設定するとダビデの星の形状、さらに大きくするとギアのような形状になります
- 星パスに [パスをスムーズ](../operations/path/smooth-path.md) を使用すると、角の丸い星形状を作成できます

## 関連項目

- [円パス](circle-path.md) - なめらかな円
- [ギア 2D](../mechanical/gear-2d.md) - 本格的なギアの輪郭
- [直線押し出し](../operations/path/linear-extrude.md) - パスに高さを与える
