#!/bin/python

# Head ends here
def quickSort(list):
	if len(list) <= 1:
		return list

	target = list[0]
	
	low = []
	high = []
	
	for num in list[1:]:
		if num < target:
			low.append(num)
		else:
			high.append(num)
			
	low = quickSort(low)
	low.append(target)
	low.extend(quickSort(high))
	
	print ' '.join(str(n) for n in low)

	return low

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)
