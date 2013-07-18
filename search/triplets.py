#!/bin/python


def triplet_count(nums):

    count = 0
    short_list = []
    triplets = []
    
    for i in nums:
        if i not in short_list:
            short_list.append(i)
            
    for i in short_list:
        for j in short_list:
            for k in short_list:
                if i < j and j < k:
                    if (i, j, k) not in triplets:
                        triplets.append((i, j, k))
                        count += 1

    print triplets

    return count

if __name__ == '__main__':
    num_length = input()
    num_list = [int(n) for n in raw_input().strip().split()]
    print "Answer found: ", triplet_count(sorted(num_list))
