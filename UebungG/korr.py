# 7.2 Kontaktbuch mit Dateispeicherung

class Person:
    def __init__(self, vorname, nachname, jahr, monat, tag, telefon, email):
        self.vorname = vorname
        self.nachname = nachname
        self.jahr = jahr
        self.monat = monat
        self.tag = tag
        self.telefon = telefon
        self.email = email


# Globale Variable für alle Kontakte
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

                    except:
                        print(f"Fehler: Kann diese Zeile nicht lesen: {zeile}")

        print("Kontakte geladen!")
    except FileNotFoundError:
        print("Keine Kontakte-Datei gefunden. Beginne mit leeren Kontakten.")
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


# 3. NEUEN KONTAKT HINZUFÜGEN
def kontakt_hinzufuegen():
    print("\n--- Neuer Kontakt ---")
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")

    # Versuche, Zahlen einzulesen
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


# 4. KONTAKT LÖSCHEN
def kontakt_loeschen():

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


    print("\n--- Alle Kontakte ---")
    for key, person in kontakte.items():
        print(f"\n{key}")
        print(f"  Geburtstag: {person.tag}.{person.monat}.{person.jahr}")
        print(f"  Telefon: {person.telefon}")
        print(f"  Email: {person.email}")


# 6. KONTAKT SUCHEN
def kontakt_suchen():

    print("\n--- Kontakt suchen ---")
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


# 7. HAUPTMENÜ
def hauptmenu():
    print("\n" + "=" * 40)
    print("KONTAKTBUCH")
    print("(n) Neuer Kontakt")
    print("(d) Kontakt löschen")
    print("(l) Alle Kontakte anzeigen")
    print("(s) Kontakt suchen")
    print("(q) Beenden")
    print("=" * 40)

    return input("Deine Wahl: ").lower()


# HAUPTPROGRAMM
print("Kontakte werden geladen...")
kontakte_laden()  # Kontakte beim Start laden

# Hauptschleife
while True:
    wahl = hauptmenu()

    if wahl == "n":
        kontakt_hinzufuegen()
    elif wahl == "d":
        kontakt_loeschen()
    elif wahl == "l":
        kontakte_anzeigen()
    elif wahl == "s":
        kontakt_suchen()
    elif wahl == "q":
        # Kontakte speichern und Programm beenden
        print("Speichere Kontakte...")
        kontakte_speichern()
        print("Auf Wiedersehen!")
        break
    else:
        print("Ungültige Eingabe!")