from UE9_4 import Person
from datetime import date

geburtstage = []

def laden():
    geburtstage.clear()

    try:
        with open("Eintraege.txt", "r") as fin:
            zeilennummer = 0
            for line in fin:
                zeilennummer += 1
                try:
                    daten = line.strip().split(",")

                    if len(daten) != 7:
                        raise ValueError("Falsche Anzahl an Feldern")

                    vorname = daten[0]
                    nachname = daten[1]
                    jahr = int(daten[2])
                    monat = int(daten[3])
                    tag = int(daten[4])
                    telefon = daten[5]
                    email = daten[6]

                    p = Person(vorname, nachname, jahr, monat, tag, telefon, email)
                    geburtstage.append(p)

                except Exception as e:
                    print(f"Fehler in Zeile {zeilennummer}: {line.strip()}")
                    print(f"→ Datensatz übersprungen ({e})")

    except FileNotFoundError:
        print("Datei 'Eintraege.txt' existiert noch nicht.")


# ===================== DATEI SPEICHERN =====================

def speichern():
    with open("Eintraege.txt", "w") as fout:
        for p in geburtstage:
            jahr, monat, tag = p.get_geburtsdatum()
            fout.write(f"{p.vorname},{p.nachname},{jahr},{monat},{tag},{p.telefon},{p.email}\n")


# ===================== MENÜ =====================

def print_menu():
    return (
        "\n(n) neuen Eintrag anlegen"
        "\n(d) einen Eintrag löschen"
        "\n(s) nach einer Person suchen"
        "\n(l) alle Einträge auflisten"
        "\n(b) Geburtstagen Countdown"
        "\n(q) Kalenderprogramm beenden\n"

    )

def n():
    try:
        vorname = input("Vorname: ")
        nachname = input("Nachname: ")
        jahr = int(input("Geburtsjahr: "))
        monat = int(input("Geburtsmonat: "))
        tag = int(input("Geburtstag: "))
        telefon = input("Telefon: ")
        email = input("Email: ")

        geburtstage.append(Person(vorname, nachname, jahr, monat, tag, telefon, email))
        speichern()

    except ValueError as e:
        print("Fehler beim Anlegen des Eintrags:", e)


def d():
    if not geburtstage:
        print("Keine Einträge vorhanden.")
        return

    for i, p in enumerate(geburtstage, start=1):
        print(i, ".", p.vorname, p.nachname)

    try:
        index = int(input("Welchen Kontakt wollen Sie löschen?: ")) - 1
        if 0 <= index < len(geburtstage):
            geburtstage.pop(index)
            speichern()
        else:
            print("Ungültige Auswahl!")
    except ValueError:
        print("Bitte eine Zahl eingeben!")


def l():
    if not geburtstage:
        print("Keine Einträge vorhanden.")
        return

    for p in geburtstage:
        print(f"{p.vorname} {p.nachname}, Tel: {p.telefon}, "
              f"Email: {p.email}, Geb.: {p.get_geburtsdatum()}")


def s():
    name = input("Nach welchem Nachnamen suchen Sie?: ").lower()
    gefunden = False

    for p in geburtstage:
        if p.nachname.lower() == name:
            print(f"{p.vorname} {p.nachname}, Tel: {p.telefon}, "
                  f"Email: {p.email}, Geb.: {p.get_geburtsdatum()}")
            gefunden = True

    if not gefunden:
        print("Keine passende Person gefunden.")

def b():
    heute = date.today()
    for p in geburtstage:
        geb = date(heute.year, p.get_monat(), p.get_tag())
        if geb < heute:
           geb = date(heute.year + 1, p.get_monat(), p.get_tag())
        noch = (geb - heute).days
        if noch == 0:
            print(f"Heute ist {p.vorname} {p.nachname}s Geburtstag! ")
        else:
            print(f"Noch {noch} Tage bis {p.vorname} {p.nachname}s Geburtstag.")