n, f = map(int, input().split())
plist = [0]*n
List = [1]*n
check = [0]*(n+1)
for i in range(1, n) :
	List[i] = List[i-1]*(n-i)//i
	
def DFS(l, Sum) :
    if l == n and Sum == f :
        for i in range(0, n) :
            print(plist[i], end=' ')
        exit()
    else : 
        for i in range(1, n+1) :
            if check[i] == 0 :
                check[i] = 1
                plist[l] = i
                DFS(l+1, Sum+(plist[l]*List[l]))
                check[i] = 0

DFS(0, 0)

