zin = input("Geef een zin: ")
woorden = zin.lower().split()

unieke_lijst = []
#unieke lijst maken met alle verschillende woorden
for woord in woorden:
    if woord not in unieke_lijst:
        unieke_lijst.append(woord)

#per uniek woord tellen hoe vaak het voorkomt
for uniek in unieke_lijst:
    teller = 0
    for woord in woorden:
        if woord == uniek:
            teller = teller + 1
    print(f"{uniek}: {teller}")

        
