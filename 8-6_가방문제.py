n, w = map(int, input().split())

gem_list = []
for i in range(0, n) :
	gem = list(map(int, input().split()))
	gem_list.append(gem)
	
Max = 0
def bag(l, Sum, weightSum) :
    global Max
    if Max < Sum :
        Max = Sum
    if l == n :
        return Max
    for i in range(0, n) :
        if weightSum+gem_list[i][0] <= w :
            bag(l+1, Sum+gem_list[i][1], weightSum+gem_list[i][0])
    

bag(0, 0, 0)
print(Max)

