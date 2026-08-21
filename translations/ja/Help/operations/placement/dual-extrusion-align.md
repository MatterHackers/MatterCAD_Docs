---
title: デュアル押し出しの位置合わせ
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: f1fcae36dcaa4216f3872cb9a8b6317311330c60
source_lang: en
---
# デュアル押し出しの位置合わせ

![20260506 160531 paste 20260506 160531](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160531-paste-20260506-160531.jpg)


デュアル押し出しの位置合わせは、選択した2つ以上のオブジェクトの中心が共有のモデリング原点に揃うように配置し直します。この原点は、デュアル押し出し印刷のためにオブジェクト同士が互いに対して占めるよう設計された位置です。

<!--  Screenshot showing two parts before and after Dual Extrusion Align -->
|![20260506 160417 paste 20260506 160417](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160417-paste-20260506-160417.jpg)
|![20260506 160501 paste 20260506 160501](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160501-paste-20260506-160501.jpg)
|

## 使い方

1. 2つ以上のオブジェクトを選択します
2. 配置メニューから **デュアル押し出しの位置合わせ** を適用します

## 使用する場面

この操作は、デュアル押し出しプリンターで一緒に印刷するよう設計されたパーツが、相対位置から動かされてしまった場合に使用します。デュアル押し出しの位置合わせは、それらを本来意図された共有座標空間に復元します。

## 関連項目

- [整列](align.md) - 任意の軸に沿ってオブジェクトを互いに対して配置します
- [境界にフィット](fit-to-bounds.md) - 矩形の境界内に収まるようにオブジェクトをスケールします
