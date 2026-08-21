---
title: 旋转
articleKey: RotateObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 9bdc210c5c375fe3179050e8a8916d895455ce5f
source_lang: en
---
# 旋转

旋转会使对象围绕指定轴按给定角度转动。您可以围绕任意轴方向旋转，并选择旋转的中心点。

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## 使用方法

1. 选择一个对象
2. 从变换菜单中应用 **旋转** 操作
3. 在属性面板中设置旋转角度和轴

您还可以直接在视口中旋转对象：单击选定对象上的旋转角控件即可。将鼠标移到角度指示器上时，会按 45 度增量吸附。

## 参数

- **角度** - 以度为单位的旋转角度（范围：3-360）。支持[表达式](../../workspace/expressions.md)。
- **旋转轴心** - 定义旋转轴和原点。您可以围绕 X、Y 或 Z 轴旋转，也可以指定自定义方向。

## 提示

- 默认情况下，旋转以对象包围盒的中心为中心
- 对于 90 度旋转，吸附指示器可让您轻松获得精确数值
- 当您需要不是 45 度倍数的精确角度时，请使用旋转操作（而非视口控件）
- 应用该操作后，您可以通过编辑旋转轴心属性来更改旋转轴

## 相关内容

- [平移](translate.md) - 按指定距离移动对象
- [缩放](scale.md) - 调整对象大小
- [镜像](mirror.md) - 创建镜像反射
