---
title: Hizala
articleKey: AlignObject3D_3
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 1fadae72ba00cb06e36a21f0b96962dcff3f60ad
source_lang: en
---
# Hizala

Hizala, birden fazla nesneyi bir sabit nokta nesnesine göre hassas biçimde konumlandırır. Kenarları hizalamak, parçaları birbirine göre ortalamak, bir nesneyi diğerinin üzerine yerleştirmek veya eşit aralıklı yığınlar oluşturmak için kullanın.

<!--  Screenshot showing two objects being aligned with alignment options visible -->
![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)


## Nasıl Kullanılır

1. İki veya daha fazla nesne seçin.
2. **Yerleşim** menüsünden **Hizala** işlemini uygulayın.
3. **Sabit Nokta** nesnesini seçin. Sabit nokta yerinde kalır, diğer nesneler hareket eder.
4. X, Y ve Z eksenleri için hizalamayı birbirinden bağımsız olarak ayarlayın.
5. Hizalanmış konumları nesne ağacına işlemek istediğinizde **Uygula**'yı kullanın.

## Parametreler

### Sabit Nokta

**Sabit Nokta** listesi, referans olarak kullanılacak alt nesneyi seçer. Sabit nokta hareket etmez. Bir eksen **Yığılmış** modunu kullanmadığı sürece, Hizala işlemindeki diğer tüm alt nesneler sabit noktaya göre yeniden konumlandırılır.

### Eksen Kontrolleri

Her eksenin kendi kontrolleri vardır. Tek bir eksende, iki eksende veya üç eksenin tamamında hizalama yapabilirsiniz. Minimum ve maksimum kenarlar eksene göre adlandırılır:

- **X Ekseni** - Min soldur, Maks sağdır.
- **Y Ekseni** - Min öndür, Maks arkadır.
- **Z Ekseni** - Min alttır, Maks üsttür.

Her eksen için:

- **Hizala** - O eksen için sabit nokta referans noktasını seçer. O eksende konumları değiştirmeden bırakmak için **Yok** seçeneğini kullanın.
- **Mod** - Seçilen hizalamanın nasıl uygulanacağını denetler:
  - **Basit** - Hareket eden her nesnenin karşılık gelen kenarını, merkezini veya orijinini sabit noktayla eşleştirir. Kaydırma kullanılmaz.
  - **Kaydırma** - Hareket eden nesnenin hangi kısmının sabit nokta referansına oturacağını seçin, ardından **Kaydırma** ile aralık ekleyin.
  - **Yığılmış** - Nesneleri o eksen boyunca birbiri ardına yerleştirir; aralarındaki boşluk için **Kaydırma** değerini kullanır.
- **AltHizalama** - **Kaydırma** modunda kullanılabilir. Hareket eden nesnenin sabit nokta referansına yerleştirilecek kısmını seçer. **AltHizalama** **Yok** ise, Hizala **Hizala** ile seçilen aynı kenarı, merkezi veya orijini kullanır.
- **Kaydırma** - **Kaydırma** ve **Yığılmış** modlarında kullanılabilir. O eksen boyunca mesafe ekler ve [ifadeler](../../workspace/expressions.md) destekler.

## Hizalama Modları

### Basit

Benzer konumları birbiriyle eşleştirirken **Basit** modunu kullanın. Örneğin, **X Hizalama: Merkez**, sabit nokta dışındaki her nesneyi X merkezi sabit noktanın X merkeziyle eşleşecek şekilde taşır. **Z Hizalama: Min** ise sabit nokta dışındaki her nesneyi alt yüzeyi sabit noktanın alt yüksekliğinde duracak şekilde taşır.

### Kaydırma

Hareket eden nesnenin kullanılacak kısmı sabit nokta referansından farklı olmalıysa **Kaydırma** modunu kullanın. Örneğin, bir nesneyi sabit noktanın üstüne yerleştirmek için:

1. **Z Hizalama** değerini **Maks** (üst) olarak ayarlayın.
2. **Z Modu** değerini **Kaydırma** olarak ayarlayın.
3. **Z AltHizalama** değerini **Alt** olarak ayarlayın.
4. **Z Ofseti** değerini istediğiniz boşluğa ayarlayın veya doğrudan temas için `0` olarak bırakın.

Bu, hareket eden nesnenin alt kısmını, isteğe bağlı bir aralıkla birlikte sabit noktanın üstüne yerleştirir.

### Yığılmış

Birden fazla nesneyi bir eksen boyunca zincirlemek için **Yığılmış** modunu kullanın. Nesneler önce ada, ardından dahili kimliğe göre işlenir; bu nedenle nesneleri açık biçimde adlandırmak öngörülebilir bir yığın sırası sağlar.

**Yığılmış** modunda, hareket eden her nesne o eksende bir önceki referansa dayanacak şekilde yerleştirilir:

- **Min** hizalaması pozitif yönde yığar; örneğin X'te soldan sağa veya Z'de alttan üste.
- **Maks** hizalaması negatif yönde yığar; örneğin X'te sağdan sola veya Z'de üstten alta.
- **Merkez** ve **Orijin** hizalaması, her nesnenin merkezi veya orijini arasındaki kaydırmayı kullanır.

Nesneler arasındaki boşluğu ayarlamak için **Yığılmış** modunda **Kaydırma** değerini kullanın.

## Örnekler

- **Nesneleri tabla alanında ortalama** - Sabit kalması gereken nesneyi **Sabit Nokta** olarak seçin, ardından **X Hizalama** ve **Y Hizalama** değerlerini **Merkez** yapın.
- **Bir nesneyi diğerinin üstüne yerleştirme** - **Z Hizalama** değerini **Maks** (üst), **Z Modu** değerini **Kaydırma** ve **Z AltHizalama** değerini **Alt** olarak ayarlayın.
- **Bir kenardan hassas bir boşluk ekleme** - **Kaydırma** modunu kullanın, hareket eden nesnenin kenarını **AltHizalama** ile seçin, ardından **Kaydırma** değerini ihtiyacınız olan aralığa ayarlayın.
- **Birkaç nesneyi uç uca dizme** - **X Hizalama** değerini **Min** (sol), **X Modu** değerini **Yığılmış** olarak ayarlayın ve boşluk için **X Ofseti** değerini kullanın.
- **Dikey bir yığın oluşturma** - **Z Hizalama** değerini **Min** (alt), **Z Modu** değerini **Yığılmış** olarak ayarlayın ve nesneler arasındaki boşluk için **Z Ofseti** değerini kullanın.

## İpuçları

- Sabit nokta nesnesi yerinde kalır; diğer nesneler onunla hizalanmak için hareket eder.
- Farklı eksenlerde farklı modlar kullanabilirsiniz; örneğin X'te **Yığılmış**, Y'de ise **Merkez** ve **Basit**.
- Aynı anda birden fazla nesne hizalandığında **Yığılmış** sırasını denetlemek için nesne adlarını kullanın.
- Hizala, uygulanana kadar tahribatsızdır. Alt nesneleri yeniden hizalamak için ayarları istediğiniz zaman değiştirebilirsiniz.
- Sınırlayıcı kutu kenarları yerine modelleme orijinlerini hizalamanız gerektiğinde **Orijin** seçeneğini kullanın.

## İlgili

- [Sınırlara Sığdır](fit-to-bounds.md) - Bir nesneyi belirli ölçülere sığacak şekilde ölçekleyin
- [Öteleme](../transform/translate.md) - Belirli bir mesafe kadar taşıyın
- [Gruplama](../../workspace/grouping.md) - Hizalanmış nesneleri bir arada tutmak için gruplayın
