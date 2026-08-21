---
title: Grupowanie
parent: "Workspace"
nav_order: 3
source_hash: 82b506a886e270535b5bd58c3913f49328abc4d5
source_lang: en
---
# Grupowanie

Grupowanie łączy wiele obiektów w jedną całość, którą można przesuwać, kopiować i na której można wykonywać operacje jak na pojedynczym obiekcie. W przeciwieństwie do operacji [Połącz](../operations/boolean/combine.md) grupowanie nie scala geometrii — każdy obiekt pozostaje wewnątrz grupy odrębny.

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
![20260318 193104 paste 20260318 193104](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193104-paste-20260318-193104.jpg)

![20260318 193235 paste 20260318 193235](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193235-paste-20260318-193235.jpg)

![20260318 193138 paste 20260318 193138](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193138-paste-20260318-193138.jpg)


## Sposób użycia

### Grupowanie obiektów

1. Wybierz dwa lub więcej obiektów (Shift+kliknięcie lub Ctrl+kliknięcie pozwala zaznaczyć wiele obiektów)
2. Kliknij przycisk **Grupuj** na pasku narzędzi
3. Obiekty są teraz zgrupowane — przemieszczają się razem jako jedna całość

### Rozgrupowywanie obiektów

1. Wybierz grupę
2. Kliknij przycisk **Rozgrupuj** na pasku narzędzi
3. ![20260318 193354 paste 20260318 193354](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193354-paste-20260318-193354.jpg)
4. Poszczególne obiekty zostają przywrócone jako osobne elementy

Rozgrupowanie próbuje również rozdzielić wiele brył zawartych w jednym zaimportowanym pliku STL, jeśli takie występują.

## Grupuj a Połącz

| Cecha | Grupuj | Połącz |
|---------|-------|---------|
| Obiekty pozostają odrębne | Tak | Nie |
| Można później rozgrupować | Tak | Nie (operacja destrukcyjna) |
| Scala nakładającą się geometrię | Nie | Tak |
| Obiekty mogą mieć różne kolory | Tak | Kolory zachowane dla każdej ścianki |
| Zastosowanie | Organizacja i przemieszczanie | Tworzenie pojedynczych brył |

## Wskazówki

- Grupy można zagnieżdżać — możesz grupować obiekty, które już należą do grup
- Wybierz grupę i spójrz na drzewo projektu, aby zobaczyć i wybrać poszczególne obiekty w jej wnętrzu
- Grupowanie nie jest destrukcyjne i zawsze można je cofnąć poleceniem Rozgrupuj

## Powiązane

- [Połącz](../operations/boolean/combine.md) — Scal obiekty w jedną bryłę zamiast je grupować
- [Zaznaczenie](selection.md) — Jak wybrać wiele obiektów do grupowania
- [Komponenty](components.md) — Utwórz grupy parametryczne do wielokrotnego użytku
