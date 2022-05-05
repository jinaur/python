n = int(input())
ans = 0
a = list(map(int,input().split()))
s = []
s.append(a[0])

# 7
# 9 9 4 1 4 9 9

# 9 18 22 23 27 36 45
for i in range(1, n) : # 합을 구해놓음
    s.append(s[i-1]+a[i])

for i in range(1, n) : # 중앙
    ans = max(ans, s[n-2]-a[0]+a[i]) 
    print(s[n-2]-a[0]+a[i])
print()

for i in range(1, n-1) : # 오른쪽
    ans = max(ans, s[i-1] - a[0] + 2*(s[n-1]-s[i]))
    print(s[i-1]-a[0]+2*(s[n-1]-s[i]))

print()
for i in range(1, n-1) : # 왼쪽
    ans = max(ans, 2*s[i-1] + s[n-2] - s[i])
    print(2*s[i-1]+s[n-2]-s[i])

print(ans) 

