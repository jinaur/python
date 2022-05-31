n = int(input())

l = []
for i in range(0, n) :
    a = list(map(int, input().split()))
    l.append(a)
l.sort()
l.reverse()

# 넓이 순서대로 정렬해서 넓이가 큰순으로 시작함
# 그후 넓이가 더 작은지 확인해 위에 놓을수 있는지 확인함
# 그중에서 가장 높은 것을 기록함
result = [0] * n
result[0] = l[0][1]
for i in range(1, n) :
    Max = 0
    for j in range(i-1, -1, -1) :
        if l[i][2] < l[j][2] and result[j] > Max :
            Max = result[j]
        result[i] = Max+l[i][1]

# print(result)
print(max(result))

