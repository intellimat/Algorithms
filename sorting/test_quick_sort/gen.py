import sys
import random

n = int(sys.argv[1])  # array length
my_seed = int(sys.argv[2])  # seed for generating pseudo-random values
random.seed(my_seed)

print(' '.join([str(random.randint(0, 1000)) for i in range(n)]))
