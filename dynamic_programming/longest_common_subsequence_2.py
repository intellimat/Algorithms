
#longest common sequence between string a and string b
#dynamic approach
def longest_common_subsequence_matrix(a, b):
    D = get_initial_matrix(a,b)

    num_of_rows = len(a) + 1
    num_of_cols = len(b) + 1
    
    for j in range(1, num_of_cols):
        for i in range(1, num_of_rows):            
            insertion = D[i][j-1]
            deletion  = D[i-1][j]
            match     = D[i-1][j-1] + 1
            mismatch  = D[i-1][j-1]
            if a[i-1] == b[j-1]:
                D[i][j] = get_max(insertion, deletion, match)
            else:
                D[i][j] = get_max(insertion, deletion, mismatch)
    return D

def get_max(*args):
    max = args[0]
    for value in args:
        if value > max:
            max = value
    return max


def get_initial_matrix(a, b):
    D = []
    for i in range(0, len(a) + 1):
        row = []
        for j in range(0, len(b) + 1):
            row.append(0)
        D.append(row)
    return D

def print_matrix(M):
    print()
    for r in M:
        for x in r:
            print(x, end = ' ')
        print()
    print()


if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))

    n = int(input())
    b = list(map(int, input().split()))
    D = longest_common_subsequence_matrix(a,b)

    last_row_index = len(D) - 1
    last_col_index = len(D[0]) - 1

    lcs = D[last_row_index][last_col_index]

    print(lcs)

    #print_matrix(D)
