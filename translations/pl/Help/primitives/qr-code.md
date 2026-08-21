---
title: Kod QR
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
source_hash: 5b941a39b8430a9536401e4af230c06a42635205
source_lang: en
---
# Kod QR

Generuj kody QR jako obiekty 3D. Możesz zakodować tekst, adresy URL lub dane logowania do sieci WiFi w skanowalnym kodzie QR 3D.

<!--  Screenshot of a 3D QR Code object on the workspace -->
![20260318 184540 paste 20260318 184540](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184540-paste-20260318-184540.jpg)


## Sposób użycia

1. Dodaj **Kod QR** z panelu Prymitywy
2. Wybierz typ danych wyjściowych (Tekst lub WiFi)
3. Wprowadź swoją treść
4. Kod QR zostanie wygenerowany jako obiekt 3D, który możesz umieścić w swoim projekcie

## Parametry

### Tryb Tekst

- **Tekst** — Tekst lub adres URL do zakodowania (domyślnie: "https://matterhackers.com")

### Tryb WiFi

- **SSID** — Nazwa sieci WiFi
- **Hasło** — Hasło do sieci WiFi
- **Zabezpieczenia** — Typ zabezpieczeń (WEP, WPA lub Brak)

## Wskazówki

- Użyj operacji [Odejmij](../operations/boolean/subtract.md), aby wygrawerować kod QR w powierzchni, albo umieść go na podstawie utworzonej z [Sześcian](cube.md)
- Przed drukiem sprawdź telefonem, czy kod QR poprawnie się skanuje
- Kody QR WiFi pozwalają innym połączyć się z Twoją siecią przez zeskanowanie kodu
- Upewnij się, że kod QR jest wystarczająco duży, aby dało się go zeskanować po wydrukowaniu — co najmniej 20–25 mm szerokości

## Powiązane

- [Tekst](text.md) — Standardowy tekst 3D
- [Obiekt Obraz](image-object.md) — Konwersja obrazów na modele 3D
