---
title: Yolu Şişir
articleKey: InflatePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: c0e11d3d24c5f832f797cde4d392e26a4694733d
source_lang: en
---
# Yolu Şişir

Yolu Şişir, bir 2B yolu dışa doğru genişleterek şeklin genel formunu korurken daha büyük olmasını sağlar. Bu, tüm kenarlara tekdüze bir ofset uygulamaya benzer.

<!--  Before and after showing a path inflated outward -->
![20260506 100652 paste 20260506 100652](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100652-paste-20260506-100652.jpg)


## Nasıl Kullanılır

1. Bir 2B yol seçin
2. Yol işlemleri menüsünden **Yolu Şişir** işlemini uygulayın
3. Şişirme miktarını ayarlayın

## Açık Bir Çizgiyi Şişirme

Şişir, bir çizgiyi şekle dönüştürmenin yoludur. Açık bir çizgi çizmek için bir [Özel Yol](../../2d-paths/custom-path.md) üzerindeki **Kapalı** seçeneğinin işaretini kaldırın, ardından onu şişirin: sonuç, çizginin her iki yanında belirlediğiniz miktar kadar geniş, dolu bir şerittir. Buradan sonra diğer tüm yollar gibi ekstrüde edilir.

**Stil**, çizginin iki ucunun nasıl kapatılacağını ve köşelerinin nasıl birleştirileceğini belirler:

- **Düz**, şeridi her uç noktada dik olarak sonlandırır
- **Yuvarlat**, her uç noktanın ötesine bir yarım daire ekler
- **Keskin**, her uç noktanın ötesine bir kare ekler

Açık bir çizginin içine doğru küçülebileceği bir iç kısmı yoktur; bu nedenle sıfır veya negatif bir miktar geriye hiçbir şey bırakmaz. Yol *tamamen* açık olduğunda, Şişir değeri küçük bir pozitif sayıya yükselterek sınırlar ve sınırlanan sayıyı kutuya geri yazar; böylece ne olduğunu görebilirsiniz.

Açık ve kapalı konturları bir arada içeren bir yol sınırlanmaz: kapalı konturlar normal şekilde küçülür, açık olanlar ise basitçe devre dışı kalır. Kapalı yollar, negatif değerlerde her zaman olduğu gibi küçülmeye devam eder.

## İpuçları

- Yolu genişletmek yerine içe doğru küçültmek için negatif değerler kullanın
- Şişir, şekillerin etrafında tolerans ofsetleri oluşturmak için kullanışlıdır
- Belirli genişliklerde kenarlıklar oluşturmak için [Dış Hat Yolu](outline-path.md) ile birleştirin

## İlgili

- [Dış Hat Yolu](outline-path.md) - Bir yoldan dış hat oluşturun
- [Kenarlık Yolu](border-path.md) - Bir kenarlık ofseti ekleyin
- [Yolu Yumuşat](smooth-path.md) - Bir yolun köşelerini yuvarlatın
