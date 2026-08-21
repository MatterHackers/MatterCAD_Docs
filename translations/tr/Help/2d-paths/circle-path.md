---
title: Daire Yolu
articleKey: CirclePathObject3D
parent: "2D Paths"
nav_order: 2
source_hash: 587edab627246f47731f9dbde2a13a00dd464807
source_lang: en
---
# Daire Yolu

Dairesel bir 2B yol. Silindir oluşturmak için [Doğrusal Ekstrüzyon](../operations/path/linear-extrude.md) ile, torus benzeri şekiller oluşturmak için [Döndürerek Katılaştır](../operations/path/revolve.md) ile kullanın.

<!-- Screenshot of a Circle Path on the workspace -->
![20260506 080110 paste 20260506 080110](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080110-paste-20260506-080110.jpg)


## Parametreler

- **Çap** - Dairenin çapı (varsayılan: 20mm)
- **Segmentler** - Daireyi oluşturan çizgi segmentlerinin sayısı. Daha fazla = daha pürüzsüz

## İpuçları

- Doğrusal Ekstrüzyon ile birleştirilen bir Daire Yolu, [Silindir](../primitives/cylinder.md) ilkeline benzer bir silindir üretir; ancak üzerine nasıl inşa edeceğiniz konusunda daha fazla esneklik sağlar
- Halka şekilleri oluşturmak için Döndürerek Katılaştır işleminin temeli olarak kullanın

## İlgili

- [Kutu Yolu](box-path.md) - Dikdörtgen bir 2B yol
- [Halka Yolu](ring-path.md) - Delikli bir daire
- [Doğrusal Ekstrüzyon](../operations/path/linear-extrude.md) - Yollara yükseklik kazandırın
