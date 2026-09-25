aantal = int(input("Hoeveel variabelen wil je invullen? "))
variabelen_lijst = []
for i in range(aantal):
    getal = float(input(f"Voer getal {i + 1} in: "))
    variabelen_lijst.append(getal)
gemiddelde = sum(variabelen_lijst) / aantal
print(f"Het gemiddelde is: {gemiddelde:.2f}")
