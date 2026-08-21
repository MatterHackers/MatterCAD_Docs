---
title: 圆形路径
articleKey: CirclePathObject3D
parent: "2D Paths"
nav_order: 2
source_hash: 587edab627246f47731f9dbde2a13a00dd464807
source_lang: en
---
# 圆形路径

圆形的二维路径。与[线性拉伸](../operations/path/linear-extrude.md)配合使用可创建圆柱体，或与[旋转成型](../operations/path/revolve.md)配合使用可创建类似圆环体的形状。

<!-- Screenshot of a Circle Path on the workspace -->
![20260506 080110 paste 20260506 080110](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080110-paste-20260506-080110.jpg)


## 参数

- **直径** - 圆的直径（默认值：20mm）
- **分段** - 构成圆的线段数量。数值越大越平滑

## 提示

- 圆形路径与线性拉伸结合使用可生成圆柱体，效果类似于[圆柱体](../primitives/cylinder.md)基本体，但在此基础上继续建模时更加灵活
- 可用作旋转成型的基础，以创建圆环形状

## 相关内容

- [方块路径](box-path.md) - 矩形的二维路径
- [圆环路径](ring-path.md) - 带孔的圆
- [线性拉伸](../operations/path/linear-extrude.md) - 为路径赋予高度
