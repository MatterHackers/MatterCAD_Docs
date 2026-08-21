---
title: 孔
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# 孔

一种立方体形状的对象，已预先配置为布尔减法工具。当您使用[合并](../operations/boolean/combine.md)时，孔对象会自动从其他形状中减去，而不是添加到其中。

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## 工作原理

孔基本体的工作方式与[立方体](cube.md)相同，但其输出类型被设置为“孔”。当您合并包含孔的对象时，孔的体积会从结果中移除。

## 参数

与[立方体](cube.md)相同：

- **宽度** - 沿 X 轴的尺寸
- **深度** - 沿 Y 轴的尺寸
- **高度** - 沿 Z 轴的尺寸

## 提示

- 调整孔的位置，使其与要切除的对象重叠
- 如果需要通孔，请让孔完全贯穿目标对象
- 您也可以使用普通形状配合[减去](../operations/boolean/subtract.md)实现相同效果，但孔更为便捷，因为它们会自动配合[合并](../operations/boolean/combine.md)使用
- 如需圆形孔，请改用[圆柱体](cylinder.md)配合减去

## 相关内容

- [立方体](cube.md) - 相同的形状，但不具备孔的行为
- [合并](../operations/boolean/combine.md) - 合并各个形状并自动减去孔
- [减去](../operations/boolean/subtract.md) - 手动从一个形状中减去另一个形状
