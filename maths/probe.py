#Youtube: Teluska
#l1: list[int] = [3,6,8,5,99]
#l2: list[str] = ['name','age']

#del l1[2:]
#print(l1)
#print(l2)

#funktion
def greet ():
    print("Hello, world!")
    print("My name is Angelina.")
greet()
#greet() -> show the function one more time

def add(x, y):
    c = x + y
#   print(c)
    return c
#add(5,4)
result = add(5,4)
print (result)


def add_sub(x, y):
    c = x - y
    d = x + y
    return c, d

result1, result2 = add_sub(5,4)
print(result1, result2)

print("\n" + "+"*30)

def update(x):
    x = 8
    print("x", x)

a = 10
update(a)
print("a ", a)