---
title: 挖空
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cc2c5555723ecfe77475fef9e7a2090cdf760204
source_lang: en
---
# 挖空

挖空通过将表面向内偏移，从实体对象创建出中空的壳体。结果是原始形状的薄壁版本。

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## 使用方法

1. 选择一个实体对象
2. 从重塑菜单中应用 **挖空** 操作
3. 设置所需的壁厚

## 参数

- **距离** - 以毫米为单位的壁厚（默认值：2mm）。这是生成壳体的厚度。
- **单元数** - 挖空算法的分辨率（默认值：64）。数值越高，内部表面越光滑，但计算时间也越长。

## 提示

- 挖空适用于创建外壳、容器、花瓶和轻量化零件
- 对于大多数 3D 打印零件，1-2mm 的壁厚较为典型
- 如果内部表面显得粗糙或呈块状，请增大单元数
- 挖空会产生开放的底部——如果需要封闭的底面，可与 [立方体](../../primitives/cube.md) 结合使用
- 对于复杂形状，计算可能需要几秒钟

## 相关内容

- [平面切割](plane-cut.md) - 在指定高度剪切对象
- [减去](../boolean/subtract.md) - 手动切除材料
