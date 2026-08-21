---
title: 平移
articleKey: TranslateObject3D
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c05550dee2397bdb58dc2e247a068a544233a71d
source_lang: en
---
# 平移

平移可将对象沿 X、Y 和/或 Z 轴移动指定的距离。与用鼠标拖动对象不同，平移允许你输入精确的偏移值。

<!--  Screenshot showing the Translate operation properties with X, Y, Z offset fields -->
![20260506 160828 paste 20260506 160828](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160828-paste-20260506-160828.jpg)


## 使用方法

1. 选择一个对象
2. 从变换菜单中应用 **平移** 操作
3. 在属性面板中输入所需的 X、Y 和 Z 偏移值

## 参数

- **X、Y、Z**（平移）- 对象沿各轴移动的距离，单位为毫米。支持使用[表达式](../../workspace/expressions.md)来计算数值。

## 提示

- 当你需要精确、可重复且之后仍可调整的定位时，请使用平移
- 平移值是相对于对象当前位置的——为 X 输入 10 会使其从当前位置向右移动 10mm
- 如需快速重新定位，你也可以直接在视口中拖动对象。参见[编辑对象](../../getting-started/editing-objects.md)

## 相关内容

- [旋转](rotate.md) - 将对象旋转指定的角度
- [缩放](scale.md) - 精确调整对象的尺寸
- [对齐](../placement/align.md) - 使对象相对彼此定位
