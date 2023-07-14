n, k = map(int, input().split())

c = []
for i in range(0, n) :
    c.append(int(input()))

dp = [0]*(k+1)
dp[0] = 1
for i in range(0, n) :
    for j in range(0, k+1) :
        if j-c[i] >= 0 :
            dp[j] += dp[j-c[i]]

print(dp[k])
