---
title: Düzlem Kesme
articleKey: PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
source_hash: 64a9901bf54b71cd2ecc12c8db189b6e2fcde25e
source_lang: en
---
# Düzlem Kesme

Düzlem Kesme, bir nesneyi belirtilen yükseklikte yatay bir düzlemle dilimler ve yalnızca kesimin altında kalan kısmı korur. Kesim yüzeyi düz bir yüzeyle kapatılır.

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## Nasıl Kullanılır

1. Bir nesne seçin
2. Yeniden Şekillendir menüsünden **Düzlem Kesme** işlemini uygulayın
3. Kesme yüksekliğini ayarlayın

## Parametreler

- **Kesme Yüksekliği** - Nesnenin dilimleneceği Z yüksekliği (varsayılan: 10mm, aralık: 1-200mm)

## İpuçları

- Bir modelin üst kısmını belirli bir yükseklikte düzleştirmek için Düzlem Kesme kullanın
- İçe aktarılan modelleri kırpmak veya düz tabanlar oluşturmak için kullanışlıdır
- Düzlemsel olmayan bir şekille kesmek için bunun yerine başka bir nesneyle [Çıkar](../boolean/subtract.md) işlemini kullanın
- Eğimli bir düzlemle kesmek için önce nesneyi döndürün, Düzlem Kesme uygulayın, ardından geri döndürün

## İlgili

- [Kesiştir](../boolean/intersect.md) - Yalnızca nesnelerin çakıştığı yeri korur
- [Çıkar](../boolean/subtract.md) - Yalnızca bir düzlemle değil, herhangi bir şekille keser
- [İçini Boşalt](hollow-out.md) - İçi boş bir kabuk oluşturur
