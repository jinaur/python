n = int(input())
apple_list = []
for i in range(0, n) :
	a = list(map(int,input().split()))
	apple_list.append(a)
distance = 0 # 양옆으로 가는 이동거리, 처음엔 양옆으로 가지않게 0
apple_count = 0 # 사과 개수

def tree(distance, m, l) :
	global apple_count
	for i in range(distance, l) :
		for j in range(0, distance) : # 중앙에서 부터 양옆으로가 사과 개수를 셈
			apple_count += apple_list[i][n//2+distance-j] # 오른쪽 사과
			apple_count += apple_list[i][n//2-distance+j] # 왼쪽 사과
		apple_count += apple_list[i][n//2] # 중앙 사과
		distance += m

tree(0, 1, n//2)
tree(n//2, -1, n)
print(apple_count)


