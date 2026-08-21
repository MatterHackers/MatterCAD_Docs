---
title: 画像オブジェクト
articleKey: ImageObject3D
parent: "Primitives"
nav_order: 10
source_hash: 4c4cedd6b49be2fc75d0c9cd1d8d30fae679a74b
source_lang: en
---
# 画像オブジェクト

画像をインポートし、明るさの値によって各ピクセルの高さが決まる3Dレリーフオブジェクトに変換します。これにより、写真、ロゴ、アートワークを3Dプリント可能なオブジェクトに変えることができます。

<!-- Screenshot showing an image converted to a 3D relief on the workspace -->
![20260318 183708 paste 20260318 183708](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183708-paste-20260318-183708.jpg)


## 使い方

1. プリミティブパネルから**画像コンバーター**を追加するか、画像ファイルを作業スペースに直接ドラッグします
2. プロパティを使用して画像を選択または変更します
3. 高さを調整して、明るい領域をどの程度隆起させるかを制御します

## パラメーター

- **高さ** - 画像の隆起部分の高さ
- 画像のプレビューはプロパティパネルに表示されます

## ヒント

- 形状が明確なコントラストの高い画像が最適です
- デスクトップから画像を直接MatterCADの作業スペースにドラッグできます
- インポートした画像でオーバーフローメニューのツールを使用すると、さらに多くの変換オプションを利用できます
- 画像からパスベースの輪郭を作成するには、[画像をパスに変換](../operations/image/image-to-path.md)を参照してください
- 背面から光を当てて表示する画像については、[リトフェイン](../operations/image/lithophane.md)を参照してください
- 画像オブジェクトと[立方体](cube.md)を組み合わせてベースを追加できます

## 関連項目

- [画像をパスに変換](../operations/image/image-to-path.md) - 画像の輪郭を2Dパスとしてトレースします
- [リトフェイン](../operations/image/lithophane.md) - 背面から光を当てたときに現れる画像を作成します
- [SVGオブジェクト](svg-object.md) - ベクターグラフィックスをインポートします
