n = int(input())
a = list(map(int, input().split()))

l = []
for i in range(0, n) :
    for j in range(1, n) :
        aa = a[i:j]
        resaa = aa[::-1]
        Max = -10000000000000
        for k in range(0, n) :
            for kk in range(0, n) :
                if sum(aa[k:kk]) > Max :
                    Max = sum(aa[k:kk])
                if sum(resaa[k:kk]) > Max :
                    Max = sum(resaa[k:kk])
        l.append(Max)

print(max(l))
