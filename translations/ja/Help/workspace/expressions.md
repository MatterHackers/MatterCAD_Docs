---
title: 数式
parent: "Workspace"
nav_order: 2
source_hash: 79a2f2c42d81f7fca56a87ad89f69e4303ed0ae5
source_lang: en
---
# 数式

MatterCAD の多くのパラメータでは、単なる数値の代わりに数式を入力できます。これにより、ある値を変更すると関連する寸法が自動的に更新されるパラメトリック設計が可能になります。

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)


## 使い方

パラメータ入力欄に単なる数値を入力する代わりに、数式を入力できます。例:

- `20 + 5` は 25 と評価されます
- `pi * 10` は 31.416 と評価されます
- `width * 2` は "width" という名前の別のパラメータを参照します

## 使用できる定数

- **pi** - 3.14159...(円周と直径の比)
- **tau** - 6.28318...(2 * pi、ラジアンでの一回転)

## サポートされる演算

- 加算: `+`
- 減算: `-`
- 乗算: `*`
- 除算: `/`
- 括弧: グループ化のための `(` と `)`

## ヒント

- 数式は、コード内で `DoubleOrExpression`、`IntOrExpression`、`StringOrExpression` を示すすべての入力欄でサポートされています。実際には、デザインツールのほとんどの数値入力欄で使用できます
- 数式を使ってパラメータ同士の関係を作成できます。たとえば、穴の直径を `outer_diameter - 4` に設定すれば、壁の厚さは常に 2mm になります
- 参照している値が変更されると、数式は自動的に更新されます
- 複数のオブジェクトで同じ名前付きの値や数式を共有する場合は、[変数シート](variable-sheet.md) を使用してください
- [配列](../operations/array/index.md) 操作で数式を使用すると、パラメトリックなパターンを作成できます

## 関連項目

- [コンポーネント](components.md) - 再利用可能なパラメータ化された設計を作成します
- [変数シート](variable-sheet.md) - 設計で共有する値や数式を保存します
- [オブジェクトの編集](../getting-started/editing-objects.md) - オブジェクトのパラメータの扱い方
