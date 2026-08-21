---
title: Çıkar ve Değiştir
articleKey: SubtractAndReplaceObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c1698bab75faca8046b23cc148803c8063ba0678
source_lang: en
---
# Çıkar ve Değiştir

Çıkar ve Değiştir, seçtiğiniz parçaları seçmediğiniz parçalardan çıkarır; ancak kesilip alınan kısmı atmak yerine kendi başına bir parça olarak korur. Kesici şekilleri seçmek için **Çıkarılacak Parça(lar)** seçeneğini kullanın; geri kalan her şey kesilen taban olur.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->
![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)

[Birleştir](combine.md), [Çıkar](subtract.md), [Kesiştir](intersect.md) ve Çıkar ve Değiştir işlemlerinin tümü tek bir Boolean nesnesi tarafından gerçekleştirilir -- araç çubuğu düğmesi bu nesneyi Çıkar ve Değiştir seçili olarak oluşturur ve Özellikler panelinin üst kısmındaki **İşlem** simge sırasından istediğiniz zaman diğer üç işlemden birine geçebilirsiniz.

Çıkar ve Değiştir 2B yollar için sunulmaz -- bir bölgenin geri verilecek kaldırılmış hacmi yoktur.

## Nasıl Kullanılır

1. İki veya daha fazla nesne seçin
2. Araç çubuğunda **Çıkar ve Değiştir** düğmesine tıklayın
3. Hangi alt nesnelerin kesici şekiller olacağını belirlemek için **Çıkarılacak Parça(lar)** seçeneğini kullanın
4. Özellikler panelinin üst kısmındaki **İşlem** sırasında farklı bir simgeye tıklayarak fikrinizi istediğiniz zaman değiştirin -- şekil yeni işlemle yeniden oluşturulur

## Parametreler

- **İşlem** - Hangi boolean işleminin gerçekleştirileceği. Panelin üst kısmında bir simge sırası olarak gösterilir
- **Çıkarılacak Parça(lar)** - Hangi alt nesnelerin kesici şekiller olduğu
- **İçi Dışa Dönük Geometriyi Koru** - İçi dışa dönük bir kabuğu, çevresindeki hacmi yok saymasına izin vermek yerine katı malzeme olarak değerlendirir. Katı olması gereken bir modelde parçalar eksik geldiğinde bunu açın. Daha yavaş olan kesin boolean motorunu zorunlu kılar
- **Sarım Sırasını Onar** - Boolean işlemi çalışmadan önce her parçanın içi dışa dönük kabuklarını yeniden sarar. Bu, sonraki her işlemin neyi katı saydığını değiştirmek yerine geometriyi bir kez düzeltir ve içi dışa dönük bir model için genellikle iki çözümden daha iyi olanıdır

## İpuçları

- İki parça birbirine tam olarak oturur, çünkü aynı işlemden çıkmışlardır
- Çok renkli tasarımlar, iç içe geçen montajlar ve kakmalar için kullanın
- Sonuç yanlış görünüyorsa, kaynak nesnelerin su geçirmez olduğunu denetleyin. **Sarım Sırasını Onar** içi dışa dönük kabukları düzeltir; [Onar](../mesh/repair.md) ise içe aktarılan modellerdeki daha kapsamlı hasarları giderir

## İlgili

- [Birleştir](combine.md) - Birden fazla nesneyi tek bir katı şekilde birleştirin
- [Çıkar](subtract.md) - Bir şekli bir diğerinden kesip çıkarın
- [Kesiştir](intersect.md) - Yalnızca nesnelerin çakıştığı hacmi koruyun
- [Düzlem Kesme](../reshape/plane-cut.md) - Başka bir şekil yerine düz bir düzlemle kesin
- [Onar](../mesh/repair.md) - Boolean işleminden önce hasarlı içe aktarılmış ağları düzeltin

Bu sayfa, işlemler birleştirilmeden önce kaydedilmiş tasarımlarda hâlâ bulunan eski Çıkar ve Değiştir nesnelerini de kapsar. Bunlar tam olarak eskisi gibi çalışmaya devam eder; yeni tasarımlar ise Çıkar ve Değiştir işlemi seçili ortak Boolean nesnesini kullanır.
