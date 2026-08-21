---
title: 円パス
articleKey: CirclePathObject3D
parent: "2D Paths"
nav_order: 2
source_hash: 587edab627246f47731f9dbde2a13a00dd464807
source_lang: en
---
# 円パス

円形の2Dパスです。[直線押し出し](../operations/path/linear-extrude.md) と組み合わせて円柱を作成したり、[回転体](../operations/path/revolve.md) と組み合わせてトーラス状の形状を作成したりできます。

<!-- Screenshot of a Circle Path on the workspace -->
![20260506 080110 paste 20260506 080110](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080110-paste-20260506-080110.jpg)


## パラメータ

- **直径** - 円の直径（デフォルト: 20mm）
- **セグメント** - 円を構成する線分の数。多いほど滑らかになります

## ヒント

- 円パスを直線押し出しと組み合わせると円柱ができます。[円柱](../primitives/cylinder.md) プリミティブに似ていますが、そこからの造形の自由度が高くなります
- 回転体のベースとして使用すると、リング状の形状を作成できます

## 関連項目

- [ボックスパス](box-path.md) - 矩形の2Dパス
- [リングパス](ring-path.md) - 穴の開いた円
- [直線押し出し](../operations/path/linear-extrude.md) - パスに高さを与えます
