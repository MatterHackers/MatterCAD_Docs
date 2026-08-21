---
title: 常见问题解答
nav_order: 101
source_hash: 929ea9e89d3f5008996615341418ba715d3f6075
source_lang: en
---
# 为什么我的对象比例不正确？
- STL 文件不存储单位信息。MatterCAD 默认 STL 的尺寸以毫米为单位，而大多数 CAD 软件都以其原生单位（通常是英寸）导出。这会在导入设计时造成比例不一致。

- 最好的解决办法是将您的设计软件配置为以毫米为单位导出 STL 文件。例如，在 SolidWorks 中，可在另存为对话框中使用选项按钮来设置 STL 导出参数。

- 或者，您也可以在 MatterCAD 中重新缩放零件。在 3D 视图中，进入编辑模式，然后从右侧工具栏中选择缩放。使用下拉菜单选择常用的换算系数，或在各轴的输入框中输入具体尺寸。

# 如何清除应用程序数据？

- 如果重新安装仍无法解决问题，您可能需要删除 MatterCAD 存储的数据。这些数据在卸载后仍会保留。若要完全恢复为默认设置，请移除应用程序文件夹。您还可以临时重命名 SQLite 数据库文件（MatterCAD.db），以测试是否是设置导致了问题。
![20260318 194137 paste 20260318 194137](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194137-paste-20260318-194137.jpg)

![20260318 194200 paste 20260318 194200](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194200-paste-20260318-194200.jpg)

![20260318 194218 paste 20260318 194218](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194218-paste-20260318-194218.jpg)


- Windows
  - 用户库和设置存储在 C:\Users\{user}\AppData\Local\MatterCAD。
