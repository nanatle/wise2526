class Land:
    def __init__(self, name: str, population: int, farbe: str) -> None:
        self.name = name
        self.population = population
        self.farbe = farbe

def sorti(liste):
    n = len(liste)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if liste[j].population < liste[min_index].population:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste


land = []

with open("FunWithFlags.txt", "r") as f:
    for line in f:
        print(line.strip())

with open("FunWithFlags.txt", "r") as f:
    for line in f:
        name, population, farbe = line.strip().split(",")
        land.append(Land(name, int(population), farbe))

sort = sorti(land)


with open("Sorted.txt", "w") as fout:
    for la in sort:
        fout.write(f"{land.name},{land.population},{land.farbe} \n")

with open("Sorted.txt", "r") as fin:
    for line in fin:
        print(line.strip())
