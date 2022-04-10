n, m = map(int, input().split())
l = []
scores = []
times = []

for i in range(0, n) :
	s, t = map(int, input().split())
	l.append(s/t)
	scores.append(s)
	times.append(t)

scorecount = 0
timecount = 0
# print(l)
for i in range(0, n) :
    # print(scorecount)
    count = 0
    for j in range(0, n) :
        if scores[j]/times[j] == max(l) == l[j] and timecount+times[j] <= m :
            scorecount += scores[j]
            timecount += times[j]
            # print(l[j], max(l), scores[j]/times[j])
            l[j] = 0
            break
        count += 1

    if count == n :
        for j in range(0, n) :
            if l[j] != 0 and timecount+times[j] <= m :
                scorecount += scores[j]
                timecount += times[j]
                l[j] = 0


print(scorecount)
