# import sys
# sys.setrecursionlimit(10000)
k = int(input())
w = list(map(int, input().split()))
s = sum(w)
# check = [i for i in range(1, s+1)]
check = []
def scale(check, l, i) :
    # if l in check :
    #     check.remove(l)
    if l > 0 :
        check.append(l)
    if i == k :
        return
    scale(check, l+w[i], i+1)
    scale(check, l-w[i], i+1)
    scale(check, l, i+1)

scale(check, 0, 0)
check = set(check)
check = list(check)
# for i in range(len(check)) :
#     if check[i] < 0 :
#         check[i] = 0
# while 0 in check :
# 	check.remove(0)

# print(check)
print(s-len(check))
