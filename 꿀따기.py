n = int(input())
ans = 0
a = list(map(int,input().split()))
# s = []
# s.append(a[0])

# 7
# 9 9 4 1 4 9 9
# * 9 4 1 4 9 *

for i in range(1, n-1) :
    ans = max(ans, sum(a[1:n-1]) + a[n-i] )

for i in range(1, n-1) : # 왼쪽
    ans = max(ans, sum(a[1:n-i]) - a[n-i-1] + 2*sum(a[n-i:]))

a.reverse() # 뒤집어서 오른쪽
for i in range(1, n-1) :
    ans = max(ans, sum(a[1:n-i]) - a[n-i-1] + 2*sum(a[n-i:]))

print(ans)


# 9 18 22 23 27 36 45
# for i in range(1, n) : # 합을 구해놓음
#     s.append(s[i-1]+a[i])

# for i in range(1, n) : # 벌통위치 중앙
#     ans = max(ans, s[n-1]-a[n-1]-a[0]+a[i])

# # s[i-1] - a[0]는 왼쪽벌이 구하는 꿀
# # + 되는 것은 왼쪽벌이랑 오른쪽벌 둘다 먹을수있기에 곱하기 2
# for i in range(1, n-1) : # 벌통위치 오른쪽
#     ans = max(ans, s[i-1] - a[0] + 2*(s[n-1] - s[i]))

# for i in range(1, n-1) : # 벌통위치 왼쪽
#     ans = max(ans, 2*s[i-1] + s[n-2] - s[i])
# print(ans) 

