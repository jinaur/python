n = int(input())
coin = list(map(int, input().split()))
m = int(input())

def coin_exchange(count, Sum) :
	global Min
	if count > Min : 
		return
	if Sum > m :
		return
	if Sum == m :
		if count < Min : 
			Min = count
	else :
		for i in range(0, n) :
			coin_exchange(count+1, Sum+coin[i]) 

Min = 100000000000 
coin.sort()
coin.reverse()
coin_exchange(0, 0)
print(Min)

