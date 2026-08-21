---
title: Döndür
articleKey: RotateObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 9bdc210c5c375fe3179050e8a8916d895455ce5f
source_lang: en
---
# Döndür

Döndür, bir nesneyi belirtilen bir eksen etrafında verilen bir açı kadar çevirir. Herhangi bir eksen yönünde döndürebilir ve dönme merkezi noktasını seçebilirsiniz.

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## Nasıl Kullanılır

1. Bir nesne seçin
2. Dönüştür menüsünden **Döndür** işlemini uygulayın
3. Özellikler panelinde dönme açısını ve eksenini ayarlayın

Ayrıca seçili bir nesnenin köşesindeki döndürme denetimlerine tıklayarak nesneleri doğrudan görünüm alanında da döndürebilirsiniz. Farenizi açı göstergelerinin üzerine getirdiğinizde 45 derecelik artışlara yaslanır.

## Parametreler

- **Açı** - Derece cinsinden dönme açısı (aralık: 3-360). [İfadeleri](../../workspace/expressions.md) destekler.
- **Şuna Göre Döndür** - Dönme eksenini ve başlangıç noktasını tanımlar. X, Y veya Z ekseni etrafında döndürebilir ya da özel bir yön belirtebilirsiniz.

## İpuçları

- Dönme, varsayılan olarak nesnenin sınırlayıcı kutusunun merkezine göre yapılır
- 90 derecelik dönmelerde yaslanma göstergeleri tam değerleri elde etmeyi kolaylaştırır
- 45'in katı olmayan hassas bir açıya ihtiyacınız olduğunda (görünüm alanı denetimleri yerine) Döndür işlemini kullanın
- İşlemi uyguladıktan sonra Şuna Göre Döndür özelliğini düzenleyerek dönme eksenini değiştirebilirsiniz

## İlgili

- [Öteleme](translate.md) - Bir nesneyi belirli bir mesafe kadar taşıyın
- [Ölçekle](scale.md) - Bir nesneyi yeniden boyutlandırın
- [Aynala](mirror.md) - Aynalanmış bir yansıma oluşturun
