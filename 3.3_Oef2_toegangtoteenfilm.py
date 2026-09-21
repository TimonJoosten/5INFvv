leeftijd = int(input("Hoe oud ben je?: "))
if leeftijd >= 16:
    print("Je mag binnen.")
elif leeftijd < 16:
    antwoord = input("Ben je met een volwassene (ja/nee): ").strip().lower()
    if antwoord == "ja":
        print("Je mag naar binnen.")
    else:
        print("Je mag niet naar binnen.")
