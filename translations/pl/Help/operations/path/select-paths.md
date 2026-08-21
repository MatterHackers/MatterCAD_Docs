---
title: Wybierz ścieżki
articleKey: SelectPathsObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: f7df7bb24841030643e4634febedcfce6e92ada9
source_lang: en
---
# Wybierz ścieżki

Wybierz ścieżki filtruje, które podścieżki złożonego obiektu ścieżki zostaną zachowane. Jest to szczególnie przydatne podczas pracy z ozdobnymi lub wieloczęściowymi czcionkami, gdy potrzebujesz zewnętrznych konturów liter i wewnętrznych wycięć jako osobnych elementów — na przykład po to, by wydrukować je w technologii 3D w dwóch różnych kolorach.

<!--  Screenshot showing Select Paths applied to decorative text with outer paths highlighted -->
![20260506 154655 paste 20260506 154655](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154655-paste-20260506-154655.jpg)

## Jak działa głębokość ścieżki

Gdy obiekt ścieżki zawiera kształty z zamkniętymi obszarami (jak wnętrze litery „O” lub pusty środek ozdobnego zawijasa), te zamknięte obszary są **otworami** o głębokości 1. Zewnętrzny kontur każdej litery lub kształtu ma **głębokość 0**.

```
Depth 0 — outer contour of each letter or shape
Depth 1 — first level of enclosed holes (inside an "O", "A", etc.)
Depth 2 — shapes nested inside a hole (rarely used)
```

## Ustawienia wstępne filtra

### Wszystko
Uwzględnia każdą ścieżkę bez zmian. To ustawienie domyślne, równoważne z całkowitym niestosowaniem operacji Wybierz ścieżki.

### Tylko ścieżki zewnętrzne
Zachowuje wyłącznie zewnętrzny kontur każdego kształtu (głębokość == 0). Użyj tego, aby uzyskać same kontury liter ozdobnej czcionki, bez wewnętrznych wycięć.

### Tylko otwory
Zachowuje wyłącznie zamknięte otwory (głębokość > 0). Użyj tego, aby uzyskać same wewnętrzne wycięcia liter i kształtów.

### Według indeksu grupy
Zachowuje tylko ścieżki należące do jednego rozłącznego kształtu. Grupa 0 to pierwszy kształt, grupa 1 to drugi i tak dalej. Użyj tego, aby wyodrębnić pojedynczy znak ze słowa.

### Niestandardowy
Wpisz wyrażenie, które jest obliczane dla każdej ścieżki. Ścieżka zostaje **uwzględniona**, gdy wynik wyrażenia jest różny od zera, a **pominięta**, gdy wynosi zero.

Wyrażenia muszą zaczynać się od `=`, aby włączyć podstawianie zmiennych. Bez `=` wartość jest traktowana jako zwykła liczba (np. `1` zawsze uwzględnia, `0` zawsze pomija).

## Przykłady wyrażeń niestandardowych

| Wyrażenie | Efekt |
|------------|--------|
| `=PathDepth==0` | Tylko kontury zewnętrzne (tak samo jak Tylko ścieżki zewnętrzne) |
| `=PathDepth>0` | Tylko otwory (tak samo jak Tylko otwory) |
| `=GroupIndex==0` | Tylko pierwszy rozłączny kształt |
| `=PathArea>100` | Kształty o polu większym niż 100 mm² |
| `=PathLength>50` | Kształty o obwodzie dłuższym niż 50 mm |

## Zmienne wyrażeń niestandardowych

| Zmienna | Znaczenie |
|----------|---------|
| `PathDepth` | 0 = kontur zewnętrzny; 1 i więcej = otwór lub kształt zagnieżdżony |
| `GroupIndex` | Indeks rozłącznego kształtu (0, 1, 2…) |
| `GroupOuterArea` | Pole ścieżki zewnętrznej tej grupy |
| `GroupOuterLength` | Obwód ścieżki zewnętrznej tej grupy |
| `ChildCount` | Liczba otworów wewnątrz ścieżki zewnętrznej tej grupy |
| `PathIndex` | Kolejny indeks tej ścieżki w obrębie jej grupy |
| `PathArea` | Pole tej pojedynczej ścieżki |
| `PathLength` | Obwód tej pojedynczej ścieżki |

## Przykład: wielokolorowy wydruk czcionki świątecznej

Częstym zastosowaniem operacji Wybierz ścieżki jest drukowanie ozdobnego tekstu, w którym litery mają wewnętrzne wycięcia. Aby wydrukować zewnętrzne litery w jednym kolorze, a wewnętrzne wycięcia w drugim:

1. Dodaj obiekt **Tekst** i ustaw go na **wyjście 2D**
2. Zastosuj **Wybierz ścieżki** → ustaw ustawienie wstępne na **Tylko ścieżki zewnętrzne**
3. Zastosuj **Wyciągnięcie liniowe**, aby nadać wysokość → przypisz kolor pierwszego filamentu
4. Wróć do pierwotnego obiektu tekstowego
5. Zastosuj drugą operację **Wybierz ścieżki** → ustaw ustawienie wstępne na **Tylko otwory**
6. Zastosuj **Wyciągnięcie liniowe** z tą samą wysokością → przypisz kolor drugiego filamentu
7. Umieść jeden wyciągnięty obiekt na drugim — oba kolory idealnie się pokryją

## Powiązane

- [Wyciągnięcie liniowe](linear-extrude.md) — Nadaj przefiltrowanym ścieżkom wysokość, aby utworzyć obiekt 3D
- [Obrót (Revolve)](revolve.md) — Obróć przefiltrowane ścieżki wokół osi
- [Obiekt SVG](../../primitives/svg-object.md) — Importuj ścieżki wektorowe, które mogą zawierać wiele podścieżek
- [Tekst](../../primitives/text.md) — Obiekty tekstowe w trybie 2D dają wynik złożony z wielu ścieżek
