---
title: 直線押し出し
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cdfdb9cfe4c3339e70a23ddfb2f5071b1e8c5557
source_lang: en
---
# 直線押し出し

直線押し出しは2Dパスに高さを与え、平面形状を3Dソリッドに変換します。これはパスを3Dオブジェクトに変換する主要な方法です。

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## 使い方

1. 2Dパスまたはパスベースのオブジェクトを選択します
2. パス操作メニューから **直線押し出し** を適用します
3. 目的の高さを設定します

## パラメータ

- **高さ** - 押し出しの高さ（デフォルト: 5mm、範囲: 0.1〜50mm）
- **上面の面取り** - 押し出しの上面に面取り（丸み）エッジを追加します（デフォルト: オフ）

### 面取りのパラメータ（上面の面取りが有効なときに表示）

- **スタイル** - 面取りのプロファイルスタイル（シャープまたは丸み）
- **半径** - 面取りが広がる幅（デフォルト: 3mm）
- **セグメント** - 面取り曲線の滑らかさ（デフォルト: 9）

## ヒント

- これはあらゆる2Dパスで使用できます: [円](../../2d-paths/circle-path.md)、[ボックス](../../2d-paths/box-path.md)、[星](../../2d-paths/star-path.md)、[SVG](../../primitives/svg-object.md)、[カスタム](../../2d-paths/custom-path.md) のパス
- より洗練されたプロフェッショナルな見た目にするには、上面の面取りを有効にします
- まっすぐ押し出す代わりにパスを軸まわりに回転させたい場合は、[回転体](revolve.md) を参照してください

## 関連項目

- [回転体](revolve.md) - パスを軸まわりに回転させます
- [2Dパス](../../2d-paths/index.md) - 利用可能なパス形状
- [テキスト](../../primitives/text.md) - テキストは自動的に押し出されます
