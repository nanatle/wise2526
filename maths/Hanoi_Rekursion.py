def hanoi(
        n: "Anzahl regelkonform zum Turm gestapelter Scheiben",
        start: "Bezeichnung für die Ausgangsfunktion des Turms",
        ziel: "Bezeichnung für die gewünschte Endposition des Turms",
        frei: "Bezeichnung für die freie Position zur Bewegung des Scheiben"):

    if n > 1:
        hanoi(n - 1, start, frei, ziel)
        hanoi(1, start, ziel, frei)
        hanoi(n - 1, frei, ziel, start)

    elif n == 1:
        print("[ {} -> {} ]".format(start, ziel), end="")

    else:
        print("Sorry, bitte ganze Zahl n>0.")

hanoi(4, 0, 2, 3)