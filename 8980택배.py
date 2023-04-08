n, c = map(int, input().split())
m = int(input())

l = []
for i in range(0, m) :
    l.append(list(map(int, input().split())))

l.sort(key=lambda x:x[1]) # 배달 도착시간이 빠른 순으로 정렬

count = 0
b = [c]*n # 마을 당 받아들일 수 있는 박스 수
for i in range(0, m) :
    m = c 
    # 목적지까지 가는동안 지나가는 마을중 가장 적게 가져갈 수 있는 택배를 선택
    for j in range(l[i][0]-1, l[i][1]-1) :
        m = min(m, b[j])
    # 가장 적은 택배를 실어야하는 박스보다 작으면 가능, 크다면 불가능
    m = min(m, l[i][2])
    # 목적지 까지 가는동안 지나가는 마을에 택배가 줄어듬
    for j in range(l[i][0]-1, l[i][1]-1) :
        b[j] -= m
    count += m

print(count)

