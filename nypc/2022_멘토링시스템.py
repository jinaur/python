from collections import deque

N, M = map(int, input().split())
con = [[] for _ in range(N + N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    con[a].append(N + b)
    con[N + b].append(a)

cnt = 0
matched = [0] * (N + N + 1)
deg = [0] * (N + N + 1)
que = deque()

for i in range(1, N + N + 1):
    deg[i] = len(con[i])
    if deg[i] == 1:
        que.append(i)

while que:
    q = que.popleft()
    if matched[q]:
        for t in con[q]:
            if not matched[t]:
                deg[t] -= 1
                if deg[t] == 1:
                    que.append(t)
    else:
        for t in con[q]:
            if not matched[t]:
                matched[q] = t
                matched[t] = q
                que.append(t)
                cnt += 1

if cnt < N:
    print("NO")
else:
    print("YES")
    for i in range(1, N + 1):
        print(matched[i] - N)
