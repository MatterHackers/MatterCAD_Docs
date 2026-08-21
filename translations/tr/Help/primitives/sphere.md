---
title: Küre
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
source_hash: c227e98ac116c3481bb2af73c55801de84e70b1e
source_lang: en
---
# Küre

Ayarlanabilir çap ve detay seviyesine sahip yuvarlak top şekli.

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## Parametreler

- **Çap** - Kürenin bir uçtan diğerine genişliği (varsayılan: 20mm)
- **Kenarlar** - Çevre boyunca yer alan segment sayısı (varsayılan: 40). Daha fazla kenar = daha pürüzsüz yüzey

### Gelişmiş Parametreler

Ek denetimler için **Gelişmiş** modunu etkinleştirin:

- **Başlangıç Açısı** - Küre yüzeyinin başladığı açı (varsayılan: 0)
- **Bitiş Açısı** - Küre yüzeyinin bittiği açı (varsayılan: 360). Kısmi küre şekilleri için 360'tan küçük bir değer ayarlayın
- **Enlem Kenarları** - Yukarıdan aşağıya doğru segment sayısı (varsayılan: 30). Daha fazlası = daha pürüzsüz kutuplar

## İpuçları

- 3D baskı için genellikle 40 kenar yeterlidir. Daha yüksek değerler daha pürüzsüz yüzeyler oluşturur ancak dosyaları büyütür
- Kase veya kubbe gibi kısmi küre şekilleri oluşturmak için Başlangıç Açısı ve Bitiş Açısı değerlerini kullanın
- Küresel boşluklar oluşturmak için [Çıkar](../operations/boolean/subtract.md) ile birlikte kullanın

## İlgili

- [Yarım Küre](half-sphere.md) - Yalnızca üst yarım küre
- [Simit](torus.md) - Halka şekli
