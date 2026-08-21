---
title: 立方体
articleKey: CubeObject3D
parent: "Primitives"
nav_order: 4
source_hash: a376a9c78d88d995f3c6ce21dd5098672d6c1dfb
source_lang: en
---
# 立方体

一种矩形盒状体，可调整宽度、深度、高度，并可选择添加圆角边。立方体是构建设计时最常用的基本体之一。

<!--  Screenshot of a Cube primitive on the workspace -->
![20260318 183230 paste 20260318 183230](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183230-paste-20260318-183230.jpg)


## 参数

- **宽度** - 沿 X 轴方向的尺寸（默认值：20mm）
- **深度** - 沿 Y 轴方向的尺寸（默认值：20mm）
- **高度** - 沿 Z 轴方向的尺寸（默认值：20mm）
- **圆角** - 启用圆角边
- **半径** - 圆角的大小（启用圆角时可见）
- **圆角分段数** - 圆角的平滑程度，分段越多 = 曲线越平滑（启用圆角时可见）

## 提示

- 将立方体用作盒体、平板、支架和外壳的起始形状
- 启用圆角可获得平滑、专业的边缘效果
- 半径不能超过最小尺寸的一半
- 将立方体与 [减去](../operations/boolean/subtract.md) 结合使用，可创建矩形挖槽和插槽

## 相关内容

- [圆柱体](cylinder.md) - 圆形柱状体
- [棱锥体](pyramid.md) - 四面锥形体
- [孔](hole.md) - 预先配置用于布尔减去运算的立方体
