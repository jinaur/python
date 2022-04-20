m, n = map(int, input().split())

dx = [-1, 0, 1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]
tomato_list = []
list1 = []
for i in range(0, n) :
	tomato = list(map(int, input().split()))
	tomato_list.append(tomato)
	for j in range(0, n) :
		if tomato[j] == 1 :
			list1.append((i, j))

def DFS(x, y, j) :
    for i in range(0, 8) : # 4방향중 안 익은곳으로 감
        xx = x+dx[i]
        yy = y+dy[i]
        if 0 <= xx < m and 0 <= yy < n and tomato_list[xx][yy] == 0 :
            tomato_list[xx][yy] = j
            DFS(xx, yy, j+1)

for i in range(0, len(list1)) :
    DFS(list1[i][0], list1[i][1], 1)

print(tomato_list)