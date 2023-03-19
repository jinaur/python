n = int(input())
l = []
for i in range(0, n) :
    a = list(map(int, input().split()))
    l.append(a)

for i in range(1, n) : # 1번째집은 계산 할것이 없으니 스킵하고 2번째 집부터 계산함
    # 전의 집에서 옆에 있는것을 제외하고 가장 최소값을 더해줌
    l[i][0] = l[i][0] + min(l[i-1][1], l[i-1][2])
    l[i][1] = l[i][1] + min(l[i-1][0], l[i-1][2])
    l[i][2] = l[i][2] + min(l[i-1][0], l[i-1][1])

print(min(l[n-1]))

