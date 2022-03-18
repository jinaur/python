dx = [-1, 1]
l = []
for i in range(0, 10) :
	a = list(map(int, input().split()))
	l.append(a)

def ladder(y, x, l) :
    if y == 0 :
        print(x)
        exit()
    for i in range(0, 2) :
        xx = x+dx[i]
        if 0 <= xx < 10 and l[y][xx] == 1 :
            l[y][xx] = 0
            ladder(y, xx, l)
    if l[y-1][x] == 1 :
        l[y-1][x] = 0
        ladder(y-1, x, l)

for i in range(0, 10) :
    if l[9][i] == 2 :
        r = ladder(9, i, l)
