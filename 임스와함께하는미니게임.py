n, t = input().split()
n = int(n)

l = []
for i in range(0, n) :
    l.append(input())

l = set(l)
l = list(l)

if t == "Y" :
    print(len(l))
elif t == "F" :
    print(len(l)//2)
elif t == "O" :
    print(len(l)//3)
