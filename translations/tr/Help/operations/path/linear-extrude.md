---
title: Doğrusal Ekstrüzyon
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cdfdb9cfe4c3339e70a23ddfb2f5071b1e8c5557
source_lang: en
---
# Doğrusal Ekstrüzyon

Doğrusal Ekstrüzyon, 2B bir yola yükseklik vererek düz bir şekli 3B katı nesneye dönüştürür. Yolları 3B nesnelere çevirmenin başlıca yolu budur.

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## Nasıl Kullanılır

1. 2B bir yol ya da yol tabanlı bir nesne seçin
2. Yol işlemleri menüsünden **Doğrusal Ekstrüzyon** uygulayın
3. İstediğiniz yüksekliği ayarlayın

## Parametreler

- **Yükseklik** - Ekstrüzyonun ne kadar yüksek olduğu (varsayılan: 5mm, aralık: 0.1-50mm)
- **Üst Pah** - Ekstrüzyonun üst kenarına pahlı (yuvarlatılmış) bir kenar ekler (varsayılan: kapalı)

### Pah Parametreleri (Üst Pah etkinken görünür)

- **Stil** - Pah profilinin stili (Keskin veya yuvarlatılmış)
- **Yarıçap** - Pahın ne kadar geniş uzandığı (varsayılan: 3mm)
- **Segmentler** - Pah eğrisinin pürüzsüzlüğü (varsayılan: 9)

## İpuçları

- Bu işlem her 2B yolla çalışır: [Daire](../../2d-paths/circle-path.md), [Kutu](../../2d-paths/box-path.md), [Yıldız](../../2d-paths/star-path.md), [SVG](../../primitives/svg-object.md) ve [Özel](../../2d-paths/custom-path.md) yollar
- Daha rafine, profesyonel bir görünüm için Üst Pah seçeneğini etkinleştirin
- Bir yolu doğrudan yukarı ekstrüzyon yapmak yerine bir eksen etrafında döndürmek için bkz. [Döndürerek Katılaştır](revolve.md)

## İlgili

- [Döndürerek Katılaştır](revolve.md) - Bir yolu eksen etrafında döndürür
- [2B Yollar](../../2d-paths/index.md) - Kullanılabilir yol şekilleri
- [Metin](../../primitives/text.md) - Metin otomatik olarak ekstrüzyon edilir
