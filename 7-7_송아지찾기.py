# 1 2 3 4 5
# 5 4 3 2 1

import sys
sys.setrecursionlimit(10000) # JUMP를 계속 돌아도 리미트에 걸리지 않게 리미트를 늘려줌
s, e = map(int, input().split())
jump_count = 0 # 점프한 횟수

def JUMP(i) :
	global jump_count
	if i == e :
		return
	jump_count += 1 
	if i > e : # 뒤에 있다면
		JUMP(i-1)
	elif i+4 <= e : # 4칸이상 앞에 있다면 
		JUMP(i+5) 
	else : # 앞에 있다면
		JUMP(i+1)

JUMP(s)
print(jump_count)

