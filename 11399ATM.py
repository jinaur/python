n = int(input())
p = list(map(int, input().split()))

p.sort()
time = 0
count = 0
for i in range(0, n) :
    time += p[i]
    count += time

print(count)
