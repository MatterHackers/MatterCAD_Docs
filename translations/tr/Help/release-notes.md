---
title: Sürüm Notları
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8 (13 Ağustos 2026)
[Windows İndirme](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## Yeni Özellikler

* **Alt Öğeleri Düzenle**
  * Tablada veya Sahne Ağacında bir nesneye çift tıklayarak içine girin ve nesnenin oluşturulduğu parçaları düzenleyin — ayrı bir pencere ya da sekme yok
  * Çıkar gibi işlemlerde kaynak parçaları düzenlersiniz ve dışarı çıktığınızda sonuç yeniden oluşturulur
  * Sahne Ağacının üst kısmındaki gezinti yolu tam yolu gösterir; bir düzeye tıklamak düzenlemelerinizi geri alınabilir tek bir adım olarak katlar ve her düzey kendi geri alma geçmişini tutar
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **Tek Bir Boole Aracı**
  * Birleştir, Çıkar, Kesiştir ve Çıkar ve Değiştir artık panelinin üst kısmında bir simge sırası bulunan tek bir işlemdir — silip yeniden uygulamak yerine tek tıklamayla mod değiştirin
  * Aynı işlem hem 3D ağları hem de 2D yolları işler ve ağır bir boole işlemi çalışırken ilerlemeyi gösterir
  * Eski, ayrı boole nesneleriyle kaydedilmiş tasarımlar normal şekilde açılmaya devam eder
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **Sorunsuz Çalışan Boole İşlemleri**
  * Boole işlemleri, daha hızlı olan ve daha önce başarısız olan ağlarda başarıya ulaşan yeni bir yerel motorda çalışır
  * Birleştir, delikli parçaları otomatik olarak onarır: temiz onarımlar birleşime katılır, güvenli biçimde birleştirilemeyen parçalar yanında tutulur ve sizin için adlandırılır, onarılamayan bir parça ise özgün geometrinizi korur
  * Düzlem Kesme artık gerçek bir katı kesişimidir; böylece sonuç açık bir kabuk yerine su geçirmez ve yazdırılabilir olur
  * Sorunlu içe aktarılmış ağlar için yeni İçi Dışa Dönük Geometriyi Koru ve Sarım Sırasını Onar seçenekleri


## İyileştirmeler

* **2D Yol Düzenleyici**
  * Dört nokta modu — Keskin, Simetrik, Hizalı ve Serbest — hem 2D düzenleyicide hem de 3D görünümde tek tıklamayla uygulanır
  * Aynala artık canlı bir simetri modudur: düzenlemeler siz yaptıkça merkez boyunca aynalanır ve aynalanmış bir çifti eksene sürüklemek onu tek bir noktada birleştirir
  * Noktaları seçim çerçevesiyle sürükleyerek seçin, grup halinde taşıyın, ızgaraya kenetleyin ve sürüklemeyi iptal etmek için Esc tuşuna basın
  * Yumuşat, tıklayarak oluşturduğunuz noktalardan tek adımda bir eğri geçirir
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **Görüntüleme ve Gezinme**
  * Düz bir yol seçiliyken Z tuşuna basarak yola göre ayarlanmış, tam tepeden bakan bir düzenleme görünümüne animasyonla geçin
  * Alt piksel metin işleme, ekranınız desteklediğinde artık otomatik olarak açıktır ve Gelişmiş ayarlar altından yine de açılıp kapatılabilir

* **Modelleme**
  * Doğrusal Ekstrüzyon, alt kenarı kendi stili, yarıçapı ve segment sayısıyla pahlayabilir
  * Yalnızca düzenleyiciye özel nesneler (3D Eğri, Ölçüm Aracı, Açıklama, Sayfa) görüntülenmeye devam eder ancak dışa aktarmaya dahil edilmez

## Öne Çıkan Hata Düzeltmeleri

  * Yarıda başarısız olan bir kaydetme, başarı bildirirken değiştirdiği dosyayı kesebiliyordu. Kaydetmeler artık tamamen tamamlanıyor, ardından hedefi atomik olarak değiştiriyor — aynı koruma kitaplık kayıtlarını ve dışa aktarmaları da kapsıyor
  * Başarısız bir kaydetme, tasarımı kaydedilmemiş olarak işaretli bırakır; böylece uygulamayı kapatmak çalışmanızı sessizce atamaz
  * Bir bulut öğesini diske kaydetmek eski sekme adını koruyor ve yeniden başlatmada sekmeyi kaybediyordu
  * 3MF alt modellerinin yüklemede sessizce atlanması ve aynı anda yüklenen 3MF dosyalarının birbirini bozması düzeltildi
  * Çökmeler, bozuk histogram filtresi ve bir görüntü parçasının kopyalarının orijinaliyle eşitlenmemesi düzeltildi
  * Bir eğri noktası silinirken oluşan çökme ve kapalı bir yolun dikiş noktasındaki noktaların seçtiğiniz modu geri alması düzeltildi
  * Çalışan bir görevdeki Durdur düğmesi artık tıklanabilir ve gerçekten iptal ediyor

---

# MatterCAD 2.2026.5 (8 Mayıs 2026)
[Windows İndirme](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## Yeni Özellikler

* **Yeniden Tasarlanan Dizi Aracı**
  * Tek ve birleşik Dizi işlemi, eski Doğrusal Dizi, Dairesel Dizi ve Gelişmiş Dizi araçlarının yerini alır
  * **Doğrusal** modu: isteğe bağlı döndürme ve kademeli ölçekle bir yön boyunca kopyalar
  * **Radyal** modu: yapılandırılabilir yarıçap, süpürme açısı ve yay veya tam daire desenleriyle merkezi bir eksen etrafında kopyalar
  * **Dönüştür** modu: manuel bir dönüşümü veya adlandırılmış bir kardeş nesnenin dönüşümünü kullanarak adım adım kopyalar
  * Doğrusal modundaki Birleştirme döndürme modu; spiralleri, yelpazeleri ve helisleri doğal biçimde oluşturur
  * Nautilus kabuğu ve geometrik dizi düzenleri için Ölçek Ofseti Etkiler seçeneği
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **Kitaplık Favorileri**
  * Herhangi bir kitaplık öğesini yıldızlayarak kalıcı bir Favoriler klasörüne ekleyin
  * En çok kullandığınız temel şekillere, üreticilere ve kaydedilmiş parçalara tek bir yerden hızla erişin
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## İyileştirmeler

* **Hizala**
  * Yığılmış hizalama artık açılır menü seçeneği yerine doğrudan bir mod düğmesidir
  * Kenarları hizalamak, hassas boşluklar eklemek ve düzenli yığınlar oluşturmak için daha anlaşılır Basit, Kaydırma ve Yığılmış modları eklendi
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **Dosya Desteği**
  * Görüntü tabanlı işlemlerde WEBP görüntü biçimi desteği eklendi
  * Daha güvenilir içe aktarmalar için SVG dosyası ayrıştırma iyileştirildi

* **Güvenilirlik**
  * 3MF dosyası yükleme hızı ve güvenilirliği iyileştirildi
  * Oturumlar arasında daha iyi sekme geri yükleme

## Öne Çıkan Hata Düzeltmeleri

* **Oturum Açma ve Bulut Kitaplığı Erişimi**
  * Bir arka uç sunucu yükseltmesinin oturum açmayı bozmasının ardından oturum açma ve Bulut Kitaplığı erişimi geri getirildi.
  * MatterCAD, bulut erişimi süresi dolmuş veya geçersiz kimlik bilgileri bulduğunda artık yeniden oturum açmanızı ister.

* **Sahne Ağacı Seçimi**
  * Sahne ağacından nesne seçerken oluşan tutarsız seçim davranışı düzeltildi.

* **Yardımda Gezinme**
  * Uygulamayla birlikte gelen yardım ve sürüm belgelerindeki gezinme sorunları düzeltildi.

* **Kitaplıkta Sağ Tıklama**
  * Kitaplık ağaç görünümündeki sağ tıklama davranışı düzeltildi.

* **Sayfalar**
  * Sayfalarla çalışırken oluşabilen bir çökme düzeltildi.

---

# MatterCAD 2.2026.3 (12 Mart 2026)
[Windows İndirme](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## Yeni Özellikler

* **Tamamen Yeni Direct3D 11 İşleme Motoru**
  * Çok daha iyi performans için OpenGL'den Direct3D 11'e tam geçiş
  * Keskin ve temiz kenarlar için FXAA kenar yumuşatma
  * Doğru, sıradan bağımsız saydamlık için çift derinlik soyma
  * Donanım hızlandırmalı tabla gölgeleri
  * İyileştirilmiş nesne dış hatları ve seçim görselleri
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **Nesne Saydamlığı**
  * Sahnedeki herhangi bir nesne için alfa/saydamlık ayarlayın
  * Yüz başına renkli ağlar, renk bozulması olmadan alfayı destekler
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **Nesneleri Kilitleme ve Gizleme**
  * Yanlışlıkla seçimi veya düzenlemeyi önlemek için nesneleri kilitleyin
  * Belirli parçalar üzerinde çalışırken görsel karmaşayı azaltmak için nesneleri gizleyin
  * Görünürlüğü hızla geri yüklemek için Tümünü Göster ve Tümünün Kilidini Aç komutları
  * Kilitli ve gizli nesneler, ışın tabanlı seçimin dışında doğru şekilde tutulur
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **İyileştirilmiş Boole Çıkar**
  * Çoklu çıkarma işlemleri belirgin biçimde daha güvenilir ve doğru

## İyileştirmeler

* **Dosya İşleme**
  * Projeler artık varsayılan olarak STL yerine 3MF olarak kaydediliyor; renkler, malzemeler ve tasarım geçmişi korunuyor
  * 3D görünüme dosya ve klasör sürükle bırak desteği geliştirildi

* **İş Akışı**
  * Farklı Kaydet ve Taşı iletişim kutuları son klasör konumunuzu hatırlar
  * İfade alanları artık `pi`, `tau`, `e` ve `count` destekler
  * Esc tuşu, tasarım düzenleme bağlamlarında geri alma yapar
  * Fare sahneden ayrıldığında 3D kontroller görünür kalır

* **Performans ve Kararlılık**
  * Başlangıç çökmeleri ve özyinelemeli yükleme sorunları düzeltildi
  * Aydınlatma ve mipmap işleme hataları düzeltildi
  * Kitaplık ağaç görünümü güncellemeleri iyileştirildi
  * Daha iyi yakınlaştırma davranışı için dinamik yakın/uzak düzlem hesaplamaları
  * .NET 10'a yükseltildi

---

# MatterCAD 2.2025.6 (20 Haziran 2025)
[Windows İndirme](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## Yeni Özellikler

* **SVG Dosyası Desteği**  
  * SVG dosyaları için tam sürükle bırak desteği
  * SVG grafiklerinden 3D nesnelere doğrudan dönüştürme
  * Mevcut CAD iş akışlarıyla sorunsuz entegrasyon

* **Gelişmiş OBJ Dosyası İşleme**  
  * ZIP arşivlerinden malzeme yükleme desteği
  * Geliştirilmiş OBJ dosyası ayrıştırma ve malzeme işleme
  * Birden çok malzemeli karmaşık 3D modeller için daha iyi destek

* **Geliştirilmiş Sekme Yönetim Sistemi**
  * Bulut Kitaplığı sekmeleri artık doğru şekilde korunuyor - çalışmanız tam olarak bıraktığınız yerde kalır
  * İyileştirilmiş sekme düzeni ve gezinme
  * Oturumlar arasında açık sekmelerin otomatik olarak geri yüklenmesi

## Kullanıcı Deneyimi İyileştirmeleri

* **Sadeleştirilmiş Arayüz**
  * Daha hızlı erişim için yeniden düzenlenen Son Kullanılanlar menüsü
  * Uzun işlemler sırasında daha iyi görsel geri bildirim
  * İyileştirilmiş uygulama başlatma süresi ve yanıt verme hızı

* **Güvenilirlik**
  * 3D sahne etkileşimlerindeki kritik çökmeler düzeltildi
  * Bellek yönetimi sorunları giderildi
  * Tüm platformlarda uygulama kararlılığı iyileştirildi

---

# MatterCAD 2.21.5 (13 Şubat 2025)

[Windows İndirme](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# Mevcut Özellikler

*Aşağıdaki özellikler, MatterCAD'in MatterControl mirasından devraldığı temeli oluşturur:*

* İçi Boş özelliği eklendi  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* Poligon Azalt eklendi  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* Ağ Onar eklendi  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* Yeni manuel destek seçeneğine ek olarak tam otomatik destek (eski destek) bir seçenek olarak eklendi
* gsSlicer desteği eklendi (Deneysel yeni dilimleme motoru)
* Hatalar düzeltildi

## Değişiklikler

* Ağın grubunu çözme (birden çok ağa bölme) iyileştirildi
    * Bozuk yüzler atılır
    * Mikroskobik ayrık özellikler atılır

## Değişiklikler

* Uygulama için arama çubuğu eklendi
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* Tasarım araç çubuğu iyileştirildi
    * Bazı öğelere gruplama eklendi
    * Çift hizalama düğmesi eklendi
    * Tümünü Düzenle düğmesi eklendi
* Tabladaki öğeleri ok tuşlarıyla kaydırın
* İndirilenler klasörü tarihe göre sıralanır

## Değişiklikler

* Arayüz iyileştirmeleri
    * Bulut Kitaplığı klasörlerinde daha hızlı güncellemeler
    * Yeniden açıldığında arayüzü geri yükleme
    * Daha iyi klavyeyle gezinme desteği
* Yeni hata algılama ve uyarı sistemi
    * Daha fazla donanım hatası işleniyor
* Tasarım Araçları iyileştirmeleri ve optimizasyonları
    * Yeni Bükme araçları 
    * İyileştirilmiş Eğri aracı
    * İyileştirilmiş Hizala


## Değişiklikler

* İyileştirilmiş düzleştirme
* İyileştirilmiş geri alma desteği
* İyileştirilmiş tasarım geçmişi

## Değişiklikler
* Sürümleme: (sürüm).(yıl).(ay) sürüm numarasına geçiliyor. Okunması daha kolay ve daha bilgilendirici.
* Yeni, son teknoloji Çıkar, Birleştir ve Kesişim (Yalnızca Windows)
* Yeni kullanıcıların yollarını bulmasına yardımcı olmak için artık bir 'Özellik Turu' ile başlıyoruz

## Değişiklikler
* Tasarım Araçları - Eksiksiz bir modelleme temel şekli setiyle 3D modelleme yeteneği
* Kendi özelleştirilmiş desteklerinizi oluşturmak için bir temel şekil kullanın
* Tasarım Uygulamaları - Tasarım Uygulamaları: gelişmiş, özelleştirilebilir tasarımlar
* 64-bit İşleme
