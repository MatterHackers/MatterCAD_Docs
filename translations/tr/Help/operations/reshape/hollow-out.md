---
title: İçini Boşalt
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cc2c5555723ecfe77475fef9e7a2090cdf760204
source_lang: en
---
# İçini Boşalt

İçini Boşalt, yüzeyi içe doğru öteleyerek katı bir nesneden içi boş bir kabuk oluşturur. Sonuç, orijinal şeklin ince duvarlı bir versiyonudur.

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## Nasıl Kullanılır

1. Katı bir nesne seçin
2. Yeniden Şekillendir menüsünden **İçini Boşalt** işlemini uygulayın
3. İstenen duvar kalınlığını ayarlayın

## Parametreler

- **Mesafe** - Milimetre cinsinden duvar kalınlığı (varsayılan: 2 mm). Ortaya çıkan kabuğun kalınlığı budur.
- **Hücre Sayısı** - İçini boşaltma algoritmasının çözünürlüğü (varsayılan: 64). Daha yüksek değerler daha pürüzsüz iç yüzeyler oluşturur ancak hesaplanması daha uzun sürer.

## İpuçları

- İçini Boşalt; muhafazalar, kaplar, vazolar ve hafif parçalar oluşturmak için kullanışlıdır
- 3D olarak yazdırılan çoğu parça için 1-2 mm duvar kalınlığı tipiktir
- İç yüzey pürüzlü veya köşeli görünüyorsa Hücre Sayısı değerini artırın
- İçini boşaltma işlemi açık bir taban oluşturur -- kapalı bir tabana ihtiyacınız varsa bir [Küp](../../primitives/cube.md) ile birleştirin
- Karmaşık şekillerde hesaplama birkaç saniye sürebilir

## İlgili

- [Düzlem Kesme](plane-cut.md) - Bir nesneyi belirli bir yükseklikte kesin
- [Çıkar](../boolean/subtract.md) - Malzemeyi elle kesip çıkarın
