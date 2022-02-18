n = int(input())
coins = []
money = [0] * 3 # 3명의 금액
min_difference = 100000000000000 # 최소 차이
for i in range(0, n) :
	coin = int(input())
	coins.append(coin)
	
def DFS(l) :
	global min_difference
	if l == n :
		difference = max(money)-min(money) # 가장큰사람와 가장작은사람의 차이
		if difference < min_difference :
			check = set()
			for x in money : # 3명의총액이 전부다른지 확인
				check.add(x)
			if len(check) == 3 :
				min_difference = difference
	else :
		for i in range(0, 3) :
			money[i] += coins[l] # i번째 사람에게 동전을 줌
			DFS(l+1)
			money[i] -= coins[l] # 끝나고난 후 다시 빼줌
	
DFS(0)
print(min_difference)

