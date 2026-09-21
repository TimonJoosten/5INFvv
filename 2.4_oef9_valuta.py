WISSELKOERS_EUR_NAAR_USD = 1.16
bedrag = float(input("Bedrag: "))
bronvaluta = input("Bronvaluta (EUR of USD):").strip().upper()
if bronvaluta == "EUR":
    doelvaluta = "USD"
    resultaat = bedrag * WISSELKOERS_EUR_NAAR_USD
elif bronvaluta == "USD":
    doelvaluta = "EUR"
    resultaat = bedrag / WISSELKOERS_EUR_NAAR_USD
print(f"{bedrag} {bronvaluta} is gelijk aan {resultaat:.2f} {doelvaluta}")