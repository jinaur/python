n = int(input())

l = []
for i in range(0, n) :
    l.append(int(input()))

l.reverse()

count = 0
for i in range(1, n) :
    if l[i-1] <= l[i] :
        count += l[i] - l[i-1] + 1
        l[i] -= l[i] - l[i-1] + 1

print(count)

