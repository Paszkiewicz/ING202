# Oppgave 1
# ==================
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

#lister()

# Oppgave 2.1
# ==================
def telefonnummer(nr):
    nummer = nr.strip().replace(" ", "").replace("-", "")
    
    if nummer.startswith("+"):
        nummer = nummer[3:]

    if nummer.startswith("00"):
        nummer = nummer[4:]
    
    return nummer

def test_telefonnummer():
    tlf_liste = [
        "12345678",
        "123-45-678",
        "123 45 678",
        "004712345678",
        "+4712345678",
        "+47 123 45 678",
        "+47-123-45-678"
    ]
    for nummer in tlf_liste:
        print(telefonnummer(nummer))

#test_telefonnummer()

# Oppgave 2.2
# ==================
småord = ["og", "eller", "med", "hos", "på", "i"]

def title_case(tekst):
    tekst = tekst.strip().split()
    settning = []
    
    for ord in tekst:
        if ord.lower() in småord:
            settning.append(ord.lower())
        else:
            settning.append(ord.capitalize())

    return " ".join(settning)

#print(title_case("skjønnheten og udyret"))
#print(title_case("huset på prærien"))

def sentence_case(tekst):
    return tekst.capitalize()

#print(sentence_case("skjønnheten og udyret"))
#print(sentence_case("huset på prærien"))

# Oppgave 3.1
# ==================
student_dict = {
    80097 : "Kåre",
    75322 : "Bente",
    59010 : "Fatima",
    69885 : "Nguyen"
}
#print(student_dict[80097])

# Oppgave 3.2
# ==================

def registrer_student():
    while True:
        studentID = int(input("Student ID: "))
        if studentID in student_dict:
            print(f"Student med ID {studentID} er allerede registrert!")

        if studentID not in student_dict:
            studentNavn = input("Student navn: ")
            student_dict[studentID] = studentNavn
            
            break

#print(student_dict)
#registrer_student()
#print(student_dict)

# Oppgave 3.3
# ==================

studenter = [
    {
        "navn": "Kåre",
        "nummer": 80097,
        "fag": ["ing202"],
    }, {
        "navn": "Bente",
        "nummer": 75322,
        "fag": ["ing202", "ing100"],
    }, {
        "navn": "Fatima",
        "nummer": 59010,
        "fag": ["ing0013", "ing202"],
    }, {
        "navn": "Nguyen",
        "nummer": 69885,
        "fag": ["mat101"],
    },
]

def print_student():
    for student in studenter:
        if "ing202" in student["fag"]:
            print(student["navn"])

#print_student()

# Oppgave 4.1
T = { i for i in range(100) }
P = { i for i in T if i % 2 == 0 }
K = { i**2 for i in T if i**2 < 100 }

print(T,"\n")
print(P,"\n")
print(K,"")
