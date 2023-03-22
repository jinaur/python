t = int(input())

Acount = t//300
t = t%300
Bcount = t//60 
t = t%60
Ccount = t//10
t = t%10

if t != 0 :
    print(-1)
else :
    print(Acount, Bcount, Ccount)

