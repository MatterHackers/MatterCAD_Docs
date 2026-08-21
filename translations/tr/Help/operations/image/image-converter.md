---
title: Görüntü Dönüştürücü
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c1a05f9688ebe115babfad5d63fc49445af7c449
source_lang: en
---
# Görüntü Dönüştürücü

Görüntü Dönüştürücü, bir raster görüntüyü piksel parlaklığının yüksekliği belirlediği 3B bir kabartmaya dönüştürür. Parlak alanlar yükselir, koyu alanlar alçalır (veya tam tersi).

![20260323 210414 paste 20260323 210414](https://matterhackers.github.io/MatterCAD_Docs/assets/20260323-210414-paste-20260323-210414.jpg)


## Nasıl Kullanılır

1. İlkeller panelinden bir Görüntü Dönüştürücü ekleyin veya bir görüntü dosyasını çalışma alanına sürükleyin
2. Görüntü 3B bir yükseklik haritasına dönüştürülür
3. Yüksekliği ve diğer parametreleri ayarlayın

## İpuçları

- Net şekillere sahip yüksek kontrastlı görüntüler en iyi sonuçları verir
- Görüntü dış hatlarını yükseklik haritası yerine düz yollar olarak izlemek için [Görüntüden Yola](image-to-path.md) kullanın
- Arkadan aydınlatmalı görüntü panoları oluşturmak için [Litofan](lithophane.md) kullanın
- Görüntüleri doğrudan masaüstünüzden çalışma alanına sürükleyebilirsiniz
- Görüntü kabartmasını bir [Küp](../../primitives/cube.md) ile birleştirerek taban ekleyin

## İlgili

- [Görüntüden Yola](image-to-path.md) - Yükseklik haritası oluşturmak yerine dış hatların izini sürer
- [Litofan](lithophane.md) - Arkadan aydınlatmalı görüntü panoları oluşturun
- [Görüntü Nesnesi](../../primitives/image-object.md) - Görüntü içe aktarmanın ilkel sürümü
