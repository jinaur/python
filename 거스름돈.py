n = int(input())

coin = [500, 100, 50, 10, 5, 1]
count = 0
m = 1000-n
for i in range(0, 6) :
    count += m//coin[i]
    m %= coin[i]

print(count)

