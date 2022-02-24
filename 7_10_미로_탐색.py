dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = []
count = 0
for i in range(0, 7) :
	board.append(list(map(int, input().split())))
board[0][0] = 1 

def DFS(x, y) : # 현재 좌표
	global count
	if x == 6 and y == 6 :
		count += 1
	else :
		for i in range(0, 4) : # 4방향으로 감
			xx = x+dx[i] 
			yy = y+dy[i]
			if 0 <= xx <= 6 and 0 <= yy <= 6 and board[xx][yy] == 0 : # 밖으로 나가지 않게 하고 통로인지 확인
				board[xx][yy] = 1 # 다음 길로 갈때 돌아오지 않게 벽으로 만듬
				DFS(xx, yy)
				board[xx][yy] = 0 # 끝나고 난후 다시 통로로 만들어줌

DFS(0, 0)
print(count)

