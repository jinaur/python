n, m = map(int,input().split())
result = [0]*(n+1) # 번호를 저장할 리스트
count = 0 # 총 경우의 수

def find_combination(l, s) :
	global count
	if l == m : # m 까지 갔는지 확인
		for i in range(l) : 
			print(result[i], end=" ") # 번호 출력
		print()
		count += 1 
	else :
		for i in range(s, n+1) : 
			result[l] = i # 번호 저장
			find_combination(l+1, i+1) # 경우의 수로 나눠짐

find_combination(0, 1)
print(count)

