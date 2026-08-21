---
title: Cod QR
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
source_hash: 5b941a39b8430a9536401e4af230c06a42635205
source_lang: en
---
# Cod QR

Generează coduri QR ca obiecte 3D. Poți codifica text, adrese URL sau date de autentificare WiFi într-un cod QR 3D scanabil.

<!--  Screenshot of a 3D QR Code object on the workspace -->
![20260318 184540 paste 20260318 184540](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184540-paste-20260318-184540.jpg)


## Mod de utilizare

1. Adaugă un **Cod QR** din panoul Primitive
2. Alege tipul de ieșire (Text sau WiFi)
3. Introdu conținutul dorit
4. Codul QR este generat ca obiect 3D pe care îl poți plasa în proiectul tău

## Parametri

### Mod Text

- **Text** - Textul sau adresa URL de codificat (implicit: "https://matterhackers.com")

### Mod WiFi

- **SSID** - Numele rețelei WiFi
- **Parolă** - Parola rețelei WiFi
- **Securitate** - Tipul de securitate (WEP, WPA sau Niciunul)

## Sfaturi

- Folosește [Scădere](../operations/boolean/subtract.md) pentru a grava codul QR într-o suprafață sau plasează-l pe o bază de tip [Cub](cube.md)
- Verifică, înainte de imprimare, că se scanează corect codul QR cu un telefon
- Codurile QR WiFi permit conectarea la rețeaua ta prin simpla scanare a codului
- Asigură-te că, la imprimare, codul QR este suficient de mare pentru a putea fi scanat -- cel puțin 20-25 mm lățime

## Articole conexe

- [Text](text.md) - Text 3D standard
- [Obiect Imagine](image-object.md) - Conversia imaginilor în 3D
