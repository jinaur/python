n, m = map(int, input().split())

l = []
for i in range(0, n) :
    a = list(map(int, input().split()))
    l.append(a)

count = 0
nl = []
sl = []
for i in range(0, m) :
    x = i
    y = 0
    if l[i] == "X" :
        count += 1
        nl.append(i+1)
        for j in range(0, n) :
            if l[x+1][y+1] == "X" :
            