---
title: Code QR
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
source_hash: 5b941a39b8430a9536401e4af230c06a42635205
source_lang: en
---
# Code QR

Générez des codes QR sous forme d'objets 3D. Vous pouvez encoder du texte, des URL ou des identifiants WiFi dans un code QR 3D scannable.

<!--  Screenshot of a 3D QR Code object on the workspace -->
![20260318 184540 paste 20260318 184540](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184540-paste-20260318-184540.jpg)


## Utilisation

1. Ajoutez un **Code QR** depuis le panneau Primitives
2. Choisissez le type de sortie (Texte ou WiFi)
3. Saisissez votre contenu
4. Le code QR est généré comme un objet 3D que vous pouvez placer sur votre conception

## Paramètres

### Mode Texte

- **Texte** - Le texte ou l'URL à encoder (par défaut : "https://matterhackers.com")

### Mode WiFi

- **SSID** - Le nom du réseau WiFi
- **Mot de passe** - Le mot de passe du WiFi
- **Sécurité** - Le type de sécurité (WEP, WPA ou Aucun)

## Astuces

- Utilisez [Soustraire](../operations/boolean/subtract.md) pour graver le code QR dans une surface, ou placez-le sur une base [Cube](cube.md)
- Vérifiez que votre code QR se scanne correctement avec un téléphone avant l'impression
- Les codes QR WiFi permettent aux personnes de se connecter à votre réseau en scannant le code
- Assurez-vous que le code QR est assez grand pour être scannable une fois imprimé -- au moins 20 à 25 mm de côté

## Voir aussi

- [Texte](text.md) - Texte 3D standard
- [Objet image](image-object.md) - Convertir des images en 3D
