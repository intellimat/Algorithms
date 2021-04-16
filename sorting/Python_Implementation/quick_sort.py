'''
In this implementation of quicksort, the pivot is always the last element of the given list.
When I talk about red zone, I mean the area of the list where all the elements are less or equal to the pivot.
On the contrary, the blue zone is the area of the list where all the elements are greater than the pivot.
T(n) = 2T(n/2) + Θ(n) on average so T(n) = Θ(n log n)
But in the worst case (partitions unbalanced): T(n) = T(n-1) + Θ(n) so T(n) = Θ(n^2)
'''
import random

def quick_sort(A, left, right):
    if left < right:
        # Randomize the pivot so that on average T(n) = theta(n log n)
        random_index = random.randint(left,right)
        temp = A[right] 
        A[right] = A[random_index]
        A[random_index] = temp

        k = partition(A, left, right)
        quick_sort(A, left, k-1)
        quick_sort(A, k+1, right)

def partition(A, left, right):
    pivot = A[right]

    i = left-1  # Initialize the red zone (at the momentd the red zone does not contain any element so i < left)

    for j in range(left, right):
        if A[j] <= pivot:
            # Make room for the next element that is less or equal to the pivot
            i += 1
            # Swap
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    # Now we have to place pivot in the correct final position
    # All the elements before i are less or equal than the pivot (red zone)
    # All the elements from i to the end of the list are greater than the pivot (blue zone)
    # So we place the pivot between the red zone and the blue zone
    i += 1
    temp = A[i]
    A[i] = A[right]
    A[right] = temp

    return i    # return the index where the pivot has been placed


if __name__ == '__main__':
    A = list(map(int, input().split()))
    quick_sort(A, 0, len(A)-1)
    for i in A:
        print(i, end=' ')
