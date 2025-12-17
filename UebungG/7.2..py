class Person:
    def __init__(self, vorname = str, nachname = str, jahr = int, monat = int, tag = int, telefon = str, email = str):
        self.vorname = vorname
        self.nachname = nachname
        self.__jahr = jahr
        self.__monat = monat
        self.__tag = tag
        self.telefon = telefon
        self.email = email

    def get_geburtsdatum(self):
        return self.__jahr, self.__monat, self.__tag

geburtstage = []

def speichern():
    with open("geburtsdatum.txt", "w") as fout:
        for p in geburtstage:
            jahr, monat, tag = p.get_geburtsdatum()
            geburtstage.write (f'{p.vorname}, {p.nachname}, {jahr}, {monat}, {tag}, {p.telefon}, {p.email}\n')

def print_menue():
   return "\n (n) neuen Eintrag anlegen \n (d) einen Eintrag löschen \n (s) nach einer Person suchen \n (l) alle Einträge auflisten \n (q) Kalenderprogramm beenden "

def n():
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    jahr = int(input("Geburtsjahr: "))
    monat = int(input("Geburtsmonat: "))
    tag = int(input("Geburtstag: "))
    telefon = input("Telefon: ")
    email = input("Email: ")

    geburtstage.append(Person(vorname, nachname, jahr, monat, tag, telefon, email))
    speichern()


def d():
    i = 1
    while i < (len(geburtstage)+1):
        p = geburtstage[i-1]
        print(i, ". ", p.vorname, p.nachname)
        i += 1

    index = (int(input("Welchen Kontakt wollen Sie löschen?: "))-1)

    if 0 <= index < len(geburtstage):
        geburtstage.pop(index)
        speichern()
    else:
        print("Ungültige Auswahl!")


def l():
    with open("Eintraege.txt", "r") as fin:
        for line in fin:
            print(line.strip())


def s():
    name = input("Nach welchem Nachnamen suchen Sie?: ")
    found = False

    i = 0
    while i < len(geburtstage):
        p = geburtstage[i]
        if p.nachname.lower() == name.lower():
            print(f"{p.vorname} {p.nachname}, Tel: {p.telefon}, Email: {p.email}, Geb.: {p.get_geburtsdatum()}")
            found = True
        i += 1

    if not found:
        print("Keine passende Person gefunden.")


start = True
while start:
    e = input(print_menue())
    if e == "n":
        n()
    elif e == "d":
        d()
    elif e == "l":
        l()
    elif e == "s":
        s()
    elif e == "q":
        start = False
