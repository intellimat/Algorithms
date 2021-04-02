from functools import reduce

# returns a three dimensional matrix n+1 x W+1 x W+1
def get_initial_matrix(n, W):
    M = []
    for i in range(n + 1):
        row = []
        for j in range(W + 1):
            d = []
            for k in range(W + 1):
                d.append(0)
            row.append(d)
        M.append(row)
    return M

# Our goal is to find out whether there exist two groups of elements such that each one adds up to 1/3 of the total_value
# If so, then the third group of elements will for sure adds up to 1/3 of the total_value (because it's the only way to add up to the total_sum)
# Then this means that we can equally split the items into three groups (each group with the same overall value, 1/3 of the total_sum)
def canPartition(items):
    total_value = reduce(lambda a, b : a + b, items)
    if total_value % 3 != 0:    # impossible to split equally
        return False

    M = get_initial_matrix(len(items), total_value // 3)    # M will receive a three dimensional matrix


    num_rows = len(M)
    num_cols = len(M[0])
    num_aisles = len(M[0][0])

    # initial state, we fill the ' upper wall '
    for j in range(num_cols):
        for k in range(num_aisles):
            if j == k == 0:
                M[0][j][k] = True
            else:
                M[0][j][k] = False

    # initial state, we fill the ' front wall '
    for i in range(1, num_rows):
        item = items[i-1]
        for j in range(1,num_cols):
            if M[i-1][j][0] == True:
                M[i][j][0] = True
            elif (j-item >= 0) and M[i][j-item][0] == True:
                M[i][j][0] = True
            else:
                M[i][j][0] = False

    # initial state, we fill the ' left wall '
    for i in range(1, num_rows):
        item = items[i-1]
        for k in range(1, num_aisles):
            if M[i-1][0][k] == True:
                M[i][0][k] == True
            elif (k-item >= 0) and M[i-1][0][k-item] == True:
                M[i][0][k] = True
            else:
                M[i][0][k] = False
    # main algorithm
    ''' 
    M[i][j][k] == True iff we there exists two groups of elements
    such that one group adds up to j and the other one adds up to k, using at most i elements
    '''
    for i in range(1, len(items)+1):
        item = items[i-1]
        for j in range(1, num_cols):
            for k in range(1, num_aisles):
                if M[i-1][j][k] == True:    # we are excluding current item from the two sets (partitions)
                    M[i][j][k] = True
                elif (j-item) >= 0 and M[i-1][j-item][k] == True:
                    M[i][j][k] = True
                elif (k-item) >= 0 and M[i-1][j][k-item] == True:
                    M[i][j][k] = True
                else:
                    M[i][j][k] = False


    max_row_index   = len(M) - 1
    max_col_index   = len(M[0]) - 1
    max_third_index = len(M[0][0]) - 1 # which in our case equals max_col_index
    
    # last cell contains the result we are looking for
    return M[max_row_index][max_col_index][max_third_index]
    



if __name__ == '__main__':
    n = input()
    items = list(map(int,input().split()))

    if canPartition(items) == True:
        print(1)
    else:
        print(0)


