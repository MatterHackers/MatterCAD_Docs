---
title: Kesiştir
articleKey: IntersectionObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b997cfc4f6d2f02559346365311f217388a6a2da
source_lang: en
---
# Kesiştir

Kesiştir, yalnızca tüm nesnelerin paylaştığı hacmi korur ve geri kalanını atar.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->
![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)

[Birleştir](combine.md), [Çıkar](subtract.md), Kesiştir ve [Çıkar ve Değiştir](subtract-and-replace.md) işlemlerinin tümü tek bir Boole nesnesi tarafından gerçekleştirilir -- araç çubuğu düğmesi bu nesneyi Kesiştir zaten seçili olarak oluşturur ve Özellikler panelinin üst kısmındaki **İşlem** simge sırasından istediğiniz zaman diğer üç işlemden birine geçebilirsiniz.

Kesiştir hem katılar hem de 2B yollar üzerinde çalışır. Kendisine verdiğinize bakar ve doğru türde işlemi uygular; böylece iki yolun kesiştirilmesi tek bir yol, iki ağın kesiştirilmesi ise tek bir katı üretir.

## Nasıl Kullanılır

1. İki veya daha fazla nesne seçin
2. Araç çubuğunda **Kesiştir** düğmesine tıklayın
3. Özellikler panelinin üst kısmındaki **İşlem** sırasında farklı bir simgeye tıklayarak istediğiniz zaman fikrinizi değiştirin -- şekil yeni işleme göre yeniden oluşturulur

## Parametreler

- **İşlem** - Hangi Boole işleminin uygulanacağı. Panelin üst kısmında bir simge sırası olarak gösterilir
- **İçi Dışa Dönük Geometriyi Koru** - İçi dışa dönük bir kabuğu, çevresindeki hacmi yok etmesine izin vermek yerine katı malzeme olarak değerlendirir. Katı olması gereken bir modelde parçalar eksik geldiğinde bunu açın. Daha yavaş olan, tam Boole motorunu kullanmaya zorlar
- **Sarım Sırasını Onar** - Boole işlemi çalışmadan önce her parçanın içi dışa dönük kabuklarını yeniden sarar. Bu, sonraki her işlemin neyi katı saydığını değiştirmek yerine geometriyi bir kez düzeltir ve içi dışa dönük bir model için genellikle iki çözümden daha iyi olanıdır

## İpuçları

- Nesnelerin üst üste binmesi gerekir. Gerçekten üst üste binmiyorlarsa sonuç boş olur
- İkiden fazla nesnede liste boyunca ilerler: önce ilk ikisi kesiştirilir, sonra bu sonuç üçüncüyle kesiştirilir ve bu böyle devam eder
- Bir sonuç yanlış görünüyorsa, kaynak nesnelerin su geçirmez olup olmadığını denetleyin. **Sarım Sırasını Onar** içi dışa dönük kabukları düzeltir; [Onar](../mesh/repair.md) ise içe aktarılan modellerdeki daha kapsamlı hasarları giderir

## İlgili

- [Birleştir](combine.md) - Birden fazla nesneyi tek bir katı şekilde birleştirin
- [Çıkar](subtract.md) - Bir şekli diğerinin içinden kesip çıkarın
- [Çıkar ve Değiştir](subtract-and-replace.md) - Bir şekli çıkarın ve kesilip alınan parçayı koruyun
- [Düzlem Kesme](../reshape/plane-cut.md) - Başka bir şekil yerine düz bir düzlemle kesin
- [Onar](../mesh/repair.md) - Boole işleminden önce hasarlı içe aktarılmış ağları düzeltin

Bu sayfa ayrıca, işlemler birleştirilmeden önce kaydedilmiş tasarımlarda hâlâ bulunan eski Kesişim nesnelerini de kapsar. Bunlar tam olarak eskisi gibi çalışmaya devam eder; yeni tasarımlar, Kesiştir işlemi seçili ortak Boole nesnesini kullanır.
