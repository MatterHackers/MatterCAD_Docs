---
title: 线性拉伸
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cdfdb9cfe4c3339e70a23ddfb2f5071b1e8c5557
source_lang: en
---
# 线性拉伸

线性拉伸为二维路径赋予高度，将平面形状转换为三维实体。这是将路径转换为三维对象的主要方式。

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## 使用方法

1. 选择一个二维路径或基于路径的对象
2. 从路径操作菜单中应用 **线性拉伸**
3. 设置所需的高度

## 参数

- **高度** - 拉伸的高度（默认值：5mm，范围：0.1-50mm）
- **顶部倒角** - 在拉伸体顶部添加倒角（圆角）边缘（默认值：关闭）

### 倒角参数（启用顶部倒角时显示）

- **样式** - 倒角轮廓样式（尖锐或圆角）
- **半径** - 倒角延伸的宽度（默认值：3mm）
- **分段** - 倒角曲线的平滑度（默认值：9）

## 提示

- 该操作适用于任何二维路径：[圆](../../2d-paths/circle-path.md)、[方块](../../2d-paths/box-path.md)、[星形](../../2d-paths/star-path.md)、[SVG](../../primitives/svg-object.md) 以及[自定义](../../2d-paths/custom-path.md)路径
- 启用顶部倒角可获得更精致、更专业的外观
- 若要让路径绕轴旋转而非直接向上拉伸，请参阅[旋转成型](revolve.md)

## 相关内容

- [旋转成型](revolve.md) - 让路径绕轴旋转
- [二维路径](../../2d-paths/index.md) - 可用的路径形状
- [文本](../../primitives/text.md) - 文本会自动拉伸
