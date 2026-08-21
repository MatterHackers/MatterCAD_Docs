---
title: Novidades
nav_order: 105
source_hash: 172343b8320204d2b0ec52419324f0efd2be95a1
source_lang: en
---
# MatterCAD 2.2026.8

# Novidades

* **Editar Filhos**
  * Dê um duplo clique em qualquer objeto para entrar nele e editar as peças que o compõem, diretamente na mesa
  * Uma trilha de navegação mostra onde você está — clique em qualquer nível para incorporar suas edições de volta
  * ![MatterCAD 2.2026.8](https://www.matterhackers.com/r/qgG4VA)

* **Uma Única Ferramenta Booleana**
  * Combinar, Subtrair, Intersectar e Subtrair e Substituir agora são uma única operação — alterne entre os modos com um clique, em vez de excluir e reaplicar
  <!-- Boolean property panel showing the four-icon operation row with Subtract selected. ~500x350px -->
  * ![One Boolean Tool](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)

* **Booleanas Que Simplesmente Funcionam**
  * Um novo motor é mais rápido e tem sucesso em malhas que antes falhavam
  * Combinar repara automaticamente peças com furos e identifica pelo nome tudo o que não conseguiu mesclar; o Corte por Plano agora deixa um sólido estanque e imprimível

* **Melhor Edição de Caminhos 2D**
  * Modos de ponto, simetria de Espelhar em tempo real, encaixe na grade, seleção por arrasto e Esc para cancelar um arrasto
  <!-- Turn on Mirror, drag a point and watch its partner follow, then drag it onto the axis to merge. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

## Melhorias

* **Navegação** — Pressione Z com um caminho 2D selecionado para obter uma vista de edição de cima para baixo
* **Texto Mais Nítido** — A renderização de texto em sub-pixel agora é ativada automaticamente quando seu monitor a suporta
* **Modelagem** — A Extrusão Linear pode chanfrar a aresta inferior com seu próprio estilo, raio e número de segmentos

## Principais Correções de Bugs

* **Confiabilidade ao Salvar** — Um salvamento com falha não pode mais danificar o arquivo que estava sendo substituído, e agora informa que falhou
* **Biblioteca na Nuvem** — Salvar um item da nuvem em disco mantém o nome da sua aba, e a aba sobrevive a um reinício
* **Carregamento de Arquivos** — Corrigido o descarte silencioso de peças 3MF durante o carregamento
* **Edição de Caminhos** — Corrigida uma falha ao excluir um ponto de curva e os pontos de emenda que revertiam o modo escolhido
* **Tarefas em Segundo Plano** — O botão Parar em uma tarefa em execução agora é clicável e realmente cancela

## Você pode ver as notas de versão completas [Aqui](release-notes.md).
