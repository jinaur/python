n, k = map(int, input().split())
a = list(map(int, input().split())) 
m = int(input())
count = 0 # 총 경우의 수

def solve_numbers(l, s, Sum) :
	global count
	if l == k : # k 까지 갔는지 확인
		if Sum%m == 0 : # m의 배수인지 확인
			count += 1
	else :
		for i in range(s, n) : # 경우의 수 나눠지기
			solve_numbers(l+1, i+1, Sum+a[i])

solve_numbers(0, 0, 0)
print(count)

