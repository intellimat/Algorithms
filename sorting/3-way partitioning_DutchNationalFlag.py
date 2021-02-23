# 3-way partitioning - Dutch National Flag
# input: a list of values (parameter: A), a start index (parameter: left) and an end index (parameter: right)
#        the start index and the end index tell us what portion of the list we want to partition (left and right are included in the partition)
# output: a permutation of A where:
#         - All the elements less than A[right] are placed on the left part of A
#         - All the elements equal to A[right] are placed in the middle part of A
#         - All the elements greater than A[right] are placed at the end part of A
def partition(A, left, right):
    pivot = A[right]

    i = left
    k = right
    j = left

    while j >= left and j <= k:
        if A[j] < pivot:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i += 1
            j += 1
        elif A[j] > pivot:
            temp = A[k]
            A[k] = A[j]
            A[j] = temp
            k -= 1
        else:
            j += 1

    return (i-1,k+1)   

# Driver code
if __name__ == '__main__':
    A = list(map(int, input('Type some numbers separated by a space: ').split()))
    m1,m2 = partition(A, 0, len(A)-1)
    for i in A:
        print(i, end=' ')
