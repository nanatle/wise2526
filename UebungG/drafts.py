class Person:
    def __init__(self, vorname = str, nachname = str, jahr = int, monat = int, tag = int, telefon = str, email = str):
        self.vorname = vorname
        self.nachname = nachname
        self.__jahr = jahr
        self.__monat = monat
        self.__tag = tag
        self.telefon = telefon
        self._email = email

    def get_geburtsdatum(self):
        return self.__jahr, self.__monat, self.__tag

#    def string(self):
        return f"{self.vorname}, {self.nachname}, {self.__jahr}, {self.__monat}, {self.__tag}, {self.telefon}, {self._email}"

geburtstage = {}
datei = "kontakte.txt"

def lade_kontakt():
    try:
        with open(datei, "r") as file:
            for zeile in file:
                zeile = zeile.strip()
                if zeile:
                    try:
                        daten = zeile.split(",")

                        if len(daten) == 7:
                            vorname = daten[0]
                            nachname = daten[1]
                            jahr = int(daten[2])
                            monat = int(daten[3])
                            tag = int(daten[4])
                            telefon = daten[5]
                            email = daten[6]

                            person = Person(vorname, nachname, jahr, monat, tag, telefon, email)
                            key = f"{vorname} {nachname}"
                            kontakte[key] = person
                        else:
                            print("Fehlende Information.")

                    except:
                        print("Fehler: {zeile}")
        print("Kontakte geladen.")
    except:
        print("Fehler aufgetreten.")

def kontakte_speichern():
    try:
        with open(datei, "w") as file:
            for key, person in kontakte.items():
                zeile = f"{person.vorname},{person.nachname}, {person.jahr}, {person.monat}, {person.tag}, {person.telefon}, {person.email}"

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
    with open("kontakte.txt", "r") as fin:
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
