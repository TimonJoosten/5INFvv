lengte = int(input("Welke lengte wil je: "))
breedte = int(input("Welke breedte wil je: "))

for rij in range(lengte):
    regel = ""
    for kolom in range(breedte):
        regel = regel + "*"
        print(regel)