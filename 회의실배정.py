n = int(input())
l = []

for i in range(0, n) :
    l.append(list(map(int, input().split())))

# 끝나는 시간 기준으로 정렬을 해준 다음 회의 시작이 빠른 것 부터 정렬
# 끝나는 시간이 빠른 것 부터 하다가 끝나는 시간이 같으면 시작하는 시간이 더 빠른 것으로 하게 정렬함
l.sort(key=lambda x: (x[1], x[0])) 
count = 0
end = 0

for i in range(0, n) :
    if l[i][0] >= end :
        count += 1
        end = l[i][1]

print(count)
