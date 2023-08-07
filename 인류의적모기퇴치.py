def listhandler(a, b, l) :
    try :
        if a < 0 or b < 0 :
            return 0
        return l[a][b]
    except :
        return 0 

n, m = map(int, input().split())

l = []
for i in range(0, n) :
    l.append(list(map(int, input().split())))

if m == 0 :
    print(max(sum(l, [])))
else :
    Max = sum(sorted(sum(l, []), reverse=True)[0:m*4+1])
    largest = 0
    a = 0
    p = False
    for i in l :
        b = 0
        for j in i :
            cross = 0
            diagonal = 0
            for k in range(1, m+1) :
                # 상하좌우
                cross += listhandler(a+i, b, l)
                cross += listhandler(a-i, b, l)
                cross += listhandler(a, b+i, l)
                cross += listhandler(a, b-i, l)
                # 대각선
                diagonal += listhandler(a+i, b+i, l)
                diagonal += listhandler(a+i, b-i, l)
                diagonal += listhandler(a-i, b+i, l)
                diagonal += listhandler(a-i, b-i, l)
            # 현재 자리
            cross += listhandler(a, b, l)
            diagonal += listhandler(a, b, l)
            b += 1
            if max(cross, diagonal) == Max :
                print(max(cross, diagonal))
                p = True
                break
            elif max(cross, diagonal) > largest :
                largest = max(cross, diagonal)
        a += 1
    if not p :
        print(largest)

    

