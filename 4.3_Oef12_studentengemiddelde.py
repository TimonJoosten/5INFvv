aantal = int(input("Hoeveel leerlingen zijn er? "))
naam_lijst = []
cijfer_lijst = []

for i in range(aantal):
    naam = (input(f"Voer naam {i + 1} in: "))
    cijfer = float(input(f"Voer cijfer {i + 1} in (op 20): "))
    naam_lijst.append(naam)
    cijfer_lijst.append(cijfer)

gemiddelde = sum(cijfer_lijst) / aantal

bovengemiddeld = []
for naam, cijfer in zip(naam_lijst, cijfer_lijst):
    if cijfer > gemiddelde:
        bovengemiddeld.append(naam)

print(f"Het gemiddelde cijfer is {gemiddelde} Studenten die boven het gemiddelde scoorden: {bovengemiddeld}")


    


