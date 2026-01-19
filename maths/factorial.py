#Falkutät mit Iteration (Schleifen)
def fact(n):
    f = 1
    for i in range (1, n + 1):
        f = f*i
    return f

x = 5
result = fact(x)
print(result)



print("\n" + "*"*30)



def fact2(n):
    f = 1
    while n > 1:
        f*=n
        n-=1
    return f

y = 5
result2 = fact2(y)
print(result2)

print("\n" + "*"*30)
