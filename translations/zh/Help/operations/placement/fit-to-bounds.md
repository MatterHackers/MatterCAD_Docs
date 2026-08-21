---
title: 适配边界
articleKey: FitToBoundsObject3D_4
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 91b9c917cb636f28403c291a4d56f22bf6758b70
source_lang: en
---
# 适配边界

适配边界可将对象缩放至指定的宽度、深度和高度尺寸范围内。您可以控制对象在目标边界内的拉伸方式和对齐方式。

<!--  Screenshot showing an object being fit to specific bounding dimensions -->
![20260506 154930 paste 20260506 154930](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154930-paste-20260506-154930.jpg)

## 使用方法

1. 选择一个对象
2. 从放置菜单中应用 **适配边界** 操作
3. 输入目标尺寸
4. 选择锁定比例和拉伸行为

## 参数

- **锁定比例** - 如何约束比例：
  - **无** - 每个轴可独立设置
  - **X & Y** - 宽度和深度一同锁定
  - **X, Y & Z** - 所有轴均匀缩放
- **宽度** - 目标宽度（X 方向尺寸）
- **深度** - 目标深度（Y 方向尺寸）
- **高度** - 目标高度（Z 方向尺寸）

### 当锁定比例为 X & Y 或 X, Y & Z 时

- **拉伸** - 对象的适配方式：
  - **内部** - 缩小以完全容纳在边界内（可能留有空隙）
  - **展开** - 放大以填满边界（可能在某些方向上超出）

### 当锁定比例为无时

每个轴都有各自的：

- **拉伸** - 每个轴分别设置内部或展开
- **对齐** - 在边界内的定位方式（最小、居中、最大）

## 提示

- 使用此功能可将导入的模型调整为精确的目标尺寸
- 锁定所有比例可进行保持原始形状的均匀缩放
- 当您需要适配特定宽度而不关心其他尺寸时，可使用逐轴控制

## 相关内容

- [缩放](../transform/scale.md) - 按比率或百分比缩放，而非按目标尺寸
- [拟合圆柱](fit-to-cylinder.md) - 适配到圆柱形边界内
- [对齐](align.md) - 使对象相互之间定位
