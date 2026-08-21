---
title: 半球
articleKey: HalfSphereObject3D
parent: "Primitives"
nav_order: 7
source_hash: 4f82c152ab27e32e36e758c83f9135f1c6bb2096
source_lang: en
---
# 半球

球の上半分 —— ドーム形状です。ドーム状の上面、レンズ形状、丸みのあるカバーの作成に便利です。

<!--  Screenshot of a Half Sphere primitive on the workspace -->
![20260318 183343 paste 20260318 183343](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183343-paste-20260318-183343.jpg)


## パラメータ

- **直径** - ドーム底面の幅（既定値: 20mm）
- **経度分割数** - 外周方向のセグメント数（既定値: 40）
- **緯度分割数** - 底面から頂点までのセグメント数（既定値: 10）。数値を大きくするほど滑らかなドームになります

## ヒント

- 2つの半球を円柱と組み合わせるとカプセル形状になります
- 円柱の上に配置すると、ドーム状のふたやボタンを作成できます
- [減算](../operations/boolean/subtract.md) と組み合わせて、ドーム形状の空洞を作成できます

## 関連項目

- [球](sphere.md) - 完全なボール形状
- [半円柱](half-cylinder.md) - 半分に切った円柱
