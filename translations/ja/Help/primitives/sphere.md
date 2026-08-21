---
title: 球
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
source_hash: c227e98ac116c3481bb2af73c55801de84e70b1e
source_lang: en
---
# 球

直径と細かさを調整できる丸いボール形状です。

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## パラメータ

- **直径** - 球の幅（既定値: 20mm）
- **側面** - 外周方向の分割数（既定値: 40）。側面が多いほど表面が滑らかになります

### 詳細設定パラメータ

**詳細設定** モードを有効にすると、次の項目を調整できます:

- **開始角度** - 球の表面が始まる角度（既定値: 0）
- **終了角度** - 球の表面が終わる角度（既定値: 360）。360 より小さくすると球の一部の形状になります
- **緯度分割数** - 上から下までの分割数（既定値: 30）。多いほど極付近が滑らかになります

## ヒント

- 3D プリントの場合、側面は 40 で通常十分です。値を大きくすると表面は滑らかになりますが、ファイルサイズが大きくなります
- 開始角度と終了角度を使うと、ボウルやドームのような球の一部の形状を作成できます
- [減算](../operations/boolean/subtract.md) と組み合わせると、球状の空洞を作成できます

## 関連項目

- [半球](half-sphere.md) - 上半分の半球のみ
- [Torus](torus.md) - ドーナツ形状
