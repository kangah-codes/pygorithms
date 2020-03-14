"""
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
"""

left_stack = []

def merge_sort(iterable):
	length = len(iterable)
	if length % 2 == 0:
		middle = length // 2
	else:
		middle = (length+1) // 2
	left = iterable[:middle]
	right = iterable[middle:]

	merge_sort(left)
	merge_sort(right)

	print(left, right)

merge_sort([4,23,5676,23,43])

