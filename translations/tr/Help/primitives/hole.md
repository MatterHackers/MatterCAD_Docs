---
title: Delik
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# Delik

Boole çıkarma aracı olarak davranacak şekilde önceden yapılandırılmış küp biçiminde bir nesne. [Birleştir](../operations/boolean/combine.md) işlemini kullandığınızda, Delik nesneleri diğer şekillere eklenmek yerine otomatik olarak onlardan çıkarılır.

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## Nasıl Çalışır

Delik ilkeli bir [Küp](cube.md) gibi çalışır, ancak çıktı türü "Delik" olarak ayarlanmıştır. İçinde bir Delik bulunan nesneleri birleştirdiğinizde, Delik'in hacmi sonuçtan kaldırılır.

## Parametreler

[Küp](cube.md) ile aynıdır:

- **Genişlik** - X ekseni boyunca boyut
- **Derinlik** - Y ekseni boyunca boyut
- **Yükseklik** - Z ekseni boyunca boyut

## İpuçları

- Deliği, kesmek istediğiniz nesneyle örtüşecek şekilde konumlandırın
- Baştan sona geçen bir delik istiyorsanız, Deliği hedef nesnenin tamamen içinden geçecek kadar uzatın
- Aynı etkiyi elde etmek için normal şekilleri [Çıkar](../operations/boolean/subtract.md) ile de kullanabilirsiniz, ancak Delikler [Birleştir](../operations/boolean/combine.md) ile otomatik olarak çalıştıkları için kullanışlıdır
- Yuvarlak delikler için bunun yerine Çıkar ile bir [Silindir](cylinder.md) kullanın

## İlgili

- [Küp](cube.md) - Delik davranışı olmayan aynı şekil
- [Birleştir](../operations/boolean/combine.md) - Şekilleri birleştirir ve Delikleri otomatik olarak çıkarır
- [Çıkar](../operations/boolean/subtract.md) - Herhangi bir şekli bir diğerinden elle çıkarın
