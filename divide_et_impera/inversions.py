def merge(A,B):
    counter = 0
    merged_list = []

    while len(A) > 0 and len(B) > 0:
        if A[0] <= B[0]:
            merged_list.append(A[0])
            A.pop(0)
        else:
            counter += len(A)
            merged_list.append(B[0])
            B.pop(0)

    if len(A) > 0:
        for n in A:
            merged_list.append(n)
    elif len(B) > 0:
        for n in B:
            merged_list.append(n)

    return (merged_list, counter)

def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if right == left:
        return ([a[left]], number_of_inversions)

    mid = (left + right) // 2

    t1 = get_number_of_inversions(a, left, mid)
    t2 = get_number_of_inversions(a, mid+1, right)

    number_of_inversions += t1[1] + t2[1]

    result = merge(t1[0], t2[0])
    number_of_inversions += result[1]

    return (result[0], number_of_inversions)

if __name__ == '__main__':
    n = int(input())
    integers = list(map(int, input().split()))
    r = get_number_of_inversions(integers, 0, len(integers)-1)
    #print(f'Ordered list: {r[0]} \nnumber_of_inversions: {r[1]}')
    print(r[1])
    
    '''
    integers_A = list(map(int, input().split()))
    integers_B = list(map(int, input().split()))
    r = merge(integers_A, integers_B)
    print('merge_counter = ' + str(r[1]))
    print('merged_list = ' + str(r[0]))
    '''