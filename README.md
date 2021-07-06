# SUDOKU-løser med GUI

Dette er et lite prosjekt jeg gjorde for å repetere python. Programmet er en sudoku-løser med et simpelt GUI for å ha muligheten til å legge inn tall selv som da blir løst når du trykker på "Solve"-knappen. Appliksjonen er utviklet i Python med pygame for å få til GUI-et.

Programmet består av:
- `main.py` som bare inneholder `main`-klassen som oppretter og kjører app_class-filen
- `app_class.py` som inneholder mesteparten av GUI-elementene og logikken bak den.
- `button.py` som har en klasse med all logikken til knappene i applikasjonen.
- `settings.py` som inneholder diverse verdier som brukes ofte som f.eks dimensjoner på brettet, farger og det 2-dimensjonale arrayet som representerer brettet.
- `solver.py` hvor logikken bak selve sudoku-løsingen ligger.

## Krav
- python3 
- pygame, se [Installer pygame](https://github.com/erikjny/Cocktails#installer-pygame)  

## Programmet kan kjøres med følgende kommando
```
  python main.py
```

### Det burde da se slik ut:

![alt text](https://github.com/erikjny/sudoku/blob/master/sudoku_unsolved.png?raw=true)

### Logikk bak løsingen

Når `Solve`-knappen trykkes kalles `solve_sudoku`-metoden i solve-klassen som forsøker å løse brettet rekursivt. Den bruker noen hjelpemetoder; `isValid` og `find_next_empty` for å "gjette" seg fram til hva som er løsningen og backtracker dersom gjettingen viser seg å være feil. 

### Installer pygame
Den enkleste måten er å installere med pip, som kan installeres gjennom brew.
Dersom brew ikke er installert:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Deretter installer python + pip
```sh
(brew --prefix)/opt/python/libexec/bin
```
Installer pygame
```sh
pip3 install pygame
```
