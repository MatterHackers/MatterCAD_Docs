---
title: Döndürerek Katılaştır
articleKey: RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: a63ebb08d982178e0e59f0b9f07c3c0dca53148b
source_lang: en
---
# Döndürerek Katılaştır

Döndürerek Katılaştır, 2B bir yolu bir eksen etrafında döndürerek 3B bir dönel katı oluşturur. Vazolar, kaseler, tekerlekler ve diğer dönel simetrik nesneleri bu şekilde oluşturursunuz.

<!--  Before and after showing a profile path being revolved into a vase shape -->
![20260506 102004 paste 20260506 102004](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-102004-paste-20260506-102004.jpg)


## Nasıl Kullanılır

1. 2B bir yol seçin
2. Yol işlemleri menüsünden **Döndürerek Katılaştır** işlemini uygulayın
3. Döndürme aralığını, eksen konumunu ve kenar sayısını ayarlayın

## Parametreler

- **Döndürme** - Döndürerek katılaştırma için toplam döndürme açısı (varsayılan: 0, aralık: 0-360). Tam bir dönüş için 360 olarak ayarlayın.
- **Eksen Konumu** - Döndürme ekseninin yol merkezine göre kaydırma miktarı (varsayılan: 0, aralık: -30 ile 30). Pozitif değerler ekseni yoldan uzaklaştırarak daha geniş bir açıklık oluşturur.
- **Başlangıç Açısı** - Dönüşün başladığı yer (varsayılan: 0)
- **Bitiş Açısı** - Dönüşün bittiği yer (varsayılan: 45). Tam bir dönüş için 360 olarak ayarlayın.
- **Kenarlar** - Dönüş boyunca yer alan segment sayısı (varsayılan: 30). Daha fazla = daha pürüzsüz yüzey.

## İpuçları

- Döndürülen şeklin iç çapını denetlemek için Eksen Konumu değerini kullanın
- Kısmi dönüşler (kemerler, oluklar) oluşturmak için Başlangıç Açısı ve Bitiş Açısı değerlerini 360'tan küçük ayarlayın
- Vazonuzun veya kasenizin şeklini bir profil yolu olarak çizin, ardından kusursuz simetri için onu döndürerek katılaştırın
- Döndürülen bir [Daire Yolu](../../2d-paths/circle-path.md) bir simit oluşturur

## İlgili

- [Doğrusal Ekstrüzyon](linear-extrude.md) - Döndürmek yerine doğrudan yukarı doğru ekstrüzyon uygular
- [2B Yollar](../../2d-paths/index.md) - Döndürülecek profil yolları oluşturun
- [Simit](../../primitives/torus.md) - Hazır, döndürülerek oluşturulmuş bir halka şekli
