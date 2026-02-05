kredit: float = 10000
zinssatz: float = 7/100
jahr: int = 0
print("*** Tilgungsplan ***\n")

annuitaet: float = float(input("Eingabe der Annuität: "))

print(f"Kreditsumme: {kredit}, Zinssatz: {zinssatz}, Annuität: {annuitaet}\n")

while kredit > 0:

    zinsen: float = kredit * zinssatz
    tilgung: float = annuitaet - zinsen
    kredit: float = kredit - tilgung

    if zinsen > annuitaet:
        print("Fehler")
        break


    if kredit < 0:
        tilgung: float = tilgung + kredit
        kredit = 0


    print(f"Jahr: {jahr} ---- Restschuld: {round(kredit, 2)} ---- Zinsen: {round(zinsen, 2)} ---- Tilgung: {round(tilgung, 2)}")
    jahr += 1



