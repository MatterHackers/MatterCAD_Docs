---
title: 缩放
articleKey: ScaleObject3D_3
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b3b5419c3db29550b2544bb6aca91ca3ce6fa715
source_lang: en
---
# 缩放

缩放可调整对象的大小，并精确控制尺寸、比例和单位换算。您可以进行等比缩放、将特定轴锁定在一起，或独立调整各轴的尺寸。

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## 使用方法

1. 选择一个对象
2. 从变换菜单中应用 **缩放** 操作
3. 选择缩放方式并输入所需数值

您还可以在视口中选中对象后，单击并拖动其角部的缩放控制柄来缩放对象。

## 参数

### 缩放类型

选择预设或自定义缩放：

- **自定义** - 输入自己的尺寸或百分比
- **英寸转 mm** - 乘以 25.4（英制转公制）
- **毫米转英寸** - 乘以 0.0393（公制转英制）
- **毫米转厘米** - 乘以 0.1
- **cm 转 mm** - 乘以 10

### 缩放方式（自定义模式）

- **直接** - 以毫米为单位输入所需的宽度、深度和高度
- **百分比** - 以原始尺寸的百分比形式输入宽度、深度和高度

### 锁定比例

- **无（自由缩放）** - 各轴独立缩放
- **X 和 Y** - 宽度和深度锁定在一起；高度独立缩放
- **X、Y 和 Z** - 三个轴等比同步缩放

### 尺寸

- **宽度** - 沿 X 轴的尺寸
- **深度** - 沿 Y 轴的尺寸
- **高度** - 沿 Z 轴的尺寸

## 提示

- 如果导入的 STL 文件是以英寸设计的且显示过小，请使用“英寸转 mm”
- 将锁定比例设为 X、Y 和 Z 可实现等比缩放——修改任一尺寸都会同步更新其余尺寸
- 缩放过程中会保持对象的底部位置，使其始终位于工作区表面上
- 您可以输入精确数值以获得准确尺寸，也可以使用滑块进行快速调整

## 相关内容

- [平移](translate.md) - 移动对象
- [旋转](rotate.md) - 旋转对象
- [适配边界](../placement/fit-to-bounds.md) - 缩放以适配指定尺寸
