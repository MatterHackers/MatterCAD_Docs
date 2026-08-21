---
title: Küp
articleKey: CubeObject3D
parent: "Primitives"
nav_order: 4
source_hash: a376a9c78d88d995f3c6ce21dd5098672d6c1dfb
source_lang: en
---
# Küp

Ayarlanabilir genişlik, derinlik, yükseklik ve isteğe bağlı yuvarlatılmış kenarlara sahip dikdörtgen bir kutu şekli. Küp, tasarımlar oluşturmak için en sık kullanılan ilkel şekillerden biridir.

<!--  Screenshot of a Cube primitive on the workspace -->
![20260318 183230 paste 20260318 183230](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183230-paste-20260318-183230.jpg)


## Parametreler

- **Genişlik** - X ekseni boyunca boyut (varsayılan: 20mm)
- **Derinlik** - Y ekseni boyunca boyut (varsayılan: 20mm)
- **Yükseklik** - Z ekseni boyunca boyut (varsayılan: 20mm)
- **Yuvarlat** - Yuvarlatılmış kenarları etkinleştirir
- **Yarıçap** - Yuvarlatmanın boyutu (Yuvarlat etkinleştirildiğinde görünür)
- **Yuvarlatma Segmentleri** - Yuvarlatmanın pürüzsüzlüğü, daha fazla segment = daha yumuşak eğriler (Yuvarlat etkinleştirildiğinde görünür)

## İpuçları

- Kutular, plakalar, braketler ve muhafazalar için başlangıç noktası olarak bir Küp kullanın
- Pürüzsüz, profesyonel görünümlü kenarlar için Yuvarlat seçeneğini etkinleştirin
- Yarıçap, en küçük boyutun yarısını aşamaz
- Dikdörtgen kesikler ve yuvalar oluşturmak için bir Küp'ü [Çıkar](../operations/boolean/subtract.md) ile birleştirin

## İlgili

- [Silindir](cylinder.md) - Yuvarlak sütun şekli
- [Piramit](pyramid.md) - Sivrilen dört yüzlü şekil
- [Delik](hole.md) - Boole çıkarma işlemi için önceden yapılandırılmış bir küp
