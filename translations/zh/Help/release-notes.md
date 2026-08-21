---
title: 发行说明
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8（2026 年 8 月 13 日）
[Windows 下载](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## 新功能

* **编辑子项**
  * 在打印平台上或场景树中双击某个对象，即可进入其内部编辑构成它的部件 —— 无需单独的窗口或选项卡
  * 对于减去之类的操作，你可以编辑源部件，退出后结果会重新生成
  * 场景树顶部的面包屑会显示完整路径；点击某一层级会将你的编辑合并为一个可撤销的步骤，并且每一层级都保留各自的撤销历史
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **统一的布尔工具**
  * 合并、减去、相交以及减去并替换现在合并为一个操作，面板顶部提供一行图标 —— 点击即可切换模式，无需删除后重新应用
  * 同一个操作同时处理 3D 网格和 2D 路径，并在执行繁重的布尔运算时显示进度
  * 使用旧版独立布尔对象保存的设计仍可正常打开
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **真正好用的布尔运算**
  * 布尔运算采用全新的原生引擎，速度更快，并且能在以往会失败的网格上成功
  * 合并会自动修复带孔洞的部件：修复干净的部件加入并集，无法安全合并的部件会保留在旁边并自动命名，无法修复的部件则保留原始几何体
  * 平面切割现在是真正的实体求交，因此结果是水密且可打印的，而不是开放的壳体
  * 针对有问题的导入网格，新增保留内外反转的几何体和修复缠绕方向选项


## 改进

* **2D 路径编辑器**
  * 四种点模式 —— 尖角、对称、对齐和自由 —— 在 2D 编辑器和 3D 视图中均可一键应用
  * 镜像现在是实时对称模式：编辑时会同步沿中心镜像，将一对镜像点拖到轴上会合并为单个点
  * 使用框选拖动选取点、整组移动、吸附到网格，并可按 Esc 取消拖动
  * 平滑可一步在你点出的各点之间拟合曲线
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **视图与导航**
  * 选中平面路径后按 Z，可动画切换到贴合该路径的正上方俯视编辑视图
  * 当显示器支持时，亚像素文本渲染现在会自动启用，也仍可在高级设置中开启或关闭

* **建模**
  * 线性拉伸可以用独立的样式、半径和分段数对底边倒角
  * 仅编辑器可见的对象（3D 曲线、测量工具、说明、图纸）仍会显示，但不会被导出

## 主要错误修复

  * 中途失败的保存可能在报告成功的同时截断被替换的文件。现在保存会先完整完成，再以原子方式替换目标文件 —— 库保存和导出同样受此保护
  * 保存失败时设计会被标记为未保存，因此关闭应用不会悄悄丢弃你的工作
  * 将云端项目保存到磁盘时会沿用旧的选项卡名称，并在重启后丢失该选项卡
  * 修复了 3MF 子模型在加载时被静默丢弃，以及同时加载的多个 3MF 文件相互污染的问题
  * 修复了崩溃、直方图筛选器失效，以及图像部件的副本无法与原件保持同步的问题
  * 修复了删除曲线点时崩溃，以及闭合路径接缝处的点会还原你所选模式的问题
  * 运行中任务上的停止按钮现在可以点击，并且会真正取消任务

---

# MatterCAD 2.2026.5（2026 年 5 月 8 日）
[Windows 下载](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## 新功能

* **重新设计的阵列工具**
  * 单一统一的阵列操作取代了旧的线性阵列、环形阵列和高级阵列
  * **线性**模式：沿某个方向复制，可选旋转和渐进缩放
  * **径向**模式：围绕中心轴复制，可配置半径、扫掠角度以及圆弧或整圆图案
  * **变换**模式：使用手动变换或指定同级对象的变换来逐步复制
  * 线性中的复合旋转模式可自然生成螺旋、扇形和螺旋线
  * 缩放影响偏移选项适用于鹦鹉螺壳和等比数列布局
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **库收藏夹**
  * 为任意库项目加星标，即可将其添加到持久的收藏夹文件夹
  * 在一处快速访问最常用的基本体、生成器和已保存的部件
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## 改进

* **对齐**
  * 堆叠对齐现在是直接的模式按钮，而不是下拉选项
  * 新增更清晰的简单、偏移和堆叠模式，用于对齐边缘、添加精确间隙以及构建有序堆叠
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **文件支持**
  * 在基于图像的操作中新增对 WEBP 图像格式的支持
  * 改进 SVG 文件解析，导入更可靠

* **可靠性**
  * 提升 3MF 文件的加载速度和可靠性
  * 会话之间的选项卡恢复更完善

## 主要错误修复

* **登录与云端库访问**
  * 后端服务器升级曾导致登录失效，现已恢复登录和云端库访问。
  * 当云端访问发现凭据过期或无效时，MatterCAD 现在会提示你重新登录。

* **场景树选择**
  * 修复了从场景树中选择对象时行为不一致的问题。

* **帮助导航**
  * 修复了内置帮助和发行文档中的导航问题。

* **库右键单击**
  * 修复了库树视图中的右键单击行为。

* **图纸**
  * 修复了处理图纸时可能发生的崩溃。

---

# MatterCAD 2.2026.3（2026 年 3 月 12 日）
[Windows 下载](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## 新功能

* **全新 Direct3D 11 渲染引擎**
  * 从 OpenGL 完全迁移到 Direct3D 11，性能大幅提升
  * FXAA 抗锯齿，边缘清晰利落
  * 双重深度剥离，实现正确的顺序无关透明
  * 硬件加速的打印平台阴影
  * 改进的对象轮廓和选择视觉效果
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **对象透明度**
  * 可为场景中任意单个对象设置 alpha/透明度
  * 逐面着色的网格支持 alpha 而不会破坏颜色
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **锁定与隐藏对象**
  * 锁定对象以防止意外选择或编辑
  * 隐藏对象，减少处理特定部件时的视觉干扰
  * 全部显示和全部解锁命令可快速恢复可见性
  * 锁定和隐藏的对象会被正确排除在射线选择之外
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **改进的布尔减去**
  * 多重减去操作明显更可靠、更准确

## 改进

* **文件处理**
  * 项目现在默认保存为 3MF 而非 STL，可保留颜色、材质和设计历史
  * 增强了将文件和文件夹拖放到 3D 视图中的支持

* **工作流**
  * 另存为和移动对话框会记住你上次使用的文件夹位置
  * 表达式字段现在支持 `pi`、`tau`、`e` 和 `count`
  * 在设计编辑上下文中按 Esc 键执行撤销
  * 鼠标离开场景时 3D 控件仍然可见

* **性能与稳定性**
  * 修复了启动崩溃和递归加载问题
  * 修复了光照和 mipmap 渲染错误
  * 改进了库树视图的更新
  * 动态近/远平面计算，缩放行为更佳
  * 升级到 .NET 10

---

# MatterCAD 2.2025.6（2025 年 6 月 20 日）
[Windows 下载](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## 新功能

* **SVG 文件支持**  
  * 完全支持 SVG 文件拖放
  * 从 SVG 图形直接转换为 3D 对象
  * 与现有 CAD 工作流无缝集成

* **高级 OBJ 文件处理**  
  * 支持从 ZIP 压缩包加载材质
  * 增强的 OBJ 文件解析和材质处理
  * 更好地支持带多种材质的复杂 3D 模型

* **增强的选项卡管理系统**
  * 云端库选项卡现在能正确保留 —— 你的工作会停留在离开时的位置
  * 改进的选项卡组织与导航
  * 会话之间自动恢复已打开的选项卡

## 用户体验增强

* **精简的界面**
  * 重新组织了“最近”菜单，访问更快
  * 长时间操作期间提供更好的视觉反馈
  * 改进了应用的启动时间和响应速度

* **可靠性**
  * 修复了 3D 场景交互中的严重崩溃
  * 解决了内存管理问题
  * 提升了各平台上的应用稳定性

---

# MatterCAD 2.21.5（2025 年 2 月 13 日）

[Windows 下载](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# 现有功能

*以下功能构成了 MatterCAD 从 MatterControl 传承而来的基础：*

* 新增中空功能  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* 新增多边形缩减  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* 新增网格修复  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* 除新的手动支撑选项外，还加入了全自动支撑（旧版支撑）作为可选项
* 新增对 gsSlicer 的支持（实验性的新切片引擎）
* 修复了若干错误

## 变更

* 改进了网格取消分组（拆分为多个网格）
    * 丢弃退化面
    * 丢弃极微小的离散特征

## 变更

* 为应用新增搜索栏
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* 改进了设计工具栏
    * 为部分项目添加了分组
    * 添加了双重对齐按钮
    * 添加了全部排列按钮
* 使用方向键在打印平台上微移项目
* 下载文件夹按日期排序

## 变更

* UI 改进
    * 云端库文件夹更新更快
    * 重新打开时恢复 UI
    * 更好的键盘导航支持
* 全新的错误检测与警告系统
    * 可处理更多硬件错误
* 设计工具的改进与优化
    * 全新的扭曲工具
    * 改进的曲线工具
    * 改进的对齐


## 变更

* 改进了展平
* 改进了撤销支持
* 改进了设计历史

## 变更
* 版本编号：改用（版本）.（年）.（月）形式的版本号。更易读，信息更丰富。
* 全新的先进减去、合并和交集（仅限 Windows）
* 现在启动时会提供“功能导览”，帮助新用户快速上手

## 变更
* 设计工具 —— 使用完整的建模基本体进行 3D 建模的能力
* 使用基本体创建你自己的自定义支撑
* 设计应用 —— 设计应用：复杂且可定制的设计
* 64 位处理
