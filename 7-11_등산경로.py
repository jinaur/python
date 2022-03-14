n = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
l = []
for i in range(0, n) :
	a = list(map(int, input().split()))
	l.append(a)

Max = 0
count = 0
Min = 10000
for i in range(0, n) :
	if max(l[i]) > Max :
		Max = max(l[i])
	if min(l[i]) < Min :
		Min = min(l[i])

def route(m, x, y) :
    global count
    if m == Max :
        count += 1
    for i in range(0, 4) : # 4방향으로 가게 함
        xx = x+dx[i] # 좌우
        yy = y+dy[i] # 위아래
        if 0 <= xx <= n-1 and 0 <= yy <= n-1 and m < l[xx][yy] :
            route(l[xx][yy], xx, yy)

for i in range(0, n) :
    if Min in l[i] :
        y = l[i].index(Min)
        x = i
        break


route(Min, x, y)
print(count)

