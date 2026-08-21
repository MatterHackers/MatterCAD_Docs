---
title: Yarım Küre
articleKey: HalfSphereObject3D
parent: "Primitives"
nav_order: 7
source_hash: 4f82c152ab27e32e36e758c83f9135f1c6bb2096
source_lang: en
---
# Yarım Küre

Bir kürenin üst yarısı -- kubbe biçimi. Kubbeli üst yüzeyler, mercek biçimleri ve yuvarlatılmış kapaklar oluşturmak için kullanışlıdır.

<!--  Screenshot of a Half Sphere primitive on the workspace -->
![20260318 183343 paste 20260318 183343](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183343-paste-20260318-183343.jpg)


## Parametreler

- **Çap** - Kubbenin tabanı boyunca genişlik (varsayılan: 20mm)
- **Boylam Kenarları** - Çevre boyunca bulunan bölüm sayısı (varsayılan: 40)
- **Enlem Kenarları** - Tabandan tepeye kadar olan bölüm sayısı (varsayılan: 10). Daha fazla = daha pürüzsüz kubbe

## İpuçları

- Kapsül biçimi elde etmek için iki yarım küreyi bir silindirle birleştirin
- Kubbeli bir kapak veya düğme oluşturmak için bir silindirin üzerine yerleştirin
- Kubbe biçimli boşluklar oluşturmak için [Çıkar](../operations/boolean/subtract.md) ile kullanın

## İlgili

- [Küre](sphere.md) - Tam top biçimi
- [Yarım Silindir](half-cylinder.md) - İkiye kesilmiş bir silindir
