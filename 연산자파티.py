n = int(input())
a, b, c, d, e, f = map(int, input().split())

X = 0
for i in range(1, n+1) :
    if i%a == 0 :
        X += i 
    if i%b == 0 :
        X %= i 
    if i%c == 0 :
        X &= i 
    if i%d == 0 :
        X ^= i 
    if i%e == 0 :
        X |= i
    if i%f == 0 :
        X = X >> i 

print(X)

