# counting sort algorithm T(n) = O(n + k)
# constraint: Every integer must be positive or zero

def count_sort(A):
    k = A[0]
    for n in A:
        if n > k:
            k = n
    # all the integers in A are in the interval [0,k]

    C = [0] * (k+1)        # Initialization C=[0,...,0]

    # counts the occurrences 
    for j in range(0,len(A)):
        C[A[j]] += 1

    # compute position for each integer in the output array
    for i in range(1,len(C)):
        C[i] = C[i] + C[i-1]
    
    P = [0] * len(A) # Initialization
    
    for n in A:
        index = C[n] - 1    # we sub 1 because the index in list starts from zero 
        P[index] = n
        C[n] = C[n] - 1

    return P


if __name__ == '__main__':
    A = list(map(int, input('Type some positive (or zero) integers and I will sort them (e.g. 3 9 2 8 4 3):\n ').split()))
    isNegative = False
    for n in A:
        if n < 0:
            isNegative = True
    if isNegative:
        print('I cannot sort negative A. ')
    else:
        print('Sorted integers: ', count_sort(A))