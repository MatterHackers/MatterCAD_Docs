---
title: Dişler
articleKey: ThreadsObject3D_2
parent: "Mechanical Parts"
nav_order: 3
source_hash: 7d881b3293a508e102d3a4b845cdfd4eb9c34fa8
source_lang: en
---
# Dişler

Yapılandırılabilir çap, adım ve diş profiline sahip vida dişleri oluşturun. Dişler bağımsız cıvata/vida olarak kullanılabilir veya dişli delikler oluşturmak için diğer nesnelerden çıkarılabilir.

<!-- AUTO_IMAGE: type=from_thumbnail item=threads file=mechanical_threads -->
![mechanical_threads](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_threads.png)

## Nasıl Kullanılır

1. Mekanik araçlarından veya İlkeller panelinden **Dişler** ekleyin
2. Çapı, adımı ve döndürme sayısını ayarlayın
3. İsteğe bağlı olarak dişli delikler oluşturmak için "Delik Olarak Kullan" seçeneğini etkinleştirin

## Parametreler

### Kullanım

- **Delik Olarak Kullan** - Etkinleştirildiğinde, dişler çıkarılan bir delik olarak kullanılmak üzere ek toleransla boyutlandırılır (varsayılan: kapalı)
- **Tolerans** - Delik olarak kullanıldığında geçme için ek boşluk (varsayılan: 0.2mm, Delik Olarak Kullan açıkken görünür)

### Öznitelikler

- **Çap** - Dişli bölümün dış çapı (varsayılan: 10mm)
- **Adım** - Her diş turu arasındaki mesafe (varsayılan: 2mm). Daha küçük adım = daha ince dişler
- **Diş Ölçeği** - Dişlerin genişliğinin adıma oranı (varsayılan: 1.0, aralık: 0.1-1.0)
- **Döndürmeler** - Tam diş turu sayısı (varsayılan: 10)

### Geometri

- **Kenarlar** - Çevre boyunca segment sayısı (varsayılan: 40). Daha fazlası = daha pürüzsüz

### Uçlar (Diş Uçları)

- **Uç Ölçeği** - Diş uçlarının ne kadar konikleştirileceği (varsayılan: 0, aralık: 0-1). Uçlarda konik bir giriş oluşturmak için 0'ın üzerine ayarlayın
- **Uç Açısı** - Uçların konikleştirileceği açı (varsayılan: 90 derece)

## İpuçları

- Dişli bir delik oluşturmak için: "Delik Olarak Kullan" seçeneğini etkinleştirin, dişleri konumlandırın ve nesnenizden [Çıkar](../operations/boolean/subtract.md) işlemini uygulayın
- Yazdırılan parçaların birbirine oturmasını sağlamak için delik olarak kullanırken Tolerans ekleyin
- Standart metrik diş adımları: M3=0.5mm, M4=0.7mm, M5=0.8mm, M6=1.0mm, M8=1.25mm, M10=1.5mm
- Dişlemeye başlamayı kolaylaştıran bir giriş oluşturmak için Uç Ölçeği'ni kullanın

## İlgili

- [Dişliler](gears.md) - Mekanik dişli şekilleri oluşturun
- [Silindir](../primitives/cylinder.md) - Düz yuvarlak bir sütun (diş yok)
- [Çıkar](../operations/boolean/subtract.md) - Delikler oluşturmak için diğer nesnelerden dişleri kesin
