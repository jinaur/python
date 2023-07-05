n = int(input())
a = list(map(int, input().split()))

l = [0] * n
l[0] = a[0]
for i in range(1, n) :
    l[i] = max(a[i], l[i-1]+a[i])

print(max(l))
