# 7.2 Kontaktbuch mit Dateispeicherung

class Person:
    def __init__(self, vorname, nachname, jahr, monat, tag, telefon, email):
        self.vorname = vorname
        self.nachname = nachname
        self.__jahr = jahr
        self.__monat = monat
        self.__tag = tag
        self.telefon = telefon
        self.email = email
    def get_geburtsdatum(self):
        return self.__jahr, self.__monat, self.__tag


kontakte = {}
datei_name = "kontakte.txt"


# 1. LADE KONTAKTE AUS DATEI (Beim Start)
def kontakte_laden():
    try:
        # Versuche, die Datei zu öffnen
        with open(datei_name, "r") as datei:
            for zeile in datei:
                zeile = zeile.strip()  # Leerzeichen entfernen
                if zeile:  # Nur wenn Zeile nicht leer ist
                    try:
                        # Teile die Zeile an Kommas
                        daten = zeile.split(",")

                        # Stelle sicher, dass alle 7 Teile da sind
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

        print("Kontakte geladen!")
    except:
        print("Ein Fehler ist beim Laden aufgetreten.")


# 2. SPEICHERE KONTAKTE IN DATEI (Beim Beenden)
def kontakte_speichern():
    try:
        with open(datei_name, "w") as datei:
            for key, person in kontakte.items():
                # Schreibe alle Daten in eine Zeile, getrennt durch Kommas
                zeile = f"{person.vorname},{person.nachname},{person.jahr},{person.monat},{person.tag},{person.telefon},{person.email}\n"
                datei.write(zeile)
        print("Kontakte gespeichert!")
    except:
        print("Fehler beim Speichern!")


def kontakt_hinzufuegen():
    print("\n--- Neuer Kontakt ---")
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    jahr = int(input("Geburtsjahr: "))
    monat = int(input("Geburtsmonat (Zahl 1-12): "))
    tag = int(input("Geburtstag: "))
    telefon = input("Telefon: ")
    email = input("Email: ")

    # Erstelle neuen Kontakt
    person = Person(vorname, nachname, jahr, monat, tag, telefon, email)
    key = f"{vorname} {nachname}"
    kontakte[key] = person
    print(f"Kontakt '{key}' wurde hinzugefügt!")


def kontakt_loeschen():
    if not kontakte:
        print("Es gibt keine Kontakte zum Löschen.")
        return

    print("\n--- Kontakt löschen ---")
    print("Verfügbare Kontakte:")
    for key in kontakte.keys():
        print(f"- {key}")

    name = input("Welchen Kontakt löschen? (Vorname Nachname): ")

    if name in kontakte:
        del kontakte[name]
        print(f"Kontakt '{name}' wurde gelöscht!")
    else:
        print(f"Kontakt '{name}' nicht gefunden!")


# 5. ALLE KONTAKTE ANZEIGEN
def kontakte_anzeigen():
    if not kontakte:
        print("Keine Kontakte vorhanden.")
        return

    print("\n--- Alle Kontakte ---")
    for key, person in kontakte.items():
        print(f"\n{key}")
        print(f"  Geburtstag: {person.tag}.{person.monat}.{person.jahr}")
        print(f"  Telefon: {person.telefon}")
        print(f"  Email: {person.email}")

def kontakt_suchen():
    if not kontakte:
        print("Keine Kontakte vorhanden.")
        return

    print("Verfügbare Kontakte:")
    for key in kontakte.keys():
        print(f"- {key}")

    name = input("Wen suchen Sie? (Vorname Nachname): ")

    if name in kontakte:
        person = kontakte[name]
        print(f"\nGefunden: {name}")
        print(f"  Geburtstag: {person.tag}.{person.monat}.{person.jahr}")
        print(f"  Telefon: {person.telefon}")
        print(f"  Email: {person.email}")
    else:
        print(f"Kontakt '{name}' nicht gefunden!")

def hauptmenu():
    print("KONTAKTBUCH")
    print("(n) Neuer Kontakt")
    print("(d) Kontakt löschen")
    print("(a) Alle Kontakte anzeigen")
    print("(s) Kontakt suchen")
    print("(q) Beenden")
    print("=" * 40)
    return input("Deine Wahl: ").lower()


print("Willkommen im Kontaktbuch!")
print("Kontakte werden geladen...")
kontakte_laden()

while True:
    wahl = hauptmenu()

    if wahl == "n":
        kontakt_hinzufuegen()
    elif wahl == "d":
        kontakt_loeschen()
    elif wahl == "a":
        kontakte_anzeigen()
    elif wahl == "s":
        kontakt_suchen()
    elif wahl == "q":
        kontakte_speichern()
        break
    else:
        print("Ungültige Eingabe!")