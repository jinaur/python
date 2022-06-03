n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(0, n)]

house = [] # 집 좌표 리스트
pizza = [] # 가게 좌표 리스트
combination = [0] * m # 선택된 피자집 조합 저장
Min = 100000000000
for i in range(0, n) :
	for j in range(0, n) :
		if l[i][j] == 1 :
			house.append((i, j))
		elif l[i][j] == 2 :
			pizza.append((i, j))
	
def DFS(L, s) :
	global Min
	if L == m : 
		Sum = 0
		for j in range(0, len(house)) :
			# 집 위치
			housex = house[j][0]
			housey = house[j][1] 
			distance = 100000000000 # 배달 거리
			for x in combination :
				# 피자가게 위치
				pizzax = pizza[x][0] 
				pizzay = pizza[x][1] 
				distance = min(distance, abs(housex-pizzax)+abs(housey-pizzay)) # 최소 배달 거리
			Sum += distance
		if Sum < Min : # 가장 적은 배달거리의 총합 저장
			Min = Sum
	else :
		for i in range(s, len(pizza)) :
			combination[L] = i # 피자집 선택
			DFS(L+1, i+1) 

DFS(0, 0)
print(Min)

