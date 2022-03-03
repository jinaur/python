t = int(input())
k = int(input())
coin_list = [] # 동전 금액
coin_number = [] # 동전 갯수
count = 0

for i in range(k) :
	p, n = map(int, input().split())
	coin_list.append(p)
	coin_number.append(n)

def DFS(l, Sum) :
	global count
	if Sum > t : # 거슬러주는돈이 거슬러줘야되는돈을 넘으면 종료
		return
	if l == k : # 동전 가지수를 다하고
		if Sum == t : # 거슬러 주는돈이 거슬러줘야되는돈과 같으면
			count += 1
	else :
		for i in range(0, coin_number[l]+1) :
			DFS(l+1, Sum+(coin_list[l]*i)) # i는 코인 사용 갯수
	
DFS(0, 0)
print(count)

