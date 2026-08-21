---
title: QR-code
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
source_hash: 5b941a39b8430a9536401e4af230c06a42635205
source_lang: en
---
# QR-code

Genereer QR-codes als 3D-objecten. Je kunt tekst, URL's of WiFi-gegevens coderen in een scanbare 3D-QR-code.

<!--  Screenshot of a 3D QR Code object on the workspace -->
![20260318 184540 paste 20260318 184540](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184540-paste-20260318-184540.jpg)


## Gebruik

1. Voeg een **QR-code** toe vanuit het paneel Primitieven
2. Kies het uitvoertype (Tekst of WiFi)
3. Voer je inhoud in
4. De QR-code wordt gegenereerd als een 3D-object dat je in je ontwerp kunt plaatsen

## Parameters

### Tekstmodus

- **Tekst** - De te coderen tekst of URL (standaard: "https://matterhackers.com")

### WiFi-modus

- **SSID** - De naam van het WiFi-netwerk
- **Wachtwoord** - Het WiFi-wachtwoord
- **Beveiliging** - Het beveiligingstype (WEP, WPA of Geen)

## Tips

- Gebruik [Aftrekken](../operations/boolean/subtract.md) om de QR-code in een oppervlak te graveren, of plaats hem bovenop een [Kubus](cube.md) als basis
- Test voor het printen of je QR-code correct wordt gescand met een telefoon
- Met WiFi-QR-codes kunnen mensen verbinding maken met je netwerk door de code te scannen
- Zorg ervoor dat de QR-code groot genoeg is om na het printen scanbaar te zijn -- minstens 20-25 mm breed

## Gerelateerd

- [Tekst](text.md) - Standaard 3D-tekst
- [Afbeeldingsobject](image-object.md) - Afbeeldingen omzetten naar 3D
