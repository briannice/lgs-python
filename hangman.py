from getpass import getpass

print("Hangman")
print("=======")

puzzel = getpass("Puzzel: ")

if len(puzzel) < 3:
    print("De puzzel moet minstens 3 letters lang zijn.")
    quit()

if len(puzzel) > 20:
    print("De puzzel mag maximum 20 letters lang zijn.")
    quit()

levens = 10

oplossing = ""

for letter in puzzel:
    if letter == " ":
        oplossing = oplossing + " "
    else:
        oplossing = oplossing + "*"

correcte_letters = []
incorrecte_letters = []

while puzzel != oplossing and levens > 0:

    print("")
    print("-----------------------------------------")
    print("")
    print(f"         Oplossing: {oplossing}")
    print(f"            Levens: {levens}")
    print(f"  Correcte letters: {correcte_letters}")
    print(f"Incorrecte letters: {incorrecte_letters}")
    print("")

    gok = input("Probeer een letter te raden: ")
    print("")

    if len(gok) == 0:
        print("Je hebt niets ingegeven. Probeer het opnieuw...")
    elif len(gok) > 1:
        print("Je hebt meer dan 1 letter opgeven, probeer het opnieuw...")
    elif gok in correcte_letters:
        print("Je hebt deze letter al geraden.")
    elif gok in incorrecte_letters:
        print("Je hebt deze letter al geraden.")
    else:
        aantal_correcte_gok = 0
        for i in range(len(puzzel)):
            letter = puzzel[i]
            if letter.lower() == gok.lower():
                aantal_correcte_gok = aantal_correcte_gok + 1
                oplossing = oplossing[:i] + letter + oplossing[i + 1:]
        
        if aantal_correcte_gok == 0:
            print(f"Oeps, de letter {gok} zit niet in het woord, probeer het opnieuw...")
            levens = levens - 1
            incorrecte_letters.append(gok)
        else:
            print(f"Joepie, de letter {gok} zit {aantal_correcte_gok} keer in het woord, doe zo verder!")
            correcte_letters.append(gok)

print("")
print("-----------------------------------------")
print("")
if levens == 0:
    print(f"Spijtig, al je levens zijn op... We zochten het woord {puzzel}")
else:
    print(f"Proficiat, je hebt gewonnen. Het juiste woord was inderdaad {puzzel}")

    
