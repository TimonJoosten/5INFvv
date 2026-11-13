while True:
    getal1 = float(input("Voer het eerste getal in: "))
    operator = input("Voer de operator in (+, -, *, /): ")
    getal2 = float(input("Voer het tweede getal in: "))

    
    if operator == "+":
        bewerking = getal1 + getal2
        print(f"{getal1} {operator} {getal2} = {bewerking}")
    if operator == "-":
        bewerking = getal1 - getal2
        print(f"{getal1} {operator} {getal2} = {bewerking}")
    if operator == "*":
        bewerking = getal1 * getal2
        print(f"{getal1} {operator} {getal2} = {bewerking}")
    if operator == "/":
        bewerking = getal1 / getal2
        print(f"{getal1} {operator} {getal2} = {bewerking}")

     
    extra = input("Wil je nog een bewerking uitvoeren?(ja/nee)").lower()
    if extra == "nee":
          break

    