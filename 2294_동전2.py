n, k = map(int, input().split())

l = []
for i in range(0, n) :
    l.append(int(input()))

dp = [10001] * (k+1)
dp[0] = 0

for i in range(0, n) :
    for j in range(l[i], k+1) :
        if dp[j] > 0 :
            dp[j] = min(dp[j], dp[j-l[i]]+1)

if dp[k] == 10001 :
    print(-1)
else :
    print(dp[k]) 

