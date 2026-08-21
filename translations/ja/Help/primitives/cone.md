---
title: 円錐
articleKey: ConeObject3D
parent: "Primitives"
nav_order: 3
source_hash: 9987a8aebe5f5b27dfa3087ec7853ddcfba15fe4
source_lang: en
---
# 円錐

上部が一点に収束するテーパー付きの円柱です。尖った形状、漏斗、面取りの作成に便利です。

<!--  Screenshot of a Cone primitive on the workspace -->
![20260318 183159 paste 20260318 183159](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183159-paste-20260318-183159.jpg)


## パラメータ

- **直径** - 底面の幅（既定値: 20mm）
- **高さ** - 円錐の高さ（既定値: 20mm）
- **側面** - 外周のセグメント数（既定値: 40）

## ヒント

- 円錐台（先端が尖らずに平らな上面になる形状）を作成するには、[円柱](cylinder.md) を詳細設定モードで使用し、直径と上部直径に異なる値を設定してください
- 円錐は [減算](../operations/boolean/subtract.md) と組み合わせることで、面取りしたエッジの作成に役立ちます

## 関連項目

- [円柱](cylinder.md) - テーパーのない円形の柱
- [ピラミッド](pyramid.md) - 四角錐の尖った形状
