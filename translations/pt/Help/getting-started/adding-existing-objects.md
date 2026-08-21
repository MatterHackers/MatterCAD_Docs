---
title: Adicionando Objetos Existentes
parent: "Getting Started"
nav_order: 1
source_hash: e384a5c024336c3c58343d262d914fa40e0b0426
source_lang: en
---
# Adicionando Objetos Existentes

Você pode trazer modelos 3D existentes para o MatterCAD importando arquivos do seu computador ou adicionando conteúdo da biblioteca integrada.

## Do Seu Computador

![20260324 081143 paste 20260324 081143](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081143-paste-20260324-081143.jpg)

![20260324 081240 paste 20260324 081240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081240-paste-20260324-081240.jpg)


Clique no botão **Abrir** na barra de ferramentas para navegar e adicionar arquivos do seu computador. O MatterCAD suporta os seguintes formatos de importação:

- **STL** (.stl) - Formato de modelo 3D padrão da indústria, amplamente usado para impressão 3D
- **AMF** (.amf) - Formato avançado com suporte a cores e objetos multimaterial
- **OBJ** (.obj) - Formato de gráficos 3D Wavefront (somente geometria de malha)
- **3MF** (.3mf) - 3D Manufacturing Format com amplo suporte a metadados
- **MCX** (.mcx) - Formato nativo do MatterCAD, que preserva todos os dados e parâmetros do projeto
- **SVG** (.svg) - Scalable Vector Graphics, importado como caminhos 2D
- **TTF / OTF** (.ttf, .otf) - Arquivos de fonte para uso com a ferramenta Texto

## Arrastar e Soltar

Você também pode arrastar e soltar arquivos diretamente da sua área de trabalho ou do explorador de arquivos no espaço de trabalho do MatterCAD. Os tipos de arquivo suportados serão importados automaticamente.

![20260324 081416 paste 20260324 081416](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081416-paste-20260324-081416.jpg)

## Da Biblioteca

### A Barra Lateral da Biblioteca

Clique no botão **Adicionar Conteúdo** na barra de ferramentas para abrir o painel de navegação da biblioteca. A partir daqui você pode:

- Navegar pelos seus projetos salvos
- Ir até a biblioteca de Primitivas para formas integradas
- Acessar sua Biblioteca na Nuvem se estiver conectado
- Arrastar e soltar qualquer item da biblioteca diretamente no seu espaço de trabalho

![20260324 081446 paste 20260324 081446](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081446-paste-20260324-081446.jpg)

### A Aba Biblioteca

Você também pode usar a aba Biblioteca para navegar pelas suas coleções. Clique com o botão direito em qualquer objeto da biblioteca e selecione **Adicionar à Cena** para importá-lo para o espaço de trabalho do seu projeto atual.

![20260324 081536 paste 20260324 081536](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081536-paste-20260324-081536.jpg)

## Dicas

- MCX é o melhor formato para reeditar projetos posteriormente, pois preserva todos os parâmetros e a árvore do projeto
- Arquivos STL contêm apenas geometria de malha. Se você importar um STL, ainda poderá aplicar operações a ele, mas não poderá editar os parâmetros originais
- Ao importar vários arquivos, cada um se torna um objeto separado na sua cena. Use [Agrupar](../workspace/grouping.md) para organizá-los

## Relacionados

- [Criando Novos Objetos](creating-new-objects.md) - Inicie um projeto do zero com primitivas
- [Salvando e Exportando](saving-and-exporting.md) - Salve e exporte seus projetos finalizados
- [Biblioteca](../library/index.md) - Saiba mais sobre como organizar sua biblioteca de projetos
