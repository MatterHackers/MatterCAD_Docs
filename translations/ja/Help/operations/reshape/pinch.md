---
title: ピンチ
articleKey: PinchObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: 87b853dab69917f9ae5718cdc73d1f2ac6bf5d5b
source_lang: en
---
# ピンチ

ピンチは、オブジェクトの背面を内側に圧縮し、上に向かうほど効果が強くなります。これにより、先細りまたは絞られたような外観が作成されます。

<!--  Before and after showing an object being pinched -->
![20260506 155449 paste 20260506 155449](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155449-paste-20260506-155449.jpg)

## 使い方

1. オブジェクトを選択します
2. 形状変更メニューから **ピンチ** 操作を適用します
3. ピンチの割合を調整します

## パラメータ

- **背面比率** - パーツの背面を内側にどれだけピンチするか（0〜300%、既定値: 50%）。値を大きくするほど圧縮が強くなります

## ヒント

- ピンチは背面から前面に向かって作用し、オブジェクトの後部を圧縮します
- 矩形や円柱形のオブジェクトから、先細りに狭まる形状を作成する場合に使用します
- 放射状（全周）の圧縮を行うには、代わりに [放射状ピンチ](radial-pinch.md) を使用します

## 関連項目

- [放射状ピンチ](radial-pinch.md) - 中心点を基準に放射状にピンチします
- [ツイスト](twist.md) - 高さに沿って回転します
- [カーブ](curve.md) - 円弧状に曲げます
