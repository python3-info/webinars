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

Założenia:

* Górny lewy róg ekranu to punkt x=0 y=0

Ustaw inicjalną pozycję smoka na x=50, y=100:

```pycon
>>> wawelski = Dragon("Wawelski", position_x=50, position_y=100)

```
