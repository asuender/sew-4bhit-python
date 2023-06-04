# [EK] 8c.4: Fibonacci-Generator

Andreas Sünder 4BHIT - 04.06.2023

## Fragestellungen

> Schau dir run_generator an: was passiert hier genau? Was ist numbers, was tut next()?

`numbers` ist ein sogenanntes "generator object". Wenn man `next()` aufruft, verhält sich dieser Aufruf so, als würde man diesen auf einen Iterator anwenden; in dem Fall wird der Generator weiter ausgeführt, welcher dann das nächste Elemnent in der Fibonacci-Folge zurückgibt.

> Interpretiere die Ergebnisse: was wurde genau gemessen? Sind die Zeiten so wie erwartet? Wie verändern sich die Zeiten, wenn sich die Untergrenze oder Obergrenze ändert? (Hint: bei größeren Zahlen die langsamste Version weglassen und nur die beiden schnelleren vergleichen)

Output:

```output
Generator...
0.003802750026807189
Iterative...
0.0164902089163661
Recursive...
2.037571083055809
```

Die beiden schnellsten Varianten sind ganz klar der Generator sowie jene, die iterativ arbeitet. Das liegt daran, dass die rekursive Variante die letzten Zwischenergebnisse nicht speichert, sondern immer wieder neu berechnet. Die rekursive Variante ist daher auch bei kleineren Zahlen langsamer als die anderen beiden Varianten.

Wenn man die Grenzen verändert (hier z.B. 11 bis 200), so sieht man einen großen Unterschied beim Generator im Gegensatz zur iterativen Variante:

```output
Generator...
0.03395579196512699
Iterative...
1.4410372080747038
```
