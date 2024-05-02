n = int(input())

xy = []
for i in range(0, n) :
    a = list(map(int, input().split()))
    xy.append(a[::-1])

xy.sort()
for i in range(0, n) :
    xy[i] = xy[i][::-1]

print(xy)

count = 0
for i in range(0, n) :
    for j in range(1, n) :
        if xy[j][0] < xy[j-1][0] :
            x = xy[j][0]
            xy[j][0] = xy[j-1][0]
            xy[j-1][0] = x
            count += 1

print(count)

