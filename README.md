# SUDOKU-løser med GUI

Dette er et lite prosjekt jeg gjorde for å repetere python. Programmet er en sudoku-løser med et simpelt GUI for å ha muligheten til å legge inn tall selv som da blir løst når du trykker på "Solve"-knappen.

```java
        new File("outputs").mkdirs();

        if(filename.split("/")[0].equals("inputs"))filename = "outputs/" + filename.split("/")[1];
````
Som oppretter en `outputs`-mappe og bytter ut 'input' i filnavnet med 'output' slik at output-filene blir lagt i en egen mappe. 

Programmet består av:
- `Oblig3.java` som inneholder `main` og kjører sorteringsalgoritmene dine på
  en gitt inputfil.
- `Sorter.java` som er en (abstrakt) klasse, som inneholder hjelpemetoder for å
  telle sammenligninger og bytter. I tillegg inneholder den hjelpemetoder for å
  kunne ta tiden på sorteringen, og returnere resultatene i form av strenger.
- `Insertion.java` som inneholder en implementasjon av insertion sort og arver fra Sorter.
- `Selction.java` som inneholder en implementasjon av selection sort og arver fra Sorter.
- `Quick.java` som inneholder en implementasjon av quicksort og som arver fra Sorter.
- `Heap.java` som inneholder en implementasjon av heap sort og som arver fra Sorter.

- `Oblig3Runner.java` som står for kjøringen av eksperimenter og skriving til
  fil. 

I tillegg finner du en rekke inputfiler i mappen `inputs`. Noen filer er store,
og algoritmene mine er ikke raske nok til å håndtere alle.

I tillegg finner du en rekke outputfiler i mappen `outputs`. Hvor 3 filer med `nearly_sorted_10000` i navnet ikke er komplette fordi de brukte for lang tid.

Ved å kjøre for eksempel:
```sh
$ javac *.java && java Oblig3 inputs/random_100
```

vil du se følgende utskrift:
```
  n, insertion_cmp, insertion_swaps, insertion_time, quick_cmp, quick_swaps, quick_time, selection_cmp, selection_swaps, selection_time, heap_cmp, heap_swaps, heap_time
```

og det vil ligge fem nye filer i `outputs`-mappen:
- `random_100_insertion.out`
- `random_100_quick.out`
- `random_100_heap.out`
- `random_100_results.csv`
- `random_100_selection_out`

Grunnen til den ene finurlige linjen med utskrift er at programmet vil én gang
i sekundet skrive ut en linje som skrives til `csv`-filen. Dette er slik at du
kan se om programmet gjør noen fremgang når du utfører eksperimenter.
