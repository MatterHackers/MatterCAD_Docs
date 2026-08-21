---
title: Birleştir
articleKey: CombineObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: a3066faa634b5a88a2fe1650a4e2ac278ac50e24
source_lang: en
---
# Birleştir

Birleştir, her şeyi tek bir katı halinde kaynaştırır. Şekillerin üst üste bindiği yerlerdeki dahili yüzeyler kaldırılır; böylece sonuç, üst üste binen kabuklar yerine tek ve sürekli bir kafes olur.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->
![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)

Birleştir, [Çıkar](subtract.md), [Kesiştir](intersect.md) ve [Çıkar ve Değiştir](subtract-and-replace.md) işlemlerinin tümü tek bir Boole nesnesi tarafından gerçekleştirilir -- araç çubuğu düğmesi bu nesneyi Birleştir seçili olarak oluşturur ve Özellikler panelinin üst kısmındaki **İşlem** simge satırından istediğiniz zaman diğer üç işlemden birine geçebilirsiniz.

Birleştir hem katılar hem de 2B yollar üzerinde çalışır. Kendisine verdiğiniz şeye bakar ve doğru türde işlemi uygular; böylece iki yolun birleştirilmesi tek bir yol, iki kafesin birleştirilmesi ise tek bir katı üretir.

## Nasıl Kullanılır

1. İki veya daha fazla nesne seçin
2. Araç çubuğunda **Birleştir**'e tıklayın
3. Özellikler panelinin üst kısmındaki **İşlem** satırında farklı bir simgeye tıklayarak istediğiniz zaman fikrinizi değiştirin -- şekil yeni işlemle yeniden oluşturulur

## Parametreler

- **İşlem** - Hangi Boole işleminin uygulanacağı. Panelin üst kısmında bir simge satırı olarak gösterilir
- **İçi Dışa Dönük Geometriyi Koru** - İçi dışa dönük bir kabuğu, çevresindeki hacmi yok saymasına izin vermek yerine katı malzeme olarak değerlendirir. Katı olması gereken bir model parçaları eksik şekilde geldiğinde bunu açın. Bu, daha yavaş olan kesin Boole motorunu zorunlu kılar
- **Sarım Sırasını Onar** - Boole işlemi çalışmadan önce her parçanın içi dışa dönük kabuklarının sarımını yeniden düzenler. Bu, sonraki her işlemin neyi katı saydığını değiştirmek yerine geometriyi bir kez onarır ve içi dışa dönük bir modele verilecek iki yanıttan genellikle daha iyi olanıdır

## İpuçları

- Birleştir, üst üste binmeyen nesneleri de tek bir kafes halinde birleştirir, ancak bunlar görsel olarak ayrı kalır
- Birleştir, Delik nesnelerini sizin için ele alır: delik olarak işaretlenen her şey sonuca eklenmek yerine sonuçtan çıkarılır
- Birleştir, orijinal nesnelerdeki yüzey başına renkleri sonuca taşır
- Sonuç hatalı görünüyorsa, kaynak nesnelerin su geçirmez olduğunu denetleyin. **Sarım Sırasını Onar** içi dışa dönük kabukları düzeltir; [Onar](../mesh/repair.md) ise içe aktarılan modellerdeki daha geniş çaplı hasarları giderir

## İlgili

- [Çıkar](subtract.md) - Bir şekli diğerinden kesip çıkarın
- [Kesiştir](intersect.md) - Yalnızca nesnelerin üst üste bindiği hacmi koruyun
- [Çıkar ve Değiştir](subtract-and-replace.md) - Bir şekli çıkarın ve kesilip ayrılan parçayı saklayın
- [Düzlem Kesme](../reshape/plane-cut.md) - Başka bir şekil yerine düz bir düzlemle kesin
- [Delik](../../primitives/hole.md) - Çıkarma için önceden yapılandırılmış bir küp
- [Onar](../mesh/repair.md) - Boole işleminden önce hasarlı içe aktarılmış kafesleri düzeltin

Bu sayfa ayrıca, işlemler birleştirilmeden önce kaydedilmiş tasarımlarda hâlâ bulunan eski Birleştir nesnelerini de kapsar. Bunlar tam olarak eskisi gibi çalışmaya devam eder; yeni tasarımlar, Birleştir işlemi seçili olan ortak Boole nesnesini kullanır.
