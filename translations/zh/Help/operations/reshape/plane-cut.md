---
title: 平面切割
articleKey: PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
source_hash: 64a9901bf54b71cd2ecc12c8db189b6e2fcde25e
source_lang: en
---
# 平面切割

平面切割使用一个水平面在指定高度处剖切物体，仅保留切割面以下的部分。切割面会以平整面封闭。

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## 使用方法

1. 选择一个物体
2. 从重塑菜单中应用 **平面切割** 操作
3. 设置切割高度

## 参数

- **切割高度** - 剖切物体所在的 Z 高度（默认值：10mm，范围：1-200mm）

## 提示

- 使用平面切割可在特定高度将模型顶部削平
- 适用于修整导入的模型或创建平整底面
- 若要使用非平面形状进行切割，请改用 [减去](../boolean/subtract.md) 与另一个物体进行运算
- 若要使用倾斜平面进行切割，请先旋转物体，应用平面切割，然后再旋转回来

## 相关内容

- [相交](../boolean/intersect.md) - 仅保留物体重叠的部分
- [减去](../boolean/subtract.md) - 使用任意形状进行切割，而不仅仅是平面
- [挖空](hollow-out.md) - 创建中空壳体
