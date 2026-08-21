---
title: Görüntüden Yola
articleKey: ImageToPathObject3D_2
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 0145587f635ede68bfc1df37b4f0d366a03d3a6c
source_lang: en
---
# Görüntüden Yola

Görüntüden Yola, 2B yollar oluşturmak için bir görüntünün dış hatlarını izler. Bu yollar daha sonra ekstrüde edilebilir, döndürülebilir veya diğer herhangi bir yol işlemiyle kullanılabilir. Logoları, siluetleri ve basit grafikleri 3B nesnelere dönüştürmek için idealdir.

![20260324 075521 paste 20260324 075521](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-075521-paste-20260324-075521.jpg)


## Nasıl Kullanılır

1. Çalışma alanınızda bir görüntü nesnesi seçin
2. Görüntü işlemleri menüsünden **Görüntüden Yola** işlemini uygulayın
3. Analiz türünü seçin ve seçim aralığını ayarlayın

## Parametreler

- **Analiz Türü** - Görüntünün iz sürme için nasıl analiz edileceği:
  - **Saydamlık** - Saydam ve opak alanlara göre iz sürer (saydam arka planlı PNG'ler için en iyisidir)
  - **Renkler** - Renk bölgelerine göre iz sürer
  - **Yoğunluk** - Parlaklık seviyelerine göre iz sürer (çoğu görüntü için en iyisidir)
- **Aralık Seç** - İz sürmeye hangi parlaklık/renk değerlerinin dahil edileceğini seçmek için bir histogram denetimi
- **Min Yüzey Alanı** - Bir yol döngüsünün dahil edilmesi için gereken en küçük alan. Küçük gürültü artefaktlarını filtrelemek için artırın

## İpuçları

- Temiz, yüksek kontrastlı ve basit şekillere sahip görüntüler en iyi sonucu verir
- Saydam arka planlı PNG görüntüler için Saydamlık modunu kullanın
- Fotoğraflar ve saydamlığı olmayan görüntüler için Yoğunluk modunu kullanın
- İz sürme işleminden sonra, yola yükseklik kazandırmak için [Doğrusal Ekstrüzyon](../path/linear-extrude.md) uygulayın
- İz sürme sonucundan küçük ve istenmeyen ayrıntıları kaldırmak için Min Yüzey Alanı değerini artırın

## İlgili

- [Görüntü Dönüştürücü](image-converter.md) - Düz yollar yerine yükseklik haritası kabartması oluşturun
- [Litofan](lithophane.md) - Arkadan aydınlatmalı görüntü panoları oluşturun
- [SVG Nesnesi](../../primitives/svg-object.md) - Vektör grafiklerini doğrudan içe aktarın (iz sürme gerekmez)
- [Doğrusal Ekstrüzyon](../path/linear-extrude.md) - İzi sürülen yola yükseklik kazandırın
