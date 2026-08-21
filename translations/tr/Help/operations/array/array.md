---
title: Dizi
articleKey: ArrayObject3D_2
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c547fa24e5f47e0d60f0cec0eac979700d946daf
source_lang: en
---
# Dizi

Dizi, bir nesnenin bir desen içinde düzenlenmiş birden çok kopyasını oluşturur. Desen türleri arasında geçiş yapmak için üstteki düğmelerden bir mod seçin — **Doğrusal**, **Radyal** veya **Dönüştür**.

<!--  Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->
![20260506 080647 paste 20260506 080647](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080647-paste-20260506-080647.jpg)


## Nasıl Kullanılır

1. Bir nesne seçin
2. Çoğaltma menüsünden **Dizi** işlemini uygulayın
3. Bir mod seçin (Doğrusal, Radyal veya Dönüştür)
4. Seçilen moda ait parametreleri ayarlayın

## Mod: Doğrusal

Doğrusal mod, kopyaları isteğe bağlı döndürme ve ölçek ilerlemesiyle birlikte bir yön boyunca yerleştirir.

**Sayı** — Kopya sayısı (tam sayı veya ifade). Kaynak nesne ilk kopyadır; ek kopyalar ondan kaydırılır.

**Kaydırma Yöntemi** — Aralığın nasıl hesaplandığı:
- **Göreli** — Kaydırma, nesnenin sınırlayıcı kutu boyutuyla çarpılır. (1, 0, 0) değerinde bir Bağıl Ofset, kopyaları X ekseni boyunca tam olarak bir nesne genişliği kadar aralıklandırır.
- **Kaydırma** — Kopya başına mm cinsinden sabit dünya uzayı mesafesi.
- **Uç Nokta** — Son kopyanın konumunu belirler; aralık kopyalar arasında eşit olarak bölünür.

**Bağıl Ofset** / **Kaydırma** / **Uç Nokta** — Seçilen Kaydırma Yöntemine bağlı olarak aralık vektörü.

**Döndürme Modu** — Döndürmenin kopyalar boyunca nasıl biriktiği:
- **Yerel** — Her kopya kendi merkezinde yerinde döner; kaydırma yönü dünya eksenlerinde kalır.
- **Birleştirme** — Döndürme birikir ve kaydırmayı yönlendirir; böylece spiraller, yelpazeler ve helisler oluşur.

**Döndürme** — Her eksende kopya başına derece cinsinden döndürme.

**Ölçekle** — Her eksende kopya başına kümülatif ölçek. 1'den küçük değerler kopyaları küçültür; 1'den büyük değerler büyütür.

**Ölçek Ofseti Etkiler** — Açık olduğunda, kopyalar arasındaki aralık da her adımda ölçeklenir. Daralan spiraller ve geometrik ilerlemeler (nautilus kabukları, üst üste dizilmiş tırnak-kabuk eğrileri) için bunu kullanın.

## Mod: Radyal

Radyal mod, kopyaları sabit bir yarıçapta bir merkez ekseni etrafında eşit şekilde dağıtır.

<!--  Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->
![20260506 092618 paste 20260506 092618](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-092618-paste-20260506-092618.jpg)


**Sayma Yöntemi** — Kopya sayısının nasıl belirlendiği:
- **Sayı** — Açıkça belirtilen kopya sayısı.
- **Mesafe** — Kopyalar arasındaki derece cinsinden açısal boşluk; sayı, süpürmeyi dolduracak şekilde hesaplanır.

**Sayı** / **Açısal Mesafe** — Kopya sayısı (Sayı modu) veya derece cinsinden açısal aralık (Mesafe modu). İfadeleri destekler.

**Merkez Ekseni** — Etrafında döndürülecek eksen (varsayılan: Z).

**Daire Dilimi** — Kopyaların tam 360°'lik bir daireyi mi (**Tam**) yoksa kısmi bir yayı mı (**Yay**) kapladığı.

**Yarıçap** — Merkez ekseninden her kopyaya olan mesafe.

**Süpürme Açısı** — Doldurulacak yay derecesi (Daire Dilimi, Yay olduğunda gösterilir). İfadeleri destekler.

