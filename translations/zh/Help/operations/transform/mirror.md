---
title: 镜像
articleKey: MirrorObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 8a8de28f5e429177d4b0092d0756387eb6b83a70
source_lang: en
---
# 镜像

镜像会沿三个主轴之一创建对象的反射副本。其结果是原始形状的镜像版本。

<!--  Before and after showing an object mirrored across the X axis -->
![20260506 160651 paste 20260506 160651](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160651-paste-20260506-160651.jpg)


## 使用方法

1. 选择一个对象
2. 从变换菜单中应用**镜像**操作
3. 选择要沿其镜像的轴

## 参数

- **镜像开启** - 用于镜像的轴：
  - **X 轴** - 将对象左右翻转
  - **Y 轴** - 将对象前后翻转
  - **Z 轴** - 将对象上下翻转

## 提示

- 镜像以对象的边界框为中心，因此镜像结果占据与原始对象相同的空间
- 镜像后会自动校正面法线，以保持正确的渲染效果
- 使用镜像来创建对称设计——先建模一半，然后将其镜像并与原始对象[合并](../boolean/combine.md)
- 镜像是非破坏性的：你可以随时更改镜像轴

## 相关内容

- [旋转](rotate.md) - 旋转对象而非镜像对象
- [缩放](scale.md) - 调整对象大小
- [合并](../boolean/combine.md) - 将原始对象与镜像副本合并为一个对象
