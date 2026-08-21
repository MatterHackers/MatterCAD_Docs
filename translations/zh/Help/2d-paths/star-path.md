---
title: 星形路径
articleKey: StarPathObject3D
parent: "2D Paths"
nav_order: 5
source_hash: 74d92e4171c452cd10069921636e45d7ef9dc70e
source_lang: en
---
# 星形路径

一种星形二维路径，可配置点的数量以及内侧/外侧半径。可与[线性拉伸](../operations/path/linear-extrude.md)配合使用，创建三维星形形状。

<!-- Screenshot of a Star Path on the workspace -->
![20260506 080319 paste 20260506 080319](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080319-paste-20260506-080319.jpg)


## 参数

- **点** - 星形的角数量
- **外侧半径** - 从中心到每个角尖端的距离
- **内侧半径** - 从中心到各角之间凹谷的距离

## 提示

- 内侧半径与外侧半径之比决定星形的“尖锐”程度。较小的内侧半径可形成锐利、突出的尖角。
- 将点设为 5 可得到经典星形，设为 6 可得到大卫之星形状，设置更大的值则可得到类似齿轮的形状
- 对星形路径使用[平滑路径](../operations/path/smooth-path.md)，可创建圆润的星形形状

## 相关内容

- [圆形路径](circle-path.md) - 平滑的圆
- [二维齿轮](../mechanical/gear-2d.md) - 标准的齿轮轮廓
- [线性拉伸](../operations/path/linear-extrude.md) - 为路径赋予高度
