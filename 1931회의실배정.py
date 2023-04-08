# 아래 함수를 완성해서 정답을 맞춰주세요.
def schedule_meetings(meetings):
  count = 0
  l = 0 # last end time 
  for s, e in meetings :
    if s >= l :
      count += 1
      l = e
  return count

# 테스트 케이스
N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
sorted_meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
print(schedule_meetings(meetings))

 