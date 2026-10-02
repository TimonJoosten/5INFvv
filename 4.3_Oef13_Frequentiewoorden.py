zin = input("Geef een zin: ")
woordenlijst = []
aantallenlijst = []
eindlijst = []
for woord in range(1):
    woorden = zin.split()
    woordenlijst.append(woorden)
    for woord in woordenlijst:
        aantal = woordenlijst.count(woord)
        aantallenlijst.append(aantal)
        for woord, cijfer in zip(woordenlijst, aantallenlijst):
            eindlijst.append(woord) and eindlijst.append(":") and eindlijst.append(cijfer)


print(f"{zin} Frequentie van woorden {eindlijst} ")