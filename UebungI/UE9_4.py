class Person:
    def __init__(self, vorname, nachname, jahr, monat, tag, telefon, email):
        self.vorname = vorname
        self.nachname = nachname
        self.__jahr = jahr
        self.__monat = monat
        self.__tag = tag
        self.telefon = telefon
        self.email = email
    def get_geburtsdatum(self):
        return self.__jahr, self.__monat, self.__tag