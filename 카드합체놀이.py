n, m = map(int, input().split())
a = list(map(int, input().split()))


for i in range(0, m) :
    a.sort()
    s = a[0] + a[1]
    a[0] = s
    a[1] = s

print(sum(a))

