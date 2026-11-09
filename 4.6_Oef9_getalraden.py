import random
geheim_getal = random.randint(1, 100)

pogingen = 0

print("Raad het geheime getal tussen 1 en 100!")


while True:
    gok = input("Jouw gok of geef op met q: ")

    if gok == "q":
        print(f"Je hebt opgegeven, het getal was {geheim_getal}")
        break

    gok = int(gok)
    pogingen += 1

    if gok < geheim_getal:
        print("Te laag!")

    elif gok > geheim_getal:
        print("Te hoog!")

    else:
        print(f"Gefeliciteerd! Je hebt het geheime getal {geheim_getal} geraden in {pogingen} pogingen.")
        break