---
title: QR-Code
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
source_hash: 5b941a39b8430a9536401e4af230c06a42635205
source_lang: en
---
# QR-Code

Erzeugen Sie QR-Codes als 3D-Objekte. Sie können Text, URLs oder WLAN-Zugangsdaten in einen scanbaren 3D-QR-Code codieren.

<!--  Screenshot of a 3D QR Code object on the workspace -->
![20260318 184540 paste 20260318 184540](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184540-paste-20260318-184540.jpg)


## Verwendung

1. Fügen Sie einen **QR-Code** aus dem Bereich Primitive hinzu
2. Wählen Sie den Ausgabetyp (Text oder WiFi)
3. Geben Sie Ihren Inhalt ein
4. Der QR-Code wird als 3D-Objekt erzeugt, das Sie in Ihrem Entwurf platzieren können

## Parameter

### Text-Modus

- **Text** – Der zu codierende Text oder die URL (Standard: "https://matterhackers.com")

### WiFi-Modus

- **SSID** – Der Name des WLAN-Netzwerks
- **Passwort** – Das WLAN-Passwort
- **Sicherheit** – Der Sicherheitstyp (WEP, WPA oder Keine)

## Tipps

- Verwenden Sie [Subtrahieren](../operations/boolean/subtract.md), um den QR-Code in eine Oberfläche zu gravieren, oder platzieren Sie ihn auf einem [Würfel](cube.md) als Basis
- Prüfen Sie vor dem Drucken mit einem Smartphone, ob sich Ihr QR-Code korrekt scannen lässt
- Mit WLAN-QR-Codes können sich andere durch Scannen des Codes mit Ihrem Netzwerk verbinden
- Achten Sie darauf, dass der QR-Code groß genug ist, um im gedruckten Zustand scanbar zu sein – mindestens 20–25 mm Kantenlänge

## Verwandte Themen

- [Text](text.md) – Standardmäßiger 3D-Text
- [Bildobjekt](image-object.md) – Bilder in 3D umwandeln
