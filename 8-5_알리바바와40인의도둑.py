import sys
sys.setrecursionlimit(1000000)
n = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
stone_list = []
check_list = []
List = []
for i in range(0, n) :
    stone = list(map(int, input().split()))
    check_list.append([0]*n)
    stone_list.append(stone)
    List.append([10]*n)

Min = 10000000000
def DFS(x, y, energy) :
    global Min
    if energy > Min :
        return
    if x == n-1 and y == n-1 :
        if energy < Min :
            Min = energy
        return Min
    for i in range(0, 4) : # 4방향
        xx = x+dx[i]
        yy = y+dy[i]
        if 0 <= xx < n and 0 <= yy < n and check_list[xx][yy] == 0 :
            check_list[xx][yy] = 1
            if List[xx][yy] > energy :
                List[xx][yy] = energy
            energy += stone_list[xx][yy]
            DFS(xx, yy, energy)

DFS(0, 0, stone_list[0][0])
print(Min)
