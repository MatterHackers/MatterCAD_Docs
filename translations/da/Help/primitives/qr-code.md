---
title: QR-kode
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
source_hash: 5b941a39b8430a9536401e4af230c06a42635205
source_lang: en
---
# QR-kode

Generer QR-koder som 3D-objekter. Du kan indkode tekst, URL'er eller WiFi-oplysninger i en scanbar 3D QR-kode.

<!--  Screenshot of a 3D QR Code object on the workspace -->
![20260318 184540 paste 20260318 184540](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184540-paste-20260318-184540.jpg)


## Sådan bruger du den

1. Tilføj en **QR-kode** fra panelet Primitiver
2. Vælg outputtypen (Tekst eller WiFi)
3. Indtast dit indhold
4. QR-koden genereres som et 3D-objekt, du kan placere i dit design

## Parametre

### Tekst-tilstand

- **Tekst** - Teksten eller URL'en, der skal indkodes (standard: "https://matterhackers.com")

### WiFi-tilstand

- **SSID** - WiFi-netværkets navn
- **Adgangskode** - WiFi-adgangskoden
- **Sikkerhed** - Sikkerhedstypen (WEP, WPA eller Ingen)

## Tips

- Brug [Træk fra](../operations/boolean/subtract.md) til at gravere QR-koden ind i en overflade, eller placer den oven på en [Terning](cube.md) som base
- Test, at din QR-kode kan scannes korrekt med en telefon, inden du printer
- WiFi QR-koder lader folk oprette forbindelse til dit netværk ved at scanne koden
- Sørg for, at QR-koden er stor nok til at kunne scannes, når den er printet -- mindst 20-25 mm på tværs

## Relateret

- [Tekst](text.md) - Almindelig 3D-tekst
- [Billedobjekt](image-object.md) - Konverter billeder til 3D
