INF = int(1e9)

n, m = map(int, input().split())

l = [[INF]* (n+1) for i in range(0, n+1)]

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if i == j :
            l[i][j] == 0

for i in range(0, m) :
    a, b = map(int, input().split())
    l[a][b] = 1
    l[b][a] = 1


x, k = map(int, input().split())

for i in range(1, n+1) :
    for j in range(1, n+1) :
        for k in range(1, n+1) :
            l[j][k] = min(l[j][k], l[j][i] + l[i][k])

r = l[1][k] + l[k][x]

if r >= INF :
    print(-1)
else :
    print(r)

ㅣ