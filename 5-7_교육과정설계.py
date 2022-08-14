r = input()
n = int(input())

for i in range(0, n) :
	count = 0
	l = []
	a = input()
	for j in range(0, len(a)) :
		for k in range(0, len(r)) :
			if a[j] == r[k] :
				l.append(a[j])
				break

	if len(l) == len(r) :
		for j in range(0, len(l)) :
			if l[j] == r[j] :
				count += 1
			else :
				print("#"+str(i+1), "NO")
				break
				
		if count == len(l) :
			print("#"+str(i+1), "YES")
	else :
		print("#"+str(i+1), "NO")

