#Geburtstagskalender v3

def menue():
    print("\n*** Kalendermenü ***")

    print(" (n) neuen Eintrag anlegen "
      "\n (d) einen Eintrag löschen"
      "\n (s) nach einer Person suchen"
      "\n (l) alle Einträge auflisten"
      "\n (q) Kalenderprogramm beenden")

def n():
    pass

def d():
    pass

def s():
    pass

def l():
    pass

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
