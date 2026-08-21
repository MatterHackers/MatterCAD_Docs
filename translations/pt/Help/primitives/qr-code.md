---
title: Código QR
articleKey: QrCodeObject3D
parent: "Primitives"
nav_order: 12
source_hash: 5b941a39b8430a9536401e4af230c06a42635205
source_lang: en
---
# Código QR

Gere códigos QR como objetos 3D. Pode codificar texto, URLs ou credenciais de WiFi num código QR 3D legível por leitores.

<!--  Screenshot of a 3D QR Code object on the workspace -->
![20260318 184540 paste 20260318 184540](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184540-paste-20260318-184540.jpg)


## Como Utilizar

1. Adicione um **Código QR** a partir do painel Primitivas
2. Escolha o tipo de saída (Texto ou WiFi)
3. Introduza o seu conteúdo
4. O código QR é gerado como um objeto 3D que pode colocar no seu design

## Parâmetros

### Modo Texto

- **Texto** - O texto ou URL a codificar (predefinição: "https://matterhackers.com")

### Modo WiFi

- **SSID** - O nome da rede WiFi
- **Senha** - A senha do WiFi
- **Segurança** - O tipo de segurança (WEP, WPA ou Nenhum)

## Dicas

- Utilize [Subtrair](../operations/boolean/subtract.md) para gravar o código QR numa superfície, ou coloque-o sobre uma base [Cubo](cube.md)
- Teste se o seu código QR é lido corretamente com um telemóvel antes de imprimir
- Os códigos QR de WiFi permitem que as pessoas se liguem à sua rede ao ler o código
- Certifique-se de que o código QR é suficientemente grande para poder ser lido depois de impresso -- pelo menos 20-25 mm de largura

## Relacionado

- [Texto](text.md) - Texto 3D padrão
- [Objeto de Imagem](image-object.md) - Converter imagens em 3D
