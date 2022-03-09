n = int(input()) # 코인 개수
coin = list(map(int, input().split())) # 코인 종류
m = int(input()) # 거슬러줄 금액

# count 동전 개수
# Sum 현재 돈
def exchange(count, Sum) :
	global result
	if count > result : # 동전 최소 개수를 넘었을 때
		return
	if Sum > m : # 거슬러줄 돈을 넘었을 때
		return
	if Sum == m : # 현재 돈과 거슬러줄 돈이 같을 때
		if count < result : # 최소 개수 저장
			result = count
	else :
		for i in range(0, n) : # 경우의 수 나눠지기
			exchange(count+1, Sum+coin[i]) 

result = 100000000000 # 최소 동전개수
coin.sort()
coin.reverse() # 큰수부터 시작하게함
exchange(0, 0)
print(result)

