import random
lijst = []

for i in range(10):
    lijst.append(random.randint(1,100))

print(lijst)

max = lijst[0]
min = lijst[0]

for getal in lijst:
    if getal > max:
        max = getal
    if getal < min:
        min = getal
        
    
print(f"Het minimum is {min}")
print(f"Het maximum is {max}")
    
        
