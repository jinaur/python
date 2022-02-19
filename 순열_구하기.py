n, m = list(map(int, input().split()))
bead_list = [0]*n # 구슬에 적힌 수 저장
bead_check = [0]*(n+1) # 같은 수를 한번에 뽑지않게 확인함
count = 0 # 총 경우의 수

def permutation(l) :
	global count
	if l == m : # M까지 갔다면 출력
		for i in range(0, l) :
			print(bead_list[i], end=" ")
		print()
		count += 1
	else :
		for i in range(1, n+1) :
			if bead_check[i] == 0 :
				bead_check[i] = 1 
				bead_list[l] = i
				permutation(l+1) # 다른 경우의수로 나눠짐
				bead_check[i] = 0 # 경우의 수 끝까지간 후 초기화

permutation(0)
print(count)

 