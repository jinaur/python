n, m = map(int, input().split())

gem = [0]*(m+1) # gem[j] : 가방에 담을수 있는 최대가치
for i in range(0, n) :
	w, p = map(int, input().split())
	for j in range(w, m+1) :
		gem[j] = max(gem[j], gem[j-w]+p) 

print(gem[m])
	

# 5 12 [0, 0, 0, 0, 0, 12, 12, 12, 12, 12, 24, 24]
# 3 8  [0, 0, 0, 8, 8, 12, 16, 16, 20, 24, 24, 28] 
#                      ^^          8번째 20은 5+3그램으로 5번째 12+8된것임


