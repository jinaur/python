n, m = map(int, input().split())
t = list(map(int, input().split()[1:]))
l = []
for i in range(0, m) :
    l.append(list(map(int, input().split()[1:])))

# 한번만 돌면 앞에서 나온건 안되서 2번 돌아야됨
for _ in range(0, m) :
    for i in range(0, m) :
        for j in range(0, len(t)) :
            if t[j] in l[i] :
                for j in range(0, len(l[i])) :
                    if l[i][j] not in t : 
                        t.append(l[i][j])

count = 0
for i in range(0, m) :
    fc = 0
    for j in range(0, len(t)) :
        if t[j] in l[i] :
            fc = 1
    if fc == 0 :
        count += 1

print(count)

# 짧고 간단하게 쓴 코드
# n, m = map(int, input().split())
# knows_truth = set(map(int, input().split()[1:]))
# parties = [set(map(int, input().split()[1:])) for _ in range(m)]

# for _ in range(m):
#     for party in parties:
#         if party & knows_truth:
#             knows_truth |= party

# count = sum(1 for party in parties if not (party & knows_truth))
# print(count)

