n = int(input())

l = []
for i in range(0, n) :
    l.append(input())

k = int(input())

for i in range(0, k) :
    a = input()
    if a in l :
        l.remove(a)

print(len(l))
for i in range(0, len(l)) :
    print(l[i])
