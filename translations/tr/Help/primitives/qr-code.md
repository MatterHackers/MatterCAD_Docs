---
title: QR Kodu
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
source_hash: 5b941a39b8430a9536401e4af230c06a42635205
source_lang: en
---
# QR Kodu

QR kodlarını 3B nesne olarak oluşturun. Metin, URL veya WiFi kimlik bilgilerini taranabilir bir 3B QR koduna kodlayabilirsiniz.

<!--  Screenshot of a 3D QR Code object on the workspace -->
![20260318 184540 paste 20260318 184540](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184540-paste-20260318-184540.jpg)


## Nasıl Kullanılır

1. İlkeller panelinden bir **QR Kodu** ekleyin
2. Çıktı türünü seçin (Metin veya WiFi)
3. İçeriğinizi girin
4. QR kodu, tasarımınıza yerleştirebileceğiniz bir 3B nesne olarak oluşturulur

## Parametreler

### Metin Modu

- **Metin** - Kodlanacak metin veya URL (varsayılan: "https://matterhackers.com")

### WiFi Modu

- **SSID** - WiFi ağının adı
- **Parola** - WiFi parolası
- **Güvenlik** - Güvenlik türü (WEP, WPA veya Yok)

## İpuçları

- QR kodunu bir yüzeye kazımak için [Çıkar](../operations/boolean/subtract.md) işlemini kullanın ya da kodu bir [Küp](cube.md) tabanın üzerine yerleştirin
- Yazdırmadan önce QR kodunuzun bir telefonla doğru şekilde tarandığını test edin
- WiFi QR kodları, insanların kodu tarayarak ağınıza bağlanmasını sağlar
- QR kodunun yazdırıldığında taranabilecek kadar büyük olduğundan emin olun -- en az 20-25 mm genişliğinde

## İlgili

- [Metin](text.md) - Standart 3B metin
- [Görüntü Nesnesi](image-object.md) - Görüntüleri 3B'ye dönüştürme
