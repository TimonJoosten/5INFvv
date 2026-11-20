def filter_even_getallen(lijst):
    evengetal = []
    for getal in lijst:
        if getal % 2 == 0:
            evengetal.append(getal)
    return evengetal

lijst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_even_getallen(lijst))
