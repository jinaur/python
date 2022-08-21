n, m = map(int, input().split())

l = []
# c0 = 0
# c1 = 0
for i in range(0, m) :
    a = list(map(int, input().split()))
    l.append(a)
#     if a[2] == 0 :
#         c0 += 1
#     elif a[2] == 1 :
#         c1 += 1
# if c0 != c1 :
#     print("NO")
#     exit()
if m%2 == 1 :
    print("NO")
    exit()

c = -1
for i in range(0, m) :
    if c == i :
        continue
    for j in range(i+1, m) :
        c = j
        if l[i][1] == l[j][1] :  
            if l[i][2] == l[j][2] :
                print("NO")
                exit()
            if l[i][2] == 1 :
                print("NO")
                exit()
            if l[j][0]-l[i][0] < 60 :
                print("NO")
                exit()
            if l[i][2] == 0 :
                if l[j][2] != 1 :
                    print("NO")
                    exit()

print("YES")

