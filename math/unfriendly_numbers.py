#!/bin/python

def find_friendly_nums(divisors, unfriendly_numbers):	
	temp = divisors[::]
	
	for num1 in divisors:
		for num2 in unfriendly_numbers:
			if num1 % num2 == 0 or num1 == num2:
				temp.remove(num1)
				unfriendly_numbers.remove(num2)
				break

	print len(temp)

if __name__ == '__main__':
	input = [int(i) for i in raw_input().strip().split()]
	unfriendly_numbers = [int(i) for i in raw_input().strip().split()]
	divisors = [num for num in range(2,input[1]+1) if input[1] % num == 0]
	find_friendly_nums(divisors, unfriendly_numbers)
