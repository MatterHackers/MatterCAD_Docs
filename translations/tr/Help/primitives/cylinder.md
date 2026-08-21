---
title: Silindir
articleKey: CylinderObject3D
parent: "Primitives"
nav_order: 5
source_hash: ab8394a14de799f83dc9c39eb86b8eaf2aab37b7
source_lang: en
---
# Silindir

Ayarlanabilir çap, yükseklik ve kenar sayısına sahip yuvarlak bir sütun şeklidir. Silindir; pimler, çubuklar, delikler ve yuvarlak özellikler oluşturmak için vazgeçilmezdir.

<!--  Screenshot of a Cylinder primitive on the workspace -->
![20260318 183248 paste 20260318 183248](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183248-paste-20260318-183248.jpg)


## Parametreler

- **Çap** - Silindirin bir uçtan diğerine genişliği (varsayılan: 20mm)
- **Yükseklik** - Silindirin ne kadar yüksek olduğu (varsayılan: 20mm)
- **Kenarlar** - Çevre boyunca bulunan segment sayısı (varsayılan: 40). Düşük değerler çokgen şekiller oluşturur (örneğin, altıgen için 6)

### Gelişmiş Parametreler

Ek denetimlere erişmek için **Gelişmiş** modu etkinleştirin:

- **Üst Çap** - Konik veya kesik koni şekilleri oluşturmak için silindirin üst kısmına farklı bir çap ayarlayın (varsayılan: Çap ile aynı)
- **Başlangıç Açısı** - Silindirin başladığı açı (varsayılan: 0). Kısmi silindirler oluşturmak için Bitiş Açısı ile birlikte kullanın
- **Bitiş Açısı** - Silindirin bittiği açı (varsayılan: 360). Dilim şeklindeki formlar için 360'tan küçük bir değer ayarlayın

## İpuçları

- Düzgün çokgenler oluşturmak için Kenarlar değerini düşük bir sayıya ayarlayın -- altıgenler için 6, sekizgenler için 8 vb.
- Kesik koniler ve konik şekiller oluşturmak için farklı Çap ve Üst Çap değerleri kullanın
- Dilim veya yay şekilleri oluşturmak için Başlangıç Açısı ve Bitiş Açısı değerlerini ayarlayın
- Silindirler, [Çıkar](../operations/boolean/subtract.md) ile yuvarlak delikler açmak için mükemmel kesme araçlarıdır

## İlgili

- [Koni](cone.md) - Bir noktada sivrilen silindir
- [Yarım Silindir](half-cylinder.md) - Boyuna ikiye kesilmiş silindir
- [Halka](ring.md) - İçi boş silindir (boru)
