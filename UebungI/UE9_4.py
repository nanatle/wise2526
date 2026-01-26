from datetime import date

class Person:
    def __init__(
        self,
        vorname: str,
        nachname: str,
        geburtsdatum: date,
        telefon: str,
        email: str
    ):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
        self.telefon = telefon
        self.email = email

    def get_geburtsdatum(self) -> date:
        return self.geburtsdatum

    def __str__(self) -> str:
        return (
            f"{self.vorname} {self.nachname}, "
            f"Tel: {self.telefon}, "
            f"Email: {self.email}, "
            f"Geb.: {self.geburtsdatum}"
        )
