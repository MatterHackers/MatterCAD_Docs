---
title: 新增功能
nav_order: 105
source_hash: 172343b8320204d2b0ec52419324f0efd2be95a1
source_lang: en
---
# MatterCAD 2.2026.8

# 新增功能

* **编辑子项**
  * 双击任意对象即可进入其内部，直接在打印平台上编辑构成它的各个部件
  * 面包屑导航会显示当前所处层级——点击任意层级即可将编辑结果折叠回去
  * ![MatterCAD 2.2026.8](https://www.matterhackers.com/r/qgG4VA)

* **统一的布尔工具**
  * 合并、减去、相交以及减去并替换现已整合为一项操作——只需点击即可切换模式，无需删除后重新应用
  <!-- Boolean property panel showing the four-icon operation row with Subtract selected. ~500x350px -->
  * ![One Boolean Tool](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)

* **真正好用的布尔运算**
  * 全新引擎速度更快，并能成功处理以往会失败的网格
  * 合并会自动修复带孔洞的部件，并标出无法合并的对象；平面切割现在可生成水密、可打印的实体

* **更出色的二维路径编辑**
  * 点模式、实时镜像对称、网格吸附、框选，以及按 Esc 取消拖动
  <!-- Turn on Mirror, drag a point and watch its partner follow, then drag it onto the axis to merge. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

## 改进

* **导航** — 选中二维路径后按 Z 键可进入自顶向下的编辑视图
* **更清晰的文本** — 当显示器支持时，将自动启用亚像素文本渲染
* **建模** — 线性拉伸可为底部边缘添加倒角，并可单独设置样式、半径和分段数

## 主要错误修复

* **保存可靠性** — 保存失败不会再损坏被替换的文件，并且会提示你保存失败
* **云端库** — 将云端项目保存到磁盘时会保留其选项卡名称，且该选项卡在重启后依然存在
* **文件加载** — 修复了 3MF 部件在加载时被静默丢弃的问题
* **路径编辑** — 修复了删除曲线点时崩溃的问题，以及接缝点会还原所选模式的问题
* **后台任务** — 运行中任务上的停止按钮现在可以点击，并能真正取消任务

## 你可以在[此处](release-notes.md)查看完整的版本说明。
