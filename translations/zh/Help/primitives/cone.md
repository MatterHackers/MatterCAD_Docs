---
title: 圆锥体
articleKey: ConeObject3D
parent: "Primitives"
nav_order: 3
source_hash: 9987a8aebe5f5b27dfa3087ec7853ddcfba15fe4
source_lang: en
---
# 圆锥体

顶部收拢成一点的锥形圆柱。适合创建尖端特征、漏斗和倒角。

<!--  Screenshot of a Cone primitive on the workspace -->
![20260318 183159 paste 20260318 183159](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183159-paste-20260318-183159.jpg)


## 参数

- **直径** - 底部的宽度（默认：20mm）
- **高度** - 圆锥体的高度（默认：20mm）
- **侧面** - 周长上的分段数量（默认：40）

## 提示

- 若需要截头圆锥（顶部为平面而非尖点），请使用[圆柱体](cylinder.md)并开启高级模式，然后设置不同的直径和顶部直径数值
- 圆锥体与[减去](../operations/boolean/subtract.md)结合使用时，可用于创建倒角边

## 相关内容

- [圆柱体](cylinder.md) - 不带锥度的圆形柱体
- [棱锥体](pyramid.md) - 四面收拢的尖顶形状
