a = input()

l = [['..#..'], ['.#.#.'], ['#.'+a[0]+'.#'], ['.#.#.'], ['..#..']]


for i in range(1, len(a)) :
    if (i+1)%3 == 0 :
        l[0][0] += '.*..'
        l[1][0] += '*.*.'
        l[2][0] += '*.'+a[i]+'.*'
        l[3][0] += '*.*.'
        l[4][0] += '.*..'
    else :
        if (i+2)%3 == 0 and len(a) >= i+2 :
            l[0][0] += '.#..'
            l[1][0] += '#.#.'
            l[2][0] += '.'+a[i]+'.'
            l[3][0] += '#.#.'
            l[4][0] += '.#..'
        else :
            l[0][0] += '.#..'
            l[1][0] += '#.#.'
            l[2][0] += '.'+a[i]+'.#'
            l[3][0] += '#.#.'
            l[4][0] += '.#..'

for i in range(0, 5) :
    print(l[i][0])


