import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

D = []

queue = deque()

for i in range(N):
    # 큐의 맨 앞에 있는 값이 범위를 벗어나면 제거
    if queue and queue[0] <= i - L:
        queue.popleft()
    
    # 현재 값보다 큰 값들은 큐에서 제거
    while queue and A[queue[-1]] > A[i]:
        queue.pop()
    
    # 현재 인덱스를 큐에 추가
    queue.append(i)
    
    # L 길이 범위의 최솟값을 D에 추가
    if i >= L - 1:
        D.append(A[queue[0]])

sys.stdout.write(' '.join(map(str, D)))
