class Person:

    def __init__(self, vorname : str, nachname : str, jahr: int, monat : int, tage : int, telefon : str, email : str):
        self.vorname = vorname
        self.nachname = nachname
        self.telefon = telefon
        self.email = email

        self.__jahr = jahr
        self.__monat = monat
        self.__tage = tage


    def get_geburtsdatum(self):
        return self.__jahr, self.__monat, self.__tage

geburtstage: dict = {}


def menu():
    return ("\nAuswahl: "
            "\n (n) neuen Eintrag anlegen "
            "\n (d) einen Eintrag löschen "
            "\n (s) nach einer Person suchen "
            "\n (l) alle Einträge auflisten "
            "\n (q) Kalenderprogramm beenden \n")

def n():
    vorname = str(input("Vorname: "))
    nachname = str(input("Nachname: "))
    jahr = int(input("Geburtsjahr: "))
    monat = int(input("Geburtsmonat: "))
    tage = int(input("Geburtstag: "))
    telefon = str(input("Telefon: "))
    email = str(input("Email: "))

    person = Person(vorname, nachname, jahr, monat, tage, telefon, email)
    key = vorname + " " + nachname
    geburtstage[key] = person

def d():
    for key, person in geburtstage.items():
        print( key )
    name = str(input("Welcher Kontakt möchten Sie löschen?"))
    geburtstage.pop(name)

def l():
    for key, person in geburtstage.items():
        print(person.vorname + " " + person.nachname +
              "\n Geburtsdatum: " + str(person.get_geburtsdatum()) +
              "\n Telefon: " + person.telefon +
              "\n Email: " + person.email)


def s():
    for key in geburtstage.keys():
        print(key)
    name = str(input("Wer suchen Sie?"))
    print(geburtstage[name].get_geburtsdatum())
    print(geburtstage[name].vorname + " " + geburtstage[name].nachname + ": "
                "\n Geburtstag: " + str(geburtstage[name].get_geburtsdatum()) +
          "\n Telefon: " + geburtstage[name].telefon +
          "\n Email: " + geburtstage[name].email)

while True:
    e = input(menu())
    if e == "n":
        n()
    elif e == "d":
        d()
    elif e == "l":
        l()
    elif e == "s":
        s()
    elif e == "q":
        break
    else:
        print("not found")