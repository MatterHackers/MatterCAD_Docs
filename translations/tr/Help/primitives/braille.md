---
title: Braille
articleKey: BrailleObject3D
parent: "Primitives"
nav_order: 2
source_hash: d1d9d4aeb9b87efbe32045f2a96cfea49048f95f
source_lang: en
---
# Braille

Standart İngilizce metinden 3D yazdırılabilir Braille metni oluşturun. Braille aracı hem Derece 1 (harf harf) hem de Derece 2 (kısaltmalı) Braille kodlamasını destekler.

<!-- Screenshot of a Braille object showing raised dots on the workspace -->
![20260318 182800 paste 20260318 182800](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-182800-paste-20260318-182800.jpg)


## Nasıl Kullanılır

1. İlkeller panelinden bir **Braille** ilkeli ekleyin
2. Metninizi **Kodlanacak Metin** alanına yazın
3. Araç, metni otomatik olarak doğru Braille nokta desenine dönüştürür

## Parametreler

- **Kodlanacak Metin** - Braille'e dönüştürülecek İngilizce metin
- **Ölçekle** - Braille çıktısının genel boyutunu ayarlar
- **Yükseklik** - Kabartma Braille noktalarının yüksekliği

## İpuçları

- Derece 2 Braille, yaygın sözcükler ve harf kombinasyonları için kısaltmalar kullanır; bu da onu daha kompakt hale getirir
- Çıktının okunabilir olmasını sağlamak için standart Braille hücre ölçüleri kullanılır
- Eksiksiz bir Braille etiketi veya tabelası oluşturmak için düz bir [Küp](cube.md) tabanla birleştirin
- Tümleşik tabanlı Braille kartları için bkz. [Braille Kartı](braille-card.md)

## İlgili

- [Braille Kartı](braille-card.md) - Tümleşik kart tabanlı Braille
- [Metin](text.md) - Standart 3D metin
