n = int(input())
m = int(input())

count = 0
l = [[]*n for i in range(0, n+1)]
for i in range(m):
    a, b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)

vl = [0]*(n+1)

def DFS(start) :
    global count
    vl[start] = 1

    for i in l[start] :
        if vl[i] == 0 :
            DFS(i)
            count += 1


DFS(1)
print(count)

