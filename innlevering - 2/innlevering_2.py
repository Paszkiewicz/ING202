# Oppgave 1
def lister():
    liste = []

    while True:
        tall = int(input("Skriv inn et positivt tall."))

        if tall == 0:
            liste.append(tall)
            break
        else:
            liste.append(tall)
    
    tall2 = int(input("Hva vil du dele på?"))
    liste2 = []
    liste3 = []
    for tall in liste:
        if tall % tall2 == 0:
            liste2.append(tall)
        else:
            liste3.append(tall)

    print(f"Tall som er delelig med {tall2} \n{liste2}")
    print(f"Tall som ikke er delelig med {tall2} \n{liste3}")

lister()