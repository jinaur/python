n, m = map(int, input().split())

l = []
for i in range(0, n) :
    a = list(map(int, input().split()))
    l.append(a)

Max = 0
for i in range(0, n) :
    for j in range(0, n) :
        s1 = l[i][j]
        s2 = l[i][j]
        for k in range(1, m+1) :
            if i+k < n :
                s1 += l[i+k][j]
            if i+k < n and j-k >= 0 :
                s2 += l[i+k][j-k]
            if i+k < n and j+k < n :
                s2 += l[i+k][j+k]
            if j+k < n : 
                s1 += l[i][j+k]
            if i-k >= 0 :
                s1 += l[i-k][j]
            if i-k >= 0 and j+k < n :
                s2 += l[i-k][j+k]
            if i-k >= 0 and j-k >= 0 :
                s2 += l[i-k][j-k]
            if j-k >= 0 :
                s1 += l[i][j-k]
                
        if s1 > Max :
            Max = s1
        if s2 > Max :
            Max = s2

print(Max)

