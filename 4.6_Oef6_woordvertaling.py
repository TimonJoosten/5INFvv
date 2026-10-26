woordenboek = {
    "hallo": {"Engels": "hello", "Frans": "bonjour", "Duits": "hallo"},
    "wereld": {"Engels": "world", "Frans": "monde", "Duits": "welt"},
}

welk_woord = input("Welk woord wil je vertalen van het Nederlands? ")
welke_taal = input("Naar welke taal (Engels/Duits/Frans)?: ")
welk_woord.lower()
welke_taal.lower()
if welk_woord in woordenboek.items:
    for woord, taal, item in woordenboek.items():
        woordenboek[taal] = item
        print(woordenboek[taal])





else:
    print("Sorry, dit woord staat niet in het woordenboek.")
    
