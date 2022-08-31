n = int(input())
a = list(map(int, input().split()))

Max = 0
for i in range(0, n) :
    l = []
    if i >= round(n/2) and Max >= round(n/2) :
        break
    for j in range(i, n) :
        if len(l) > Max and j >= round((n-i)/2) :
            break
        if a[j] in l :
            break
        else :
            l.append(a[j])
    if len(l) > Max :
        Max = len(l)

print(Max)

