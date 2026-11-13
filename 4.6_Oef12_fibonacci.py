limiet = int(input("Wat is het limiet: "))
getal1 = 0
getal2 = 1
fibonacci = []

while True:
    if getal1 <= limiet:
        resultaat = getal1 + getal2
        fibonacci.append(getal1)
        getal1 = getal2
        getal2 = resultaat
    if getal1 > limiet:
        print(fibonacci)
        break




