---
title: QRコード
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
source_hash: 5b941a39b8430a9536401e4af230c06a42635205
source_lang: en
---
# QRコード

QRコードを3Dオブジェクトとして生成します。テキスト、URL、WiFiの認証情報をスキャン可能な3D QRコードにエンコードできます。

<!--  Screenshot of a 3D QR Code object on the workspace -->
![20260318 184540 paste 20260318 184540](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184540-paste-20260318-184540.jpg)


## 使い方

1. プリミティブパネルから **QRコード** を追加します
2. 出力タイプ（テキストまたはWiFi）を選択します
3. 内容を入力します
4. QRコードが3Dオブジェクトとして生成され、デザイン上に配置できます

## パラメータ

### テキストモード

- **テキスト** - エンコードするテキストまたはURL（デフォルト: 「https://matterhackers.com」）

### WiFiモード

- **SSID** - WiFiネットワークの名前
- **パスワード** - WiFiのパスワード
- **セキュリティ** - セキュリティの種類（WEP、WPA、またはなし）

## ヒント

- [減算](../operations/boolean/subtract.md) を使ってQRコードを面に彫り込んだり、[立方体](cube.md) のベースの上に配置したりできます
- 印刷する前に、QRコードがスマートフォンで正しくスキャンできるかテストしてください
- WiFiのQRコードを使うと、コードをスキャンするだけでネットワークに接続できます
- 印刷したときにスキャンできるよう、QRコードは十分な大きさ（少なくとも一辺20〜25mm）にしてください

## 関連項目

- [テキスト](text.md) - 標準の3Dテキスト
- [画像オブジェクト](image-object.md) - 画像を3Dに変換
