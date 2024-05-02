N = int(input())
A = list(map(int, input().split()))
X = max(A)

ans = 0
last = [-1] * (X + 1)
j = 0
for i in range(N):
    j = max(j, last[A[i]] + 1)
    ans = max(ans, i - j + 1)
    last[A[i]] = i

print(ans)

