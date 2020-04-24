def quicksort(iterable, l, h):
	"""
	iterable -> the list to be sorted
	l -> starting indec
	h -> last index
	"""
	if l < h:
		p = partition(iterable, l, h)
		quicksort(iterable, l, p-1)
		quicksort(iterable, p+1, h)

def partition(iterable, l, h):
	pivot = iterable[h]
	i = l
	for j in range(l, h+1):
		if iterable[j] < pivot:
			iterable[j], iterable[i] = iterable[i], iterable[j]
			i += 1
	iterable[i], iterable[h] = iterable[h], iterable[i]
	return i

a = [1,2,43543,234,54,0,-1,5]
quicksort(a, 0,len(a)-1)
print(a)