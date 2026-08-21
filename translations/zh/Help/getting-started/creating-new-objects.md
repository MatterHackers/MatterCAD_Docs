---
title: 创建新对象
parent: "Getting Started"
nav_order: 2
source_hash: 3eccb5aac5bb6f4d88f1ca3583eedd2f70384eeb
source_lang: en
---
# 创建新对象

MatterCAD 提供了丰富的 3D 对象创建工具。您可以从基本体形状开始，使用文本和二维码等专用工具，也可以通过布尔操作和阵列构建复杂的形体。

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## 添加基本体

开始设计最快的方式是添加基本体形状。在库中打开基本体面板，点击任意形状即可将其添加到工作区。可用的基本体包括：

- **基础形状** - 立方体、圆柱体、球体、圆锥体、圆环体、圆环、棱锥体、楔形体，以及它们的半形变体
- **文本与特殊对象** - 文本、盲文、二维码、图像对象、SVG 对象

每个基本体在选中后都可以在属性面板中调整其参数。例如，立方体具有宽度、深度和高度控件。有关每种形状的详细信息，请参阅 [基本体](../primitives/index.md)。

## 操作工具栏

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

视口顶部的工具栏可让您快速使用常用操作：

- **撤销 / 重做** - 撤回或重新应用更改。您还可以使用 **Ctrl+Z** 撤销，使用 **Ctrl+Y** 重做
- **组 / 取消组合** - 将选中的对象合并为一个组，使其作为一个整体移动和操作，或将组拆散
- **复制 / 删除** - 复制或移除选中的对象。标准的 **Ctrl+C**、**Ctrl+X** 和 **Ctrl+V** 快捷键同样有效
- **对齐** - 将多个对象相对彼此定位
- **布尔操作** - [合并](../operations/boolean/combine.md)、[减去](../operations/boolean/subtract.md)、[相交](../operations/boolean/intersect.md) 和 [减去并替换](../operations/boolean/subtract-and-replace.md)
- **阵列** - 为复制的对象创建 [线性、径向、曲线和变换图案](../operations/array/array.md)
- **变换** - 应用 [旋转](../operations/transform/rotate.md)、[缩放](../operations/transform/scale.md)、[镜像](../operations/transform/mirror.md) 及其他修改

## 构建复杂形状

MatterCAD 中的大多数设计都是通过组合简单形状构建的：

1. **从基本体开始** - 添加所需的基础形状
2. **对其进行定位** - 移动和旋转对象，使它们在需要的位置重叠
3. **应用布尔操作** - 使用 [合并](../operations/boolean/combine.md) 将形状融合在一起，或使用 [减去](../operations/boolean/subtract.md) 从一个形状中切除另一个形状
4. **细化** - 使用倒角、曲线或扭曲等 [重塑](../operations/reshape/index.md) 操作添加细节

## 相关内容

- [基本体](../primitives/index.md) - 所有基本体形状的完整参考
- [添加现有对象](adding-existing-objects.md) - 导入文件，而不是从零开始创建
- [布尔操作](../operations/boolean/index.md) - 将形状组合成复杂的形体
- [编辑对象](editing-objects.md) - 创建对象后对其进行移动、旋转和缩放