**Dönüşü Hizala** — Her kopyayı, ileri ekseni merkezden dışarı bakacak şekilde döndürür.

**İleri Ekseni** — Hizalama için kopyanın hangi ekseninin "ileri" kabul edileceği (Dönüşü Hizala açık olduğunda gösterilir).

## Mod: Dönüştür

Dönüştür modu, kopyaları elle girilen bir dönüşüm kullanarak veya başka bir nesnenin dönüşümünü izleyerek adımlar.

**Sayı** — Kopya sayısı (tam sayı veya ifade).

**Dönüşüm Referansı** — Adım başına dönüşümün nereden geldiği:
- **Giriş** — Ötelemeyi, döndürmeyi ve ölçeği doğrudan siz belirtirsiniz.
- **Nesne** — Dönüşüm, adı belirtilen kardeş bir nesneden okunur.

**Öteleme** — Adım başına mm cinsinden dünya uzayı kaydırması (Referans, Giriş olduğunda gösterilir).

**Döndürme** — Adım başına eksen başına derece cinsinden döndürme (Referans, Giriş olduğunda gösterilir).

**Ölçekle** / **Ölçek Eksenleri** — Her adımda uygulanan tekdüze ve eksen başına ölçek (Referans, Giriş olduğunda gösterilir).

**Dönüşüm Adı** — Dönüşümü adım başına artış olarak kullanılan kardeş nesnenin adı (Referans, Nesne olduğunda gösterilir).

**Bağıl Uzay** — Açık olduğunda, her kopyanın dönüşümü bir önceki kopyanın yerel çerçevesinde birikir; kapalı olduğunda her adım dünya uzayında uygulanır (Referans, Nesne olduğunda gösterilir).

## Rastgele Yap

Tüm kopyalara çeşitlilik katmak için **Rastgele Yap** seçeneğini etkinleştirin.

- **Rastgele Ofset** — Eksen başına mm cinsinden maksimum rastgele konum kaydırması.
- **Rastgele Döndürme** — Eksen başına derece cinsinden maksimum rastgele döndürme.
- **Rastgele Ölçek Eksenleri** — Eksen başına maksimum rastgele ölçek değişimi.
- **İlkini Hariç Tut** — İlk kopyayı tam olarak hesaplanan konumunda tutar (varsayılan: açık).
- **Sonuncuyu Hariç Tut** — Son kopyayı tam olarak hesaplanan konumunda tutar.
- **Rastgele Tohum** — Farklı bir rastgele düzen elde etmek için bunu değiştirin. İfadeleri destekler.

## Birleştir

- **Tek Kafes Oluştur** — Tüm kopyaları tek bir birleştirilmiş kafes nesnesinde toplar.
- **Köşe Noktalarını Birleştir** — Birleştirme mesafesi eşiği içindeki köşe noktalarını kaynaştırır (Tek Kafes Oluştur açık olduğunda gösterilir).
- **Mesafe** — mm cinsinden birleştirme eşiği (Köşe Noktalarını Birleştir açık olduğunda gösterilir).

## İpuçları

- Parametrik desenler oluşturmak için Sayı, Döndürme veya Uç Nokta değerlerinde ifadeler kullanın
- Dairesel desenler için Radyal modu kullanın — daire boyutunu denetlemek üzere Yarıçap değerini ayarlayın ve kopyaların dışa bakması gerekiyorsa Dönüşü Hizala seçeneğini etkinleştirin
- Doğrusal moddaki Birleştirme döndürmesi, açı kaydırmalarını elle hesaplamadan spiraller ve yelpazeler oluşturur
- Ölçek Ofseti Etkiler, nautilus kabuğu ve geometrik ilerleme düzenlerini doğal biçimde oluşturur
- Her kopyanın farklı bir varyantı gösterdiği desenler oluşturmak için Dizi işlemini [Alt Öğe Seç](select-child.md) ile birleştirin

## İlgili

- [Hizala](../placement/align.md) - Nesneleri birbirine göre konumlandırın
- [Alt Öğe Seç](select-child.md) - Bir diziden dizin veya ada göre belirli bir kopya seçin
