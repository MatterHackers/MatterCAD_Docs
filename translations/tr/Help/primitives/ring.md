---
title: Halka
articleKey: RingObject3D
parent: "Primitives"
nav_order: 13
source_hash: fd16c400f3d8c8af13416ab57ddd8407e761d93a
source_lang: en
---
# Halka

Bağımsız iç ve dış çaplara ve belirli bir yüksekliğe sahip içi boş bir silindir (boru). Boru veya tüp şekli olarak da bilinir.

<!--  Screenshot of a Ring primitive on the workspace -->
![20260318 183848 paste 20260318 183848](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183848-paste-20260318-183848.jpg)


## Parametreler

- **Dış Çap** - Halkanın dış genişliği (varsayılan: 20mm)
- **İç Çap** - İçi boş merkezin çapı (varsayılan: 15mm)
- **Yükseklik** - Halkanın ne kadar yüksek olduğu (varsayılan: 5mm)
- **Kenarlar** - Çevre boyunca yer alan segment sayısı (varsayılan: 40)

### Gelişmiş Parametreler

Ek denetimler için **Gelişmiş** modu etkinleştirin:

- **Başlangıç Açısı** - Halkanın başladığı açı (varsayılan: 0)
- **Bitiş Açısı** - Halkanın bittiği açı (varsayılan: 360). Kısmi bir halka için 360'tan küçük bir değer girin
- **Yuvarlat** - Kenarlara yuvarlatma ekler (Yok, Yukarı veya Aşağı)
- **Yön** - İç veya dış kenara doğru yuvarlatma yapar (Yuvarlat etkinleştirildiğinde görünür)
- **Yuvarlatma Segmentleri** - Yuvarlatmanın pürüzsüzlüğü (Yuvarlat etkinleştirildiğinde görünür)

## İpuçları

- Duvar kalınlığı (Dış Çap - İç Çap) / 2 değerine eşittir
- Bunu pullar, ara parçalar, burçlar ve boru benzeri özellikler için kullanın
- Borular için yüksekliği büyük, düz pullar için küçük ayarlayın
- C klipsleri gibi kısmi halka şekilleri için Başlangıç Açısı ve Bitiş Açısı değerlerini kullanın

## İlgili

- [Torus](torus.md) - Yuvarlak kesitli, simit biçiminde bir halka
- [Silindir](cylinder.md) - Katı, yuvarlak bir sütun (içi boş merkez yok)
