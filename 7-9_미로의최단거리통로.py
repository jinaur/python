from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = []
for i in range(0, 7) :
    a = list(map(int, input().split()))
    board.append(a)

l = [[0]*7 for i in range(7)] # 갈때마다 간거리를 저장
q = deque()
q.append((0, 0))
board[0][0] = 1

while q : # 전부 확인하면 빠져나오게 함
    tmp = q.popleft() # 현재 좌표
    for i in range(0, 4) : # 4방향으로 가게 함
        x = tmp[0]+dx[i] # 좌우
        y = tmp[1]+dy[i] # 위아래
        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0 :
            board[x][y] = 1 # 다시 돌아가지않게 벽으로 만듬
            l[x][y] = l[tmp[0]][tmp[1]]+1
            q.append((x, y)) # 바뀐 현재 좌표를 넣어줌

if l[6][6] == 0 : # 도달하지 못했다면 -1
    print(-1)
else :
    print(l[6][6])

