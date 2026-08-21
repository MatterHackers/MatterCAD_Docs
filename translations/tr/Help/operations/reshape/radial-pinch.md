---
title: Dairesel Sıkıştırma
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: 95ef5847767e5cfcdbae9df9aaa1cb1727da2f5e
source_lang: en
---
# Dairesel Sıkıştırma

Dairesel Sıkıştırma, bir nesneyi özelleştirilebilir bir profil eğrisiyle bir merkez noktasından içeriye doğru sıkıştırır. Arkadan öne doğru çalışan normal [Sıkıştır](pinch.md) işleminin aksine, Dairesel Sıkıştırma bir merkez ekseni etrafında simetrik olarak sıkıştırma uygular.

<!--  Before and after showing an object with radial pinch applied, creating a waisted shape -->
![20260506 155741 paste 20260506 155741](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155741-paste-20260506-155741.jpg)

## Nasıl Kullanılır

1. Bir nesne seçin
2. Yeniden Şekillendir menüsünden **Dairesel Sıkıştırma** işlemini uygulayın
3. Her yükseklikte ne kadar sıkıştırma uygulanacağını tanımlamak için yol profilini düzenleyin
4. Pürüzsüzlük için dilim sayısını ayarlayın

## Parametreler

- **Yol** - Her yükseklik seviyesindeki sıkıştırma miktarını tanımlayan bir profil eğrisi düzenleyicisi. Özel sıkıştırma profilleri oluşturmak için eğriyi düzenleyin
- **Dilimler** - Pürüzsüz sıkıştırma için parça boyunca eşit aralıklarla yerleştirilen yatay kesitlerin sayısı. Daha fazla dilim = daha pürüzsüz sonuçlar

### Gelişmiş Parametreler

- **Sıkıştırma Türü** - Sıkıştırma yönü:
  - **Radyal** - Merkeze doğru her yönden eşit şekilde sıkıştırır
  - **X Ekseni** - Yalnızca X ekseni boyunca sıkıştırır
  - **Y Ekseni** - Yalnızca Y ekseni boyunca sıkıştırır
- **Döndürme Ofseti** - Sıkıştırma etkisinin merkezini kaydırır

## İpuçları

- Kum saati, şişe veya vazo benzeri şekiller oluşturmak için yol düzenleyicisini kullanın
- Dairesel sıkıştırma, silindirik nesnelerden organik ve yuvarlak formlar oluşturmak için idealdir
- Özellikle dar sıkıştırma profillerinde daha pürüzsüz eğriler için Dilimler değerini artırın

## İlgili

- [Sıkıştır](pinch.md) - Basit arkadan öne sıkıştırma
- [Burma](twist.md) - Yükseklik boyunca spiral döndürme
- [Eğri](curve.md) - Bir yay şeklinde bükme
