---
title: SVG Nesnesi
articleKey: SvgObject3D
parent: "Primitives"
nav_order: 15
source_hash: dab97cdde74d938b5612d959f83b54b4a04a49da
source_lang: en
---
# SVG Nesnesi

SVG (Scalable Vector Graphics) dosyalarını içe aktarın ve bunları tasarımınızda 2B yol olarak kullanın. SVG'ler daha sonra [Doğrusal Ekstrüzyon](../operations/path/linear-extrude.md) veya [Döndürerek Katılaştır](../operations/path/revolve.md) kullanılarak 3B şekillere dönüştürülebilir.

<!--  Screenshot showing an imported SVG path being extruded into a 3D shape -->
![20260318 184807 paste 20260318 184807](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184807-paste-20260318-184807.jpg)



## Nasıl Kullanılır

1. Bir SVG dosyasını çalışma alanına sürükleyerek veya Aç düğmesini kullanarak içe aktarın
2. SVG, 2B yol olarak içe aktarılır
3. Yükseklik kazandırmak için [Doğrusal Ekstrüzyon](../operations/path/linear-extrude.md) uygulayın veya diğer [Yol İşlemleri](../operations/path/index.md) araçlarını kullanın

## İpuçları

- En iyi sonuç için SVG dosyaları dolgulu şekiller veya kapalı yollar içermelidir
- Çok sayıda yol içeren karmaşık SVG'lerin işlenmesi daha uzun sürebilir
- Çok yollu bir SVG'nin belirli bölümleriyle çalışmak için [Yolları Seç](../operations/path/select-paths.md) kullanın
- Logolar, simgeler ve dekoratif desenler için çevrimiçi olarak birçok ücretsiz SVG dosyası bulunabilir

## İlgili

- [Görüntüden Yola](../operations/image/image-to-path.md) - SVG kullanmak yerine raster görüntüleri yollara dönüştürün
- [Metin](text.md) - SVG'ye ihtiyaç duymadan doğrudan metin oluşturun
- [Doğrusal Ekstrüzyon](../operations/path/linear-extrude.md) - Düz yollara yükseklik kazandırın
- [2B Yollar](../2d-paths/index.md) - Yerleşik yol ilkelleri
