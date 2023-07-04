t = int(input())

l = []
for i in range(0, 12) :
    l.append(i)
l[2] = 2
l[3] = 4

for i in range(4, 11) :
    l[i] = l[i-1] + l[i-2] + l[i-3]

for i in range(0, t) :
    n = int(input())
    print(l[n])

