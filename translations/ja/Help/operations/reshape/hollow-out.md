---
title: 中空化
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cc2c5555723ecfe77475fef9e7a2090cdf760204
source_lang: en
---
# 中空化

中空化は、サーフェスを内側にオフセットすることで、ソリッドオブジェクトから中空のシェルを作成します。結果として、元の形状の薄肉バージョンが得られます。

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## 使い方

1. ソリッドオブジェクトを選択します
2. 形状変更メニューから **中空化** 操作を適用します
3. 必要な肉厚を設定します

## パラメータ

- **距離** - 肉厚（ミリメートル単位、既定値: 2mm）。作成されるシェルの厚さになります。
- **セル数** - 中空化アルゴリズムの解像度（既定値: 64）。値を大きくすると内部サーフェスが滑らかになりますが、計算に時間がかかります。

## ヒント

- 中空化は、エンクロージャ、容器、花瓶、軽量パーツの作成に便利です
- ほとんどの3Dプリントパーツでは、1〜2mmの肉厚が一般的です
- 内部サーフェスが粗く、階段状に見える場合はセル数を増やしてください
- 中空化では底面が開いた状態になります。閉じた底面が必要な場合は [立方体](../../primitives/cube.md) と組み合わせてください
- 複雑な形状の場合、計算に数秒かかることがあります

## 関連項目

- [平面カット](plane-cut.md) - 指定した高さでオブジェクトを切り取ります
- [減算](../boolean/subtract.md) - 手動で材料を切り取ります
