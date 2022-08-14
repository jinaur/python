n = int(input())

l = []
for i in range(0, n) :
	a, b = list(map(int, input().split()))
	l.append((a, b))

count = 0

for i in range(0, n) :
    c = 0
    for j in range(0, n) :
        if l[i][0] < l[j][0] and l[i][1] < l[j][1] :
            c += 1
            break
    if c == 0 :
        count += 1

print(count)

