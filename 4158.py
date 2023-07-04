# import sys

# while True:
#     n, m = map(int, sys.stdin.readline().split())
#     if n == 0 and m == 0:
#         break
#     nl = []
#     for i in range(0, n) :
#         nl.append(int(input()))
#     ml = []
#     for i in range(0, m) :
#         ml.append(int(input()))
        
#     nl = set(nl)
#     ml = set(ml)
#     print(len(nl&ml))


from collections import defaultdict
import sys
input = sys.stdin.readline

while True:
    cd = defaultdict(bool)
    n, m = map(int, input().split())
    count = 0
    if n == 0 and m == 0:
        break
    for i in range(0, n):
        cd[int(input())] = True
    for i in range(0, m):
        if cd[int(input())]:
            count += 1

    print(count)

    