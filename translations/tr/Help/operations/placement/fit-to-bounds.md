---
title: Sınırlara Sığdır
articleKey: FitToBoundsObject3D_4
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 91b9c917cb636f28403c291a4d56f22bf6758b70
source_lang: en
---
# Sınırlara Sığdır

Sınırlara Sığdır, bir nesneyi belirtilen genişlik, derinlik ve yükseklik boyutlarına sığacak şekilde ölçekler. Nesnenin hedef sınırlar içinde nasıl uzatılacağını ve hizalanacağını denetleyebilirsiniz.

<!--  Screenshot showing an object being fit to specific bounding dimensions -->
![20260506 154930 paste 20260506 154930](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154930-paste-20260506-154930.jpg)

## Nasıl Kullanılır

1. Bir nesne seçin
2. Yerleşim menüsünden **Sınırlara Sığdır** işlemini uygulayın
3. Hedef boyutları girin
4. Oran kilitleme ve uzatma davranışını seçin

## Parametreler

- **Oranı Kilitle** - Oranların nasıl sınırlanacağı:
  - **Yok** - Her eksen bağımsız olarak ayarlanabilir
  - **X & Y** - Genişlik ve derinlik birlikte kilitlenir
  - **X, Y & Z** - Tüm eksenlerde eşit ölçekleme
- **Genişlik** - Hedef genişlik (X boyutu)
- **Derinlik** - Hedef derinlik (Y boyutu)
- **Yükseklik** - Hedef yükseklik (Z boyutu)

### Oranı Kilitle, X & Y ya da X, Y & Z olduğunda

- **Uzat** - Nesnenin nasıl sığdırılacağı:
  - **İç** - Tamamen sınırların içine sığacak şekilde küçültür (boşluklar kalabilir)
  - **Genişlet** - Sınırları dolduracak şekilde büyütür (bazı boyutlarda taşabilir)

### Oranı Kilitle, Yok olduğunda

Her eksenin kendine ait şu ayarları vardır:

- **Uzat** - Eksen başına İç veya Genişlet
- **Hizala** - Sınırlar içinde nereye konumlandırılacağı (Min, Merkez, Maks)

## İpuçları

- İçe aktarılan modelleri tam hedef boyutlara yeniden boyutlandırmak için bunu kullanın
- Özgün şekli koruyan eşit ölçekleme için tüm oranları kilitleyin
- Belirli bir genişliğe sığdırmanız gerektiğinde ancak diğer boyutlar önemli olmadığında eksen başına denetimi kullanın

## İlgili

- [Ölçekle](../transform/scale.md) - Hedef boyut yerine oran veya yüzdeyle ölçekleme
- [Silindire Uydur](fit-to-cylinder.md) - Silindirik bir sınır içine sığdırma
- [Hizala](align.md) - Nesneleri birbirine göre konumlandırma
