n, m = map(int, input().split())
scores = [] # 문제 점수 list
times = [] # 시간 list

# i 현재 인덱스
# Sum 현재 점수
# t 현재 시간
def DFS(i, Sum, t) :
	global result
	if t > m : #제한 시간 넘으면 멈추기
		return
	if i == n : # 마지막 문제까지 갔으면
		if Sum > result : # 최대값 기록
			result = Sum
	else :
		DFS(i+1, Sum + scores[i], t + times[i]) # 문제를 푼 경우의 수
		DFS(i+1, Sum, t) # 문제를 안푼 경우의 수

for i in range(0, n) :
	score, time = map(int, input().split())
	scores.append(score)
	times.append(time)
	
result = -100000000000
DFS(0, 0, 0)
print(result)
