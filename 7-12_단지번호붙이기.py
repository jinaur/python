n = int(input())
home_list = [list(map(int, input())) for _ in range(n)]
result = [] 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y) :
	global count
	count += 1
	home_list[x][y] = 0
	for i in range(0, 4) :
		xx = x+dx[i]
		yy = y+dy[i]
		if 0 <= xx < n and 0 <= yy < n and home_list[xx][yy] == 1 :
			DFS(xx, yy)
	
for i in range(0, n) :
	for j in range(0, n) :
		if home_list[i][j] == 1 :
			count = 0
			DFS(i, j)
			result.append(count)

print(len(result))
result.sort() # 오름차순으로 정렬한후 한줄씩 출력
for i in range(0, len(result)) :
	print(result[i])
	
