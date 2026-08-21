---
title: Özel Yol
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
source_hash: 3633c708477de3ac77d3547b730c33f7e4431cf6
source_lang: en
---
# Özel Yol

Kontrol noktalarıyla kendi 2B yolunuzu çizin. Bu, daha sonra ekstrüzyonla ya da döndürülerek 3B bir nesneye dönüştürülebilecek her türlü 2B şekli oluşturmanız için tam bir özgürlük sağlar.

<!-- Screenshot showing a custom path being edited with control points -->
![20260506 080247 paste 20260506 080247](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080247-paste-20260506-080247.jpg)


## Nasıl Kullanılır

1. 2B Yollar kitaplığından bir **Özel Yol** ekleyin
2. Şeklinizi tanımlamak için kontrol noktalarını düzenleyin
3. 3B bir nesne oluşturmak için [Doğrusal Ekstrüzyon](../operations/path/linear-extrude.md) işlemini veya diğer yol işlemlerini uygulayın

## Açık ve Kapalı Yollar

**Kapalı** onay kutusu, yolun son noktasının yeniden ilk noktasına birleşip birleşmeyeceğini belirler.

- **Kapalı** (varsayılan) seçeneği, yolun bir bölgeyi çevrelemesini sağlar. [Doğrusal Ekstrüzyon](../operations/path/linear-extrude.md) ve [Döndürerek Katılaştır](../operations/path/revolve.md) işlemlerinin doldurduğu şey budur.
- **Aç** seçeneği yolu bir çizgiye dönüştürür. Bir çizgi hiçbir alanı çevrelemediğinden, sahnede dolu bir şekil olarak değil, uzunluğu boyunca ince bir şerit olarak görünür. Ona bir genişlik kazandırıp yeniden katı bir şeye dönüştürmek için [Yolu Şişir](../operations/path/inflate-path.md) işlemini kullanın.

**Kapalı** seçeneğinin işaretini kaldırmadan önce bilmeniz gereken iki şey var:

- **Yeniden kapatmak bir geri alma işlemi değildir.** Bir yolu açmak, onun kapatma parçasını atar. Bu parça eğriyse, **Kapalı** seçeneğini yeniden işaretlemek eğriyi değil düz bir çizgiyi geri getirir. Bunun yerine Ctrl+Z kullanın; geri alma, orijinal yolu tam olarak geri yükler.
- **Bazı konturlar açılmaz.** Geriye ikiden az nokta kalacak bir kontur (tek bir nokta ve ona geri dönen bir eğriyle çizilmiş bir gözyaşı şekli gibi), artık göremeyeceğiniz veya tıklayamayacağınız bir şeye dönüşmek yerine kapalı kalır. İçe aktarılmış bir SVG'de bulunabilen ikinci dereceden bir eğri içeren kontur da öyledir: onu açmak eğriyi bir köşeye düzleştirirdi. Bu reddetme kontur bazındadır, dolayısıyla yolun geri kalanı yine de açılır.

Bir yolda birden çok kontur varsa ve bunlar birbiriyle uyuşmuyorsa, onay kutusu açık olarak görünür. Onu işaretlemek bütün konturları aynı duruma getirir.

Bir bölgeye ihtiyaç duyan işlemler, açık bir yolu reddetmek yerine sizin için kapatır. Doğrusal Ekstrüzyon, Döndürerek Katılaştır, Çıkar ve diğer boole işlemlerinin tümü bunu yapar; böylece açık bir yol, kapalı hâlinin oluşturacağı katının aynısını üretir.

## İpuçları

- Yerleşik yol şekillerinin hiçbiri ihtiyacınıza uymadığında Özel Yol kullanın
- Şekilleri harici vektör düzenleyicilerden içe aktarmak için bkz. [SVG Nesnesi](../primitives/svg-object.md)
- Bir çizgi çizip onu bir parçaya dönüştürmek için **Kapalı** seçeneğinin işaretini kaldırın, kalınlık kazandırmak için [Yolu Şişir](../operations/path/inflate-path.md) işlemini, ardından yükseklik kazandırmak için [Doğrusal Ekstrüzyon](../operations/path/linear-extrude.md) işlemini uygulayın

## İlgili

- [Daire Yolu](circle-path.md) - Hazır bir daire
- [Kutu Yolu](box-path.md) - Hazır bir dikdörtgen
- [SVG Nesnesi](../primitives/svg-object.md) - SVG dosyalarından vektör yollarını içe aktarın
- [Doğrusal Ekstrüzyon](../operations/path/linear-extrude.md) - Yollara yükseklik kazandırın
