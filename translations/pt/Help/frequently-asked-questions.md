---
title: Perguntas Frequentes
nav_order: 101
source_hash: 929ea9e89d3f5008996615341418ba715d3f6075
source_lang: en
---
# Por que meus objetos estão na escala errada?
- Os arquivos STL não armazenam informações de unidade. O MatterCAD espera dimensões STL em milímetros, enquanto a maioria dos softwares CAD exporta em suas unidades nativas (geralmente polegadas). Isso causa discrepâncias de escala ao importar projetos.

- A melhor solução é configurar seu software de projeto para exportar arquivos STL em milímetros. Por exemplo, no SolidWorks, use o botão **Opções** na caixa de diálogo **Salvar Como** para definir os parâmetros de exportação de STL.

- Como alternativa, você pode redimensionar a peça dentro do MatterCAD. Em Visualizar 3D, entre no modo **Editar** e selecione ESCALA na barra de ferramentas à direita. Use o menu suspenso para fatores de conversão comuns ou insira dimensões específicas nos campos de eixo.

# Como faço para limpar os dados do aplicativo?

- Se a reinstalação não resolver um problema, talvez seja necessário excluir os dados armazenados do MatterCAD. Esses dados permanecem após a desinstalação. Para redefinir completamente as configurações padrão, **remover** a pasta do aplicativo. **Você também pode** renomear temporariamente o arquivo do banco de dados SQLite (MatterCAD.db) para testar se as configurações estão causando problemas.
![20260318 194137 paste 20260318 194137](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194137-paste-20260318-194137.jpg)

![20260318 194200 paste 20260318 194200](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194200-paste-20260318-194200.jpg)

![20260318 194218 paste 20260318 194218](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194218-paste-20260318-194218.jpg)


- Windows
  - A biblioteca do usuário e as configurações são armazenadas em C:\Users\{user}\AppData\Local\MatterCAD.
