n = int(input())

dx = [-1, 0, 1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]
island_list = []
for i in range(0, n) :
	island = list(map(int, input().split()))
	island_list.append(island)

def DFS(x, y) :
	island_list[x][y] = 0
	for i in range(0, 8) : # 8방향중 섬이 있는곳으로 감
		xx = x+dx[i]
		yy = y+dy[i]
		if 0 <= xx < n and 0 <= yy < n and island_list[xx][yy] == 1 :
			DFS(xx, yy)

count = 0
for i in range(0, n) :
	for j in range(0, n) :
		if island_list[i][j] == 1 :
			DFS(i, j)
			count += 1

print(count)

