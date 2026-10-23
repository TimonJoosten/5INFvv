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
for item, prijs in producten:
    nieuwe_prijs = prijs * 1.05
    producten[item] = nieuwe_prijs

    if nieuwe_prijs >= 1.50:
        dure_producten.append(item)

print(dure_producten)

        

