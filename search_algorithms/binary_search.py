def binary_search(iterable, i, r, val):
	while i <= r:
		mid = i + (r - 1) // 2
		if iterable[mid] == val:
			return mid
		elif iterable[mid] < val:
			i = mid + 1
		else:
			r = mid - 1
	return None

