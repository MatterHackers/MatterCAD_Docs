---
title: 圆环路径
articleKey: RingPathObject3D
parent: "2D Paths"
nav_order: 4
source_hash: 3ee3dd9ab102cfabf1e79d1093b237fb90f12aca
source_lang: en
---
# 圆环路径

二维圆环形状 —— 中心带有圆形孔的圆。可与[线性拉伸](../operations/path/linear-extrude.md)配合使用，创建管状或垫圈状形体。

<!-- Screenshot of a Ring Path on the workspace -->
![20260506 080211 paste 20260506 080211](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080211-paste-20260506-080211.jpg)

## 参数

- **外径** - 圆环的外侧直径
- **内径** - 中心孔的直径

## 提示

- 圆环的壁厚为（外径 - 内径）/ 2
- 拉伸圆环路径可生成与[圆环](../primitives/ring.md)基本体类似的管状体

## 相关内容

- [圆路径](circle-path.md) - 实心圆（无孔）
- [圆环](../primitives/ring.md) - 现成的三维管状形体
- [线性拉伸](../operations/path/linear-extrude.md) - 为路径赋予高度
