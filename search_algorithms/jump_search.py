import math
def jump_search(iterable, search):
	n = len(iterable)
	jump = math.sqrt(n)
	prev = 0

	while iterable[int(min(jump, n)-1)] < search:
		prev = jump
		jump += math.sqrt(n)
		if prev >= n:
			return -1

	while iterable[int(prev)] < search:
		prev += 1
		if prev == min(jump, n):
			return -1

	if iterable[int(prev)] == search:
		return iterable[int(prev)]

	return -1

print(jump_search([3,4,5,6,6,77,84,455], 77))

