import re

input = input("> ")

if not re.match(r"\d+ \d+ \D+", input):
    print("Falsche Eingabe")
    exit(1)

width, height, char = input.split(" ")
char = char[0]

for i in range(int(height)):
    print(char * int(width))