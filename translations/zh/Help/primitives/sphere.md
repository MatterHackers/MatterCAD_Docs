---
title: 球体
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
source_hash: c227e98ac116c3481bb2af73c55801de84e70b1e
source_lang: en
---
# 球体

直径与细节程度均可调节的圆球形状。

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## 参数

- **直径** - 球体的横向宽度（默认值：20mm）
- **侧面** - 周向的分段数量（默认值：40）。侧面越多 = 表面越光滑

### 高级参数

启用**高级**模式以使用更多控件：

- **起始角度** - 球体表面开始处的角度（默认值：0）
- **终止角度** - 球体表面结束处的角度（默认值：360）。设置为小于 360 可得到部分球体形状
- **纬向分段数** - 从顶部到底部的分段数量（默认值：30）。数量越多 = 两极越光滑

## 提示

- 用于 3D 打印时，40 个侧面通常已足够。数值越高，表面越光滑，但文件也越大
- 使用起始角度和终止角度可创建碗形或穹顶等部分球体形状
- 与[减去](../operations/boolean/subtract.md)配合使用可创建球形空腔

## 相关内容

- [半球](half-sphere.md) - 仅上半球
- [Torus](torus.md) - 甜甜圈形状
