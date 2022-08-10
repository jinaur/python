n = int(input())

l = []
order = [0]*n
for i in range(0, n) :
    a = list(map(int, input().split()))
    a.append(i)
    l.append(a)

for i in range(0, n) :
    count = 1
    for j in range(0, n) :
        if l[i][0] < l[j][0] and l[i][1] < l[j][1] :
            count += 1
    print(count, end= " ")

