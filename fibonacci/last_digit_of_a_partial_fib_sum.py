def partial_sum_remainder(m,n):
    if n < 2:
        return n
    pisano_period = find_pisano_period(n, 10)
    a = n % 60
    b = m % 60
    sum = 0
    if (a+1) < b:
        for i in range(b, 60):
            sum += pisano_period[i]
        for i in range(a+1):
            sum += pisano_period[i]
    else:
        for i in range(b, a + 1):
            sum += pisano_period[i]
    digit = sum % 10
    return digit


def find_pisano_period(n,m):
    pisano_period = [0,1] # it always start with 0 1

    array = [0,1]   # base cases
    for i in range(2,m*m + 1):      # m*m is just an arbitrary maximum length. No one knows the exact pisano period maximum length
        fib_i = array[i-1] + array[i-2]
        array.append(fib_i)
        pisano_period.append(fib_i % m)

        if pisano_period[-2] == 0 and pisano_period[-1] == 1:   # we are in a new period
            pisano_period.pop()
            pisano_period.pop()
            return pisano_period

    return None
  

if __name__ == '__main__':
    input = input()
    m, n = map(int, input.split())
    print(partial_sum_remainder(m,n))