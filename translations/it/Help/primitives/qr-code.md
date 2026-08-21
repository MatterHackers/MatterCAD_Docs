---
title: Codice QR
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
source_hash: 5b941a39b8430a9536401e4af230c06a42635205
source_lang: en
---
# Codice QR

Genera codici QR come oggetti 3D. Puoi codificare testo, URL o credenziali WiFi in un codice QR 3D scansionabile.

<!--  Screenshot of a 3D QR Code object on the workspace -->
![20260318 184540 paste 20260318 184540](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184540-paste-20260318-184540.jpg)


## Come si usa

1. Aggiungi un **Codice QR** dal pannello Primitive
2. Scegli il tipo di output (Testo o WiFi)
3. Inserisci il tuo contenuto
4. Il codice QR viene generato come oggetto 3D che puoi collocare nel tuo progetto

## Parametri

### Modalità Testo

- **Testo** - Il testo o l'URL da codificare (predefinito: "https://matterhackers.com")

### Modalità WiFi

- **SSID** - Il nome della rete WiFi
- **Password** - La password del WiFi
- **Sicurezza** - Il tipo di sicurezza (WEP, WPA o Nessuno)

## Suggerimenti

- Usa [Sottrai](../operations/boolean/subtract.md) per incidere il codice QR in una superficie, oppure collocalo sopra una base [Cubo](cube.md)
- Verifica con un telefono che il codice QR venga scansionato correttamente prima di stamparlo
- I codici QR WiFi permettono alle persone di connettersi alla tua rete scansionando il codice
- Assicurati che il codice QR sia abbastanza grande da poter essere scansionato una volta stampato -- almeno 20-25 mm di lato

## Correlati

- [Testo](text.md) - Testo 3D standard
- [Oggetto Immagine](image-object.md) - Converti immagini in 3D
