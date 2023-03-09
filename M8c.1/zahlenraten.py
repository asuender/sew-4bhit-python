import random

number = random.randint(1, 10)
attempts = 1

while True:
    guess = int(input(f"{attempts}. Versuch: Was ist die Geheimzahl? "))

    if guess == number:
        break
        
    elif guess < number:
        print("Die eingegebene Zahl ist zu klein")

    elif guess > number:
        print("Die eingegebene Zahl ist zu groß")

    attempts += 1

print(f"Gratulation! Das Geheimnis {number} wurde nach {attempts} Versuchen erraten.")