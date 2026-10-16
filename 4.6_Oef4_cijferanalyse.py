cijferlijst = {}
aantal_vakken = int(input("Hoeveel vakken in totaal: "))
for beurt in range(aantal_vakken):
    vak = input("Welk vak: ")
    cijfer = float(input("Welk cijfer: "))
    cijferlijst[vak] = cijfer

for cijfer in cijferlijst:
    bewerking = sum(cijfer) / aantal_vakken
    gemiddelde = f"{bewerking:.1f}"
    print(gemiddelde)
    laagste_cijfer = min(cijferlijst.values())
    hoogste_cijfer = max(cijferlijst.values())
    print(f"Het hoogste cijfer is: {hoogste_cijfer}")
    print(f"Het laagste cijfer is: {laagste_cijfer}")
    if cijfer >= 6:
        print(f"Voldoendes: {cijfer}")
    else:
        print(f"Onvoldoende: {cijfer}")


