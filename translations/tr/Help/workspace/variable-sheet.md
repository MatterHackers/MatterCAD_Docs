---
title: Değişken Sayfası
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
source_hash: 3137a4da2b9d2086d4dcace156435caca288dd79
source_lang: en
---
# Değişken Sayfası

Değişken Sayfası, bir tasarıma ait paylaşılan değerleri saklar. Birden fazla nesnenin aynı ölçüleri, sayıları, etiketleri veya formülleri referans alması gerektiğinde bunu kullanın. Sayfadaki bir değeri değiştirmek, ona bağlı nesneleri yeniden hesaplar; böylece parametrik tasarımlar, her nesneyi tek tek düzenlemeye gerek kalmadan tutarlı kalır.

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## Değişken Sayfası Nasıl Eklenir

1. Kütüphaneyi açın ve sahneye **Değişken Sayfası** ekleyin.
2. Sayfa düzenleyicisini göstermek için Değişken Sayfası nesnesini seçin.
3. Bir hücre seçin, ardından bir **Ad** ve bir değer ya da formül girin.
4. Hücre adını, tasarımdaki ifade destekleyen diğer alanlarda kullanın.

## Hücreleri Düzenleme

Her hücrenin düzenlenebilir iki parçası vardır:

- **Ad** - Hücre için isteğe bağlı bir değişken adı. Adlar büyük/küçük harfe duyarlı değildir, boşluklar alt çizgiye dönüştürülür ve yinelenen adlar otomatik olarak ayarlanır.
- **İfade** - Hücrenin değeri. Düz metin veya sayılar doğrudan saklanır. Formüller `=` ile başlar.

Hücrelere `A1` veya `B2` gibi adresleriyle de başvurulabilir. Adlandırılmış hücreler, `wall_thickness`, `outer_diameter` veya `hole_count` gibi amacı anlattıkları için tasarım parametrelerinde genellikle daha anlaşılırdır.

## Formüller

Sayfada değerlendirilmesi için bir formüle `=` ile başlayın:

- `=20 + 5` şunu döndürür: `25`
- `=pi * 10` şunu döndürür: `31.41592653589793`
- `=A1 * 2` başka bir hücreye adresiyle başvurur
- `=wall_thickness + 4` adlandırılmış bir hücreye başvurur

Sayfa; aritmetik işlemleri, parantezleri, karşılaştırma operatörlerini, `sin`, `cos`, `sqrt` ve `round` gibi yaygın `Math` fonksiyonlarını ve `pi`, `tau` ile `e` dahil sabitleri destekler.

## Sayfa Değerlerini Nesnelerde Kullanma

MatterCAD'deki sayısal alanların çoğu ifadeleri destekler. Bir nesne parametresinde sayfa değeri kullanmak için başvurunun önüne `=` ekleyin:

- Bir Küp **Genişlik** değerini `=case_width` olarak ayarlayın.
- Bir Dizi **Sayı** değerini `=hole_count` olarak ayarlayın.
- Bir Öteleme **Kaydırma** değerini `=wall_thickness * 2` olarak ayarlayın.

Sayfa değiştiğinde MatterCAD, ona bağlı nesneleri yeniden hesaplar.

## Metin ve Yardımcı Fonksiyonlar

Değişken Sayfası hücreleri sayıların yanı sıra metin de tutabilir. Metin değerleri; oluşturulan etiketler, parça numaraları, içe aktarılan veriler ve özel tasarım uygulamaları için kullanışlıdır.

İşe yarar yardımcı fonksiyonlar şunlardır:

- `concat()` veya `strcat()` - Metinleri ya da değerleri birleştirir.
- `substring()` - Bir metin değerinin bir bölümünü çıkarır.
- `split()` - Metni böler ve bir öğe döndürür.
- `count()` - Metindeki ayraçla ayrılmış öğeleri sayar.
- `substitute()` - Metni değiştirir.
- `rand(seed)` - Bir tohum değeri verildiğinde belirlenimci bir rastgele değer üretir.
- `importdata()` - Bir URL'den veya yerel dosya yolundan değer okur.

## İpuçları

- Diğer nesnelerin kullandığı değerlerde hücre adresleri yerine açıklayıcı adları tercih edin.
- Temel ölçüleri sayfanın sol üst kısmına yakın tutun ki kolayca bulunabilsinler.
- Türetilmiş değerler için formül kullanın, örneğin `inner_diameter = outer_diameter - wall_thickness * 2`.
- `pi`, `e`, `true`, `false` gibi ayrılmış sözcükleri veya fonksiyon adlarını hücre adı olarak kullanmaktan kaçının.
- Bir formül ayrıştırılamazsa MatterCAD, özgün girdiyi metin olarak saklar.

## İlgili

- [İfadeler](expressions.md) - Nesne parametrelerinde ifadeleri kullanın
- [Bileşenler](components.md) - Yeniden kullanılabilir parametrik tasarımlar oluşturun
- [Dizi](../operations/array/array.md) - Sayfa değerleriyle yönetilen tekrarlı desenler oluşturun
