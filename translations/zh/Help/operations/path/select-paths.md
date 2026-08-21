---
title: 选择路径
articleKey: SelectPathsObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: f7df7bb24841030643e4634febedcfce6e92ada9
source_lang: en
---
# 选择路径

选择路径用于筛选复杂路径对象中保留哪些子路径。当处理装饰性字体或多部件字体时，它尤其有用——你可以把字母的外轮廓与内部镂空形状拆分为独立的部件，例如用两种不同颜色进行 3D 打印。

<!--  Screenshot showing Select Paths applied to decorative text with outer paths highlighted -->
![20260506 154655 paste 20260506 154655](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154655-paste-20260506-154655.jpg)

## 路径深度的工作原理

当路径对象包含带有封闭区域的形状（例如字母“O”的内部，或装饰性涡卷的中空部分）时，这些封闭区域即为深度 1 的**孔**。每个字母或形状的外轮廓则处于**深度 0**。

```
Depth 0 — outer contour of each letter or shape
Depth 1 — first level of enclosed holes (inside an "O", "A", etc.)
Depth 2 — shapes nested inside a hole (rarely used)
```

## 筛选预设

### 全部
原样包含所有路径。这是默认设置，等同于完全不应用选择路径。

### 仅外部路径
仅保留每个形状的外轮廓（深度 == 0）。使用该选项可只获取装饰性字体的字母轮廓，而不包含内部镂空区域。

### 仅孔
仅保留封闭的孔（深度 > 0）。使用该选项可只获取字母和形状的内部切除区域。

### 按组索引
仅保留属于某一个不连通形状的路径。组 0 是第一个形状，组 1 是第二个，依此类推。使用该选项可从一个单词中分离出单个字符。

### 自定义
编写一个针对每条路径求值的表达式。当表达式结果非零时，该路径被**包含**；结果为零时被**排除**。

表达式必须以 `=` 开头才能启用变量替换。若没有 `=`，该值将被视为普通数字（例如，`1` 表示始终包含，`0` 表示始终排除）。

## 自定义表达式示例

| 表达式 | 效果 |
|------------|--------|
| `=PathDepth==0` | 仅外轮廓（与仅外部路径相同） |
| `=PathDepth>0` | 仅孔（与仅孔相同） |
| `=GroupIndex==0` | 仅第一个不连通形状 |
| `=PathArea>100` | 面积大于 100 mm² 的形状 |
| `=PathLength>50` | 周长大于 50 mm 的形状 |

## 自定义表达式变量

| 变量 | 含义 |
|----------|---------|
| `PathDepth` | 0 = 外轮廓；1 及以上 = 孔或嵌套形状 |
| `GroupIndex` | 不连通形状的索引（0、1、2……） |
| `GroupOuterArea` | 该组外部路径的面积 |
| `GroupOuterLength` | 该组外部路径的周长 |
| `ChildCount` | 该组外部路径内部的孔数量 |
| `PathIndex` | 该路径在其所属组内的顺序索引 |
| `PathArea` | 该条路径自身的面积 |
| `PathLength` | 该条路径自身的周长 |

## 示例：多色圣诞字体打印

选择路径的一个常见用途是打印带有内部镂空形状的装饰性文本。若要用一种颜色打印字母外形、用第二种颜色打印内部切除部分：

1. 添加一个**文本**对象，并将其设置为 **2D 输出**
2. 应用**选择路径** → 将预设设为**仅外部路径**
3. 应用**线性拉伸**赋予其高度 → 指定第一种耗材颜色
4. 返回原始文本对象
5. 再应用一次**选择路径** → 将预设设为**仅孔**
6. 以相同高度应用**线性拉伸** → 指定第二种耗材颜色
7. 将一个拉伸后的对象叠放在另一个之上——两种颜色可完美对齐

## 相关内容

- [线性拉伸](linear-extrude.md) — 为筛选后的路径赋予高度以创建 3D 对象
- [旋转成型](revolve.md) — 将筛选后的路径绕轴旋转
- [SVG 对象](../../primitives/svg-object.md) — 导入可能包含多条子路径的矢量路径
- [文本](../../primitives/text.md) — 2D 模式下的文本对象会产生多路径输出
