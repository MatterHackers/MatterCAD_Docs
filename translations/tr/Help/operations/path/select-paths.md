---
title: Yolları Seç
articleKey: SelectPathsObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: f7df7bb24841030643e4634febedcfce6e92ada9
source_lang: en
---
# Yolları Seç

Yolları Seç, karmaşık bir yol nesnesindeki alt yollardan hangilerinin korunacağını filtreler. Özellikle, dış harf formlarına ve iç kesim şekillerine ayrı parçalar olarak ihtiyaç duyduğunuz dekoratif veya çok parçalı yazı tipleriyle çalışırken kullanışlıdır — örneğin bunları iki farklı renkte 3D yazdırmak için.

<!--  Screenshot showing Select Paths applied to decorative text with outer paths highlighted -->
![20260506 154655 paste 20260506 154655](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154655-paste-20260506-154655.jpg)

## Yol Derinliği Nasıl Çalışır

Bir yol nesnesi kapalı alanlar içeren şekiller barındırdığında ("O" harfinin içi veya dekoratif bir kıvrımın boşluğu gibi), bu kapalı alanlar 1. derinlikteki **deliklerdir**. Her harfin veya şeklin dış konturu ise **0 derinliğindedir**.

```
Depth 0 — outer contour of each letter or shape
Depth 1 — first level of enclosed holes (inside an "O", "A", etc.)
Depth 2 — shapes nested inside a hole (rarely used)
```

## Filtre Ön Ayarları

### Tümü
Her yolu değiştirmeden dahil eder. Bu varsayılan seçenektir ve Yolları Seç'i hiç uygulamamakla eşdeğerdir.

### Yalnızca Dış Yollar
Yalnızca her şeklin dış konturunu korur (derinlik == 0). Dekoratif bir yazı tipinden iç kesim alanları olmadan yalnızca harf ana hatlarını elde etmek için bunu kullanın.

### Yalnızca Delikler
Yalnızca kapalı delikleri korur (derinlik > 0). Harflerin ve şekillerin yalnızca iç kesim alanlarını elde etmek için bunu kullanın.

### Grup İndeksine Göre
Yalnızca tek bir kopuk şekle ait yolları korur. Grup 0 ilk şekil, grup 1 ikinci şekildir ve bu şekilde devam eder. Bir kelimeden tek bir karakteri ayırmak için bunu kullanın.

### Özel
Her yol için değerlendirilen bir ifade yazın. İfade sıfırdan farklı olduğunda yol **dahil edilir**, sıfır olduğunda ise **dışarıda bırakılır**.

Değişken yerine koymayı etkinleştirmek için ifadeler `=` ile başlamalıdır. `=` olmadan değer düz bir sayı olarak ele alınır (örneğin, `1` her zaman dahil eder, `0` her zaman dışarıda bırakır).

## Özel İfade Örnekleri

| İfade | Etki |
|------------|--------|
| `=PathDepth==0` | Yalnızca dış konturlar (Yalnızca Dış Yollar ile aynı) |
| `=PathDepth>0` | Yalnızca delikler (Yalnızca Delikler ile aynı) |
| `=GroupIndex==0` | Yalnızca ilk kopuk şekil |
| `=PathArea>100` | Alanı 100 mm²'den büyük şekiller |
| `=PathLength>50` | Çevresi 50 mm'den uzun şekiller |

## Özel İfade Değişkenleri

| Değişken | Anlam |
|----------|---------|
| `PathDepth` | 0 = dış kontur; 1 ve üzeri = delik veya iç içe şekil |
| `GroupIndex` | Kopuk şeklin indeksi (0, 1, 2…) |
| `GroupOuterArea` | Bu gruba ait dış yolun alanı |
| `GroupOuterLength` | Bu gruba ait dış yolun çevresi |
| `ChildCount` | Bu grubun dış yolu içindeki delik sayısı |
| `PathIndex` | Bu yolun kendi grubu içindeki sıralı indeksi |
| `PathArea` | Bu tek yolun alanı |
| `PathLength` | Bu tek yolun çevresi |

## Örnek: Çok Renkli Noel Yazı Tipi Baskısı

Yolları Seç'in yaygın bir kullanımı, harflerinde iç kesim şekilleri bulunan dekoratif metinlerin yazdırılmasıdır. Dış harfleri bir renkte, iç kesimleri ikinci bir renkte yazdırmak için:

1. Bir **Metin** nesnesi ekleyin ve **2B çıktı** olarak ayarlayın
2. **Yolları Seç** uygulayın → ön ayarı **Yalnızca Dış Yollar** olarak belirleyin
3. Yükseklik kazandırmak için **Doğrusal Ekstrüzyon** uygulayın → ilk filament renginizi atayın
4. Özgün metin nesnesine geri dönün
5. İkinci bir **Yolları Seç** uygulayın → ön ayarı **Yalnızca Delikler** olarak belirleyin
6. Aynı yükseklikle **Doğrusal Ekstrüzyon** uygulayın → ikinci filament renginizi atayın
7. Ekstrüde edilmiş nesnelerden birini diğerinin üzerine konumlandırın — iki renk kusursuz biçimde hizalanır

## İlgili

- [Doğrusal Ekstrüzyon](linear-extrude.md) — Bir 3D nesne oluşturmak için filtrelenmiş yollara yükseklik kazandırın
- [Döndürerek Katılaştır](revolve.md) — Filtrelenmiş yolları bir eksen etrafında döndürün
- [SVG Nesnesi](../../primitives/svg-object.md) — Birden fazla alt yol içerebilen vektör yollarını içe aktarın
- [Metin](../../primitives/text.md) — 2B modundaki metin nesneleri çok yollu çıktı üretir
