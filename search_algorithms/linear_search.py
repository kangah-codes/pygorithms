def linear_search(iterable, search):
	for i in iterable:
		if i == search:
			return search
	return -1