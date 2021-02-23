import sys
import os
import random


tests = int(sys.argv[1])

arrays_length = int(sys.argv[2])    # array_length

PASSED = 'PASSED'
FAILED = 'FAILED'
NOT_EQUAL = False

for i in range(tests):
    # run the generator gen.py with parameter n and the seed i
    os.system('python gen.py ' + str(arrays_length) + ' ' + str(i) + ' > input.txt')
    os.system('python model.py <input.txt >model_output.txt')
    os.system('python quick_sort.py <input.txt >quick_sort_output.txt')
    
    with open('model_output.txt') as f:
        model_output = f.read()

    with open('quick_sort_output.txt') as f:
        quick_sort_output = f.read()

    if model_output != quick_sort_output:
        NOT_EQUAL = True
        print(f'Test #{i} FAILED')
        break
    else:
        print(f'Test #{i} OK')

if NOT_EQUAL:
    print(FAILED)
else:
    print(PASSED)