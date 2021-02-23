# Merge sort algorithm
# input values are cast to integers but the algorithm can be slightly fixed to accept also floats
# T(n) = 2T(n/2) + O(n)     when n > 1, otherwise O(1)
# T(n) = O(n log(n))

def merge_sort(A):
    if len(A) == 1:
        return A

    half = len(A) // 2

    left = merge_sort(A[:half])
    right = merge_sort(A[half:])

    result = merge(left,right)

    return result


def merge(A,B):
    merged_list = []

    while len(A) > 0 and len(B) > 0:
        if A[0] <= B[0]:
            merged_list.append(A[0])
            A.pop(0)
        else:
            merged_list.append(B[0])
            B.pop(0)

    if len(A) > 0:
        for n in A:
            merged_list.append(n)
    elif len(B) > 0:
        for n in B:
            merged_list.append(n)

    return merged_list



if __name__ == '__main__':
    A = list(map(int, input().split()))
    sorted_list = merge_sort(A)
    for i in sorted_list:
        print(i, end=' ')
