# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

# Our goal is to place paranthesis such that the value of the arithmetic expression is maximized
def get_maximum_value(operands, operators):
    m, M = get_initial_matrices(operands)

    for k in range(1, len(operators) + 1):
        for i in range(len(operands) - k):
            j = i + k
            m[i][j], M[i][j] = minAndMax(i, j, m, M, operators)
    return M[0][len(operands)-1]


def get_initial_matrices(operands):
    M = [[operands[i] if i == j else '' for j in range(len(operands))] for i in range(len(operands))]
    m = [[operands[i] if i == j else '' for j in range(len(operands))] for i in range(len(operands))]
    return (m, M)


def minAndMax(i, j, m, M, operators):
    _min = float('inf')
    _max = float('-inf')
    for k in range(i,j):
        a = evalt(M[i][k], M[k+1][j], operators[k])
        b = evalt(M[i][k], m[k+1][j], operators[k])
        c = evalt(m[i][k], M[k+1][j], operators[k])
        d = evalt(m[i][k], m[k+1][j], operators[k])
        _min = min(_min, a, b, c, d)
        _max = max(_max, a, b, c, d)
    return (_min, _max)

if __name__ == "__main__":
    s = list(input())
    operands = []
    operators = []
    for i in range(len(s)):
        if i % 2 == 0:
            operands.append(int(s[i]))
        else:
            operators.append(s[i])


    print(get_maximum_value(operands, operators))
