---
title: 组
parent: "Workspace"
nav_order: 3
source_hash: 82b506a886e270535b5bd58c3913f49328abc4d5
source_lang: en
---
# 组

分组可将多个对象合并为一个整体，使其能够作为单个对象进行移动、复制和操作。与 [合并](../operations/boolean/combine.md) 不同，分组不会融合几何体——每个对象在组内仍保持独立。

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
![20260318 193104 paste 20260318 193104](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193104-paste-20260318-193104.jpg)

![20260318 193235 paste 20260318 193235](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193235-paste-20260318-193235.jpg)

![20260318 193138 paste 20260318 193138](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193138-paste-20260318-193138.jpg)


## 使用方法

### 将对象分组

1. 选择两个或更多对象（按住 Shift 单击或 Ctrl 单击可多选）
2. 单击工具栏中的 **组** 按钮
3. 这些对象现已成组——它们将作为一个整体一起移动

### 取消对象分组

1. 选择一个组
2. 单击工具栏中的 **取消组合** 按钮
3. ![20260318 193354 paste 20260318 193354](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193354-paste-20260318-193354.jpg)
4. 各个对象将恢复为独立项目

如果单个导入的 STL 文件中包含多个实体，取消组合还会尝试将它们分离开来。

## 组与合并的区别

| 特性 | 组 | 合并 |
|---------|-------|---------|
| 对象保持独立 | 是 | 否 |
| 之后可以取消组合 | 是 | 否（破坏性操作） |
| 融合重叠的几何体 | 否 | 是 |
| 对象可以具有不同颜色 | 是 | 按面保留颜色 |
| 适用场景 | 整理与移动 | 创建单一实体形状 |

## 提示

- 组可以嵌套——你可以将已经位于组中的对象再次分组
- 选择一个组，然后查看设计树，即可查看并选择其中的各个对象
- 分组是非破坏性操作，随时可以通过取消组合还原

## 相关内容

- [合并](../operations/boolean/combine.md) - 将对象合并为单一实体，而非分组
- [选择](selection.md) - 如何选择多个对象以进行分组
- [组件](components.md) - 创建可重复使用的参数化组
