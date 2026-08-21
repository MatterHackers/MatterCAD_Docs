---
title: Eğri
articleKey: CurveObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 6adde5da3bb469384f59eb5e9dfe5cb642b3eec5
source_lang: en
---
# Eğri

Eğri, düz bir nesneyi bir yay veya dairesel şekle büker. Bükümü, ya bir açı ya da etrafına sarılacak bir çap belirterek kontrol edebilirsiniz.

<!--  Before and after showing a straight bar being curved into an arc -->
![20260506 155243 paste 20260506 155243](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155243-paste-20260506-155243.jpg)

## Nasıl Kullanılır

1. Bir nesne seçin
2. Yeniden Şekillendir menüsünden **Eğri** işlemini uygulayın
3. Açı veya Çap bükme türü arasında seçim yapın
4. İstediğiniz eğriliği elde etmek için parametreleri ayarlayın

## Parametreler

- **Bükme Türü** - Şunlar arasında seçim yapın:
  - **Açı** - Bükme açısını doğrudan belirtin (1-360 derece)
  - **Çap** - Parçanın etrafına sarıldığı dairenin çapını belirtin
- **Bükme Yönü** - Yukarı Bük veya Aşağı Bük
- **Başlangıç Yüzdesi** - Bükümün nesnenin neresinde başlayacağı (%0-100)
- **Ağı Böl** - Pürüzsüz eğriler için ağı böler (varsayılan: açık)
- **Dönüş Başına Min Kenar** - Tam bir devir başına düşen minimum ağ segmenti sayısı. Daha yüksek değerler = daha pürüzsüz eğriler

### Gelişmiş Parametreler

- **Başlangıç Bükülme Yüzdesi** - Bükümün başladığı, soldan itibaren yüzde değeri
- **Bitiş Bükülme Yüzdesi** - Bükümün bittiği, soldan itibaren yüzde değeri

## İpuçları

- Düz stok şekillerden kemerler, halkalar ve bükülmüş braketler oluşturmak için Eğri'yi kullanın
- Açıyı 360 olarak ayarlamak, nesneyi tam bir halka haline getirir
- Dar bükümlerde daha pürüzsüz sonuçlar için Dönüş Başına Min Kenar değerini artırın
- Nesne, uzunluğu boyunca (X ekseni) bükülür

## İlgili

- [Burma](twist.md) - Bükmek yerine yükseklik boyunca döndürür
- [Simit](../../primitives/torus.md) - Hazır bir halka şekli
