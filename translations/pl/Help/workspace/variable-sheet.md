---
title: Arkusz zmiennych
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
source_hash: 3137a4da2b9d2086d4dcace156435caca288dd79
source_lang: en
---
# Arkusz zmiennych

Arkusz zmiennych przechowuje wspólne wartości projektu. Używaj go, gdy kilka obiektów ma odwoływać się do tych samych wymiarów, liczb, etykiet lub formuł. Zmiana wartości w arkuszu powoduje przeliczenie zależnych obiektów, dzięki czemu projekty parametryczne pozostają spójne bez konieczności edytowania każdego obiektu z osobna.

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## Jak dodać Arkusz zmiennych

1. Otwórz bibliotekę i dodaj **Arkusz zmiennych** do sceny.
2. Wybierz obiekt Arkusz zmiennych, aby wyświetlić edytor arkusza.
3. Wybierz komórkę, a następnie wprowadź **Nazwa** oraz wartość lub formułę.
4. Używaj nazwy komórki w innych polach projektu obsługujących wyrażenia.

## Edytowanie komórek

Każda komórka ma dwie edytowalne części:

- **Nazwa** — opcjonalna nazwa zmiennej dla komórki. Nazwy nie rozróżniają wielkości liter, spacje są zamieniane na podkreślenia, a zduplikowane nazwy są automatycznie korygowane.
- **Wyrażenie** — wartość komórki. Zwykły tekst lub liczby są zapisywane bezpośrednio. Formuły zaczynają się od `=`.

Do komórek można też odwoływać się przez adres, na przykład `A1` lub `B2`. Nazwane komórki są zwykle czytelniejsze dla parametrów projektu, ponieważ opisują ich przeznaczenie, na przykład `wall_thickness`, `outer_diameter` czy `hole_count`.

## Formuły

Rozpocznij formułę od `=`, aby została obliczona w arkuszu:

- `=20 + 5` zwraca `25`
- `=pi * 10` zwraca `31.41592653589793`
- `=A1 * 2` odwołuje się do innej komórki przez adres
- `=wall_thickness + 4` odwołuje się do nazwanej komórki

Arkusz obsługuje działania arytmetyczne, nawiasy, operatory porównania, popularne funkcje `Math`, takie jak `sin`, `cos`, `sqrt` i `round`, oraz stałe, w tym `pi`, `tau` i `e`.

## Używanie wartości arkusza w obiektach

Większość pól liczbowych w MatterCAD obsługuje wyrażenia. Aby użyć wartości z arkusza w parametrze obiektu, poprzedź odwołanie znakiem `=`:

- Ustaw **Szerokość** obiektu Sześcian na `=case_width`.
- Ustaw **Liczba** obiektu Szyk na `=hole_count`.
- Ustaw wartość **Przesunięcie** operacji Przesuń na `=wall_thickness * 2`.

Gdy arkusz się zmieni, MatterCAD przelicza zależne od niego obiekty.

## Tekst i funkcje pomocnicze

Komórki Arkusza zmiennych mogą przechowywać zarówno tekst, jak i liczby. Wartości tekstowe przydają się do generowanych etykiet, numerów części, importowanych danych i własnych aplikacji projektowych.

Przydatne funkcje pomocnicze:

- `concat()` lub `strcat()` — łączy teksty lub wartości.
- `substring()` — wyodrębnia fragment wartości tekstowej.
- `split()` — dzieli tekst i zwraca jeden element.
- `count()` — zlicza elementy rozdzielone separatorem w tekście.
- `substitute()` — zamienia tekst.
- `rand(seed)` — generuje deterministyczną wartość losową, gdy podano ziarno.
- `importdata()` — odczytuje wartość z adresu URL lub lokalnej ścieżki pliku.

## Wskazówki

- Dla wartości używanych przez inne obiekty stosuj opisowe nazwy zamiast adresów komórek.
- Umieszczaj kluczowe wymiary w pobliżu lewego górnego rogu arkusza, aby łatwo je znaleźć.
- Używaj formuł dla wartości pochodnych, takich jak `inner_diameter = outer_diameter - wall_thickness * 2`.
- Unikaj używania słów zastrzeżonych, takich jak `pi`, `e`, `true`, `false`, ani nazw funkcji jako nazw komórek.
- Jeśli formuły nie da się przetworzyć, MatterCAD zachowuje pierwotne dane wejściowe jako tekst.

## Powiązane

- [Wyrażenia](expressions.md) — używanie wyrażeń w parametrach obiektów
- [Komponenty](components.md) — tworzenie parametrycznych projektów wielokrotnego użytku
- [Szyk](../operations/array/array.md) — tworzenie powtarzalnych wzorów sterowanych wartościami z arkusza
