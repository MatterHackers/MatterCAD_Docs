---
title: Mevcut Nesneleri Ekleme
parent: "Getting Started"
nav_order: 1
source_hash: e384a5c024336c3c58343d262d914fa40e0b0426
source_lang: en
---
# Mevcut Nesneleri Ekleme

Bilgisayarınızdan dosya içe aktararak veya yerleşik kitaplıktan içerik ekleyerek mevcut 3D modelleri MatterCAD'e getirebilirsiniz.

## Bilgisayarınızdan

![20260324 081143 paste 20260324 081143](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081143-paste-20260324-081143.jpg)

![20260324 081240 paste 20260324 081240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081240-paste-20260324-081240.jpg)


Bilgisayarınızdaki dosyalara göz atmak ve bunları eklemek için araç çubuğundaki **Aç** düğmesine tıklayın. MatterCAD aşağıdaki içe aktarma biçimlerini destekler:

- **STL** (.stl) - Endüstri standardı 3D model biçimi, 3D baskıda yaygın olarak kullanılır
- **AMF** (.amf) - Renkleri ve çok malzemeli nesneleri destekleyen gelişmiş biçim
- **OBJ** (.obj) - Wavefront 3D grafik biçimi (yalnızca ağ geometrisi)
- **3MF** (.3mf) - Zengin meta veri desteğine sahip 3D Üretim Biçimi
- **MCX** (.mcx) - Tüm tasarım verilerini ve parametrelerini koruyan, MatterCAD'in yerel biçimi
- **SVG** (.svg) - Ölçeklenebilir Vektör Grafikleri, 2D yollar olarak içe aktarılır
- **TTF / OTF** (.ttf, .otf) - **Metin** aracıyla kullanılacak yazı tipi dosyaları

## Sürükle ve Bırak

Ayrıca dosyaları doğrudan masaüstünüzden veya dosya gezgininizden MatterCAD çalışma alanına sürükleyip bırakabilirsiniz. Desteklenen dosya türleri otomatik olarak içe aktarılır.

![20260324 081416 paste 20260324 081416](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081416-paste-20260324-081416.jpg)

## Kitaplıktan

### Kitaplık Kenar Çubuğu

Kitaplık tarayıcısı panelini açmak için araç çubuğundaki **İçerik Ekle** düğmesine tıklayın. Buradan şunları yapabilirsiniz:

- Kaydedilmiş tasarımlarınıza göz atma
- Yerleşik şekiller için İlkeller kitaplığına gitme
- Oturum açtıysanız Bulut Kitaplığınıza erişme
- Kitaplıktaki herhangi bir öğeyi doğrudan çalışma alanınıza sürükleyip bırakma

![20260324 081446 paste 20260324 081446](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081446-paste-20260324-081446.jpg)

### Kitaplık Sekmesi

Koleksiyonlarınıza göz atmak için Kitaplık sekmesini de kullanabilirsiniz. Kitaplıktaki herhangi bir nesneye sağ tıklayın ve geçerli tasarım çalışma alanınıza aktarmak için **Sahneye Ekle** seçeneğini belirleyin.

![20260324 081536 paste 20260324 081536](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081536-paste-20260324-081536.jpg)

## İpuçları

- Tüm parametreleri ve tasarım ağacını koruduğu için, tasarımları daha sonra yeniden düzenlemek üzere en iyi biçim MCX'tir
- STL dosyaları yalnızca ağ geometrisi içerir. Bir STL dosyasını içe aktarırsanız yine de üzerinde işlemler uygulayabilirsiniz, ancak özgün parametreleri düzenleyemezsiniz
- Birden çok dosyayı içe aktardığınızda her biri sahnenizde ayrı bir nesne olur. Bunları düzenlemek için [Grupla](../workspace/grouping.md) komutunu kullanın

## İlgili

- [Yeni Nesneler Oluşturma](creating-new-objects.md) - İlkellerle sıfırdan bir tasarıma başlayın
- [Kaydediliyor ve Dışa aktarılıyor](saving-and-exporting.md) - Tamamlanmış tasarımlarınızı kaydedin ve dışa aktarın
- [Kitaplık](../library/index.md) - Tasarım kitaplığınızı düzenleme hakkında daha fazla bilgi edinin
