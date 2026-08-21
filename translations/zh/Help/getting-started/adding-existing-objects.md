---
title: 添加现有对象
parent: "Getting Started"
nav_order: 1
source_hash: e384a5c024336c3c58343d262d914fa40e0b0426
source_lang: en
---
# 添加现有对象

您可以通过从计算机导入文件或从内置库中添加内容，将现有的 3D 模型引入 MatterCAD。

## 从您的计算机

![20260324 081143 paste 20260324 081143](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081143-paste-20260324-081143.jpg)

![20260324 081240 paste 20260324 081240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081240-paste-20260324-081240.jpg)


单击工具栏中的 **打开** 按钮，即可浏览并添加计算机中的文件。MatterCAD 支持以下导入格式：

- **STL** (.stl) - 行业标准 3D 模型格式，广泛用于 3D 打印
- **AMF** (.amf) - 支持颜色和多材质对象的高级格式
- **OBJ** (.obj) - Wavefront 3D 图形格式（仅网格几何体）
- **3MF** (.3mf) - 具有丰富元数据支持的 3D 制造格式
- **MCX** (.mcx) - MatterCAD 的原生格式，保留所有设计数据和参数
- **SVG** (.svg) - 可缩放矢量图形，导入为 2D 路径
- **TTF / OTF** (.ttf, .otf) - 用于 **文本** 工具的字体文件

## 拖放

您还可以将文件直接从桌面或文件资源管理器拖放到 MatterCAD 工作区中。支持的文件类型将被自动导入。

![20260324 081416 paste 20260324 081416](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081416-paste-20260324-081416.jpg)

## 从库中添加

### 库侧边栏

单击工具栏中的 **添加内容** 按钮，打开库浏览面板。在这里您可以：

- 浏览已保存的设计
- 转到 **基本体** 库使用内置形状
- 登录后访问您的 **云端库**
- 将库中的任意项目直接拖放到工作区中

![20260324 081446 paste 20260324 081446](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081446-paste-20260324-081446.jpg)

### 库选项卡

您还可以使用 **库** 选项卡浏览您的收藏集。在库中的任意对象上单击右键，然后选择 **添加到场景**，即可将其导入当前的设计工作区。

![20260324 081536 paste 20260324 081536](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081536-paste-20260324-081536.jpg)

## 提示

- MCX 是日后重新编辑设计的最佳格式，因为它保留了所有参数和设计树
- STL 文件仅包含网格几何体。导入 STL 后，您仍可对其应用各种操作，但无法编辑其原始参数
- 导入多个文件时，每个文件都会成为场景中的一个独立对象。可使用 [组](../workspace/grouping.md) 来整理它们

## 相关内容

- [创建新对象](creating-new-objects.md) - 使用基本体从零开始设计
- [保存与导出](saving-and-exporting.md) - 保存并导出您完成的设计
- [库](../library/index.md) - 详细了解如何整理您的设计库
