#Buchstaben zählen

def buchstabe(text: str, zeichen: str) -> int:
    if zeichen in text:
        return text.count(zeichen)

    else:
        print(f"Buchstabe {zeichen} nicht gefunden!")
        return 0

texte = "Thu Haa"
print(buchstabe(texte,"i"))