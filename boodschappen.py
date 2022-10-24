print("Boodschappenlijst")
print("=================")


boodschappen = []
spelen = True

while spelen:
    print("")
    print("Wat wilt u doen?")
    print("1) Boodschappen tonen")
    print("2) Boodschap toevoegen")
    print("3) Boodschap verwijderen")
    print("4) Programma stoppen")

    keuze = int(input("-> "))

    if keuze == 1:
        print("")
        print(f"Boodschappen: {boodschappen}")
    elif keuze == 2:
        print("")
        nieuwe_boodschap = input("Welke boodschap wilt u toevoegen: ")
        if nieuwe_boodschap in boodschappen:
            print(f"{nieuwe_boodschap} bestaat al")
        else:
            boodschappen.append(nieuwe_boodschap)
            print(f"{nieuwe_boodschap} is toegevoegd")
    elif keuze == 3:
        print("")
        oude_boodschap = input("Welke boodschap wil u verwijderen: ")
        if oude_boodschap not in boodschappen:
            print(f"{oude_boodschap} bestaat niet")
        else:
            boodschappen.remove(oude_boodschap)
            print(f"{oude_boodschap} is verwijderd")
    elif keuze == 4:
        print("")
        print("Tot volgende keer :D")
        spelen = False

