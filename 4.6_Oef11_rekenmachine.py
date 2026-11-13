getal1 = int(input("Voer het eerste getal in: "))
operator = input("Voer de operator in (+, -, *, /): ")
getal2 = int(input("Voer het tweede getal in: "))

while True:
    if operator == "+":
        bewerking = getal1 + getal2
    if operator == "-":
        bewerking = getal1 - getal2
    if operator == "*":
        bewerking = getal1 * getal2
    if operator == "/":
        bewerking = getal1 / getal2

    print(bewerking)