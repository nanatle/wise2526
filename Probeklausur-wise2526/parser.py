#1.1 Count in string

def countIn(text: str, zeichen: str) -> int:
    return text.count(zeichen)

print(countIn("Nana Tle", "e"))


#1.2 Convert input

def convertInput(input_number: str) -> float:
    
    return float(input_number)

print(convertInput("12356432"))