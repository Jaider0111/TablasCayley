def permutaciones(num):
    ans = []
    aux = num[:]
    n = 0
    if len(num) == 1:
        ans.append(num)
        return ans
    for i in range(len(num)):
        aux.remove(num[i])
        for j in permutaciones(aux):
            ans.append([])
            ans[n].append(num[i])
            for p in j:
                ans[n].append(p)
            n += 1
        aux = num[:]
    return ans    

def oper(o1, o2):
    p = [0 for i in range(len(o1))]
    for i in range(len(o1)):
        p[o2[i]-1] = o1[i]
    print(p, end="|")

def cayley(num):
    if len(num) == 0:
        return
    print(" "*(3*len(num[0]))+"|", end="")
    for i in num:
        print(i, end="|")
    print()
    print("-"*((3*len(num[0])+1)*(len(num)+1)))
    for i in num:
        print(i, end="|")
        for j in num:
            oper(i,j)
        print()
        print("-"*((3*len(num[0])+1)*(len(num)+1)))

ent = int(input())
perms = [x for x in range(1,ent+1)]
cayley(permutaciones(perms))
print("Terminamos")