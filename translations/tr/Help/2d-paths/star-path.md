---
title: Yıldız Yolu
articleKey: StarPathObject3D
parent: "2D Paths"
nav_order: 5
source_hash: 74d92e4171c452cd10069921636e45d7ef9dc70e
source_lang: en
---
# Yıldız Yolu

Nokta sayısı ve iç/dış yarıçapı yapılandırılabilen yıldız şeklinde bir 2B yol. 3B yıldız şekilleri oluşturmak için [Doğrusal Ekstrüzyon](../operations/path/linear-extrude.md) ile birlikte kullanın.

<!-- Screenshot of a Star Path on the workspace -->
![20260506 080319 paste 20260506 080319](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080319-paste-20260506-080319.jpg)


## Parametreler

- **Noktalar** - Yıldız uçlarının sayısı
- **Dış Yarıçap** - Merkezden her bir ucun tepesine olan mesafe
- **İç Yarıçap** - Merkezden uçlar arasındaki çukurlara olan mesafe

## İpuçları

- İç Yarıçap ile Dış Yarıçap arasındaki oran, yıldızın ne kadar "sivri" olduğunu belirler. Küçük bir İç Yarıçap, keskin ve belirgin uçlar oluşturur.
- Klasik bir yıldız için Noktalar değerini 5, Davut Yıldızı şekli için 6, dişliye benzer şekiller için ise daha yüksek bir değere ayarlayın
- Yuvarlatılmış yıldız şekilleri oluşturmak için bir Yıldız Yolu üzerinde [Yolu Yumuşat](../operations/path/smooth-path.md) kullanın

## İlgili

- [Daire Yolu](circle-path.md) - Pürüzsüz bir daire
- [Dişli 2D](../mechanical/gear-2d.md) - Gerçek bir dişli profili
- [Doğrusal Ekstrüzyon](../operations/path/linear-extrude.md) - Yollara yükseklik kazandırın
