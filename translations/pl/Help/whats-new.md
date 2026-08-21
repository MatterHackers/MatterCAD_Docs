---
title: Co nowego
nav_order: 105
source_hash: 172343b8320204d2b0ec52419324f0efd2be95a1
source_lang: en
---
# MatterCAD 2.2026.8

# Co nowego

* **Edytuj elementy podrzędne**
  * Kliknij dwukrotnie dowolny obiekt, aby wejść do jego wnętrza i edytować części, z których jest zbudowany, bezpośrednio na stole roboczym
  * Ścieżka nawigacyjna pokazuje, gdzie się znajdujesz — kliknij dowolny poziom, aby zatwierdzić wprowadzone zmiany
  * ![MatterCAD 2.2026.8](https://www.matterhackers.com/r/qgG4VA)

* **Jedno narzędzie boolowskie**
  * Połącz, Odejmij, Część wspólna oraz Odejmij i Zamień to teraz jedna operacja — tryby przełączasz jednym kliknięciem, zamiast usuwać i stosować operację ponownie
  <!-- Boolean property panel showing the four-icon operation row with Subtract selected. ~500x350px -->
  * ![One Boolean Tool](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)

* **Operacje boolowskie, które po prostu działają**
  * Nowy silnik jest szybszy i radzi sobie z siatkami, na których wcześniej operacje zawodziły
  * Połącz automatycznie naprawia części z otworami i nazywa wszystko, czego nie udało się scalić; Cięcie płaszczyzną pozostawia teraz szczelną bryłę gotową do druku

* **Lepsza edycja ścieżek 2D**
  * Tryby punktów, symetria Odbicie lustrzane na żywo, przyciąganie do siatki, zaznaczanie przeciągnięciem oraz Esc do anulowania przeciągania
  <!-- Turn on Mirror, drag a point and watch its partner follow, then drag it onto the axis to merge. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

## Ulepszenia

* **Nawigacja** — Naciśnij Z przy zaznaczonej ścieżce 2D, aby przejść do widoku edycji z góry
* **Wyraźniejszy tekst** — Renderowanie tekstu z dokładnością subpikselową włącza się teraz automatycznie, gdy wyświetlacz je obsługuje
* **Modelowanie** — Wyciągnięcie liniowe może sfazować dolną krawędź z własnym stylem, promieniem i liczbą segmentów

## Najważniejsze poprawki błędów

* **Niezawodność zapisu** — Nieudany zapis nie może już uszkodzić zastępowanego pliku, a program informuje o niepowodzeniu
* **Biblioteka w chmurze** — Zapisanie elementu z chmury na dysku zachowuje nazwę karty, a karta pozostaje po ponownym uruchomieniu
* **Wczytywanie plików** — Naprawiono ciche pomijanie części 3MF podczas wczytywania
* **Edycja ścieżek** — Naprawiono awarię przy usuwaniu punktu krzywej oraz przywracanie wybranego trybu przez punkty szwu
* **Zadania w tle** — Przycisk Zatrzymaj w trwającym zadaniu jest teraz klikalny i faktycznie je anuluje

## Pełne informacje o wydaniu znajdziesz [Tutaj](release-notes.md).
