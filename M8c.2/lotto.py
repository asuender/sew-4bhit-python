def checkTipp(zahlen: list, tipps: list):
    if len(zahlen) != 7 or len(tipps) != 6:
        raise ValueError("Die Listen habeb eine ungültige Länge.")

    treffer = 0
    for i in range(6):
        if zahlen[i] in tipps:
            treffer += 1
    return treffer

checkTipp([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6])