from datetime import date

class Person:

    def __init__(self, vorname: str, nachname: str, tag: str, monat: str, jahr: str, telefon: str, email: str):
        self.vorname = vorname
        self.nachname = nachname
        self.__jahr = jahr
        self.__monat = monat
        self.__tag = tag
        self.telefon = telefon
        self.email = email


    def get_geburtsdatum(self) -> date:
        return date(self.__jahr, self.__monat, self.__tag)


    def __str__(self) -> str:
        return (
            f"{self.vorname} {self.nachname}, "
            f"Tel: {self.telefon}, "
            f"Email: {self.email}, "
            f"Geb.: {self.geburtsdatum}"
        )
