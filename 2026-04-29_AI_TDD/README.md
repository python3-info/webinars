# TDD w Pythonie z AI: szybsze testy, lepsza jakość kodu

* https://github.com/python3-info/webinars/tree/main/2026-04-29_AI_TDD
* https://python3.info/dragon/polish/sprint-01.html
* https://aatc.pl

## Dragon

### Nazwa

* Smok przy tworzeniu ma nazwę
* Smok przy tworzeniu podnosi błąd jeżeli nie ma nazwy

Przygotowanie:

```pycon
>>> from random import seed; seed(0)
>>> from dragon import Dragon

```

Stwórz smoka o nazwie "Wawelski":

```pycon
>>> wawelski = Dragon("Wawelski")

```

Stworzenie smoka bez nazwy podnosi błąd:

```pycon
>>> wawelski = Dragon()
Traceback (most recent call last):
TypeError: Dragon.__init__() missing 1 required positional argument: 'name'

```

### Punkty życia

* Smok przy tworzeniu ma losowe punkty życia z zakresu 50 do 100

Smok przy tworzeniu ma losowe punkty życia:

```pycon
>>> wawelski = Dragon("Wawelski")
>>> wawelski.health
98

```

### Pozycja

* Smok przy tworzeniu zajmuje domyślną pozycję x=0 y=0
* Smok przy tworzeniu może mieć ustawioną dowolną pozycję
* Smok w trakcie gry może zwrócić pozycję którą zajmuje
* Smok w trakcie gry może być ustawiony w dowolne miejsce ekranu
* Smok w trakcie gry może zmienić pozycję w jedną stronę o zadaną wartość (tylko: prawo lub lewo lub góra lub dół)
* Smok w trakcie gry może zmienić pozycję horyzontalnie o zadaną wartość (jednocześnie: prawo i lewo)
* Smok w trakcie gry może zmienić pozycję wertykalnie o zadaną wartość (jednocześnie: góra i dół)
* Smok w trakcie gry może zmienić pozycję dookólnie o zadaną wartość (jednocześnie: prawo i lewo i dół i góra)

Założenia:

* Przyjmij górny lewy róg ekranu za punkt początkowy x=0 y=0
* Idąc w prawo dodajesz x
* Idąc w lewo odejmujesz x
* Idąc w górę odejmujesz y
* Idąc w dół dodajesz y
* Zwróć uwagę, że w grafice komputerowej oś y jest odwrócona

Use case:

Ustaw inicjalną pozycję smoka na x=50, y=100:

```pycon
>>> wawelski = Dragon("Wawelski", position_x=50, position_y=100)

```

* Pobierz aktualną pozycję

```pycon
>>> wawelski.get_position()
(50, 100)

```

* Ustaw nową pozycję smoka na x=10, y=20

```pycon
>>> wawelski.set_position(10, 20)

```

Przesuń smoka w lewo o 10 i w dół o 20:

```pycon
>>> wawelski.move(left=10, down=20)

```

Przesuń smoka w lewo o 10 i w prawo o 15:

```pycon
>>> wawelski.move(left=10, right=15)

```

Przesuń smoka w prawo o 15 i w górę o 5:

```pycon
>>> wawelski.move(right=15, up=5)

```

Przesuń smoka w dół o 5:

```pycon
>>> wawelski.move(down=5)

```
