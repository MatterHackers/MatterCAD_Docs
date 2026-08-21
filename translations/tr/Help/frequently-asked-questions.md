---
title: Sık Sorulan Sorular
nav_order: 101
source_hash: 929ea9e89d3f5008996615341418ba715d3f6075
source_lang: en
---
# Nesnelerimin ölçeği neden yanlış?
- STL dosyaları birim bilgisini saklamaz. MatterCAD, STL ölçülerinin milimetre cinsinden olmasını bekler; oysa çoğu CAD yazılımı kendi yerel birimlerinde (genellikle inç) dışa aktarım yapar. Bu durum, tasarımları içe aktarırken ölçek uyuşmazlıklarına yol açar.

- En iyi çözüm, tasarım yazılımınızı STL dosyalarını milimetre cinsinden dışa aktaracak şekilde yapılandırmaktır. Örneğin SolidWorks'te, STL dışa aktarma parametrelerini ayarlamak için **Farklı Kaydet** iletişim kutusundaki **Seçenekler** düğmesini kullanın.

- Alternatif olarak, parçayı MatterCAD içinde yeniden ölçeklendirebilirsiniz. 3D Görünüm'de **Düzenle** moduna girin ve sağ araç çubuğundan ÖLÇEKLE seçeneğini seçin. Yaygın dönüştürme çarpanları için açılır menüyü kullanın ya da eksen alanlarına belirli ölçüleri girin.

# Uygulama verilerini nasıl temizlerim?

- Yeniden yükleme sorunu çözmüyorsa, MatterCAD'in kayıtlı verilerini silmeniz gerekebilir. Bu veriler, uygulama kaldırıldıktan sonra da kalır. Varsayılan ayarlara tamamen dönmek için uygulama klasörünü kaldırın. Ayarların soruna yol açıp açmadığını test etmek için SQLite veritabanı dosyasını (MatterCAD.db) geçici olarak yeniden adlandırabilirsiniz.
![20260318 194137 paste 20260318 194137](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194137-paste-20260318-194137.jpg)

![20260318 194200 paste 20260318 194200](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194200-paste-20260318-194200.jpg)

![20260318 194218 paste 20260318 194218](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194218-paste-20260318-194218.jpg)


- Windows
  - Kullanıcı kitaplığı ve ayarlar C:\Users\{user}\AppData\Local\MatterCAD konumunda saklanır.
