#Kontaktbuch

class Person:
    def __init__(self, vorname: str, nachname: str, jahr: str, monat: str, tag: str, telefon: str, haustier: str):
        self.vorname: str = vorname
        self.nachname: str = nachname
        self._jahr: str = jahr
        self._monat: str = monat
        self._tag: str = tag
        self.telefon: str = telefon
        self.haustier: str = haustier

    def getGeburtstage(self):
        return self._jahr, self._monat, self._tag

geburtstage = {}

def menue():
    print("\n*** Kalendermenü ***")

    print(" (n) neuen Eintrag anlegen "
      "\n (d) einen Eintrag löschen"
      "\n (s) nach einer Person suchen"
      "\n (l) alle Einträge auflisten"
      "\n (q) Kalenderprogramm beenden")

def n():
    vorname = str(input("Vorname? "))
    nachname = str(input("Nachname? "))
    jahr = str(input("Jahr? "))
    monat = str(input("Monat? "))
    tag = str(input("Tag? "))
    telefon = str(input("Telefon? "))
    haustier = str(input("Haustier? "))

    person = Person(vorname, nachname, jahr, monat, tag, telefon, haustier)
    key = vorname + " " + nachname
    geburtstage[key] = person

def d():
    for key, person in geburtstage.items():
        print(key)
    name = str(input("Wer wird gelöscht? -"))
    geburtstage.pop(name)

def s():
    for key, person in geburtstage.items():
        print(key)

    name = str(input("Wen suchst du? -"))
    print(geburtstage[name].getGeburtstage())


def l():
    for key, person in geburtstage.items():
        print(key, person.getGeburtstage(), person.telefon, person.haustier)


def q():
    print("Programm beendet.")



while True:
    menue()
    wahl = str(input("\nWahl: "))

    if wahl == "n":
        n()

    elif wahl == "d":
        d()

    elif wahl == "s":
        s()

    elif wahl == "l":
        l()

    elif wahl == "q":
        q()
        break

    else:
        print("Wahl nicht gefunden.")
