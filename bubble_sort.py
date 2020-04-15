__author__ = "Joshua Akangah"

def bubble_sort(iterable):
   length = len(iterable)

   for i in range(0, length-1):
      swapped = f=False

      for j in range(0, length-1):
         if iterable[j] > iterable[j+1]:
            iterable[j], iterable[j+1] = iterable[j+1], iterable[j]
            swapped = True
      if not swapped:
         break

   return iterable

# test
print(bubble_sort([3,5,23,76,9]))