import sys


def max_pairwise_product_fast(numbers):
    if len(numbers) == 0:
        return 0
    if len(numbers) == 1:
        return numbers[0]

    maxint1 = -1
    for i in range(len(numbers)):
        if maxint1 == -1 or numbers[i] > numbers[maxint1]:
            maxint1 = i

    maxint2 = -1
    for i in range(len(numbers)):
        if (maxint2 == -1 or (numbers[i] > numbers[maxint2])) and i != maxint1:
            maxint2 = i

    return numbers[maxint1] * numbers[maxint2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
