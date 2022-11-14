print("Encrypteren en decrypteren")
print("--------------------------")
print("")
print("Om te encrypteren, kies operatie 'e'.")
print("Om te decrypteren, kies operatie 'd'.")
operatie = input("Operatie (e/d): ")
print("")
zin = input("Geef een zin: ")
print("")

if operatie == "e":
    resultaat = ""
    even_letters = []
    oneven_letters = []
    for i in range(len(zin)):
        if i % 2 == 0:
            even_letters.append(zin[i])
        else:
            oneven_letters.append(zin[i])
    for letter in even_letters:
        resultaat = resultaat + letter
    for letter in oneven_letters:
        resultaat = resultaat + letter
    print(resultaat)
elif operatie == "d":
    resultaat = ""
    aantal_oneven_letters = len(zin) // 2
    aantal_even_letters = len(zin) - aantal_oneven_letters
    even_letters = []
    oneven_letters = []
    for i in range(aantal_even_letters):
        even_letters.append(zin[i])
    for i in range(aantal_even_letters, len(zin)):
        oneven_letters.append(zin[i])
    for i in range(aantal_oneven_letters):
        resultaat += even_letters[i]
        resultaat += oneven_letters[i]
    if aantal_even_letters != aantal_oneven_letters:
        resultaat += even_letters[-1]
    print(resultaat)
else:
    print("Ongeldige operatie...")