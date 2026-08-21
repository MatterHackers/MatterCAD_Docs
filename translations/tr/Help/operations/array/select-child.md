---
title: Alt Öğe Seç
articleKey: SelectChildObject3D
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: f6f71d2b457b82126f272ea9354f877c36570df0
source_lang: en
---
# Alt Öğe Seç

Alt Öğe Seç, bir nesne grubundan bir dizin numarasına veya bir ada göre tek bir alt öğe seçer. Bu, hangi nesnenin görüntüleneceğini dinamik olarak belirlemek istediğiniz betik tabanlı ve parametrik tasarımlarda özellikle kullanışlıdır.

<!-- IMAGE: Screenshot showing Select Child operation with multiple children and one selected by index -->
![20260506 080526 paste 20260506 080526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080526-paste-20260506-080526.jpg)


## Nasıl Kullanılır

1. İki veya daha fazla nesne seçin
2. Çoğaltma menüsünden **Alt Öğe Seç** işlemini uygulayın
3. Alt öğenin nasıl seçileceğini denetlemek için **Dizine Göre** veya **Ada Göre** seçeneğini belirleyin
4. Eşleştirilecek dizin numarasını veya adı ayarlayın

## Parametreler

- **Seçim Yöntemi** - **Dizine Göre** (konuma göre seçim) ile **Ada Göre** (nesne adına göre seçim) arasında seçim yapın. Düğmeler olarak görüntülenir.
- **Alt Dizini** - Seçilecek alt öğenin sıfır tabanlı dizini (Dizine Göre kullanılırken gösterilir). [İfadeleri](../../workspace/expressions.md) destekler.
- **Alt Adı** - Seçilecek alt öğenin adı (Ada Göre kullanılırken gösterilir). [İfadeleri](../../workspace/expressions.md) destekler.

Dizin aralık dışındaysa veya ad hiçbir alt öğeyle eşleşmiyorsa, yedek olarak ilk alt öğe döndürülür. Hiç alt öğe yoksa hiçbir şey döndürülmez.

## Betik Yazma İçinde Kullanım

Alt Öğe Seç, dinamik ve veriye dayalı tasarımlar oluşturmak için ifadelerle ve `rand()` işleviyle birlikte çalışacak şekilde tasarlanmıştır. Örneğin, alt öğe olarak birkaç varyant nesne içeren bir sahne oluşturabilir ve rastgele birini seçmek için dizin tohumu olarak `rand(42)` gibi bir ifade kullanabilirsiniz.

**Örnek: Bir sahne gösterisi için rastgele kitap aksesuarları**

1. 5 farklı kitap kafesini bir Alt Öğe Seç işleminin alt öğeleri olarak içe aktarın
2. Seçim Yöntemi'ni **Dizine Göre** olarak ayarlayın
3. Alt Dizini için, `seed` bir sayfa değişkeni olmak üzere `floor(rand(seed) * 5)` gibi bir ifade kullanın
4. Alt Öğe Seç işlemini, her biri farklı bir tohum değerine sahip olacak şekilde birden çok kez çoğaltın
5. Her örnek, kümeden rastgele farklı bir kitap seçer

Bu yöntem, bir varyant kümesinden seçim yapmanız gereken her senaryoda işe yarar: mobilyalar, süslemeler, mimari öğeler veya birbirinin yerine geçebilen herhangi bir parça koleksiyonu.

## İpuçları

- Her kopyanın farklı bir alt öğe seçtiği çeşitlendirilmiş desenler oluşturmak için [Dizi](array.md) ile birleştirin
- Seçimi bir elektronik tablodan yönlendirmek için dizin veya ad olarak sayfa değişkenlerini kullanın
- İlk alt öğeye geri dönme davranışı sayesinde, dizin veya ad yanlış olsa bile tasarımınız asla bozulmaz

## İlgili

- [Dizi](array.md) - Nesneleri doğrusal, dairesel, eğri ve dönüşüm desenlerinde çoğaltın
