
# T(n) = 1.5n
def max_pairwise_product_faster(array):
    firstIndex = -1
    secondIndex = -1

    if len(array) == 1:
        return 0

    for i in range(0,len(array)//2):  # n/2 iterations
        if firstIndex == -1 or array[i] > array[firstIndex]:
            firstIndex = i
    
    for i in range(len(array)//2,len(array)):  # n/2 iterations
        if secondIndex == -1 or array[i] > array[secondIndex]:
            secondIndex = i
    
    if array[firstIndex] > array[secondIndex]:
        firstMax = array[firstIndex]
        secondMax = array[secondIndex]  # Not sure this is really the secondMax
        # look for second max in the other half
        for i in range(0, len(array)//2):   # n/2 iterations
            if array[i] > secondMax and i != firstIndex:
                secondMax = array[i]
    else:
        firstMax = array[secondIndex]
        secondMax = array[firstIndex]  # Not sure this is really the secondMax
        # look for second max in the other half
        for i in range(len(array)//2, len(array)):  # n/2 iterations
            if array[i] > secondMax and i != secondIndex:
                secondMax = array[i]
    
    return firstMax * secondMax

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_faster(input_numbers))
