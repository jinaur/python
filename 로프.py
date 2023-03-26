n = int(input())

l = []
for i in range(0, n) :
    l.append(int(input()))

l.sort()
Max = 0
for i in range(0, n) :
    if l[i]*(n-i) > Max :
        Max = l[i]*(n-i)

print(Max)

