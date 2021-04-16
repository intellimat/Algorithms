if __name__ == '__main__':
    A = list(map(int, input().split()))
    A.sort()
    for i in A:
        print(i, end=' ')