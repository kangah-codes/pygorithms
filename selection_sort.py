def selection_sort(iterable):
	n = len(iterable)
	for i in range(n):
		min_index = i
		for j in range(i+1, n):
			if iterable[j] < iterable[min_index]:
				min_index = j
		iterable[min_index], iterable[i] = iterable[i], iterable[min_index]
	else:
		return iterable

print(selection_sort([45,1,2,45,4352,43]))