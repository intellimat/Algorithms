
# longest common sequence between string a and string b and string c
# dynamic approach
def longest_common_subsequence_matrix(a, b, c):
    D = get_initial_matrix(a,b, c)

    num_of_rows = len(a) + 1
    num_of_cols = len(b) + 1
    num_of_z_indeces = len(c) + 1
    
    for j in range(1, num_of_cols):
        for i in range(1, num_of_rows):            
            for k in range(1, num_of_z_indeces):
                option_1  = D[i][j-1][k-1]
                option_2  = D[i-1][j][k-1]
                option_3  = D[i-1][j-1][k]
                option_4  = D[i][j][k-1]
                option_5  = D[i][j-1][k]
                option_6  = D[i-1][j][k]

                match     = D[i-1][j-1][k-1] + 1
                mismatch  = D[i-1][j-1][k-1]
                if a[i-1] == b[j-1] == c[k-1]:
                    D[i][j][k] = get_max(option_1, option_2, option_3, option_4, option_5, option_6, match)
                else:
                    D[i][j][k] = get_max(option_1, option_2, option_3, option_4, option_5, option_6, mismatch)
    return D

def get_max(*args):
    max = args[0]
    for value in args:
        if value > max:
            max = value
    return max


def get_initial_matrix(a, b, c):
    D = []
    for i in range(0, len(a) + 1):
        row = []
        for j in range(0, len(b) + 1):
            z_row = []
            for k in range(0,len(c) + 1):
                z_row.append(0)
            row.append(z_row)
        D.append(row)
    return D

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))

    n = int(input())
    b = list(map(int, input().split()))

    n = int(input())
    c = list(map(int, input().split()))

    D = longest_common_subsequence_matrix(a, b, c)

    last_row_index = len(D) - 1
    last_col_index = len(D[0]) - 1
    last_z_index = len(D[0][0]) - 1

    lcs = D[last_row_index][last_col_index][last_z_index]

    print(lcs)

