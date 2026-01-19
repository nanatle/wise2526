import kollektion
import rekursion
import parser

def menue():
    print("Welcome to Probeklausur")
    print("Hauptmenü")
    print("\n")
    print("1. Kollektion/Tupel")
    print("2. Rekursion")
    print("3. Parser")
    print("4. Programm beenden.")
    print("\n")

def main():
    while True:
        menue()
        try:
            choice = int(input("Bitte wählen Sie eine Option (1-4): "))

            if choice == 1:
                print("Kollektion/Tupel")
                kollektion.run_all()

            elif choice == 2:
                print("Rekursion")
                rekursion.run_all()

            elif choice == 3:
                print("Parser")
                parser.run_all()

            elif choice == 4:
                print("Programm beenden")

            else:
                print("Ungültige Eingabe: {choice}.")

        except Exception as e:
            print("Fehler aufgetrete: {e}.")