---
title: QR-kode
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
source_hash: 5b941a39b8430a9536401e4af230c06a42635205
source_lang: en
---
# QR-kode

Generer QR-koder som 3D-objekter. Du kan kode tekst, URL-er eller WiFi-legitimasjon inn i en skannbar 3D QR-kode.

<!--  Screenshot of a 3D QR Code object on the workspace -->
![20260318 184540 paste 20260318 184540](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184540-paste-20260318-184540.jpg)


## Slik bruker du den

1. Legg til en **QR-kode** fra Primitiver-panelet
2. Velg utdatatypen (Tekst eller WiFi)
3. Skriv inn innholdet ditt
4. QR-koden genereres som et 3D-objekt du kan plassere i designet ditt

## Parametere

### Tekstmodus

- **Tekst** – Teksten eller URL-en som skal kodes (standard: «https://matterhackers.com»)

### WiFi-modus

- **SSID** – Navnet på WiFi-nettverket
- **Passord** – WiFi-passordet
- **Sikkerhet** – Sikkerhetstypen (WEP, WPA eller Ingen)

## Tips

- Bruk [Trekk fra](../operations/boolean/subtract.md) for å gravere QR-koden inn i en overflate, eller plasser den oppå en [Kube](cube.md) som base
- Test at QR-koden skannes korrekt med en telefon før du skriver den ut
- WiFi QR-koder lar folk koble seg til nettverket ditt ved å skanne koden
- Pass på at QR-koden er stor nok til å kunne skannes når den er skrevet ut – minst 20–25 mm bred

## Relatert

- [Tekst](text.md) – Standard 3D-tekst
- [Bildeobjekt](image-object.md) – Konverter bilder til 3D
