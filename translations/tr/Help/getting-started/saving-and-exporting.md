---
title: Kaydediliyor ve Dışa aktarılıyor
parent: "Getting Started"
nav_order: 4
source_hash: 020d4bf43f07d3ab7dbd7d585e13c99309f0c0b8
source_lang: en
---
# Kaydediliyor ve Dışa aktarılıyor

MatterCAD, tasarımlarınızı kaydetmek ve dışa aktarmak için birkaç dosya biçimini destekler. Seçeceğiniz biçim, dosyayı nasıl kullanmayı planladığınıza bağlıdır.

## Kaydetme Biçimleri

### MCX (Yerel Biçim)

MCX, MatterCAD'in yerel dosya biçimidir ve daha sonra düzenlemeye devam etmek istediğiniz tasarımlar için en iyi seçimdir. Şunları korur:

- Tüm nesneleri ve hiyerarşilerini içeren eksiksiz tasarım ağacı
- Her nesneye ait tüm parametreler ve ayarlar
- Boole işlemleri, diziler ve diğer işlemler düzenlenebilir biçimde
- Bileşen ilişkileri

**MCX'i şu durumda kullanın:** Çalışmanızı kaydedip daha sonra düzenlemeye devam etmek istediğinizde.

### STL

STL, 3D baskı için en yaygın kullanılan biçimdir. Yalnızca son üçgen kafes geometrisini içerir; herhangi bir tasarım geçmişi veya parametre barındırmaz.

**STL'i şu durumda kullanın:** Tasarımınızın 3D baskısını almak veya MatterCAD kullanmayan biriyle paylaşmak istediğinizde.

### OBJ

OBJ (Wavefront), çoğu 3D yazılım tarafından desteklenen yaygın bir 3D biçimidir. STL gibi yalnızca kafes geometrisi içerir.

**OBJ'yi şu durumda kullanın:** Tasarımınızı Blender gibi başka bir 3D yazılımda veya bir oyun motorunda açmanız gerektiğinde.

### SVG

SVG dışa aktarımı, tasarımınızın üstten görünümünden 2D bir vektör dosyası oluşturur. Bu, lazer kesim veya CNC frezeleme için kullanışlıdır.

**SVG'yi şu durumda kullanın:** Lazer kesim veya gravür için tasarımınızın 2D dış hattına ihtiyaç duyduğunuzda.

## Nasıl Kaydedilir

![20260324 080726 paste 20260324 080726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080726-paste-20260324-080726.jpg)

1. **marka menüsünü** açın (sol üst köşedeki MatterCAD logosu)
2. Bir konum ve biçim seçmek için **Farklı Kaydet** seçeneğini seçin
3. Biçim açılır listesinden dosya biçimini seçin
4. Dosyanın kaydedileceği yeri seçin ve **Kaydet** düğmesine tıklayın

Tasarımınız siz çalışırken otomatik olarak da kaydedilir; böylece uygulamayı kapatsanız bile değişiklikleriniz kaybolmaz.

## İpuçları

- Daha sonra değişiklik yapabilmek için tasarımınızı STL veya OBJ olarak dışa aktarmadan önce her zaman bir MCX kopyasını kaydedin
- STL olarak dışa aktarırken sahnedeki tüm nesneler tek bir kafeste birleştirilir
- Bir tasarımı MatterCAD kullanan biriyle paylaşmanız gerekiyorsa, tam düzenlenebilirliği korumak için MCX dosyasını gönderin
- Ayrıca tasarımlarınızı, herhangi bir bilgisayardan erişebilmek için [Bulut Kitaplığı](../library/cloud-library.md) konumuna kaydedebilirsiniz

## İlgili

- [Mevcut Nesneleri Ekleme](adding-existing-objects.md) - Dosyaları MatterCAD'e içe aktarın
- [Kitaplık](../library/index.md) - Kaydettiğiniz tasarımları düzenleyin
- [Bulut Kitaplığı](../library/cloud-library.md) - Tasarımları bulutta saklayın
