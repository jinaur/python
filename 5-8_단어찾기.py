n = int(input())

l1 = []
for i in range(0, n) : 
	l1.append(input())

l2 = []	
for i in range(0, n-1) :
    l2.append(input())

for i in range(0, n) :
    count = 0
    for j in range(0, n-1) :
        if l1[i] == l2[j] :
            break
        else :
            count += 1
    if count == n-1 :
        print(l1[i])

