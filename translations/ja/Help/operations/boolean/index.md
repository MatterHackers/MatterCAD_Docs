---
title: ブーリアン演算
articleKey: BooleanObject3D
parent: "Operations"
has_children: true
nav_order: 2
source_hash: 06a4b60560c11fc32af4d90dd3d70e3f21c96701
source_lang: en
---
# ブーリアン演算
<!-- AUTO_IMAGE: type=toolbar_icons group=Merge -->
![Merge toolbar icons](https://matterhackers.github.io/MatterCAD_Docs/assets/toolbar-icons-Merge.png)

ブーリアン演算を使うと、単純な形状を組み合わせて複雑な形状を作成できます。2つ以上のオブジェクトを選択してブーリアン演算を適用すると、それらを結合したり、切り取ったり、重なり部分を求めたりできます。

4つの演算はすべて1つのブーリアンオブジェクトで実行されます。以下のツールバーボタンは、開始時にどの操作を使うかをあらかじめ選択するだけのもので、後から**プロパティ**パネル上部の**操作**アイコン列で変更できます。

|結合|減算|交差|減算して置換|
| :--- | :--- | :--- | :--- |
|<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)|<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)|<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)|<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)|

## 操作

- [結合](combine.md) - 複数のオブジェクトを1つのソリッド形状に結合します
- [減算](subtract.md) - 一方の形状を他方から切り取ります
- [交差](intersect.md) - オブジェクトが重なっている体積のみを残します
- [減算して置換](subtract-and-replace.md) - 一方の形状を他方から減算し、切り取った領域を置き換えます
