---
title: Burma
articleKey: TwistObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: 8ea8d2017c16f20dc42b433bcf91815262bb5380
source_lang: en
---
# Burma

Burma, bir nesnenin üst kısmını alt kısmına göre döndürerek yükseklik boyunca spiral veya burulmuş bir etki oluşturur. Varsayılan olarak döndürme alttan üste doğru eşit şekilde ilerler; **Gelişmiş** altında, dönmenin yükseklik boyunca tam olarak nerede gerçekleşeceğini çizebilirsiniz.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## Nasıl Kullanılır

1. Bir nesne seçin
2. Yeniden Şekillendir menüsünden **Burma** işlemini uygulayın
3. Burma açısını ayarlayın ve pürüzsüzlük için dilimlemeyi düzenleyin
4. Burmanın parça boyunca nasıl dağıldığını çizmek istiyorsanız **Gelişmiş** seçeneğini açın

## Burma Profili

**Gelişmiş** altında, **Burma Profili** eğrisi burmanın nerede gerçekleşeceğini belirler. Toplam burma miktarı yine **Açı** (veya **Döndürme Mesafesi**) denetimiyle ayarlanır - eğri yalnızca bu miktarı dağıtır:

- **Eğri boyunca yukarı** yön, parçadaki yüksekliği yüzde olarak gösterir - altta 0, üstte 100. Düzenleyicideki bir kılavuz çizgi yüzde 100'ü işaretler ve parçanın mm cinsinden gerçek yüksekliğiyle etiketlenir.
- **Eğri boyunca yatay** yön, o yükseklikte ulaşılan toplam burmanın yüzdesidir - hiç yoksa 0, tamamı için 100.

Yeni bir **Burma**, 0'dan 100'e düz bir çapraz çizgiyle başlar; bu da **Gelişmiş** hiç kullanılmadığında elde ettiğiniz sade, eşit dağılımlı burmadır.

Eğrideki düz bir bölüm, parçanın burulmayan bir bandıdır. Eğrinin tüm yüksekliği kapsamadığı yerlerde en yakın uç değeri korunur; bu nedenle yalnızca yüzde 40 ile 60 arasında çizilen bir eğri, parçanın altını ve üstünü sabit bırakır - bir burmayı parçanın ortasında başlatıp durdurmanın yolu budur.

Yukarı giderken geri düşen bir bölüm geri sarılır: parçanın o bandı ters yöne, başladığı konuma doğru döner. Profili 100'ün üzerine çıkarıp sonra geri indirmek, toplamı aşıp yeniden ona dönmenin yoludur.

## Parametreler

- **Döndürme Tipi** - Şunlar arasından seçin:
  - **Açı** - Toplam burma açısını derece cinsinden belirtin (3-360)
  - **Mesafe** - Burmayı çevre boyunca bir mesafe olarak belirtin
- **Dilimler** - Pürüzsüz burma için eklenen ve parça boyunca eşit aralıklı yerleştirilen yatay kesitlerin sayısı. Daha fazla dilim = daha pürüzsüz burma
- **Minimum Kenar Sayısı** - Parçanın burma ekseni etrafında sahip olması gereken en az kenar sayısı. Küp gibi kaba bir şeklin çevresinde döndürmeyi taşıyacak geometri bulunmaz, bu yüzden düz yüzeyleri eğrilmek yerine köşeli görünür; bu ayar, o yüzeylerin burmayı izleyebilmesi için burma ekseninden geçen dikey kesitler ekler. 0 (varsayılan) parçaya dokunmaz
- **Sağa Burma** - Burma yönü: sağ (saat yönünde) veya sol (saat yönünün tersine)
- **Tercih Edilen Yarıçap** - Salt okunur: parçanın kendi bildirdiği ya da şeklinin ima ettiği yarıçap; burma mesafesi bunun çevresinde ölçülür (yalnızca **Mesafe** modunda)
- **Yarıçapı Düzenle** - Kendi değerinizi girebilmek için bildirilen yarıçapı kapatın (yalnızca **Mesafe** modunda ve yalnızca parça bir yarıçap bildirdiğinde)
- **Yarıçapı Geçersiz Kıl** - Burma hesaplaması için özel yarıçap (yalnızca **Mesafe** modunda)

### Gelişmiş Parametreler

- **Burma Profili** - Yukarıda açıklanan eğri düzenleyicisi: yüzde olarak her yükseklikte ulaşılan toplam burma yüzdesi
- **Döndürme Ofseti** - Parçanın etrafında döndürüldüğü merkezi, parçanın ortasından kaydırın

## İpuçları

- Daha yüksek **Dilimler** değerleri daha pürüzsüz sonuçlar verir ancak daha fazla geometri oluşturur
- Burulmuş bir küp veya başka bir düz yüzeyli şekil eğri yerine köşeli görünüyorsa **Minimum Kenar Sayısı** değerini artırın
- Burulmuş bir sütunun altında düz bir taban bırakmak için profili altta düz, sonrasında yükselen şekilde çizin
- Kare bir sütuna uygulanan 90 derecelik burma, zarif bir mimari etki oluşturur
- Parçanın ortasını burup her iki ucu sabit bırakmak için kısa bir yükselişle birleştirilmiş iki düz bölüm çizin

## İlgili

- [Eğri](curve.md) - Bir nesneyi yay şeklinde bükün
- [Sıkıştır](pinch.md) - Merkeze doğru sıkıştırın
- [Dairesel Sıkıştırma](radial-pinch.md) - Profili aynı şekilde bir eğriyle şekillendirin
