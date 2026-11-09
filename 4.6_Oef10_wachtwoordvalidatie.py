print("Je wachtwoord moet 8 tekens hebben, 1 speciaal teken hebben, minstens 1 cijfer en minstens 1 hoofdletter.")
speciale_tekens = "!@#$%^&*"
while True:
    ingevuld_wachtwoord = input("Vul je nieuw wachtwoord in: ")
    fouten = []

    if not any(teken.isupper() for teken in ingevuld_wachtwoord):
        fouten.append("Minimaal 1 hoofdletter")

    if not any(teken.isdigit() for teken in ingevuld_wachtwoord):
        fouten.append("Minimaal 1 cijfer")

    if not any(teken in speciale_tekens for teken in ingevuld_wachtwoord):
        fouten.append("Minimaal 1 speciaal teken")

    if len(ingevuld_wachtwoord) < 8:
        fouten.append("Minimaal 8 karakters")

    if len(fouten) == 0:
        print("Je wachtwoord is opgeslagen.")
        break
    else:
        print("Ongeldig wachtwoord")
        for fout in fouten:
            print(fout)