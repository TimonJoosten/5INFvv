cijferlijst = {}
alle_cijfers = []

aantal_vakken = int(input("Hoeveel vakken in totaal: "))
if aantal_vakken > 0:
    for beurt in range(aantal_vakken):
        vak = input("Welk vak: ")
        cijfer = float(input("Welk cijfer: "))
        cijferlijst[vak] = cijfer
        alle_cijfers.append(cijfer)
    
    laagste_cijfer = min(cijferlijst, key=cijferlijst.get)
    hoogste_cijfer = max(cijferlijst, key=cijferlijst.get)
    print(f"Het hoogste cijfer is: {cijferlijst[hoogste_cijfer]}, {hoogste_cijfer}")
    print(f"Het laagste cijfer is: {cijferlijst[laagste_cijfer]}, {laagste_cijfer}")
    
    bewerking = sum(alle_cijfers) / aantal_vakken
    gemiddelde = f"{bewerking:.1f}"
    print(f"Het gemiddelde is: {gemiddelde}")


    print("Voldoendes:")
    for vak, cijfer in cijferlijst.items():
            if cijfer >= 6:
                print(f"{vak}")
    print("Onvoldoendes:")        
    for vak, cijfer in cijferlijst.items():
            if cijfer < 6:
                print(f"{vak}")
else:
    print("Er is een fout opgetreden.")


