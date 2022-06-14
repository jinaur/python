n, k = map(int, input().split())

friend = []
for i in range(0, n) :
    f = input()
    friend.append(f)

count = 0
for i in range(0, n) :
    for j in range(1, k) :
        if i-k > 0 and len(friend[i-k]) == len(friend[i]) :
            count += 1
        if i+k < n and len(friend[i+k]) == len(friend[i]) :
            count += 1 
    friend[i] = ""

print(count)
