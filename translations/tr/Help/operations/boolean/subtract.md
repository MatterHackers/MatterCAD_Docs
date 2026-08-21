---
title: Çıkar
articleKey: SubtractObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 59685bd0a635b70d7f938780f71e90be595dd993
source_lang: en
---
# Çıkar

Çıkar, seçtiğiniz parçaları seçmediğiniz parçaların içinden keser. Kesici şekilleri belirlemek için **Çıkarılacak Parça(lar)** seçeneğini kullanın; geri kalan her şey kesilecek olan temeldir.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->
![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)

[Birleştir](combine.md), Çıkar, [Kesiştir](intersect.md) ve [Çıkar ve Değiştir](subtract-and-replace.md) işlemlerinin tümü tek bir Boole nesnesi tarafından gerçekleştirilir -- araç çubuğu düğmesi bu nesneyi Çıkar seçili olarak oluşturur ve Özellikler panelinin üst kısmındaki **İşlem** simge satırından istediğiniz zaman diğer üçünden birine geçebilirsiniz.

Çıkar hem katılarda hem de 2B yollarda çalışır. Kendisine verilene bakar ve doğru türde işlemi uygular; böylece bir yoldan başka bir yolu çıkarmak bir yol, bir kafesten başka bir kafesi çıkarmak ise bir katı üretir.

## Nasıl Kullanılır

1. İki veya daha fazla nesne seçin
2. Araç çubuğunda **Çıkar** düğmesine tıklayın -- hemen bir sonuç vermesi için kesilip atılacak varsayılan bir parça sizin adınıza seçilir
3. Hangi alt öğelerin kesici şekiller olacağını belirlemek için **Çıkarılacak Parça(lar)** seçeneğini kullanın
4. Özellikler panelinin üst kısmındaki **İşlem** satırında farklı bir simgeye tıklayarak istediğiniz zaman fikrinizi değiştirin -- şekil yeni işlemle yeniden oluşturulur

## Parametreler

- **İşlem** - Hangi Boole işleminin uygulanacağı. Panelin üst kısmında bir simge satırı olarak gösterilir
- **Çıkarılacak Parça(lar)** - Hangi alt öğelerin kesici şekiller olduğu
- **Çıkarılan Parçaları Koru** - Kesilip atılan parçaları silmek yerine sahnede bırakır
- **İçi Dışa Dönük Geometriyi Koru** - İçi dışa dönük bir kabuğu, çevresindeki hacmi yok saymasına izin vermek yerine katı malzeme olarak değerlendirir. Katı olması gereken bir modelde parçalar eksik geldiğinde bunu açın. Daha yavaş olan, hassas Boole motorunu kullanmaya zorlar
- **Sarım Sırasını Onar** - Boole işlemi çalışmadan önce her parçanın içi dışa dönük kabuklarının sarımını düzeltir. Bu, sonraki her işlemin neyi katı saydığını değiştirmek yerine geometriyi bir kez onarır ve içi dışa dönük bir modele verilecek iki yanıttan genellikle daha iyi olanıdır

## İpuçları

- Çıkar işleminin bir etki yaratması için nesnelerin çakışması gerekir
- Boydan boya bir delik açmak için kesici nesnenin temeli tamamen geçtiğinden emin olun
- Basit bir delik için [Delik](../../primitives/hole.md) ilkeli zaten çıkarma yapacak şekilde ayarlanmıştır
- Kesici nesneler tasarım ağacında kalır; böylece onları taşıyabilir veya yeniden boyutlandırabilirsiniz ve kesme güncellenir
- Sonuç hatalı görünüyorsa kaynak nesnelerin su geçirmez olduğunu denetleyin. **Sarım Sırasını Onar** içi dışa dönük kabukları düzeltir; [Onar](../mesh/repair.md) ise içe aktarılan modellerdeki daha kapsamlı hasarları giderir

## İlgili

- [Birleştir](combine.md) - Birden fazla nesneyi tek bir katı şekilde birleştirir
- [Kesiştir](intersect.md) - Yalnızca nesnelerin çakıştığı hacmi korur
- [Çıkar ve Değiştir](subtract-and-replace.md) - Bir şekli çıkarır ve kesilip atılan parçayı korur
- [Düzlem Kesme](../reshape/plane-cut.md) - Başka bir şekil yerine düz bir düzlemle keser
- [Delik](../../primitives/hole.md) - Çıkarma yapacak şekilde önceden yapılandırılmış bir küp
- [Onar](../mesh/repair.md) - Boole işleminden önce hasarlı içe aktarılmış kafesleri düzeltir

Bu sayfa ayrıca, işlemler birleştirilmeden önce kaydedilmiş tasarımlarda hâlâ bulunan eski Çıkar nesnelerini de kapsar. Bunlar tam olarak eskisi gibi çalışmayı sürdürür; yeni tasarımlar, Çıkar işlemi seçili olarak ortak Boole nesnesini kullanır.
