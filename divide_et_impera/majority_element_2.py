# Uses python3
def get_majority_element(A,left,right):
    
    if left > right:
        return -1

    if left == right:
        return A[left]

    mid = (left + right) // 2

    ml = get_majority_element(A, left, mid)
    mr = get_majority_element(A, mid+1, right)

    if ml == mr:    # if ml==mr then both sublist agree on the majority element
        return ml
    # otherwise we have to choose the majority element between ml mr by counting the occurrences of ml and mr in the concatenated list
    counter_ml = 0
    counter_mr = 0
    for i in range(left, right+1):
        if A[i] == ml:
            counter_ml += 1

    for i in range(left,right+1):
        if A[i] == mr:
            counter_mr += 1

    if counter_ml > (right-left + 1)//2:
        return ml
    elif counter_mr > (right-left + 1)//2:
        return mr
    else:
        return -1
        


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    m = get_majority_element(A,0, len(A)-1)
    if m != -1:
        print(1)
    else:
        print(0)
