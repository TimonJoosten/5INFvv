tekst = input("Voer een zin in: ")
woorden = tekst.split()

frequentie = {}
for woord in woorden:
    if woord in frequentie:
        frequentie[woord] += 1
    else:
        frequentie[woord] = 1

print(f"{woord}: {frequentie}")