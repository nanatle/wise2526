l1: list[int] = list(range(1,101))
print(l1)


l2 = l1.copy()
l2.reverse()
print(l2)


index: int = int(input("Index zwischen 0 und 99 wählen: "))
l1.append(l1[index])
l1.remove(l1[index])
print(l1)