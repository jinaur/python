int_code = list(map(int, input())) # 숫자 코드
n = len(int_code) # 코드 길이
int_code.insert(n, -1) # 마지막 코드를 확인할 떄 Indexerror:list index out of range 가 일어나지 않게함
str_code=[0]*(n+3) # 문자 코드
count = 0 

def code_translate(l, p) :
	global count
	if l == n :
		count += 1
		for i in range(p) :
			print(chr(str_code[i]+64), end='')  # 아스키코드를 활용해서 문자로 바꿈
		print()
	else :
		for i in range(1, 27) :
			if int_code[l] == i : 
				str_code[p] = i # 코드 기록
				code_translate(l+1, p+1) 
			# 코드가 2자리수 일때   10의 자리 코드 확인       1의 자리 코드 확인
			elif i >= 10 and int_code[l] == i//10 and int_code[l+1] == i%10 :
				str_code[p] = i # 코드 기록
				code_translate(l+2, p+1) # 2자리 만큼 건너뜀
				
code_translate(0, 0)
print(count)

