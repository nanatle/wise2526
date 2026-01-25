l1: list[int] = [1, 2, 3, 4]
l2: list [int] = []
l3: list[int] = []
print(l1, l2, l3)

print("--------\n----------")

l2.append(l1[3])
l1.pop(3)
print(l1, l2, l3)
print("--------\n----------")

l3.append(l1[2])
l1.remove(l1[2])
print(l1, l2, l3)

print("--------\n----------")

l3.append(l2[0])
l2.remove(l2[0])
print(l1, l2, l3)
print("--------\n----------")

l2.append(l1[1])
l1.remove(l1[1])
print(l1, l2, l3)
print("--------\n----------")

l1.append(l3[1])
l3.remove(l3[1])
print(l1, l2, l3)
print("--------\n----------")

l2.append(l3[0])
l3.remove(l3[0])
print(l1, l2, l3)
print("--------\n----------")

l2.append(l1[1])
l1.remove(l1[1])
print(l1, l2, l3)
print("--------\n----------")

l3.append(l1[0])
l1.remove(l1[0])
print(l1, l2, l3)
print("--------\n----------")

l1.append(l2[2])
l2.remove(l2[2])
print(l1, l2, l3)
print("--------\n----------")

l3.append(l2[1])
l2.remove(l2[1])
print(l1, l2, l3)
print("--------\n----------")

l3.append(l1[0])
l1.remove(l1[0])
print(l1, l2, l3)
print("--------\n----------")

l1.append(l2[0])
l2.remove(l2[0])
print(l1, l2, l3)
print("--------\n----------")

l2.append(l3[1])
l3.remove(l3[1])
print(l1, l2, l3)
print("--------\n----------")

l2.append(l3[1])
l3.remove(l3[1])
print(l1, l2, l3)
print("--------\n----------")

l3.append(l1[0])
l1.remove(l1[0])
print(l1, l2, l3)
print("--------\n----------")

l1.append(l2[1])
l2.remove(l2[1])
print(l1, l2, l3)
print("--------\n----------")

l3.append(l2[0])
l2.remove(l2[0])
print(l1, l2, l3)
print("--------\n----------")

l3.append(l1[0])
l1.remove(l1[0])
print(l1, l2, l3)
print("--------\nEnde")