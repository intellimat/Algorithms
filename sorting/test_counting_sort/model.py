if __name__ == '__main__':
    A = list(map(int, input().split()))
    isNegative = False
    for n in A:
        if n < 0:
            isNegative = True
    if isNegative:
        print('I cannot sort negative A. ')
    else:
        A.sort()
        for i in A:
            print(i, end=' ')