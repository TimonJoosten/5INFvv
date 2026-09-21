import random

Getal = random.randint(1,10)
Raadgetal = int(input("Raad eens een getal tussen 1 en 10:"))

if Getal == Raadgetal:
    print("Goed geraden!")
else:
    print(f"Fout, het was {Getal}")