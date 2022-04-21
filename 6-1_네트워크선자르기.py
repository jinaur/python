n = int(input())
len_list = [0]*(n+1)

def DFS(l) :
	if len_list[l] > 0 :
		return len_list[l]
	if l == 1 or l == 2 :
		return l
	else :
		len_list[l] = DFS(l-1)+DFS(l-2)
		return len_list[l]

print(DFS(n))

