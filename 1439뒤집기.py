s = input()

count = 1
for i in range(0, len(s)-1) :
    if s[i] != s[i+1] :
        count += 1

print(count//2)

