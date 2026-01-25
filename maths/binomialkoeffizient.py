res = {}

def binomial (n, k):
    if k == 0 or k ==n:
        return 1
    else:
        t = (n, k)
        if t in res:
            return res[t]
        else:
            t = (n - 1, k)
            r = res[t] if t in res else binomial (*t)
            t = (n - 1, k -1 )
            l = res[t] if t in res else binomial (*t)
            t = (n, k)
            res[t] = r + l
            return res[t]

print(binomial (5, 3))
print(res)