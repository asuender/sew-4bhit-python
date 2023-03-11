import random, re

def checkTipp(zahlen: list, tipps: list):
    if len(zahlen) != 7 or len(tipps) != 6:
        raise ValueError("Die Listen habeb eine ungültige Länge.")

    treffer = 0
    for i in range(6):
        if zahlen[i] in tipps:
            treffer += 1

    if treffer < 3:
        return "Keine Treffer"
    
    nachricht = f"{treffer} übereinstimmende Treffer"

    if zahlen[6] in tipps:
        nachricht += " + Zusatzzahl"

    return treffer

if __name__ == "__main__":
    zahlen = [random.randint(1, 49) for i in range(7)]

    print("Tipp eingeben:", end=" ")
    input = input()
    tipps = [int(i) for i in re.findall(r"\d+", input)]
    
    print(f"Die Zahlen waren: {zahlen}")
    print(checkTipp(zahlen, tipps))