---
title: Napraw
articleKey: RepairObject3D_2
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: f637470dee4f722b595f07d2da9dcdaac5e8da72
source_lang: en
---
# Napraw

Operacja Napraw usuwa typowe problemy geometrii siatki, w tym krawędzie niebędące rozmaitością, otwory, niespójną orientację ścianek oraz niemal pokrywające się wierzchołki. Jest to szczególnie przydatne w przypadku importowanych plików STL i OBJ, które mogą zawierać błędy.

![20260324 080517 paste 20260324 080517](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080517-paste-20260324-080517.jpg)


## Sposób użycia

1. Wybierz obiekt z problemami siatki
2. Zastosuj operację **Napraw** z menu Siatka
3. Przejrzyj statystyki przed i po, aby zobaczyć, co zostało naprawione

## Statystyki (tylko do odczytu)

- **Wierzchołki początkowe / Wierzchołki końcowe** - liczba wierzchołków przed naprawą i po niej
- **Ściany początkowe / Ściany końcowe** - liczba ścian przed naprawą i po niej
- **Krawędzie początkowe niebędące rozmaitością / Krawędzie końcowe niebędące rozmaitością** - liczba problematycznych krawędzi przed i po

### Opcje zaawansowane

Włącz tryb **Zaawansowane**, aby uzyskać precyzyjną kontrolę:

- **Scal wierzchołki** - scala niemal pokrywające się wierzchołki (domyślnie: włączone)
- **Tolerancja scalania** - jak blisko siebie muszą znajdować się wierzchołki, aby zostały scalone
- **Orientacja ścianki** - odwraca powłoki wywrócone na lewą stronę we właściwą stronę, tak aby każda bryła była odczytywana jako pełna. Każda powłoka jest oceniana osobno, dzięki czemu model wydrążony zachowuje swoje wnęki, zamiast mieć je wypełnione. Powłoki, których ścianki są ze sobą niezgodne, pozostają nietknięte zamiast być zgadywane, a modele, które nie są szczelne, są naprawiane w bardziej tolerancyjny sposób - jeśli sama orientacja ich nie naprawi, uruchom najpierw **Wypełnij otwory**.
- **Scal krawędzie** - naprawia niewielkie pęknięcia i wadliwe szwy
- **Wypełnij otwory** - wypełnia luki w powierzchni siatki
- **Tryb usuwania** - usuwa geometrię wewnętrzną lub zasłoniętą:
  - **Brak** - zachowuje całą geometrię
  - **Wnętrze** - usuwa wewnętrzne bryły ukryte wewnątrz głównego kształtu
  - **Zasłonięty** - usuwa ścianki niewidoczne z zewnątrz

## Wskazówki

- Spróbuj najpierw użyć operacji Napraw, jeśli operacje logiczne (Połącz, Odejmij) dają nieoczekiwane wyniki na importowanych modelach
- Ustawienia domyślne (Scal wierzchołki włączone, reszta wyłączona) usuwają najczęstsze problemy
- Włącz Wypełnij otwory, jeśli widzisz prześwity w modelu
- Użyj opcji Wnętrze w ustawieniu Tryb usuwania, aby oczyścić modele zawierające ukrytą geometrię wewnątrz

## Powiązane

- [Decymacja](decimate.md) - zmniejsza liczbę wielokątów
- [Dodawanie istniejących obiektów](../../getting-started/adding-existing-objects.md) - importuj modele, które mogą wymagać naprawy
