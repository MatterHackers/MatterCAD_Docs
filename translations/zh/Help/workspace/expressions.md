---
title: 表达式
parent: "Workspace"
nav_order: 2
source_hash: 79a2f2c42d81f7fca56a87ad89f69e4303ed0ae5
source_lang: en
---
# 表达式

MatterCAD 中的许多参数除了可以输入普通数字外，还接受数学表达式。这实现了参数化设计：更改一个数值即可自动更新相关的尺寸。

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)


## 使用方法

在参数字段中，你可以输入数学表达式来代替普通数字。例如：

- `20 + 5` 计算结果为 25
- `pi * 10` 计算结果为 31.416
- `width * 2` 引用另一个名为 “width” 的参数

## 可用常量

- **pi** - 3.14159...（圆周长与直径之比）
- **tau** - 6.28318...（2 * pi，即一整圈的弧度值）

## 支持的运算

- 加法：`+`
- 减法：`-`
- 乘法：`*`
- 除法：`/`
- 括号：`(` 和 `)` 用于分组

## 提示

- 凡是在代码中显示 `DoubleOrExpression`、`IntOrExpression` 或 `StringOrExpression` 的字段都支持表达式 —— 实际上，设计工具中的大多数数值字段都可以使用表达式
- 使用表达式在参数之间建立关联 —— 例如，将孔的直径设为 `outer_diameter - 4`，使其始终保持 2mm 的壁厚
- 当被引用的数值发生变化时，表达式会自动更新
- 当多个对象需要共享相同的命名数值或公式时，请使用[变量表](variable-sheet.md)
- 你可以在[阵列](../operations/array/index.md)操作中使用表达式，以创建参数化的图案

## 相关内容

- [组件](components.md) - 创建可重复使用的参数化设计
- [变量表](variable-sheet.md) - 存储设计中共享的数值和公式
- [编辑对象](../getting-started/editing-objects.md) - 使用对象参数进行操作
