import sys

# KOI 2021 Preliminary
# '두 개의 팀' (Two teams) Model solution
# Author: Suchan Park

input = sys.stdin.readline

def main():
  N = int(input())
  A = []
  ch = [[] for _ in range(N)]
  root = -1
  for i in range(N):
    a, p = map(int, input().split())
    A.append(a)
    p -= 1
    if p < 0:
      root = i
    else:
      ch[p].append(i)

  dp0 = [0]*N
  dp1 = A[:]
  dpe = [0]*N

  que = [root]
  for u in que:
    que.extend(ch[u])
  
  for u in que[::-1]:
    dp1[u] += sum(dp1[v] for v in ch[u] if dp1[v] > 0)
    dpe[u] = max([dpe[v] for v in ch[u] if dp1[v] > 0] + [dp0[v] for v in ch[u] if dp1[v] <= 0], default=-10**18)
    dp0[u] = max(dp1[u], max([dp0[v] for v in ch[u]], default=-10**18))

  ans = -10**18
  def upd(cur):
    nonlocal ans
    ans = max(cur, ans)

  for u in range(N):
    child_dp0s = sorted(dp0[v] for v in ch[u])
    if len(child_dp0s) >= 2:
      upd(sum(child_dp0s[-2:]))
    
  for u in range(N):
    for v in ch[u]:
      if dp1[v] <= 0:
        upd(dp1[u] + dp0[v])
      if dp1[v] >= 0:
        upd(dp1[u] + dpe[v])

  print(ans)

if __name__ == "__main__":
  main()

