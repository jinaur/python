import sys

n = int(sys.stdin.readline())

t = []
p = []
l = [0] * (n+1)
for i in range(0, n) :
    a, b =  list(map(int, sys.stdin.readline().split()))
    t.append(a)
    p.append(b)

m = 0
for i in range(0, n) :
    m = max(m, l[i])
    if i+t[i] <= n :
        l[i+t[i]] = max(m+p[i], l[i+t[i]])

print(max(l))

