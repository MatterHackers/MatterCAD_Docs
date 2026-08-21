---
title: SVG 对象
articleKey: SvgObject3D
parent: "Primitives"
nav_order: 15
source_hash: dab97cdde74d938b5612d959f83b54b4a04a49da
source_lang: en
---
# SVG 对象

导入 SVG（可缩放矢量图形）文件，并将其用作设计中的 2D 路径。随后可使用[线性拉伸](../operations/path/linear-extrude.md)或[旋转成型](../operations/path/revolve.md)将 SVG 拉伸为 3D 形状。

<!--  Screenshot showing an imported SVG path being extruded into a 3D shape -->
![20260318 184807 paste 20260318 184807](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184807-paste-20260318-184807.jpg)



## 使用方法

1. 将 SVG 文件拖放到工作区，或使用打开按钮导入该文件
2. SVG 会作为 2D 路径导入
3. 应用[线性拉伸](../operations/path/linear-extrude.md)为其赋予高度，或使用其他[路径操作](../operations/path/index.md)

## 提示

- SVG 文件应包含填充形状或闭合路径，以获得最佳效果
- 包含大量路径的复杂 SVG 处理时间可能较长
- 使用[选择路径](../operations/path/select-paths.md)处理多路径 SVG 中的特定部分
- 网上有许多免费的 SVG 文件，可用于徽标、图标和装饰图案

## 相关内容

- [图像转路径](../operations/image/image-to-path.md) - 将栅格图像转换为路径，而无需使用 SVG
- [文本](text.md) - 无需 SVG 即可直接创建文本
- [线性拉伸](../operations/path/linear-extrude.md) - 为平面路径赋予高度
- [2D 路径](../2d-paths/index.md) - 内置路径基本图元
