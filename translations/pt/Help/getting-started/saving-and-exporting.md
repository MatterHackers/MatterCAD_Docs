---
title: Salvando e Exportando
parent: "Getting Started"
nav_order: 4
source_hash: 020d4bf43f07d3ab7dbd7d585e13c99309f0c0b8
source_lang: en
---
# Salvando e Exportando

O MatterCAD oferece suporte a diversos formatos de arquivo para salvar e exportar seus projetos. O formato escolhido depende de como você pretende usar o arquivo.

## Formatos de Salvamento

### MCX (Formato Nativo)

O MCX é o formato de arquivo nativo do MatterCAD e a melhor escolha para projetos que você deseja continuar editando depois. Ele preserva:

- A árvore de projeto completa com todos os objetos e sua hierarquia
- Todos os parâmetros e configurações de cada objeto
- Operações booleanas, matrizes e outras operações em forma editável
- Relações entre componentes

**Use MCX quando:** você quiser salvar seu trabalho e continuar editando-o mais tarde.

### STL

O STL é o formato mais utilizado para impressão 3D. Ele contém apenas a geometria final da malha de triângulos, sem qualquer histórico de projeto ou parâmetros.

**Use STL quando:** você quiser imprimir seu projeto em 3D ou compartilhá-lo com alguém que não usa o MatterCAD.

### OBJ

O OBJ (Wavefront) é um formato 3D comum, compatível com a maioria dos softwares 3D. Assim como o STL, ele contém somente a geometria da malha.

**Use OBJ quando:** você precisar abrir seu projeto em outro software 3D, como o Blender ou um motor de jogo.

### SVG

A exportação em SVG cria um arquivo vetorial 2D a partir da vista superior do seu projeto. Isso é útil para corte a laser ou usinagem CNC.

**Use SVG quando:** você precisar de um contorno 2D do seu projeto para corte a laser ou gravação.

## Como Salvar

![20260324 080726 paste 20260324 080726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080726-paste-20260324-080726.jpg)

1. Abra o **menu da marca** (o logotipo do MatterCAD no canto superior esquerdo)
2. Escolha **Salvar Como** para selecionar um local e um formato
3. Selecione o formato de arquivo na lista suspensa de formatos
4. Escolha onde salvar o arquivo e clique em **Salvar**

Seu projeto também é salvo automaticamente enquanto você trabalha, portanto você não perderá alterações se fechar o aplicativo.

## Dicas

- Sempre salve uma cópia em MCX do seu projeto antes de exportar para STL ou OBJ, para que você possa fazer alterações depois
- Ao exportar em STL, todos os objetos da cena são mesclados em uma única malha
- Se precisar compartilhar um projeto com alguém que usa o MatterCAD, envie o arquivo MCX para preservar a total capacidade de edição
- Você também pode salvar projetos na sua [Biblioteca na Nuvem](../library/cloud-library.md) para acessá-los de qualquer computador

## Relacionados

- [Adicionando Objetos Existentes](adding-existing-objects.md) - Importar arquivos para o MatterCAD
- [Biblioteca](../library/index.md) - Organize seus projetos salvos
- [Biblioteca na Nuvem](../library/cloud-library.md) - Armazene projetos na nuvem
