#Geburtstagskalender v1

name: str = str
jahr: str = str
monat: str = str
tag: str = str

geburt: tuple = (jahr, monat, tag)
kontakt: dict[str: str] = {name: geburt}


leute: dict = {"thu ha": ("2003", "09", "05"),
               "feyza": ("2004", "02", "22"),
               "ange": ("2005", "05", "14"),
               "lisa": ("2005", "01", "20"),
               "nisreen": ("2004", "08", "29")}

print("\nGeburtsdaten: ")
print(leute)

leute.pop('thu ha')
leute.pop('feyza')
print("\nNach dem Löschen: ", leute)