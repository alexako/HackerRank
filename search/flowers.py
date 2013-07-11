#!/bin/python

import math

# code snippet illustrating input/output methods
N, K=raw_input().split()
N=int(N)
K=int(K)
C=[]

numbers = raw_input()

result=0
i=0
for number in numbers.split():
    i=i+1
    C.append(int(number))
    if(N == K):
        result+=int(number)

if(N != K):
    C.sort()
    counter = 0
    a = N - 1
    while(a >= 0):
        result += math.ceil(float((counter/K)+1))*C[a]
        counter = counter + 1
        a = a - 1

index = [n for n in str(result) if n == '.']
print result[:index]
