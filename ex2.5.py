def mergesort2(S, low, high):
	if (low < high):
		mid = (low + high) // 2
		mergesort2(S, low, mid)
		mergesort2(S, mid + 1, high)
		merge2(S, low, mid, high)

def merge2 (S, low, mid, high):
	U = []
	i = low
	j = mid + 1
	while (i <= mid and j <= high):
		if (S[i] < S[j]):
			U.append(S[i])
			i += 1
		else:
			U.append(S[j])
			j += 1
	if (i <= mid):
		U += S[i : mid + 1]
	else:
		U += S[j : high + 1]
	for k in range(low, high + 1):
		S[k] = U[k - low]

S = [27, 10, 12, 20, 25, 13, 15, 22]
print('Before: ', S)
mergesort2(S, 0, len(S) -1)
print('Aefore: ', S)


# [27, 10, 12, 20, 25, 13, 15, 22]
# [10, 27, 12, 20, 25, 13, 15, 22]
# [10, 12, 20, 27, 25, 13, 15, 22]
# [10, 12, 20, 27, 13, 25, 15, 22]
# [10, 12, 20, 27, 13, 25, 15, 22]
# [10, 12, 20, 27, 13, 15, 22, 25]