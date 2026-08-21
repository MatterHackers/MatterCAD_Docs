---
title: 二维码
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
source_hash: 5b941a39b8430a9536401e4af230c06a42635205
source_lang: en
---
# 二维码

将二维码生成为 3D 对象。您可以将文本、网址或 WiFi 凭据编码为可扫描的 3D 二维码。

<!--  Screenshot of a 3D QR Code object on the workspace -->
![20260318 184540 paste 20260318 184540](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184540-paste-20260318-184540.jpg)


## 使用方法

1. 从**基本体**面板添加一个**二维码**
2. 选择输出类型（文本或 WiFi）
3. 输入您的内容
4. 二维码会生成为 3D 对象，可放置到您的设计中

## 参数

### 文本模式

- **文本** - 要编码的文本或网址（默认：“https://matterhackers.com”）

### WiFi 模式

- **SSID** - WiFi 网络的名称
- **密码** - WiFi 密码
- **安全** - 安全类型（WEP、WPA 或无）

## 提示

- 使用[减去](../operations/boolean/subtract.md)可将二维码雕刻到表面上，或将其放置在[立方体](cube.md)底座之上
- 打印前请先用手机测试二维码能否正确扫描
- WiFi 二维码可让他人通过扫码连接到您的网络
- 确保二维码足够大，打印后仍可扫描——至少 20-25mm 宽

## 相关内容

- [文本](text.md) - 标准 3D 文本
- [图像对象](image-object.md) - 将图像转换为 3D
