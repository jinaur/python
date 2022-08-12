n, m = map(int, input().split())
a = list(map(int, input().split()))

count = 0
for i in range(0, n) :
    if a[i] == 0 :
        continue
    Max = 0
    Maxj = 0
    for j in range(0, n) :
        if Max < a[i]+a[j] and a[i]+a[j] <= m and i != j :
            Max = a[i]+a[j]
            Maxj = j

    if Max != 0 :
        a[i] = 0
        a[Maxj] = 0
        count += 1
	
print(count)

