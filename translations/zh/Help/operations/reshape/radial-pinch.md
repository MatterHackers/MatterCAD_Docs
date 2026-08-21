---
title: 径向收缩
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: 95ef5847767e5cfcdbae9df9aaa1cb1727da2f5e
source_lang: en
---
# 径向收缩

径向收缩使用可自定义的轮廓曲线，将物体从中心点向内压缩。与常规的 [收缩](pinch.md)（从后向前作用）不同，径向收缩围绕中心轴对称地进行压缩。

<!--  Before and after showing an object with radial pinch applied, creating a waisted shape -->
![20260506 155741 paste 20260506 155741](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155741-paste-20260506-155741.jpg)

## 使用方法

1. 选择一个物体
2. 从重塑菜单中应用 **径向收缩** 操作
3. 编辑路径轮廓，以定义每个高度处施加的收缩量
4. 调整切片数量以获得平滑效果

## 参数

- **路径** - 轮廓曲线编辑器，用于定义每个高度层级的收缩量。编辑曲线可创建自定义收缩轮廓
- **切片** - 用于平滑收缩的水平切割数量，沿零件高度均匀分布。切片越多 = 结果越平滑

### 高级参数

- **收缩类型** - 压缩的方向：
  - **径向** - 从各个方向均匀地向中心压缩
  - **X 轴** - 仅沿 X 轴压缩
  - **Y 轴** - 仅沿 Y 轴压缩
- **旋转偏移** - 移动收缩效果的中心

## 提示

- 使用路径编辑器可创建沙漏形、瓶形或花瓶形的形状
- 径向收缩非常适合从圆柱形物体创建有机的圆润造型
- 增加切片数量可获得更平滑的曲线，尤其是在收缩轮廓较陡时

## 相关内容

- [收缩](pinch.md) - 简单的从后向前压缩
- [扭曲](twist.md) - 沿高度方向螺旋旋转
- [曲线](curve.md) - 弯曲成弧形
