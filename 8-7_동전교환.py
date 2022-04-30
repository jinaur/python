n = int(input())
coin = list(map(int, input().split()))
m = int(input())

List = [1000]*(m+1) # List[j] = j원을 교환해주는데 든 동전의 최소개수
List[0] = 0

for i in range(0, n) :
	for j in range(coin[i], m+1) :
		List[j] = min(List[j], List[j-coin[i]]+1)

print(List[m])
	
 
# List[j-coin[i]]+1 는 j원을 교환해주는데 드는 동전 개수
# 5일때 List[10-5]는 List[5]이고 List[5]는 1이기에 10은 하나 5원을 하나 더해서 동전 2개
