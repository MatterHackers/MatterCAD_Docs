---
title: Notas da Versão
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8 (13 de agosto de 2026)
[Download para Windows](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## Novos Recursos

* **Editar Filhos**
  * Clique duas vezes em um objeto na mesa ou na Árvore de Cena para entrar nele e editar as peças que o compõem — sem janela ou aba separada
  * Em operações como Subtrair, você edita as peças de origem e o resultado é reconstruído quando você sai
  * Um caminho de navegação no topo da Árvore de Cena mostra o percurso completo; clicar em um nível incorpora suas edições como uma única etapa desfazível, e cada nível mantém seu próprio histórico de desfazer
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **Uma Única Ferramenta Booleana**
  * Combinar, Subtrair, Intersectar e Subtrair e Substituir agora são uma única operação com uma linha de ícones no topo do seu painel — alterne os modos com um clique em vez de excluir e reaplicar
  * A mesma operação lida com malhas 3D e caminhos 2D, e mostra o progresso enquanto uma operação booleana pesada é executada
  * Projetos salvos com os antigos objetos booleanos separados continuam abrindo normalmente
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **Operações Booleanas Que Simplesmente Funcionam**
  * As operações booleanas rodam em um novo motor nativo, mais rápido e que tem sucesso em malhas que antes falhavam
  * Combinar repara peças com furos automaticamente: reparos limpos entram na união, peças que não podem ser mescladas com segurança são mantidas ao lado dela e nomeadas para você, e uma peça que não pôde ser reparada mantém sua geometria original
  * Corte por Plano agora é uma verdadeira interseção sólida, então o resultado é estanque e imprimível, em vez de uma casca aberta
  * Novas opções Manter Geometria Invertida e Reparar Ordem de Enrolamento para malhas importadas problemáticas


## Melhorias

* **Editor de Caminho 2D**
  * Quatro modos de ponto — Anguloso, Simétrico, Alinhado e Livre — aplicados com um clique, tanto no editor 2D quanto na vista 3D
  * Espelhar agora é um modo de simetria ao vivo: as edições são espelhadas através do centro conforme você as faz, e arrastar um par espelhado sobre o eixo o mescla em um único ponto
  * Selecione pontos arrastando uma caixa de seleção, mova-os em grupo, encaixe-os na grade e pressione Esc para cancelar um arraste
  * Suavizar ajusta uma curva através dos pontos que você clicou em uma única etapa
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **Visualização e Navegação**
  * Pressione Z com um caminho plano selecionado para animar até uma vista de edição perpendicular ajustada ao caminho
  * A renderização de texto sub-pixel agora é ativada automaticamente quando seu monitor a suporta, e ainda pode ser ligada ou desligada nas configurações de Avançado

* **Modelagem**
  * Extrusão Linear pode chanfrar a aresta inferior com estilo, raio e número de segmentos próprios
  * Objetos exclusivos do editor (Curva 3D, Ferramenta de Medição, Descrição, Folha) continuam sendo exibidos, mas são excluídos da exportação

## Principais Correções de Bugs

  * Um salvamento que falhava no meio podia truncar o arquivo que estava substituindo enquanto relatava sucesso. Os salvamentos agora são concluídos por completo e só então substituem o destino de forma atômica — a mesma proteção cobre salvamentos na biblioteca e exportações
  * Um salvamento com falha deixa o projeto marcado como não salvo, de modo que fechar o aplicativo não pode descartar seu trabalho silenciosamente
  * Salvar um item da nuvem no disco mantinha o nome antigo da aba e perdia a aba ao reiniciar
  * Corrigido o descarte silencioso de submodelos 3MF durante o carregamento, e arquivos 3MF carregados ao mesmo tempo contaminando uns aos outros
  * Corrigidas falhas, um filtro de histograma quebrado e cópias de uma peça de imagem que não permaneciam sincronizadas com a original
  * Corrigida uma falha ao excluir um ponto de curva, e pontos na emenda de um caminho fechado que revertiam o modo escolhido
  * O botão Parar em uma tarefa em execução agora é clicável e realmente cancela

---

# MatterCAD 2.2026.5 (8 de maio de 2026)
[Download para Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## Novos Recursos

* **Ferramenta de Matriz Redesenhada**
  * Uma única operação de Matriz unificada substitui as antigas Matriz Linear, Matriz Radial e Matriz avançada
  * Modo **Linear**: cópias ao longo de uma direção com rotação opcional e escala progressiva
  * Modo **Radial**: cópias ao redor de um eixo central com raio, ângulo de varredura e padrões em arco ou círculo completo configuráveis
  * Modo **Transformar**: cópias em etapas usando uma transformação manual ou a transformação de um objeto irmão nomeado
  * O modo de rotação Composição no Linear cria espirais, leques e hélices naturalmente
  * Opção Escala Afeta Deslocamento para layouts em concha de náutilo e progressão geométrica
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **Favoritos da Biblioteca**
  * Marque com estrela qualquer item da biblioteca para adicioná-lo a uma pasta Favoritos persistente
  * Acesse rapidamente suas primitivas, geradores e peças salvas mais usadas em um só lugar
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## Melhorias

* **Alinhar**
  * O alinhamento Empilhado agora é um botão de modo direto em vez de uma opção de menu suspenso
  * Adicionados modos Simples, Deslocamento e Empilhado mais claros para alinhar arestas, adicionar espaçamentos precisos e construir pilhas ordenadas
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **Suporte a Arquivos**
  * Adicionado suporte ao formato de imagem WEBP em operações baseadas em imagem
  * Análise de arquivos SVG aprimorada para importações mais confiáveis

* **Confiabilidade**
  * Melhorada a velocidade e a confiabilidade do carregamento de arquivos 3MF
  * Melhor restauração de abas entre sessões

## Principais Correções de Bugs

* **Login e Acesso à Biblioteca na Nuvem**
  * O login e o acesso à Biblioteca na Nuvem foram restaurados depois que uma atualização do servidor de backend quebrou a autenticação.
  * O MatterCAD agora solicita que você entre novamente quando o acesso à nuvem encontra credenciais expiradas ou inválidas.

* **Seleção na Árvore de Cena**
  * Corrigido o comportamento inconsistente de seleção ao escolher objetos na árvore de cena.

* **Navegação da Ajuda**
  * Corrigidos problemas de navegação na ajuda integrada e na documentação de versões.

* **Clique com o Botão Direito na Biblioteca**
  * Corrigido o comportamento do clique com o botão direito na visualização em árvore da biblioteca.

* **Folhas**
  * Corrigida uma falha que podia ocorrer ao trabalhar com folhas.

---

# MatterCAD 2.2026.3 (12 de março de 2026)
[Download para Windows](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## Novos Recursos

* **Novíssimo Motor de Renderização Direct3D 11**
  * Migração completa do OpenGL para o Direct3D 11 para um desempenho drasticamente melhor
  * Anti-aliasing FXAA para arestas nítidas e limpas
  * Dual depth peeling para transparência correta independente da ordem
  * Sombras da mesa aceleradas por hardware
  * Contornos de objetos e visuais de seleção aprimorados
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **Transparência de Objeto**
  * Defina alfa/transparência em qualquer objeto individual da cena
  * Malhas com cor por face suportam alfa sem danificar a cor
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **Bloquear e Ocultar Objetos**
  * Bloqueie objetos para evitar seleção ou edição acidental
  * Oculte objetos para reduzir a poluição visual enquanto trabalha em peças específicas
  * Comandos Reexibir Tudo e Desbloquear Tudo para restaurar rapidamente a visibilidade
  * Objetos bloqueados e ocultos são corretamente excluídos da seleção por raio
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **Subtrair Booleano Aprimorado**
  * As operações de subtração múltipla são significativamente mais confiáveis e precisas

## Melhorias

* **Manipulação de Arquivos**
  * Os projetos agora são salvos como 3MF por padrão em vez de STL, preservando cores, materiais e o histórico de design
  * Suporte aprimorado para arrastar e soltar arquivos e pastas na vista 3D

* **Fluxo de Trabalho**
  * Os diálogos Salvar Como e Mover lembram a última pasta usada
  * Os campos de expressão agora suportam `pi`, `tau`, `e` e `count`
  * A tecla Esc executa desfazer em contextos de edição de design
  * Os controles 3D permanecem visíveis quando o mouse sai da cena

* **Desempenho e Estabilidade**
  * Corrigidas falhas na inicialização e problemas de carregamento recursivo
  * Corrigidos bugs de renderização de iluminação e mipmapping
  * Melhoradas as atualizações da visualização em árvore da biblioteca
  * Cálculos dinâmicos dos planos próximo/distante para melhor comportamento do zoom
  * Atualizado para .NET 10

---

# MatterCAD 2.2025.6 (20 de junho de 2025)
[Download para Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## Novos Recursos

* **Suporte a Ficheiro SVG**  
  * Suporte completo para arrastar e soltar arquivos SVG
  * Conversão direta de gráficos SVG em objetos 3D
  * Integração perfeita com os fluxos de trabalho CAD existentes

* **Manipulação Avançada de Arquivo OBJ**  
  * Suporte ao carregamento de materiais a partir de arquivos ZIP
  * Análise de arquivos OBJ e manipulação de materiais aprimoradas
  * Melhor suporte para modelos 3D complexos com múltiplos materiais

* **Sistema Aprimorado de Gerenciamento de Abas**
  * As abas da biblioteca na nuvem agora persistem corretamente — seu trabalho permanece exatamente onde você o deixou
  * Organização e navegação de abas aprimoradas
  * Restauração automática das abas abertas entre sessões

## Melhorias na Experiência do Usuário

* **Interface Simplificada**
  * Menu Recentes reorganizado para acesso mais rápido
  * Melhor feedback visual durante operações longas
  * Tempo de inicialização e capacidade de resposta do aplicativo aprimorados

* **Confiabilidade**
  * Corrigidas falhas críticas nas interações da cena 3D
  * Resolvidos problemas de gerenciamento de memória
  * Estabilidade do aplicativo aprimorada em todas as plataformas

---

# MatterCAD 2.21.5 (13 de fevereiro de 2025)

[Download para Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# Recursos Existentes

*Os recursos a seguir representam a base sobre a qual o MatterCAD se apoia, herdada do MatterControl:*

* Adicionado o recurso Oco  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* Adicionado Reduzir Polígonos  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* Adicionado Reparar Malha  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* Incluído o suporte totalmente automático (suporte legado) como opção, além da nova opção de suporte manual
* Adicionado suporte ao gsSlicer (novo motor de fatiamento experimental)
* Bugs corrigidos

## Alterações

* Melhorado o desagrupamento de malha (divisão em múltiplas malhas)
    * Descarte de faces degeneradas
    * Descarte de recursos discretos microscópicos

## Alterações

* Adicionada barra de pesquisa ao aplicativo
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* Melhorada a barra de ferramentas de design
    * Adicionado agrupamento a alguns itens
    * Adicionado botão de alinhamento duplo
    * Adicionado botão Organizar Tudo
* Desloque itens na mesa com as teclas de seta
* A pasta Downloads é ordenada por data

## Alterações

* Melhorias na interface
    * Atualizações mais rápidas nas pastas da Biblioteca na Nuvem
    * Restauração da interface ao reabrir
    * Melhor suporte à navegação por teclado
* Novo sistema de detecção de erros e avisos
    * Mais erros de hardware tratados
* Melhorias e otimizações nas ferramentas de design
    * Novas ferramentas de Torção
    * Ferramenta de Curva melhorada
    * Alinhar melhorado


## Alterações

* Melhorado o achatamento
* Melhorado o suporte a desfazer
* Melhorado o histórico de design

## Alterações
* Versionamento: mudança para um número de versão no formato (versão).(ano).(mês). Mais fácil de ler e mais informativo.
* Novos Subtrair, Combinar e Interseção de última geração (somente Windows)
* Agora iniciamos com um 'Tour de Recursos' para ajudar novos usuários a se orientarem

## Alterações
* Ferramentas de Design - A capacidade de modelar em 3D com um conjunto completo de primitivas de modelagem
* Use uma primitiva para criar seus próprios suportes personalizados
* Aplicativos de Design - Aplicativos de Design: designs sofisticados e personalizáveis
* Processamento de 64 bits
