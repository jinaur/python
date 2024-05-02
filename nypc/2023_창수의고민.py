n, K = map(int, input().split())
a = list(map(int, input().split()))

dp = []
for i in range(0, n) :
    for j in range(1, n) :
        l = a[:]
        for k in range(i, j) :
            l[k] += K
        l.append(i+1)
        l.append(j)
        if l not in dp :
            dp.append(l)

Max = 0
for i in range(0, len(dp)) :
    count = 0
    for j in range(0, n) :
        for k in range(j+1, n) :
            if dp[i][j] >= dp[i][k] :
                count += 1
    if count > Max :
        Maxi = dp[i][-2]
        Maxj = dp[i][-1]
        Max = count

print(Maxi, Maxj)


 