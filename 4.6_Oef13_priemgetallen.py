limiet = int(input("Geef een limiet hoger dan 1: "))
priemgetallen = []
getal = 2
while getal <= limiet:
    deler = 1
    restteller = 0
    for deler in range(1, getal + 1):
        if getal % deler == 0:
            restteller += 1
        deler += 1
    if restteller == 2:
        priemgetallen.append(getal)

    getal += 1

print(priemgetallen)

