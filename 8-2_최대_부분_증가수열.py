n = int(input())
arr = list(map(int, input().split()))
List = [0]*(n) # 수열의 길이 리스트
result = 0

for i in range(1, n) :
	Max = 0
	for j in range(i-1, 0, -1) : # 뒤에서 부터 시작하기
		if arr[j] < arr[i] and List[j] > Max : # 앞에 원소가 더 작은지 확인
			Max = List[j] 
				
	List[i] = Max+1 # 수열의 마지막 항에 가장 큰수가 붙으니 +1해줌
	if List[i] > result : # 수열의 최대 길이 저장
		result = List[i]
		
print(result)

