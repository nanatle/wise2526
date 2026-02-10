#1.1 Count in string

def countIn(text: str, zeichen: str) -> int:
    return text.count(zeichen)

txt = "Zur Kreuzung? Gut. Durch die Tür hinaus, zur linke Reihe, jeder nur ein Kreuz."
print(txt)
print("Zeichen 'K' zählen:", countIn(txt, "K"))
print("\n*****")



#1.2 Convert input

def convertInput(input_number: str) -> float:
    while True:
        try:
            return float(input_number)

        except Exception as e:
            print(e)
            input_number = input("Geben Sie den richtigen Zeichen ein: ")

p = str(input("Geben Sie einen nummerische String ein: "))
print("Umgewandelt: ", convertInput(p))
print("\n*****")



#1.3 String teilung

def teileString(text: str, zeichen: str) -> list:
   if len(zeichen) != 1:
       return []

   return text.split(zeichen)

txt = "Wie heißt ein Bär, der fliegen kann? Hubschraubär"
print("Original: ", txt)
print("-> ", teileString(txt, "??"))
