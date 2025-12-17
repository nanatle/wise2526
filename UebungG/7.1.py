with open ("FunWithFlags.txt", "r") as fin:
    for line in fin:
        print(line.strip())

class Land:
    def __init__(self, name: str, bev: int, farbe: str):
        self.name = name
        self.bev = bev
        self.farbe = farbe
laender = []

with open ("FunWithFlags.txt", "r") as f:
    for line in f:
        name, bev, farbe = line.strip().split(",")
        laender.append(Land(name, int(bev), farbe))

def sort(liste):
    n = len(liste)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if liste[j].bev < liste[min_index].bev:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

sortlaender = sort(laender)

with open ("FunWithFlagsSorted.txt", "w") as fout:
    for land in sortlaender:
        fout.write(f"{land.name},{land.bev},{land.farbe} \n")