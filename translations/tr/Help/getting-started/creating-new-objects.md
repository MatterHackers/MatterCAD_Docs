---
title: Yeni Nesneler Oluşturma
parent: "Getting Started"
nav_order: 2
source_hash: 3eccb5aac5bb6f4d88f1ca3583eedd2f70384eeb
source_lang: en
---
# Yeni Nesneler Oluşturma

MatterCAD, 3D nesneler oluşturmak için zengin bir araç seti sunar. İlkel şekillerle başlayabilir, metin ve QR kodu gibi özel araçları kullanabilir ya da Boole işlemleri ve dizilerle karmaşık formlar kurabilirsiniz.

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## İlkel Şekiller Ekleme

Bir tasarıma başlamanın en hızlı yolu ilkel şekiller eklemektir. Kitaplıktaki İlkeller panelini açın ve çalışma alanınıza eklemek için herhangi bir şekle tıklayın. Kullanılabilir ilkeller şunlardır:

- **Temel şekiller** - Küp, Silindir, Küre, Koni, Simit, Halka, Piramit, Kama ve bunların yarım varyantları
- **Metin ve özel** - Metin, Braille, QR Kodu, Görüntü Nesnesi, SVG Nesnesi

Her ilkelin, seçtikten sonra Özellikler panelinde ayarlayabileceğiniz parametreleri vardır. Örneğin bir Küp'ün Genişlik, Derinlik ve Yükseklik denetimleri bulunur. Her şeklin ayrıntıları için bkz. [İlkeller](../primitives/index.md).

## İşlemler Araç Çubuğu

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

Görünüm alanının üst kısmındaki araç çubuğu, yaygın işlemlere hızlı erişim sağlar:

- **Geri Al / Yinele** - Değişiklikleri geri alın veya yeniden uygulayın. Ayrıca geri almak için **Ctrl+Z**, yinelemek için **Ctrl+Y** tuşlarını kullanabilirsiniz
- **Grupla / Grubu Çöz** - Seçili nesneleri tek bir birim olarak hareket eden ve işlem gören bir grupta birleştirin ya da bir grubu parçalarına ayırın
- **Kopyala / Sil** - Seçili nesneleri çoğaltın veya kaldırın. Standart **Ctrl+C**, **Ctrl+X** ve **Ctrl+V** kısayolları da çalışır
- **Hizala** - Birden fazla nesneyi birbirine göre konumlandırın
- **Boole işlemleri** - [Birleştir](../operations/boolean/combine.md), [Çıkar](../operations/boolean/subtract.md), [Kesiştir](../operations/boolean/intersect.md) ve [Çıkar ve Değiştir](../operations/boolean/subtract-and-replace.md)
- **Diziler** - Çoğaltılmış nesnelerden [doğrusal, radyal, eğri ve dönüştür desenleri](../operations/array/array.md) oluşturun
- **Dönüştür işlemleri** - [Döndür](../operations/transform/rotate.md), [Ölçekle](../operations/transform/scale.md), [Aynala](../operations/transform/mirror.md) ve diğer değişiklikleri uygulayın

## Karmaşık Şekiller Oluşturma

MatterCAD'deki çoğu tasarım, basit şekillerin birleştirilmesiyle oluşturulur:

1. **İlkellerle başlayın** - İhtiyacınız olan temel şekilleri ekleyin
2. **Konumlandırın** - Nesneleri istediğiniz yerde üst üste gelecek şekilde taşıyın ve döndürün
3. **Boole işlemlerini uygulayın** - Şekilleri birbiriyle kaynaştırmak için [Birleştir](../operations/boolean/combine.md), bir şekli diğerinden kesip çıkarmak için [Çıkar](../operations/boolean/subtract.md) işlemini kullanın
4. **İnceltin** - Ayrıntı eklemek için Pah, Eğri veya Burma gibi [Yeniden Şekillendir](../operations/reshape/index.md) işlemlerini kullanın

## İlgili

- [İlkeller](../primitives/index.md) - Tüm ilkel şekiller için tam referans
- [Mevcut Nesneleri Ekleme](adding-existing-objects.md) - Sıfırdan oluşturmak yerine dosyaları içe aktarın
- [Boole İşlemleri](../operations/boolean/index.md) - Şekilleri karmaşık formlarda birleştirin
- [Nesneleri Düzenleme](editing-objects.md) - Nesneleri oluşturduktan sonra taşıyın, döndürün ve ölçekleyin
