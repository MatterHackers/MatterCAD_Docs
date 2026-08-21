---
title: Dişliler
articleKey: GearObject3D
parent: "Mechanical Parts"
nav_order: 2
source_hash: 23098f94da8cd032e0617fbf346621504446347f
source_lang: en
---
# Dişliler

Tamamen yapılandırılabilir diş geometrisine sahip 3B dişliler oluşturun. MatterCAD, aynı modül ve basınç açısına sahip diğer dişlilerle doğru şekilde kavraşan uygun evolvent dişli profilleri üretir.

<!-- AUTO_IMAGE: type=from_thumbnail item=gear file=mechanical_gears -->
![mechanical_gears](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_gears.png)

## Nasıl Kullanılır

1. Mekanik araçlarından veya İlkeller panelinden bir **Dişli** ekleyin
2. Diş sayısını ve diğer parametreleri ayarlayın
3. Dişli profili otomatik olarak oluşturulur

## Parametreler

### Özellikler

- **Dişli Tipi** - Dış dişli veya Kremayer (dişli düz çubuk)
- **Yükseklik** - Dişlinin kalınlığı (ekstrüzyon yüksekliği)
- **Diş Sayısı** - Dişli çevresindeki diş sayısı (varsayılan: 30, aralık: 4-60)
- **Dairesel Adım** - Adım dairesi boyunca dişler arasındaki yay mesafesi (aralık: 3-30). Bu, genel boyutu belirler.
- **Orta Delik Çapı** - Orta mil deliğinin çapı (varsayılan: 4mm, delik olmaması için 0 girin). Yalnızca dış dişliler için.
- **Dış Kenar Genişliği** - İç dişlerin dışındaki kenarın genişliği
- **İç Dişli Diş Sayısı** - Kavraşan iç dişlinin diş sayısı

### Gelişmiş

- **Basınç Açısı** - Diş temas yüzeyinin açısı (yaygın değerler: 14.5, 20 veya 25 derece). Kavraşan tüm dişliler aynı basınç açısını kullanmalıdır.
- **Boşluk** - Diş ucu ile kavraşan diş boşluğunun tabanı arasındaki minimum aralık
- **Boşluk** - Sıkışmayı önlemek için kavraşan dişli dişleri arasındaki minimum aralık

### Dişli Verileri (Salt Okunur)

- **Adım Yarıçapı** - Dişlilerin birbiriyle kavraştığı yarıçap
- **Dış Çap** - Diş uçlarına kadar olan toplam çap

## İpuçları

- İki dişli, aynı Dairesel Adım ve Basınç Açısı değerlerine sahip olduğunda doğru şekilde kavraşır
- Kavraşan dişlileri doğru aralıklarla yerleştirmek için Adım Yarıçapı değerlerini kullanın -- dişli merkezleri arasındaki mesafe, adım yarıçaplarının toplamına eşit olmalıdır
- 3B baskı toleranslarını hesaba katmak için 3B basılan dişlilere Boşluk ekleyin
- 2B dişli profilleri için (Ekstrüzyon ile kullanılmak üzere) bkz. [Gear 2D](gear-2d.md)

## İlgili

- [Gear 2D](gear-2d.md) - Yol işlemleri için 2B dişli yolu
- [Dişler](threads.md) - Dişli özellikler oluşturun
