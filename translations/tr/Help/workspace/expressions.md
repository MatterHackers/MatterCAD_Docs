---
title: İfadeler
parent: "Workspace"
nav_order: 2
source_hash: 79a2f2c42d81f7fca56a87ad89f69e4303ed0ae5
source_lang: en
---
# İfadeler

MatterCAD'deki birçok parametre, düz sayılar yerine matematiksel ifadeler kabul eder. Bu, bir değeri değiştirdiğinizde ilgili ölçülerin otomatik olarak güncellendiği parametrik tasarıma olanak tanır.

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)


## Nasıl Kullanılır

Bir parametre alanına düz sayı yazmak yerine matematiksel bir ifade yazabilirsiniz. Örneğin:

- `20 + 5` ifadesi 25 olarak hesaplanır
- `pi * 10` ifadesi 31,416 olarak hesaplanır
- `width * 2` ifadesi "width" adlı başka bir parametreye başvurur

## Kullanılabilir Sabitler

- **pi** - 3,14159... (çevrenin çapa oranı)
- **tau** - 6,28318... (2 * pi, radyan cinsinden tam bir tur)

## Desteklenen İşlemler

- Toplama: `+`
- Çıkarma: `-`
- Çarpma: `*`
- Bölme: `/`
- Parantezler: gruplama için `(` ve `)`

## İpuçları

- İfadeler, kodda `DoubleOrExpression`, `IntOrExpression` veya `StringOrExpression` gösteren her alanda desteklenir -- pratikte tasarım araçlarındaki çoğu sayısal alan bunları kabul eder
- Parametreler arasında ilişkiler kurmak için ifadeleri kullanın -- örneğin, bir deliğin çapını `outer_diameter - 4` olarak ayarlayın, böylece her zaman 2 mm duvarı olsun
- Başvurulan değerler değiştiğinde ifadeler otomatik olarak güncellenir
- Birden fazla nesnenin aynı adlandırılmış değerleri veya formülleri paylaşması gerektiğinde [Değişken Sayfası](variable-sheet.md) kullanın
- Parametrik desenler oluşturmak için [Dizi](../operations/array/index.md) işlemlerinde ifadeleri kullanabilirsiniz

## İlgili

- [Bileşenler](components.md) - Yeniden kullanılabilir parametrik tasarımlar oluşturun
- [Değişken Sayfası](variable-sheet.md) - Bir tasarım için paylaşılan değerleri ve formülleri saklayın
- [Nesneleri Düzenleme](../getting-started/editing-objects.md) - Nesne parametreleriyle çalışma
