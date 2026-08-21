---
title: 变量表
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
source_hash: 3137a4da2b9d2086d4dcace156435caca288dd79
source_lang: en
---
# 变量表

变量表用于存储设计中共享的值。当多个对象需要引用相同的尺寸、数量、标签或公式时，请使用它。修改表中的某个值会重新计算依赖它的对象，因此参数化设计无需逐个编辑对象即可保持一致。

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## 如何添加变量表

1. 打开库并将 **变量表** 添加到场景中。
2. 选择变量表对象以显示表格编辑器。
3. 选择一个单元格，然后输入 **名称** 以及一个值或公式。
4. 在设计中其他支持表达式的字段里使用该单元格名称。

## 编辑单元格

每个单元格有两个可编辑部分：

- **名称** - 单元格的可选变量名称。名称不区分大小写，空格会转换为下划线，重复的名称会自动调整。
- **表达式** - 单元格的值。纯文本或数字会直接存储。公式以 `=` 开头。

单元格也可以通过地址引用，例如 `A1` 或 `B2`。对于设计参数，具名单元格通常更清晰，因为它们能表达用途，例如 `wall_thickness`、`outer_diameter` 或 `hole_count`。

## 公式

以 `=` 开头的公式会在表中求值：

- `=20 + 5` 返回 `25`
- `=pi * 10` 返回 `31.41592653589793`
- `=A1 * 2` 通过地址引用另一个单元格
- `=wall_thickness + 4` 引用一个具名单元格

变量表支持算术运算、括号、比较运算符，常用的 `Math` 函数（如 `sin`、`cos`、`sqrt` 和 `round`），以及包括 `pi`、`tau` 和 `e` 在内的常量。

## 在对象中使用表中的值

MatterCAD 中的大多数数值字段都支持表达式。要在对象参数中使用表中的值，请在引用前加上 `=` 前缀：

- 将立方体的 **宽度** 设置为 `=case_width`。
- 将阵列的 **数量** 设置为 `=hole_count`。
- 将平移的 **偏移** 值设置为 `=wall_thickness * 2`。

当表中的内容发生变化时，MatterCAD 会重新计算依赖它的对象。

## 文本与辅助函数

变量表的单元格既可以保存数字，也可以保存文本。文本值适用于生成的标签、零件编号、导入的数据以及自定义设计应用。

常用的辅助函数包括：

- `concat()` 或 `strcat()` - 将文本或值连接在一起。
- `substring()` - 提取文本值的一部分。
- `split()` - 拆分文本并返回其中一项。
- `count()` - 统计文本中以分隔符分隔的项数。
- `substitute()` - 替换文本。
- `rand(seed)` - 在提供随机种子时生成确定性的随机值。
- `importdata()` - 从 URL 或本地文件路径读取值。

## 提示

- 对于会被其他对象使用的值，优先使用描述性名称而非单元格地址。
- 将核心尺寸放在表格左上角附近，便于查找。
- 对派生值使用公式，例如 `inner_diameter = outer_diameter - wall_thickness * 2`。
- 避免使用保留字（如 `pi`、`e`、`true`、`false`）或函数名作为单元格名称。
- 如果公式无法解析，MatterCAD 会将原始输入保留为文本。

## 相关内容

- [表达式](expressions.md) - 在对象参数中使用表达式
- [组件](components.md) - 创建可重复使用的参数化设计
- [阵列](../operations/array/array.md) - 创建由表中的值驱动的重复图案
