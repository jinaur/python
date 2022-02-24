n = int(input())
term_list = [] # 기간리스트
price_list = [] # 금액리스트
result = 0
for i in range(0, n) : 
	term, price = map(int, input().split())
	term_list.append(term)
	price_list.append(price)
	
# l = 현재 날짜
# Sum = 현재 금액
def max_profit(l, Sum) :
	global result
	if l == n : 
		if Sum > result : # 최고금액 기록
			result = Sum 
	else :
		if l+term_list[l] <= n : # 상담이 끝나는날이 휴가가기전 끝나지않으면 하지않음
			max_profit(l+term_list[l], Sum+price_list[l]) # 상담을 하고 넘어감
		max_profit(l+1, Sum) # 상담을 안하고 넘어감

	
max_profit(0, 0)
print(result)

