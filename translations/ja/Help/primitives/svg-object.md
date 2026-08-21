---
title: SVG オブジェクト
articleKey: SvgObject3D
parent: "Primitives"
nav_order: 15
source_hash: dab97cdde74d938b5612d959f83b54b4a04a49da
source_lang: en
---
# SVG オブジェクト

SVG（Scalable Vector Graphics）ファイルをインポートし、デザイン内で 2D パスとして使用します。インポートした SVG は、[直線押し出し](../operations/path/linear-extrude.md) や [回転体](../operations/path/revolve.md) を使って 3D 形状に変換できます。

<!--  Screenshot showing an imported SVG path being extruded into a 3D shape -->
![20260318 184807 paste 20260318 184807](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184807-paste-20260318-184807.jpg)



## 使い方

1. SVG ファイルをワークスペースにドラッグするか、開くボタンを使ってインポートします
2. SVG は 2D パスとしてインポートされます
3. [直線押し出し](../operations/path/linear-extrude.md) を適用して高さを与えるか、その他の [パス操作](../operations/path/index.md) を使用します

## ヒント

- 最良の結果を得るには、SVG ファイルに塗りつぶされた形状または閉じたパスが含まれている必要があります
- パスが多い複雑な SVG は、処理に時間がかかる場合があります
- 複数パスの SVG のうち特定の部分だけを扱うには、[パスを選択](../operations/path/select-paths.md) を使用します
- ロゴ、アイコン、装飾パターンなど、無料の SVG ファイルが数多くオンラインで入手できます

## 関連項目

- [画像をパスに変換](../operations/image/image-to-path.md) - SVG を使わずにラスター画像をパスに変換します
- [テキスト](text.md) - SVG を用意しなくても直接テキストを作成できます
- [直線押し出し](../operations/path/linear-extrude.md) - 平面のパスに高さを与えます
- [2D パス](../2d-paths/index.md) - 組み込みのパスプリミティブ
