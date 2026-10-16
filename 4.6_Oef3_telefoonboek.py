telefoonboek = {} 
afgesloten = False
for beurt in range(1000):
    if not afgesloten:
        print("Telefoonboek Menu:")
        print("1. Contact toevoegen")
        print("2. Contact opzoeken")
        print("3. Contact verwijderen")
        print("4. Alle contacten weergeven")
        print("5. Afsluiten")
        keuze = (input("Kies een optie:"))
        print()
        if keuze == "1":
            naam = input("Wat is de naam: ")
            ingevulde_telefoonnummer = input("Welk telefoonnummer: ")
            telefoonboek[naam] = ingevulde_telefoonnummer
            print(f"{naam} is toegevoegd in je telefoonboek")
            naam.lower()
            
        elif keuze == "2":
            naam = input("Welk contact zoek je: ")
            naam.lower()
            if naam in telefoonboek:
                print(f"{naam}:{telefoonboek[naam]}")
            else:
                print("Contact niet gevonden")
        
        elif keuze == "3":
            naam = input("Welk contact wil je verwijderen: ")
            naam.lower()
            del telefoonboek[naam]

        elif keuze == "4":
            if len(telefoonboek) == 0:
                print("Het telefoonboek is leeg.")
            else:
                print("Telefoonboek: ")
                for naam, nummer in telefoonboek.items():
                    print(f"{naam}: {nummer}")

        elif keuze == "5":
            print("Tot ziens")
            afgesloten = True
        else:
            print("Er is een fout opgetreden.")