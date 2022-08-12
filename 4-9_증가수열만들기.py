n = int(input())
a = list(map(int, input().split()))

l = ""
List = []
count = 0

if a[0] < a[len(a)-1] :
    count += 1
    l += "L"
    List.append(a[0])
    a.remove(a[0])
elif a[0] > a[len(a)-1] :
    count += 1
    l += "R"
    List.append(a[len(a)-1])
    a.remove(a[len(a)-1])

for i in range(0, n-1) :
    if List[len(List)-1] < a[0] :
        if a[0] < a[len(a)-1] or List[len(List)-1] > a[len(a)-1] :
            count += 1
            l += "L"
            List.append(a[0])
            a.remove(a[0])
    if List[len(List)-1] < a[len(a)-1] :    
        if a[0] > a[len(a)-1] or List[len(List)-1] > a[0] :
            count += 1
            l += "R"
            List.append(a[len(a)-1])
            a.remove(a[len(a)-1])

if List[len(List)-1] < a[0] :
    count += 1
    l += "L"
    List.append(a[0])
    a.remove(a[0])
if List[len(List)-1] < a[len(a)-1] :    
    count += 1
    l += "R"
    List.append(a[len(a)-1])
    a.remove(a[len(a)-1])

print(count)
print(l)

