---
title: Código QR
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
source_hash: 5b941a39b8430a9536401e4af230c06a42635205
source_lang: en
---
# Código QR

Genera códigos QR como objetos 3D. Puedes codificar texto, URL o credenciales WiFi en un código QR 3D escaneable.

<!--  Screenshot of a 3D QR Code object on the workspace -->
![20260318 184540 paste 20260318 184540](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184540-paste-20260318-184540.jpg)


## Cómo se usa

1. Agrega un **Código QR** desde el panel Primitivas
2. Elige el tipo de salida (Texto o WiFi)
3. Introduce tu contenido
4. El código QR se genera como un objeto 3D que puedes colocar en tu diseño

## Parámetros

### Modo Texto

- **Texto** - El texto o la URL que se va a codificar (valor predeterminado: "https://matterhackers.com")

### Modo WiFi

- **SSID** - El nombre de la red WiFi
- **Contraseña** - La contraseña de la red WiFi
- **Seguridad** - El tipo de seguridad (WEP, WPA o Ninguno)

## Consejos

- Usa [Restar](../operations/boolean/subtract.md) para grabar el código QR en una superficie, o colócalo sobre una base de [Cubo](cube.md)
- Comprueba que tu código QR se escanea correctamente con un teléfono antes de imprimirlo
- Los códigos QR de WiFi permiten que la gente se conecte a tu red escaneando el código
- Asegúrate de que el código QR sea lo bastante grande para poder escanearse una vez impreso: al menos 20-25 mm de ancho

## Relacionado

- [Texto](text.md) - Texto 3D estándar
- [Objeto Imagen](image-object.md) - Convierte imágenes en 3D
