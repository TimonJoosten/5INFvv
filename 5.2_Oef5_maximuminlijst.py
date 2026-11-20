def vind_maximum(getallen):
    maximum = getallen[0]
    for getal in getallen:
        if getal > maximum:
            maximum = getal
    return maximum

lijst = [12,55,77,14,59]
print(vind_maximum(lijst))
