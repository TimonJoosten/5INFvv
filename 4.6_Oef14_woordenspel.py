import random
woord = random.choice(["appel", "peer", "kiwi"])
aantal_letters = int(len(woord))
geraden = {}

print(f"Het woord is {woord}") #Voor mezelf om te testen
print("")

levens = 6
while levens > 0:

    weergave = ""

    for letter in woord:
        if letter in geraden:
            weergave += letter
        else:
            weergave += "_"
    print(f"Woord: {weergave}")
    print(f"Levens: {levens}")
    gok = input("Raad een letter: ")
