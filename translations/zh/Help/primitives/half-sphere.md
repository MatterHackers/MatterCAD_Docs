---
title: 半球
articleKey: HalfSphereObject3D
parent: "Primitives"
nav_order: 7
source_hash: 4f82c152ab27e32e36e758c83f9135f1c6bb2096
source_lang: en
---
# 半球

球体的上半部分——一种穹顶形状。适用于创建穹顶顶部、透镜形状和圆弧形盖子。

<!--  Screenshot of a Half Sphere primitive on the workspace -->
![20260318 183343 paste 20260318 183343](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183343-paste-20260318-183343.jpg)


## 参数

- **直径** - 穹顶底部的宽度（默认值：20mm）
- **经度分段数** - 沿周长方向的分段数量（默认值：40）
- **纬向分段数** - 从底部到顶部的分段数量（默认值：10）。数值越大 = 穹顶越光滑

## 提示

- 将两个半球与一个圆柱体组合，可得到胶囊形状
- 放置在圆柱体顶部，可创建穹顶形盖子或按钮
- 与[减去](../operations/boolean/subtract.md)配合使用，可创建穹顶形空腔

## 相关内容

- [球体](sphere.md) - 完整的球形
- [半圆柱](half-cylinder.md) - 对半剖开的圆柱体
