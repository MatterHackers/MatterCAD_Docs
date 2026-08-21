---
title: Aynala
articleKey: MirrorObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 8a8de28f5e429177d4b0092d0756387eb6b83a70
source_lang: en
---
# Aynala

Aynala, bir nesnenin üç ana eksenden biri boyunca yansıtılmış bir kopyasını oluşturur. Sonuç, özgün şeklin aynalanmış bir sürümüdür.

<!--  Before and after showing an object mirrored across the X axis -->
![20260506 160651 paste 20260506 160651](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160651-paste-20260506-160651.jpg)


## Nasıl Kullanılır

1. Bir nesne seçin
2. Dönüştür menüsünden **Aynala** işlemini uygulayın
3. Hangi eksen boyunca aynalanacağını seçin

## Parametreler

- **Aynalama Açık** - Aynalamanın yapılacağı eksen:
  - **X Ekseni** - Nesneyi soldan sağa çevirir
  - **Y Ekseni** - Nesneyi önden arkaya çevirir
  - **Z Ekseni** - Nesneyi yukarıdan aşağıya çevirir

## İpuçları

- Aynalama, nesnenin sınırlayıcı kutusuna göre ortalanır; bu nedenle aynalanmış sonuç özgün nesneyle aynı alanı kaplar
- Doğru görüntülemenin korunması için yüzey normalleri aynalama sonrasında otomatik olarak düzeltilir
- Simetrik tasarımlar oluşturmak için Aynala işlemini kullanın -- bir yarısını modelleyin, ardından aynalayıp özgün nesneyle [Birleştir](../boolean/combine.md) işlemini uygulayın
- Aynala tahribatsızdır: aynalama eksenini istediğiniz zaman değiştirebilirsiniz

## İlgili

- [Döndür](rotate.md) - Aynalamak yerine bir nesneyi döndürün
- [Ölçekle](scale.md) - Bir nesneyi yeniden boyutlandırın
- [Birleştir](../boolean/combine.md) - Özgün nesneyi ve aynalanmış kopyayı tek bir nesnede birleştirin
