from UE9_4 import Person
from datetime import date

geburtstage: list[Person] = []

def laden():
    try:
        with open("Eintraege.txt", "r") as fin:
            for zeilennummer, line in enumerate(fin, start=1):
                try:
                    daten = line.strip().split(",")

                    if len(daten) != 7:
                        raise ValueError("Falsche Anzahl an Feldern")

                    vorname = str(daten[0])
                    nachname = str(daten[1])
                    jahr = int(daten[2])
                    monat = int(daten[3])
                    tag = int(daten[4])
                    telefon = str(daten[5])
                    email = str(daten[6])

                    geburtsdatum = date(jahr, monat, tag)
                    geburtstage.append(
                        Person(vorname, nachname, geburtsdatum, telefon, email)
                    )

                except Exception as e:
                    print(f"Fehler in Zeile {zeilennummer}: {e}")

    except FileNotFoundError:
        print("Datei 'Eintraege.txt' existiert noch nicht.")



def speichern():
    with open("Eintraege.txt", "w") as fin:
        for p in geburtstage:
            gd = p.get_geburtsdatum()
            fin.write(
                f"{p.vorname},{p.nachname},"
                f"{gd.year},{gd.month},{gd.day},"
                f"{p.telefon},{p.email}\n"
            )


def print_menu():
    print(
        "\n(n) neuen Eintrag anlegen"
        "\n(d) einen Eintrag löschen"
        "\n(s) nach einer Person suchen"
        "\n(l) alle Einträge auflisten"
        "\n(b) Geburtstags-Countdown"
        "\n(q) Kalenderprogramm beenden\n" )



def n():
    try:
        vorname = str(input("Vorname: "))
        nachname = str(input("Nachname: "))
        jahr = int(input("Geburtsjahr: "))
        monat = int(input("Geburtsmonat: "))
        tag = int(input("Geburtstag: "))
        telefon = str(input("Telefon: "))
        email = str(input("Email: "))

        geburtsdatum = date(jahr, monat, tag)
        geburtstage.append(Person(vorname, nachname, geburtsdatum, telefon, email))
        speichern()

    except ValueError as e:
        print("Fehler beim Anlegen:", e)


def d():
    if not geburtstage:
        print("Keine Einträge vorhanden.")
        return

    for i, p in enumerate(geburtstage, start=1):
        print(i, ".", p.vorname, p.nachname)

    try:
        index = int(input("Welchen Kontakt löschen?: ")) - 1
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
        print(p)


def s():
    name = input("Nach welchem Nachnamen suchen Sie?: ").lower()
    gefunden = False

    for p in geburtstage:
        if p.nachname.lower() == name:
            print(p)
            gefunden = True

    if not gefunden:
        print("Keine passende Person gefunden.")


def b():
    if not geburtstage:
        print("Keine Einträge vorhanden.")
        return

    heute = date.today()

    for p in geburtstage:
        gd = p.get_geburtsdatum()

        try:
            naechster = date(heute.year, gd.month, gd.day)
        except ValueError:
            naechster = date(heute.year, 3, 1)

        if naechster < heute:
            naechster = date(heute.year + 1, naechster.month, naechster.day)

        tage = (naechster - heute).days

        if tage == 0:
            print(f"Heute ist {p.vorname} {p.nachname}s Geburtstag!")
        else:
            print(f"Noch {tage} Tage bis {p.vorname} {p.nachname}s Geburtstag.")


laden()

while True:
    print_menu()
    wahl = input("Ihre Wahl: ").lower()

    if wahl == "n":
        n()
    elif wahl == "d":
        d()
    elif wahl == "l":
        l()
    elif wahl == "s":
        s()
    elif wahl == "b":
        b()
    elif wahl == "q":
        print("Programm beendet.")
        break
    else:
        print("Ungültige Eingabe!")
