class Person:
    def __init__(self, vorname, nachname, geburtsdatum, telefon, email):
        self.vorname = vorname
        self.nachname = nachname
        self.__geburtsdatum = geburtsdatum  # nicht änderbar
        self.telefon = telefon
        self.email = email

    def show(self):
        return (f"{self.vorname} {self.nachname}, "
                f"Geburtstag: {self.__geburtsdatum}, "
                f"Telefon: {self.telefon}, Email: {self.email}")

kontakte: list = []

def neues_kontakt():
    print("Neuen Kontakt anlegen:")
    v = input("Vorname: ")
    n = input("Nachname: ")
    g = input("Geburtsdatum: ")
    t = input("Telefon: ")
    e = input("Email: ")

    p = Person(v, n, g, t, e)
    kontakte.append(p)
    print("Kontakt gespeichert!\n")


def kontakte_anzeigen():
    if not kontakte:
        print("Keine Kontakte vorhanden.\n")
        return

    print("\n--- Kontaktliste ---")
    for i, p in enumerate(kontakte):
        print(i+1, p.show())
    print()


def kontaktbuch_menu():
    while True:
        print("1 - Neuer Kontakt")
        print("2 - Kontakte anzeigen")
        print("3 - Beenden")

        wahl = input("Auswahl: ")

        if wahl == "1":
            neues_kontakt()
        elif wahl == "2":
            kontakte_anzeigen()
        elif wahl == "3":
            break
        else:
            print("Ungültige Eingabe!\n")