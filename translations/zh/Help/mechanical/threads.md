---
title: 螺纹
articleKey: ThreadsObject3D_2
parent: "Mechanical Parts"
nav_order: 3
source_hash: 7d881b3293a508e102d3a4b845cdfd4eb9c34fa8
source_lang: en
---
# 螺纹

创建可配置直径、螺距和牙型的螺纹。螺纹可作为独立的螺栓/螺钉使用，也可从其他物体中减去以创建螺纹孔。

<!-- AUTO_IMAGE: type=from_thumbnail item=threads file=mechanical_threads -->
![mechanical_threads](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_threads.png)

## 使用方法

1. 从机械工具或基本体面板中添加**螺纹**
2. 设置直径、螺距和旋转数量
3. 如需创建螺纹孔，可选择启用“用作孔”

## 参数

### 用途

- **用作孔** - 启用后，螺纹将带有额外公差，以便作为被减去的孔使用（默认：关闭）
- **公差** - 用作孔时的额外配合间隙（默认：0.2mm，启用“用作孔”时可见）

### 属性

- **直径** - 螺纹段的外径（默认：10mm）
- **螺距** - 每圈螺纹之间的距离（默认：2mm）。螺距越小 = 螺纹越细
- **螺纹比例** - 螺纹宽度相对于螺距的比值（默认：1.0，范围：0.1-1.0）
- **旋转** - 完整的螺纹圈数（默认：10）

### 几何

- **侧面** - 周向上的分段数量（默认：40）。数量越多 = 越光滑

### 尖端（螺纹末端）

- **尖端比例** - 螺纹末端的收缩程度（默认：0，范围：0-1）。设为大于 0 可在末端形成锥形导入段
- **尖端角度** - 尖端收缩所经过的角度（默认：90 度）

## 提示

- 创建螺纹孔：启用“用作孔”，放置好螺纹，然后从物体上执行 [减去](../operations/boolean/subtract.md)
- 用作孔时请添加公差，以确保打印出的零件能够配合
- 标准公制螺纹螺距：M3=0.5mm、M4=0.7mm、M5=0.8mm、M6=1.0mm、M8=1.25mm、M10=1.5mm
- 使用尖端比例创建导入段，可以更容易地开始旋入螺纹

## 相关内容

- [齿轮](gears.md) - 创建机械齿轮形状
- [圆柱体](../primitives/cylinder.md) - 普通的圆形柱体（无螺纹）
- [减去](../operations/boolean/subtract.md) - 从其他物体中切除螺纹以创建孔
