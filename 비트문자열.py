t = int(input())

a = ["0110", "1001"]
for i in range(0, t) :
    rr = ""
    k, l, r = map(int, input().split())
    if k == 1 :
        rr = "01"
    elif k == 2 :
        rr = "0110"
    elif k%2 == 1 :
        for j in range(1, (2**k)//4+1) :
            rr += a[j%2]
    else :
        rr += a[0]
        for j in range(0, (2**k)//4-2) :
            rr += a[1]
        rr += a[0]
    print(rr[l-1:r].count("1"))

