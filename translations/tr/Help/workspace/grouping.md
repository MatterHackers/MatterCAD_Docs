---
title: Grupla
parent: "Workspace"
nav_order: 3
source_hash: 82b506a886e270535b5bd58c3913f49328abc4d5
source_lang: en
---
# Grupla

Gruplama, birden fazla nesneyi taşınabilen, kopyalanabilen ve tek bir nesne gibi işlem görebilen tek bir birim halinde birleştirir. [Birleştir](../operations/boolean/combine.md) işleminden farklı olarak gruplama geometriyi kaynaştırmaz -- her nesne grubun içinde ayrı kalır.

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
![20260318 193104 paste 20260318 193104](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193104-paste-20260318-193104.jpg)

![20260318 193235 paste 20260318 193235](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193235-paste-20260318-193235.jpg)

![20260318 193138 paste 20260318 193138](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193138-paste-20260318-193138.jpg)


## Nasıl Kullanılır

### Nesneleri Gruplama

1. İki veya daha fazla nesne seçin (çoklu seçim için Shift-tıklama veya Ctrl-tıklama yapın)
2. Araç çubuğundaki **Grupla** düğmesine tıklayın
3. Nesneler artık gruplanmıştır -- tek bir birim olarak birlikte hareket ederler

### Nesnelerin Grubunu Çözme

1. Bir grup seçin
2. Araç çubuğundaki **Grubu Çöz** düğmesine tıklayın
3. ![20260318 193354 paste 20260318 193354](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193354-paste-20260318-193354.jpg)
4. Tek tek nesneler ayrı öğeler olarak geri getirilir

Grubu çözme işlemi, varsa tek bir içe aktarılmış STL dosyası içindeki birden fazla gövdeyi de ayırmayı dener.

## Grupla ile Birleştir Karşılaştırması

| Özellik | Grupla | Birleştir |
|---------|-------|---------|
| Nesneler ayrı kalır | Evet | Hayır |
| Daha sonra grubu çözülebilir | Evet | Hayır (geri alınamaz) |
| Üst üste binen geometriyi kaynaştırır | Hayır | Evet |
| Nesneler farklı renklere sahip olabilir | Evet | Renkler yüzey bazında korunur |
| Kullanım amacı | Düzenleme ve hareket ettirme | Tek parça katı şekiller oluşturma |

## İpuçları

- Gruplar iç içe olabilir -- halihazırda gruplar içinde bulunan nesneleri de gruplayabilirsiniz
- Bir grup seçin ve içindeki tek tek nesneleri görmek ve seçmek için Tasarım Ağacı'na bakın
- Gruplama geri alınabilir bir işlemdir ve her zaman **Grubu Çöz** ile tersine çevrilebilir

## İlgili Konular

- [Birleştir](../operations/boolean/combine.md) - Nesneleri gruplamak yerine tek bir katı parçada birleştirin
- [Seçim](selection.md) - Gruplamak için birden fazla nesnenin nasıl seçileceği
- [Bileşenler](components.md) - Yeniden kullanılabilir parametreli gruplar oluşturun
