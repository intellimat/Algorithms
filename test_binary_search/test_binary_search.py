import sys
import os
import random
from binary_search import binary_search

# we will use it for testing the binary search
def linear_search(l,x):
    for i in range(0,len(l)):
        if l[i] == x:
            return i
    return -1


tests = int(sys.argv[1]) # how many tests
arrays_length = int(sys.argv[2])

PASSED = True

for i in range(tests):
    x = random.randint(0,2000)
    random.seed(i)
    l = [random.randint(0, 1000) for i in range(arrays_length)]
    l.sort()
    index = binary_search(l,x, 0, len(l)-1)
    if index != -1:
        if l[index] == x:
            print(f'Test #{i} PASSED')
        else:
            print(f'Test #{i} FAILED ----- l[index]={l[index]}, x = {x}')
            PASSED = False
            break
    else:
        k = linear_search(l,x)
        if k != index:
            PASSED = False
            print(f'Test #{i} FAILED ----- index={index}, k = {k} (they should be both -1)')
            break
        else:
            print(f'Test #{i} PASSED')

if PASSED:
    print('ALL TESTS PASSED')
else:
    print('TEST FAILED')