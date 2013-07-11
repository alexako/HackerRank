#!/bin/python

def pairs(N, K, numbers):
    numbers.sort()
    counter = 0

    for index, num in enumerate(numbers):
        while index < N and num + K > numbers[index]:
            index += 1
        if index == N:
            continue
        elif num + K == numbers[index]:
            counter += 1
        
    print counter

if __name__ == '__main__':
    input = [int(i) for i in raw_input().strip().split()]
    N = input[0]
    K = input[1]
    numbers = [int(i) for i in raw_input().strip().split()]
    pairs(N, K, numbers)
