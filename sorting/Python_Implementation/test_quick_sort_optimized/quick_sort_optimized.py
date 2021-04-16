'''
In this implementation of quicksort:
# The pivot is always the last element of the given list.
# The pivot is randomized each time by taking the middle value between the first, the median, and the last element
# The red zone is the part of the list where all the elements are strictly less than the pivot.
# The blue zone is the part of the list where all the elements are greater than the pivot.
# Green zone is the part of the list where all the elements are equal to the pivot.
  This version of quicksort significantly improve the sorting when there are multiple elements equal to the pivot.
  When that happens, partition() simply skips those elements because they are already placed in correct final positions.
# Before calling partition, we put at the end of the current list the middle value between the first, the last and the median
  By doing so the algorithm becomes stable (with respect to calling randint() to choose a random element)

### This implementation of quicksort can still be improved by decreasing the size of the stack used for the recursions ( tail-recursive quicksort )

T(n) = 2T(n/2) + Θ(n) on average so T(n) = Θ(n log n)
But in the worst case (partitions unbalanced): T(n) = T(n-1) + Θ(n) so T(n) = Θ(n^2)
'''
import random

def quick_sort(A, left, right):
    if left < right:
        # Randomize the pivot so that on average T(n) = theta(n log n)
        first = A[left]
        median = A[left + (right-left+1)//2]
        last = A[right]
        if (first > median and first < last) or (first < median and first > last):
            index = left
        elif (median > first and median < last) or (median < first and median > last):
            index = left + (right-left+1)//2
        elif (last > median and last < first) or (last < median and last > first):
            index = right
        elif median == first:
            index = right
        elif median == last:
            index = left
        else:
            index = left + (right-left+1)//2

        # other solution that randomizes the pivot: index = random.randint(left,right)
        # but as mentioned above, then algorithm is not deterministic anymore
        # Swap
        temp = A[right] 
        A[right] = A[index]
        A[index] = temp

        m1, m2 = partition(A, left, right)
        # Each A[i] where m1<i<m2 are already in their final position (due to partition())
        quick_sort(A, left, m1)
        quick_sort(A, m2, right)

def partition(A, left, right):
    pivot = A[right]

    i = left  # Initialize the red zone (at the moment the red zone does not contain any element so i < left)
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

    return (i-1,k+1)    # return i-1, an index that points to the last element of the red zone
                        # and k+1, an index that points to the first element of the blue zone
                        # all the elements equal to the pivot has been places in the in indexes [i,k] 


if __name__ == '__main__':
    A = list(map(int, input().split()))
    quick_sort(A, 0, len(A)-1)
    for i in A:
        print(i, end=' ')
