# List A must be sorted otherwise the algorithm does not work
def binary_search(A,value,left, right):
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if A[mid] == value:
        return mid

    elif A[mid] < value:
        return binary_search(A,value, mid+1, right)
    else:
        return binary_search(A,value, left, mid-1)
    
    

if __name__ == '__main__':
    A = list(map(int, input().split()))
    value = int(input())
    i = binary_search(A,value, 0, len(A)-1)
    print(str(i))
