

def fib_n_mod_m(n,m):
    if m == 1:
        return 0
    if n < 2:
        return n
    pisano_period = find_pisano_period(n,m)
    if pisano_period is not None:
        index = n % len(pisano_period)
        return pisano_period[index]
    else:
        print('I could not find pisano period')
    


def find_pisano_period(n,m):
    pisano_period_found = False
    pisano_period = [0,1] # it always start with 0 1

    array = [0,1]   # base cases
    for i in range(2,m*m):      # m*m is just an arbitrary maximum length. No one knows the exact pisano period maximum length
        fib_i = array[i-1] + array[i-2]
        array.append(fib_i)
        pisano_period.append(fib_i % m)

        if pisano_period[-1] == 1 and pisano_period[-2] == 0:   # we are in a new period
            pisano_period.pop()
            pisano_period.pop()
            return pisano_period

    return None
             
if __name__ == '__main__':
    input = input()
    n, m = map(int, input.split())
    print(fib_n_mod_m(n,m))