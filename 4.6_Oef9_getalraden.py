import random
geheim_getal = random.randint(1, 100)

pogingen = 0

print("Raad het geheime getal tussen 1 en 100!")

while True:
    pogingen += 1
    gok = (input("Jouw gok of geef op met q: "))

    if gok != "q":
        int(gok)
    
    if gok == "q":
        print(f"Je hebt opgegeven, het getal was {geheim_getal}")
        break
        
    int(gok)
    
    if gok < geheim_getal:
        print("Te laag!")
    if gok > geheim_getal:
        print("Te hoog!")
    else:
        print(f"Gefeliciteerd! Je hebt het geheime getal {geheim_getal} geraden in {pogingen} pogingen.")
        break