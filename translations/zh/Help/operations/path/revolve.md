---
title: 旋转成型
articleKey: RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: a63ebb08d982178e0e59f0b9f07c3c0dca53148b
source_lang: en
---
# 旋转成型

旋转成型将二维路径绕某一轴旋转，生成三维回转实体。花瓶、碗、轮子以及其他旋转对称的物体都可以通过这种方式创建。

<!--  Before and after showing a profile path being revolved into a vase shape -->
![20260506 102004 paste 20260506 102004](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-102004-paste-20260506-102004.jpg)


## 使用方法

1. 选择一条二维路径
2. 从路径操作菜单中应用 **旋转成型**
3. 调整旋转范围、轴位置和侧面数量

## 参数

- **旋转** - 旋转成型的总旋转角度（默认值：0，范围：0-360）。设为 360 可获得完整回转。
- **轴位置** - 旋转轴相对于路径中心的偏移（默认值：0，范围：-30 至 30）。正向会使轴远离路径，形成更大的开口。
- **起始角度** - 回转开始的位置（默认值：0）
- **终止角度** - 回转结束的位置（默认值：45）。设为 360 可获得完整回转。
- **侧面** - 回转一周的分段数量（默认值：30）。数值越大，表面越光滑。

## 提示

- 使用轴位置可控制旋转成型形状的内径
- 将起始角度和终止角度设为小于 360，可创建部分回转（拱形、排水槽）
- 绘制花瓶或碗形的轮廓路径，然后进行旋转成型，即可获得完美的对称效果
- 对[圆路径](../../2d-paths/circle-path.md)进行旋转成型可生成圆环体

## 相关内容

- [线性拉伸](linear-extrude.md) - 直接向上拉伸，而非旋转成型
- [二维路径](../../2d-paths/index.md) - 创建用于旋转成型的轮廓路径
- [Torus](../../primitives/torus.md) - 现成的旋转成型环形形状
