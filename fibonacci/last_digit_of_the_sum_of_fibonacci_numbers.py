def last_digit_of_the_sum_of_fib_numbers(n):
    if n < 2:
        return n
    pisano_period = find_pisano_period(n,10)

    if pisano_period is not None:
        index = n % len(pisano_period)
        sum = 0
        for i in range(index + 1):
            sum += pisano_period[i]
        return sum % 10
    else:
        return 'I could not find pisano period'


def find_pisano_period(n,m):
    pisano_period_found = False
    pisano_period = [0,1] # it always start with 0 1

    array = [0,1]   # base cases
    for i in range(2,m*m + 1):      # m*m is just an arbitrary maximum length. No one knows the exact pisano period maximum length
        fib_i = array[i-1] + array[i-2]
        array.append(fib_i)
        pisano_period.append(fib_i % m)

        if pisano_period[-1] == 1 and pisano_period[-2] == 0:   # we are in a new period
            pisano_period.pop()
            pisano_period.pop()
            return pisano_period

    return None
             
if __name__ == '__main__':
    n = int(input())
    print(last_digit_of_the_sum_of_fib_numbers(n))