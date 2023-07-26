a = input()
b = input()
la = len(a)
lb = len(b)

l = []
for i in range(0, la+1) :
    l.append([0]*(lb+1))

for i in range(1, la+1) :
    for j in range(1, lb+1) :
        if a[i-1] == b[j-1] :
            l[i][j] = l[i-1][j-1] +1
        else :
            l[i][j] = max(l[i-1][j], l[i][j-1])

print(l[-1][-1])

