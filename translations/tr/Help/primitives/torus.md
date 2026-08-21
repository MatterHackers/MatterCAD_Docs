---
title: Simit
articleKey: TorusObject3D
parent: "Primitives"
nav_order: 17
source_hash: aaec1652de4d6713bd01a707964cf4985d3fb5f6
source_lang: en
---
# Simit

Genel boyut ve halka kesitinin kalınlığı üzerinde bağımsız denetim sunan, çörek biçimli bir halka.

<!--  Screenshot of a Torus primitive on the workspace -->
![20260318 184240 paste 20260318 184240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184240-paste-20260318-184240.jpg)


## Parametreler

- **Dış Çap** - Simidin uçtan uca toplam genişliği (varsayılan: 20mm)
- **İç Çap** - Ortadaki deliğin çapı (varsayılan: 10mm)
- **Kenarlar** - Ana halka çevresindeki bölüt sayısı (varsayılan: 40)

### Gelişmiş Parametreler

Ek denetimler için **Gelişmiş** modunu etkinleştirin:

- **Başlangıç Açısı** - Simidin başladığı açı (varsayılan: 0)
- **Bitiş Açısı** - Simidin bittiği açı (varsayılan: 360). Açık bir halka veya yay için 360'tan küçük bir değer verin
- **Halka Kenar Sayısı** - Halkanın kesiti çevresindeki bölüt sayısı (varsayılan: 15). Daha fazlası = daha pürüzsüz boru profili
- **Halka Faz Açısı** - Kesit profilini döndürür (varsayılan: 0)

## İpuçları

- Halka borusunun kalınlığı, Dış Çap ile İç Çap arasındaki farkla belirlenir
- Açık halka bölütleri, yaylar veya C biçimleri oluşturmak için Başlangıç Açısı ve Bitiş Açısı değerlerini kullanın
- O-ringler, tutamaklar, dekoratif halkalar ve boru dirsekleri oluşturmak için kullanışlıdır

## İlgili

- [Halka](ring.md) - Düz duvarlı içi boş bir silindir (boru)
- [Küre](sphere.md) - Dolu bir top biçimi
- [Yarım Küre](half-sphere.md) - Kubbe biçimi
