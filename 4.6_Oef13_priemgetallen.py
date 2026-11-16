limiet = int(input("Geef een limiet hoger dan 1: "))
priemgetallen = []
getal = 2
while getal <= limiet:
    deler = 2
    priemgetal = True
    while deler < getal:
        if getal % deler == 0:
            priemgetal = False
            break
        deler += 1
        if priemgetal:
            priemgetallen.append(getal)

getal += 1


print(priemgetallen)
