n, m = map(int, input().split())
a = list(map(int, input().split()))

l = list(range(n))
i = 0
while True :
    count = 0
    for j in range(0, n) :
        if a[0] < a[j] :
            l.append(l[0])
            l.remove(l[0])
            a.append(a[0])
            a.remove(a[0])
            break
        else :
            count += 1
    if count == n :
        a[0] = 0
        i += 1
        if l[0] == m :
            print(i)
            break
	
		