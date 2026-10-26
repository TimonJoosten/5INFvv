producten = {
    "appel": 0.75,
    "banaan": 1.20,
    "sinaasappel": 1.50,
    "kiwi": 2.00,
    "druiven": 2.50,
    "mango": 1.95,
    "ananas": 3.25
}

dure_producten = {}
boven_waarde = {}
hoofdletters = {}
for item, prijs in producten.items():
    nieuwe_prijs = prijs * 1.05
    nieuwe_prijs = round(nieuwe_prijs, 2)
    dure_producten[item] = nieuwe_prijs

for item, prijs in dure_producten.items():
    if prijs >= 1.50:
        boven_waarde[item] = prijs

for item, prijs in producten.items():
    item = item.upper()
    hoofdletters[item] = prijs

print("Productenlijst:")
print(producten)
print("5 procent duurder")
print(dure_producten)
print("Boven 1.50 euro")
print(boven_waarde)

print(hoofdletters)

        

