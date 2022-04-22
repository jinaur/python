import sys
sys.setrecursionlimit(100000)
n = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
land_list = []
Min_list = [] 
for i in range(0, n) :
	land = list(map(int, input().split()))
	land_list.append(land)
	for j in range(0, n) :
		Min_list.append(land[j])

Min_list.sort()
Min_list = set(Min_list)
Min_list = list(Min_list)
def DFS(x, y, h) :
	for i in range(0, 4) :
		xx = x+dx[i]
		yy = y+dy[i]
		if 0 <= xx < n and 0 <= yy < n and check[xx][yy] == 0 and land_list[xx][yy] > h :
			check[xx][yy] = 1
			DFS(xx, yy, h)

Max = 0 
for h in Min_list :
	count = 0 
	check = [[0]*n for i in range(0, n)]
	for i in range(0, n) :
		for j in range(0, n) :
			if check[i][j] == 0 and land_list[i][j] > h :
				count += 1
				DFS(i, j, h)
	if count > Max :
		Max = count
	if count == 0 :
		break

print(Max)

