import kollektion
import rekursion
import parser

def menue():
    print("\n")
    print("Welcome to Probeklausur")
    print("Hauptmenü")

    print("1. Kollektion/Tupel")
    print("2. Rekursion")
    print("3. Parser")
    print("4. Programm beenden.")
    print("\n")

def main():
    while True:
        menue()
        choice = int(input("Bitte wählen Sie eine Option (1-4): "))

        if choice == 1:
            print("Kollektion/Tupel:")
            


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

if (__name__ == "__main__"):
    print(main())