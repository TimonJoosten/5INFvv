woordenboek = {
    "hallo": {
        "Engels": "hello",
        "Frans": "bonjour",
        "Duits": "hallo"
    },
    "wereld": {
        "Engels": "world",
        "Frans": "monde",
        "Duits": "Welt"
    },
    "boek": {
        "Engels": "book",
        "Frans": "livre",
        "Duits": "Buch"
    },
    "kat": {
        "Engels": "cat",
        "Frans": "chat",
        "Duits": "Kat"
    },
    "hond": {
        "Engels": "dog",
        "Frans": "chien",
        "Duits": "Hund"
    }
}


welk_woord = input("Welk woord wil je vertalen van het Nederlands? ")
welke_taal = input("Naar welke taal (Engels/Duits/Frans)?: ")
welk_woord = welk_woord.lower()
welke_taal = welke_taal.capitalize()
if welk_woord in woordenboek.keys():
    if welke_taal in woordenboek[welk_woord]:
        print("De vertaalde versie is:")            
        print(woordenboek[welk_woord][welke_taal])
    else:
        print("Sorry, deze taal staat niet in het woordenboek.")
else:
    print("Sorry, dit woord staat niet in het woordenboek.")
    
