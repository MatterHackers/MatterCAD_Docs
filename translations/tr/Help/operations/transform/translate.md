---
title: Öteleme
articleKey: TranslateObject3D
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c05550dee2397bdb58dc2e247a068a544233a71d
source_lang: en
---
# Öteleme

Öteleme, bir nesneyi X, Y ve/veya Z eksenleri boyunca belirli bir mesafe kadar hareket ettirir. Bir nesneyi fareyle sürüklemenin aksine, Öteleme kesin ofset değerleri girmenize olanak tanır.

<!--  Screenshot showing the Translate operation properties with X, Y, Z offset fields -->
![20260506 160828 paste 20260506 160828](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160828-paste-20260506-160828.jpg)


## Nasıl Kullanılır

1. Bir nesne seçin
2. Dönüştür menüsünden **Öteleme** işlemini uygulayın
3. Özellikler panelinde X, Y ve Z için istediğiniz ofset değerlerini girin

## Parametreler

- **X, Y, Z** (Öteleme) - Nesnenin her eksen boyunca hareket edeceği mesafe, milimetre cinsinden. Hesaplanan değerler için [ifadeleri](../../workspace/expressions.md) destekler.

## İpuçları

- Daha sonra ayarlayabileceğiniz hassas ve tekrarlanabilir bir konumlandırmaya ihtiyaç duyduğunuzda Öteleme'yi kullanın
- Öteleme değerleri nesnenin mevcut konumuna görelidir -- X için 10 girmek, nesneyi bulunduğu yerden 10 mm sağa taşır
- Hızlı yeniden konumlandırma için nesneleri doğrudan görüntü alanında da sürükleyebilirsiniz. Bkz. [Nesneleri Düzenleme](../../getting-started/editing-objects.md)

## İlgili

- [Döndür](rotate.md) - Bir nesneyi belirli bir açıyla döndürün
- [Ölçekle](scale.md) - Bir nesneyi hassas şekilde yeniden boyutlandırın
- [Hizala](../placement/align.md) - Nesneleri birbirine göre konumlandırın
