---
title: Ölçekle
articleKey: ScaleObject3D_3
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b3b5419c3db29550b2544bb6aca91ca3ce6fa715
source_lang: en
---
# Ölçekle

Ölçekle, bir nesneyi boyutlar, oranlar ve birim dönüşümü üzerinde hassas denetimle yeniden boyutlandırır. Nesneyi eşit biçimde ölçekleyebilir, belirli eksenleri birbirine kilitleyebilir veya her ekseni bağımsız olarak yeniden boyutlandırabilirsiniz.

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## Nasıl Kullanılır

1. Bir nesne seçin
2. Dönüştür menüsünden **Ölçekle** işlemini uygulayın
3. Ölçekleme yönteminizi seçin ve istediğiniz değerleri girin

Ayrıca seçili bir nesnenin ölçek köşe denetimlerini tıklayıp sürükleyerek nesneleri görünüm alanında da ölçekleyebilirsiniz.

## Parametreler

### Ölçek Türü

Hazır bir ayar ya da özel ölçekleme seçin:

- **Özel** - Kendi boyutlarınızı veya yüzdelerinizi girin
- **İnçten mm'ye** - 25.4 ile çarpar (emperyal birimi metriğe dönüştürür)
- **mm'den inç'e** - 0.0393 ile çarpar (metrik birimi emperyale dönüştürür)
- **mm'den cm'ye** - 0.1 ile çarpar
- **cm'den mm'ye** - 10 ile çarpar

### Ölçekleme Yöntemi (Özel modu)

- **Doğrudan** - İstediğiniz Genişlik, Derinlik ve Yükseklik değerlerini milimetre cinsinden girin
- **Yüzde** - Genişlik, Derinlik ve Yükseklik değerlerini özgün boyutun yüzdesi olarak girin

### Oranı Kilitle

- **Yok (Serbest Ölçekle)** - Her eksen bağımsız olarak ölçeklenir
- **X ve Y** - Genişlik ile Derinlik birbirine kilitlenir; Yükseklik bağımsız olarak ölçeklenir
- **X, Y ve Z** - Üç eksenin tümü eşit biçimde birlikte ölçeklenir

### Boyutlar

- **Genişlik** - X ekseni boyunca boyut
- **Derinlik** - Y ekseni boyunca boyut
- **Yükseklik** - Z ekseni boyunca boyut

## İpuçları

- İnç cinsinden tasarlanmış ve çok küçük görünen bir STL dosyasını içe aktardıysanız "İnçten mm'ye" seçeneğini kullanın
- Eşit ölçekleme için Oranı Kilitle seçeneğini X, Y ve Z olarak ayarlayın -- herhangi bir boyutu değiştirmek hepsini günceller
- Nesnenin taban konumu ölçekleme sırasında korunur, böylece çalışma alanı yüzeyinde kalır
- Hassas boyutlandırma için tam değerler yazabilir veya hızlı ayarlamalar için kaydırıcıları kullanabilirsiniz

## İlgili

- [Öteleme](translate.md) - Bir nesneyi taşıyın
- [Döndür](rotate.md) - Bir nesneyi döndürün
- [Sınırlara Sığdır](../placement/fit-to-bounds.md) - Belirli bir boyuta sığacak şekilde ölçekleyin
