# Uses python3
import sys

def get_majority_element(A):
    A.sort()
    max_count = 1
    x = A[0]
    for i in range(1, len(A)):
        if x == A[i]:
            max_count += 1
            if max_count > len(A) // 2:
                return x
        else:
            x = A[i]
            max_count = 1
    return -1

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    if get_majority_element(A) != -1:
        print(1)
    else:
        print(0)
