n = int(input())

stone_list = []
check_list = []
for i in range(0, n) :
	stone = list(map(int, input().split()))
	check_list.append([0]*n)
	stone_list.append(stone)

check_list[0][0] = stone_list[0][0]

for i in range(0, n) :
	check_list[0][i] = check_list[0][i-1]+stone_list[0][i]
	check_list[i][0] = check_list[i-1][0]+stone_list[i][0]
	
for i in range(1, n) :
	for j in range(1, n) :
		check_list[i][j] = min(check_list[i-1][j], check_list[i][j-1])+stone_list[i][j]

print(check_list[n-1][n-1])

