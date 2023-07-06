import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

l = [0]
s = 0
for i in range(0, n) :
    s += a[i]
    l.append(s)


for k in range(0, m) :
    i, j = map(int, sys.stdin.readline().split())
    print(l[j]-l[i-1])

