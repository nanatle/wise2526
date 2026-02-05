wort: str = str(input("das zu erratende Wort: ")).lower()
anzeige: str = "-" * len(wort)
fehler: int = 0
print("\n"*10)


while "-" in anzeige:
    print("Rate jetzt! Das Wort: ", anzeige)
    raten: str = str(input("Buchstabe: "))

    if raten in wort:
        neu = ""

        for i in range(len(wort)):

            if wort[i] == raten:
                neu = neu + wort[i]

            else:
                neu = neu + anzeige[i]

        anzeige = neu

    else:
       fehler = fehler + 1
       print("Falsch, Fehlversuch: ", fehler)

print("Glückwunsch, das Wort war: ", wort)
