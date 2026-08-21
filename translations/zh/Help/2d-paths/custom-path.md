---
title: 自定义路径
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
source_hash: 3633c708477de3ac77d3547b730c33f7e4431cf6
source_lang: en
---
# 自定义路径

使用控制点绘制自己的二维路径。这让你可以完全自由地创建任意二维形状，随后可将其拉伸或旋转成型为三维对象。

<!-- Screenshot showing a custom path being edited with control points -->
![20260506 080247 paste 20260506 080247](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080247-paste-20260506-080247.jpg)


## 使用方法

1. 从二维路径库中添加一个**自定义路径**
2. 编辑控制点以定义形状
3. 应用[线性拉伸](../operations/path/linear-extrude.md)或其他路径操作来创建三维对象

## 打开与已闭合的路径

**已闭合**复选框控制路径是否将最后一个点与第一个点连接起来。

- **已闭合**（默认）使路径勾勒出一个区域。这正是[线性拉伸](../operations/path/linear-extrude.md)和[旋转成型](../operations/path/revolve.md)所填充的内容。
- **打开**使路径成为一条线。线条不包围任何区域，因此它在场景中显示为沿其长度延伸的细窄带，而不是填充的形状。使用[膨胀路径](../operations/path/inflate-path.md)为其赋予宽度，将其重新变为实体。

在取消勾选**已闭合**之前，有两点需要了解：

- **重新闭合并不等于撤销。** 打开路径会丢弃其闭合线段。如果该线段是曲线，再次勾选**已闭合**只会得到一条直线，而不是原来的曲线。请改用 Ctrl+Z——撤销会精确还原原始路径。
- **某些轮廓无法打开。** 如果打开后某个轮廓剩下的点少于两个——例如由一个点和一条绕回该点的曲线画成的水滴形——它将保持闭合，而不会坍缩成你再也看不到或点不到的东西。包含二次曲线的轮廓同样如此（导入的 SVG 中可能含有这类曲线）：打开它会把曲线压平成一个尖角。这种拒绝是按轮廓生效的，因此路径的其余部分仍会打开。

如果一条路径包含多个轮廓且它们的状态不一致，该复选框会显示为打开状态。勾选它可使所有轮廓保持一致。

需要区域的操作会自动为你闭合打开的路径，而不是拒绝它。线性拉伸、旋转成型、减去以及其他布尔操作都是如此，因此打开的路径拉伸后得到的实体与其闭合版本完全相同。

## 提示

- 当内置的路径形状都不符合需求时，使用自定义路径
- 若要从外部矢量编辑器导入形状，请参阅 [SVG 对象](../primitives/svg-object.md)
- 若要绘制一条线并将其变成零件，取消勾选**已闭合**，应用[膨胀路径](../operations/path/inflate-path.md)为其赋予厚度，然后用[线性拉伸](../operations/path/linear-extrude.md)赋予高度

## 相关内容

- [圆路径](circle-path.md) —— 现成的圆形
- [方块路径](box-path.md) —— 现成的矩形
- [SVG 对象](../primitives/svg-object.md) —— 从 SVG 文件导入矢量路径
- [线性拉伸](../operations/path/linear-extrude.md) —— 为路径赋予高度
