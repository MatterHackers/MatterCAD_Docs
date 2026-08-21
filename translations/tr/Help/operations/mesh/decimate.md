---
title: Azalt
articleKey: DecimateObject3D
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 58a2573b968808e98203832142fa8bacf7a9cf99
source_lang: en
---
# Azalt (Sadeleştirme)

Azalt, genel şekli korurken bir ağın poligon sayısını düşürür. Bu, çok ayrıntılı modelleri sadeleştirmek, dosya boyutunu küçültmek ve karmaşık geometri üzerindeki işlemleri hızlandırmak için kullanışlıdır.

![20260324 080430 paste 20260324 080430](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080430-paste-20260324-080430.jpg)


## Nasıl Kullanılır

1. Bir nesne seçin
2. Ağ menüsünden **Azalt** işlemini uygulayın
3. Hedefinizi (sayı veya yüzde) belirleyin ve ayarlayın

## Parametreler

- **Mod** - Hedefin nasıl belirtileceğini seçin:
  - **Yüzde** - Orijinal poligonların bir yüzdesini korur (varsayılan: %50)
  - **Sayı** - Belirli bir poligon sayısını hedefler
- **Kaynak Poligon Sayısı** - Orijinal poligon sayısı (salt okunur)
- **Hedef Yüzde** - Korunacak poligonların yüzdesi (Yüzde modunda görünür)
- **Hedef Sayısı** - Korunacak tam poligon sayısı (Sayı modunda görünür)
- **Yüzde Azaltma Sonrası Sayı** - Yüzde azaltmasından sonraki nihai poligon sayısı (salt okunur)
- **Yüzeyi Koru** - Daha yüksek doğruluk için köşe noktalarını orijinal yüzeye geri yansıtır (daha yavaştır ancak orijinal şekle daha sadıktır)

## İpuçları

- %50 azaltma genellikle görsel kaliteyi iyi korur
- Doğruluk hızdan daha önemli olduğunda Yüzeyi Koru seçeneğini etkinleştirin
- Poligon sayısını azaltmak, karmaşık içe aktarılmış modellerdeki boole işlemlerini hızlandırır
- Çok düşük poligon sayıları şekli gözle görülür biçimde bozar -- kesinleştirmeden önce sonucu kontrol edin

## İlgili

- [Onar](repair.md) - Ağ sorunlarını giderir
