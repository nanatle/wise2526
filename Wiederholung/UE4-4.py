name: str = str(input("Wer (Vor + Nachname): "))
tag: str = str(input("Tag: "))
monat: str = str(input("Monat: "))
jahr: str = str(input("Jahr: "))
geburtsdatum: dict = {name: (jahr, monat, tag)}

print(geburtsdatum)