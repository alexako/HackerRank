#!/bin/python

# Head ends here
def insertionSort(list):
	counter = 0
	for index in range(1,len(list)):
		on_deck = list[index]
		comparing = index - 1

		while comparing >= 0 and on_deck < list[comparing] :
			list[comparing+1] = list[comparing]
			list[comparing] = on_deck
			comparing -= 1
			counter += 1

	print counter
	
# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

