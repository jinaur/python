n, m = map(int, input().split())

gem = [0]*(m+1) # gem[5] 는5그램 담을수 있단 의미
for i in range(0, n) :
	w, p = map(int, input().split())
	for j in range(w, m+1) :
		gem[j] = max(gem[j], gem[j-w]+p)
	print(gem(m))
	

