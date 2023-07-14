# 1 = 1^2
# 2 = 1^2+1^2
# 3 = 1^2+1^2+1^2
# 4 = 2^2
# 5 = 1^2+2^2

n = int(input())

dp = [i for i in range(n+1)]

for i in range(1, n+1) :
    for j in range(1, i) :
        if j**2 > i :
            break
        if dp[i] > dp[i-(j**2)]+1 :
            dp[i] = dp[i-(j**2)]+1

print(dp[n])
