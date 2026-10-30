---
title: QR Code
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
description: Make a scannable QR code from text, a web address or WiFi details, to raise or engrave on a part.
keywords: barcode, scan code, link, url, website code, wifi password, scannable
---
# QR Code

QR Code makes a scannable QR code from text, a web address or WiFi login details. It arrives as a flat picture plate (60 × 60 mm, 0.2 mm thick) that works like an [Image Object](image-object.md): use it as the picture for [Image Converter](../operations/image/image-converter.md) or [Lithophane](../operations/image/lithophane.md) to turn it into a raised or engraved code.

<!--  Screenshot of a 3D QR Code object on the workspace -->
<!-- AUTO_IMAGE: type=shot id=primitives-qr-code -->
![A QR Code selected in the 3D view beside its Properties panel: Output Option set to Text, the Text it encodes and a preview of the code](https://matterhackers.github.io/MatterCAD_Docs/assets/primitives-qr-code.png)


## How to Use

1. Open **Included > Tools** in the Library (or under **Add to Bed**) and add **QR Code** to the bed
2. Choose **Text** or **WiFi** for **Output Option**
3. Enter your content; the code updates as you type
4. With the QR Code selected, click **Image Converter** in the Image group of the toolbar to make a solid code

## Parameters

- **Output Option** - **Text** (default) or **WiFi**: what the code holds

### Text

- **Text** - The text or web address to encode (default "https://matterhackers.com")

### WiFi

- **SSID** - The name of the WiFi network
- **Password** - The password of the WiFi network
- **Security** - **WEP**, **WPA** (default) or **None**

### Both

- **Invert** - Off by default. Swaps the dark and light squares

## Tips

- After Image Converter, place the solid code on top of a [Cube](cube.md) base, or [Subtract](../operations/boolean/subtract.md) it to engrave the code into a surface
- Test that your QR code scans correctly with a phone before you export it
- WiFi QR codes let people connect to your network by scanning the code
- Keep the code large enough to scan on the finished part: scale it down only as far as a phone can still read it

## Related

- [Text](text.md) - Standard 3D text
- [Image Object](image-object.md) - Place a picture in your design as the input for the image operations
