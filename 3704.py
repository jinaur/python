import sys
sys.setrecursionlimit(1000000)
n = int(input())

def r(a, l) :
    if a == 1 :
        l[1] = 1
        return l[1]
    elif a == 2 :
        l[2] = 2
        return l[2]
    elif a == 3 :
        l[3] = 4
        return l[3]
        
    if l[a] :
        return l[a]
    else :
        l[a] = (r(a-3, l)+r(a-2, l)+r(a-1, l)) % 1000
        return l[a]

l = [0 for i in range(n+1)]
print(r(n, l))
