---
title: Szyk
articleKey: ArrayObject3D_2
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c547fa24e5f47e0d60f0cec0eac979700d946daf
source_lang: en
---
# Szyk

Szyk tworzy wiele kopii obiektu rozmieszczonych we wzorze. Wybierz tryb za pomocą przycisków u góry — **Liniowy**, **Promieniowy** lub **Przekształć** — aby przełączać się między typami wzorów.

<!--  Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->
![20260506 080647 paste 20260506 080647](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080647-paste-20260506-080647.jpg)


## Sposób użycia

1. Wybierz obiekt
2. Zastosuj operację **Szyk** z menu Duplikacja
3. Wybierz tryb (Liniowy, Promieniowy lub Przekształć)
4. Dostosuj parametry wybranego trybu

## Tryb: Liniowy

Tryb liniowy rozmieszcza kopie wzdłuż kierunku, z opcjonalną progresją obrotu i skali.

**Liczba** — Liczba kopii (liczba całkowita lub wyrażenie). Obiekt źródłowy jest pierwszą kopią; kolejne kopie są względem niego przesunięte.

**Metoda przesunięcia** — Sposób obliczania odstępów:
- **Względny** — Przesunięcie jest mnożone przez rozmiar obwiedni obiektu. Przesunięcie względne równe (1, 0, 0) rozmieszcza kopie dokładnie co jedną szerokość obiektu wzdłuż osi X.
- **Przesunięcie** — Stała odległość w przestrzeni świata w mm na kopię.
- **Punkt końcowy** — Ustaw pozycję ostatniej kopii; odstępy są rozdzielane równomiernie między kopiami.

**Przesunięcie względne** / **Przesunięcie** / **Punkt końcowy** — Wektor odstępu, zależnie od wybranej Metody przesunięcia.

**Tryb obrotu** — Sposób kumulowania obrotu kolejnych kopii:
- **Lokalny** — Każda kopia obraca się w miejscu wokół własnego środka; kierunek przesunięcia pozostaje w osiach świata.
- **Łączenie** — Obrót kumuluje się i steruje przesunięciem, tworząc spirale, wachlarze i helisy.

**Obrót** — Obrót przypadający na kopię, w stopniach, dla każdej osi.

**Skaluj** — Skumulowana skala przypadająca na kopię dla każdej osi. Wartości mniejsze niż 1 zmniejszają kopie; wartości większe niż 1 je powiększają.

**Skala wpływa na offset** — Gdy opcja jest włączona, odstęp między kopiami również skaluje się z każdym krokiem. Użyj tego do zacieśniających się spiral i postępów geometrycznych (muszle łodzika, ułożone krzywe muszli).

## Tryb: Promieniowy

Tryb promieniowy rozmieszcza kopie równomiernie wokół osi centralnej w stałym promieniu.

<!--  Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->
![20260506 092618 paste 20260506 092618](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-092618-paste-20260506-092618.jpg)


**Metoda zliczania** — Sposób określania liczby kopii:
- **Liczba** — Jawnie podana liczba kopii.
- **Odległość** — Odstęp kątowy między kopiami w stopniach; liczba jest obliczana tak, aby wypełnić zakres.

**Liczba** / **Odległość kątowa** — Liczba kopii (tryb Liczba) lub odstęp kątowy w stopniach (tryb Odległość). Obsługuje wyrażenia.

**Oś centralna** — Oś, wokół której następuje obrót (domyślnie: Z).

**Segment okręgu** — Czy kopie obejmują pełny okrąg 360° (**Pełny**), czy tylko część łuku (**Łuk**).

**Promień** — Odległość od osi centralnej do każdej kopii.

**Kąt przeciągnięcia** — Liczba stopni łuku do wypełnienia (widoczne, gdy Segment okręgu ma wartość Łuk). Obsługuje wyrażenia.

**Wyrównaj obrót** — Obraca każdą kopię tak, aby jej oś przednia była skierowana na zewnątrz od środka.

