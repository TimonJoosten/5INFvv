print("Telefoonboek Menu:")
print("1. Contact toevoegen")
print("2. Contact opzoeken")
print("3. Contact verwijderen")
print("4. Alle contacten weergeven")
print("5. Afsluiten")
keuze = int(input("Kies een optie:"))
contact = {} 
for keuze in range(1):
    if keuze == 1:
        ingevulde_naam = input("Wat is de naam: ")
        ingevulde_telefoonnummer = input("Welk telefoonnummer: ")
        contact["naam"] = ingevulde_naam
        contact["telefoonnummer"] = ingevulde_telefoonnummer
        print(f"{ingevulde_naam} is toegevoegd in je telefoonboek")
        nieuwcontact = input("Wil je nog een contact toevoegen (ja/nee): ")
        if nieuwcontact == "nee":
            
    if keuze == 2:
        gezochte_naam = input("Welk contact zoek je: ")
        if gezochte_naam not in contact:
            print("Deze persoon staat niet in je contacten")
        else:
            print(f"Het telefoonnummer is:")



    
