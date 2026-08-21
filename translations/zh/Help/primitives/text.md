---
title: 文本
articleKey: TextObject3D_2
parent: "Primitives"
nav_order: 16
source_hash: 526f3190c7b2150243499b5874ac455d74810bb2
source_lang: en
---
# 文本

创建三维拉伸文本，内容、字体、尺寸和高度均可自定义。文本对象非常适合用于标签、标牌、铭牌和装饰性字体。

<!--  Screenshot of a 3D Text object on the workspace showing extruded letters -->
![20260318 184207 paste 20260318 184207](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184207-paste-20260318-184207.jpg)


## 使用方法

1. 从基本体面板中添加一个 **文本** 基本体
2. 在属性面板的 **名称** 字段中输入您的文本
3. 根据需要调整字体、尺寸和拉伸高度

## 参数

- **名称** - 要显示的文本内容
- **点大小** - 字体大小。该值与标准印刷尺寸相对应——MatterCAD 中的 12 点大小与二维打印机上的 12 点字号一致
- **高度** - 拉伸高度（文本从表面凸起的距离）
- **字体** - 从可用的系统字体中选择

## 提示

- 使用 [减去](../operations/boolean/subtract.md) 可将文本雕刻进表面，而不是凸起于表面
- 对于非常小的文本，可增大点大小，然后对整个对象进行[缩放](../operations/transform/scale.md)，以获得更好的细节
- 文本中的每个字母都是一条独立的路径，并被一起拉伸

## 相关内容

- [盲文](braille.md) - 生成可三维打印的盲文文本
- [二维码](qr-code.md) - 将二维码生成为三维对象
- [图像对象](image-object.md) - 将图像转换为三维模型
