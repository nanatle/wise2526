#Palindrom

def istPalindrom(wort: str) -> bool:
    wort = wort.lower()
    wort = "".join(c for c in wort if c.isalnum())    #isalnum() erlaubt nur Buchstaben und Ziffern

    if wort == wort[::-1]:
        return True

    else:
        return False

print(istPalindrom("Ein Esel lese nie."))

