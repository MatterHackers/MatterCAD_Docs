---
title: Metin
articleKey: TextObject3D_2
parent: "Primitives"
nav_order: 16
source_hash: 526f3190c7b2150243499b5874ac455d74810bb2
source_lang: en
---
# Metin

Özelleştirilebilir içerik, yazı tipi, boyut ve yükseklik ile 3B kabartma metin oluşturun. Metin nesneleri; etiketler, tabelalar, isimlikler ve dekoratif harfler için idealdir.

<!--  Screenshot of a 3D Text object on the workspace showing extruded letters -->
![20260318 184207 paste 20260318 184207](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184207-paste-20260318-184207.jpg)


## Nasıl Kullanılır

1. İlkeller panelinden bir **Metin** ilkeli ekleyin
2. Özellikler panelindeki **Ad** alanına metninizi yazın
3. Yazı tipini, boyutu ve kabartma yüksekliğini gerektiği gibi ayarlayın

## Parametreler

- **Ad** - Görüntülenecek metin içeriği
- **Nokta Boyutu** - Yazı tipi boyutu. Bu değer standart baskı ölçülendirmesine göre doğrudur -- MatterCAD'deki 12 punto bir boyut, 2B bir yazıcıdaki 12 puntoluk yazıyla eşleşir
- **Yükseklik** - Kabartma yüksekliği (metnin yüzeyden ne kadar yukarı çıktığı)
- **Yazı Tipi** - Kullanılabilir sistem yazı tipleri arasından seçim yapın

## İpuçları

- Metni yüzeyden yükseltmek yerine yüzeye kazımak için [Çıkar](../operations/boolean/subtract.md) işlemini kullanın
- Çok küçük metinlerde daha iyi ayrıntı için Nokta Boyutu değerini artırın ve ardından nesnenin tamamını [Ölçekle](../operations/transform/scale.md) ile küçültün
- Metindeki her harf, birlikte kabartılan ayrı bir yoldur

## İlgili

- [Braille](braille.md) - 3B yazdırılabilir Braille metni oluşturun
- [QR Kodu](qr-code.md) - 3B nesne olarak bir QR kodu oluşturun
- [Görüntü Nesnesi](image-object.md) - Görüntüleri 3B'ye dönüştürün
