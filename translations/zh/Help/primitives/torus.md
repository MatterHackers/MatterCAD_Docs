---
title: Torus
articleKey: TorusObject3D
parent: "Primitives"
nav_order: 17
source_hash: aaec1652de4d6713bd01a707964cf4985d3fb5f6
source_lang: en
---
# Torus

甜甜圈形状的圆环，可独立控制整体尺寸和圆环横截面的粗细。

<!--  Screenshot of a Torus primitive on the workspace -->
![20260318 184240 paste 20260318 184240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184240-paste-20260318-184240.jpg)


## 参数

- **外径** - 圆环体的整体宽度（默认值：20mm）
- **内径** - 中心孔的直径（默认值：10mm）
- **侧面** - 主圆环周围的分段数量（默认值：40）

### 高级参数

启用**高级**模式以获得更多控制项：

- **起始角度** - 圆环体开始的角度（默认值：0）
- **终止角度** - 圆环体结束的角度（默认值：360）。设置为小于 360 可得到开口圆环或圆弧
- **圆环边数** - 圆环横截面周围的分段数量（默认值：15）。数值越大 = 管状轮廓越光滑
- **圆环相位角** - 旋转横截面轮廓（默认值：0）

## 提示

- 圆环管的粗细由外径与内径之差决定
- 使用起始角度和终止角度可创建开口圆环段、圆弧或 C 形
- 适合用于创建 O 形圈、把手、装饰环和弯管

## 相关内容

- [圆环](ring.md) - 直壁空心圆柱（管）
- [球体](sphere.md) - 实心球体形状
- [半球](half-sphere.md) - 穹顶形状
