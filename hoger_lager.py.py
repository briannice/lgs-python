from random import randint

aantal_kansen = int(input("Hoeveel kansen wil je: "))
hoogste_getal = int(input("Range: "))
print()

random_getal = randint(0, hoogste_getal)
print(f"Random getal: {random_getal}")
print()
ronde = 1
spelen = True

while spelen:
    print(f"Ronde {ronde}")
    print("=======")
    gok = int(input("Doe een gok: "))
    print()

    if gok == random_getal:
        print(f"Je hebt gewonnen!")
        print(f"Het getal was {gok}!")
        print(f"Je deed dit in {ronde} ronden.")
        print()
        spelen = False
    elif ronde == aantal_kansen:
        print(f"Oeps, je hebt verloren!")
        print(f"Het getal was {random_getal}!")
        print()
        spelen = False
    elif gok < random_getal:
        print(f"Het getal dat we zoeken in groter dan {gok}...")
        print(f"Je hebt nog {aantal_kansen - ronde} ronden om het getal te raden!")
        print()
        ronde = ronde + 1
    elif gok > random_getal:
        print(f"Het getal dat we zoeken in kleiner dan {gok}...")
        print(f"Je hebt nog {aantal_kansen - ronde} ronden om het getal te raden!")
        print()
        ronde = ronde + 1