**Oś przednia** — Która oś kopii jest traktowana jako „przednia” przy wyrównywaniu (widoczne, gdy Wyrównaj obrót jest włączone).

## Tryb: Przekształć

Tryb Przekształć powiela kopie krokowo, używając ręcznie zadanego przekształcenia lub podążając za przekształceniem innego obiektu.

**Liczba** — Liczba kopii (liczba całkowita lub wyrażenie).

**Odniesienie przekształcenia** — Źródło przekształcenia dla pojedynczego kroku:
- **Wejście** — Bezpośrednio podajesz przesunięcie, obrót i skalę.
- **Obiekt** — Przekształcenie jest odczytywane z nazwanego obiektu równorzędnego.

**Przesunięcie** — Przesunięcie w przestrzeni świata w mm na krok (widoczne, gdy Odniesienie ma wartość Wejście).

**Obrót** — Obrót na krok w stopniach dla każdej osi (widoczne, gdy Odniesienie ma wartość Wejście).

**Skaluj** / **Osie skalowania** — Skala jednolita i osiowa stosowana w każdym kroku (widoczne, gdy Odniesienie ma wartość Wejście).

**Nazwa przekształcenia** — Nazwa obiektu równorzędnego, którego przekształcenie jest używane jako przyrost w każdym kroku (widoczne, gdy Odniesienie ma wartość Obiekt).

**Przestrzeń względna** — Gdy opcja jest włączona, przekształcenie każdej kopii kumuluje się w lokalnym układzie poprzedniej kopii; gdy jest wyłączona, każdy krok jest stosowany w przestrzeni świata (widoczne, gdy Odniesienie ma wartość Obiekt).

## Losuj

Włącz **Losuj**, aby dodać zróżnicowanie wszystkim kopiom.

- **Losowe przesunięcie** — Maksymalne losowe przesunięcie pozycji na oś w mm.
- **Losowy obrót** — Maksymalny losowy obrót na oś w stopniach.
- **Osie losowej skali** — Maksymalna losowa zmiana skali na oś.
- **Wyklucz pierwszy** — Zachowuje pierwszą kopię dokładnie w obliczonej pozycji (domyślnie: włączone).
- **Wyklucz ostatni** — Zachowuje ostatnią kopię dokładnie w obliczonej pozycji.
- **Ziarno losowości** — Zmień tę wartość, aby uzyskać inne losowe rozmieszczenie. Obsługuje wyrażenia.

## Scal

- **Utwórz pojedynczą siatkę** — Łączy wszystkie kopie w jeden scalony obiekt siatkowy.
- **Scal wierzchołki** — Zespawa wierzchołki znajdujące się w zadanym progu odległości scalania (widoczne, gdy Utwórz pojedynczą siatkę jest włączone).
- **Odległość** — Próg scalania w mm (widoczne, gdy Scal wierzchołki jest włączone).

## Wskazówki

- Używaj wyrażeń dla parametrów Liczba, Obrót lub Punkt końcowy, aby tworzyć wzory parametryczne
- Do wzorów kołowych używaj trybu Promieniowy — ustaw Promień, aby kontrolować rozmiar okręgu, i włącz Wyrównaj obrót, jeśli kopie mają być skierowane na zewnątrz
- Obrót w trybie Łączenie w trybie Liniowy tworzy spirale i wachlarze bez ręcznego obliczania przesunięć kątowych
- Skala wpływa na offset w naturalny sposób tworzy układy typu muszla łodzika i postęp geometryczny
- Połącz Szyk z operacją [Wybierz element podrzędny](select-child.md), aby tworzyć wzory, w których każda kopia pokazuje inny wariant

## Powiązane

- [Wyrównaj](../placement/align.md) - Pozycjonuje obiekty względem siebie
- [Wybierz element podrzędny](select-child.md) - Wybiera z szyku konkretną kopię według indeksu lub nazwy
