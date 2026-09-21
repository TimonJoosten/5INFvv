bedrag = float(input("Hoeveel kost het: "))
if bedrag > 100:
    bedrag100 = bedrag * 0.9
    print("Je krijgt 10% korting.")
    print(f"{bedrag100:.2f} is je nieuwe prijs")
if bedrag > 50 and bedrag <= 100:
    bedrag50 = bedrag * 0.95
    print("Je krijgt 5% korting.")
    print(f"{bedrag50:.2f} is je nieuwe prijs.")
else:
    print("Je krijgt geen korting.")
    print(f"{bedrag:.2f} dit is het prijs.")
