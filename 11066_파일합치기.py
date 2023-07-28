import sys
input = sys.stdin.readline

t = int(input())
for _ in range(0, t):
    k = int(input())
    a = list(map(int, input().split()))
    dp = [[0]*(k) for i in range(0, k)]
    
    for i in range(0, k-1) :
        dp[i][i] = a[i]+a[i+1]
        for j in range(i+2, k):
            dp[i][j-1] = dp[i][j-2] + a[j]

    for v in range(2,k) :
        for i in range(0, k-v) :
            j = i+v
            dp[i][j-1] += min([dp[i][K-1] + dp[K+1][j-1] for K in range(i,j)])
    
    print(dp[0][k-2])
