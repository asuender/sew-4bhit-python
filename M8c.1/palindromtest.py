import re

def ist_palindrom(wort: str):
    wort = wort.lower().strip().replace(" ", "")
    return wort == "".join(reversed(wort))

def ist_satzpalindrom(satz: str):
    satz = satz.lower().strip()
    satz = re.sub(r"[!?.,]", "", satz)

    return ist_palindrom(satz)

def test(func, input: str):
    print(f"{func.__name__}({input}) = {func(input)}")


if __name__ == "__main__":
    test(ist_palindrom, "otto")
    test(ist_satzpalindrom, "Regine, wette weniger!")