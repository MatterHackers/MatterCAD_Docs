---
title: 编辑对象
parent: "Getting Started"
nav_order: 3
source_hash: 5190f3e59be7ea02497903b15c1956ed68b4d270
source_lang: en
---
# 编辑对象

MatterCAD 在 3D 视图中内置了直观的控件，用于移动、旋转和缩放对象。您还可以在属性面板中编辑对象参数。

## 移动零件


- **在平台上拖动** - 点击并拖动任意对象，使其在工作区表面上滑动
- **上下移动** - 使用所选对象顶部的垂直箭头控件调整其高度（Z 位置）
- 如需精确定位，请使用[平移](../operations/transform/translate.md)操作，或在属性面板中输入精确数值

## 旋转零件

![20260324 080843 paste 20260324 080843](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080843-paste-20260324-080843.jpg)

点击选择对象时出现的任意**旋转角控件**。这些控件可让您在该控件所在的平面上旋转对象。

- 将鼠标移动到某个角度指示器上，可将旋转吸附为 **45 度增量**
- 如需精确旋转，请使用[旋转](../operations/transform/rotate.md)操作并输入精确角度

## 缩放零件

![20260324 080819 paste 20260324 080819](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080819-paste-20260324-080819.jpg)


点击任意**缩放角控件**，即可在工作区中调整零件大小。

- 拖动一个角以按比例缩放
- 如需精确设置尺寸或进行非等比缩放，请使用[缩放](../operations/transform/scale.md)操作，您可以在其中设置精确尺寸或分别缩放各个轴

## 编辑参数

当您选择一个对象时，其参数会显示在屏幕右侧的属性面板中。例如：

- **立方体**会显示宽度、深度、高度以及可选的圆角控件
- **圆柱体**会显示直径、高度和侧面
- **文本**对象会显示文本内容、字体、尺寸和高度

您可以直接输入数值、使用滑块，或输入[表达式](../workspace/expressions.md)来建立参数化关系。

## 上下文菜单

右键点击任意对象即可访问更多选项，包括：

- 复制、剪切、删除
- 组 / 取消组合
- 所选对象的可用操作
- 针对特定对象类型的帮助（如果可用）

## 提示

- 点击时按住 **Shift** 可选择多个对象，然后一起移动或对其执行操作
- 按下 **Ctrl+Z** 可撤销所做的任何更改
- 使用[对齐](../operations/placement/align.md)可精确地将多个对象相对彼此定位
- 按下**空格键**可清除选择

## 相关内容

- [视口导航](viewport-navigation.md) - 如何旋转、平移和缩放视图
- [选择](../workspace/selection.md) - 详细的选择行为
- [变换操作](../operations/transform/index.md) - 精确的变换控件
- [键盘快捷键](../workspace/keyboard-shortcuts.md) - 全部可用快捷键
