def bereken_bmi(gewicht, lengte):
    gewicht = int(input("Wat is je gewicht: "))
    lengte = int(input("Wat is je lengte: "))
    bmi = gewicht / (lengte*lengte)
    bmi = float(bmi)
    return bmi

print(bereken_bmi())