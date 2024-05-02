import sys
input = sys.stdin.readline

n, q = map(int, input().split())
p = list(map(int, input().split()))

sum_value = 0
prefix_sum = [0]
for i in p :
    sum_value += i
    prefix_sum.append(sum_value)

for _ in range(0, q) :
    l, r, x = map(int, input().split())
    
    Max = 0
    # Min = min(prefix_sum[l-1:r])
    # count = (p[x-1]*(x-prefix_sum.index(Min, l-1, r)) - (prefix_sum[x]-Min))
    
    # if count > Max :
    #     Max = count

    for i in range(l-1, r) :
        count = (p[x-1]*(x-i)) - (prefix_sum[x]-prefix_sum[i])
        if count > Max :
            Max = count
    
    print(Max)
