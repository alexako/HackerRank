#!/bin/python

# Head ends here
def partition(ar):
    target = ar[0]
    lower = []
    higher = []
    
    for num in ar:
        if num < target:
            lower.append(num)
        elif num > target:
            higher.append(num)
            
    new = [n for n in lower]
    new.append(target)
    new.extend(higher)
    print ' '.join(str(n) for n in new)
    return ""

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
