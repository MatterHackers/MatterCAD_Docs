---
title: QR kód
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
source_hash: 5b941a39b8430a9536401e4af230c06a42635205
source_lang: en
---
# QR kód

Generujte QR kódy jako 3D objekty. Můžete zakódovat text, URL adresy nebo přihlašovací údaje k WiFi do naskenovatelného 3D QR kódu.

<!--  Screenshot of a 3D QR Code object on the workspace -->
![20260318 184540 paste 20260318 184540](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184540-paste-20260318-184540.jpg)


## Jak jej použít

1. Přidejte **QR kód** z panelu Základní tělesa
2. Zvolte typ výstupu (Text nebo WiFi)
3. Zadejte svůj obsah
4. QR kód se vygeneruje jako 3D objekt, který můžete umístit do svého návrhu

## Parametry

### Režim Text

- **Text** – text nebo URL adresa k zakódování (výchozí: „https://matterhackers.com“)

### Režim WiFi

- **SSID** – název WiFi sítě
- **Heslo** – heslo k WiFi
- **Zabezpečení** – typ zabezpečení (WEP, WPA nebo Žádný)

## Tipy

- Pomocí operace [Odečíst](../operations/boolean/subtract.md) vygravírujte QR kód do povrchu, nebo jej umístěte na podstavu z [Kvádr](cube.md)
- Před tiskem vyzkoušejte, zda se váš QR kód správně načte telefonem
- WiFi QR kódy umožňují lidem připojit se k vaší síti naskenováním kódu
- Ujistěte se, že je QR kód dostatečně velký, aby byl po vytištění naskenovatelný – alespoň 20–25 mm napříč

## Související

- [Text](text.md) – standardní 3D text
- [Obrázek jako objekt](image-object.md) – převod obrázků do 3D
