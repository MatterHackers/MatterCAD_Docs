---
title: Onar
articleKey: RepairObject3D_2
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: f637470dee4f722b595f07d2da9dcdaac5e8da72
source_lang: en
---
# Onar

Onar; manifold olmayan kenarlar, delikler, tutarsız yüzey yönü ve neredeyse çakışık köşe noktaları dahil olmak üzere ağ geometrisindeki yaygın sorunları giderir. Bu, hata içerebilen içe aktarılmış STL ve OBJ dosyaları için özellikle kullanışlıdır.

![20260324 080517 paste 20260324 080517](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080517-paste-20260324-080517.jpg)


## Nasıl Kullanılır

1. Ağ sorunları olan bir nesne seçin
2. Ağ menüsünden **Onar** işlemini uygulayın
3. Nelerin düzeltildiğini görmek için önce/sonra istatistiklerini inceleyin

## İstatistikler (Salt Okunur)

- **Başlangıç Köşe Noktaları / Son Köşeler** - Onarımdan önceki ve sonraki köşe sayısı
- **Başlangıç Yüzeyleri / Son Yüzeyler** - Onarımdan önceki ve sonraki yüzey sayısı
- **Başlangıçtaki Manifold Olmayan Kenarlar / Sondaki Manifold Olmayan Kenarlar** - Önceki ve sonraki sorunlu kenar sayısı

### Gelişmiş Seçenekler

İnce ayar denetimi için **Gelişmiş** modu etkinleştirin:

- **Köşeleri Kaynakla** - Neredeyse çakışık köşe noktalarını birleştirir (varsayılan: açık)
- **Kaynak Toleransı** - Köşe noktalarının birleştirilmesi için ne kadar yakın olmaları gerektiği
- **Yüzey Yönü** - İçi dışına dönmüş kabukları doğru yöne çevirir, böylece her gövde katı olarak algılanır. Her kabuk kendi başına değerlendirilir; bu sayede içi boş bir model, boşlukları doldurulmadan korunur. Kendi yüzeyleri birbiriyle çelişen kabuklar tahmin yürütülmeden olduğu gibi bırakılır ve su geçirmez olmayan modeller için daha hoşgörülü bir onarıma geçilir - yalnızca yön düzeltmesi sorunu çözmüyorsa önce **Delikleri Doldur** işlemini çalıştırın.
- **Kenarları Kaynakla** - Küçük çatlakları ve bozuk dikişleri onarır
- **Delikleri Doldur** - Ağ yüzeyindeki boşlukları doldurur
- **Kaldırma Modu** - İç veya örtülü geometriyi kaldırır:
  - **Yok** - Tüm geometriyi korur
  - **İç Kısım** - Ana şeklin içinde gizli kalan iç gövdeleri kaldırır
  - **Örtülü** - Dışarıdan görünmeyen yüzeyleri kaldırır

## İpuçları

- İçe aktarılmış modellerde boole işlemleri (Birleştir, Çıkar) beklenmedik sonuçlar veriyorsa önce Onar işlemini deneyin
- Varsayılan ayarlar (Köşeleri Kaynakla açık, diğer her şey kapalı) en yaygın sorunları giderir
- Modeldeki boşluklardan öbür tarafı görebiliyorsanız Delikleri Doldur seçeneğini etkinleştirin
- İçinde gizli geometri bulunan modelleri temizlemek için Kaldırma Modu'nda İç Kısım seçeneğini kullanın

## İlgili

- [Sadeleştir](decimate.md) - Poligon sayısını azaltır
- [Mevcut Nesneleri Ekleme](../../getting-started/adding-existing-objects.md) - Onarım gerekebilecek modelleri içe aktarın
