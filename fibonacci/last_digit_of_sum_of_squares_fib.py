
computed = {0:0, 1:1}
def fib(n):
    if n not in computed:
        #compute it
        computed[n] = fib(n-1) + fib(n-2)
    return computed.get(n)  # get it from the dictionary

def calc(n):
    rem_period = [0,1] # it always start with 0 1
    for i in range(2,60):
        x = fib(i)
        x *= x
        rem_period.append((x + rem_period[i-1]) % 10)
    index = n % len(rem_period)
    return rem_period[index]
    

if __name__ == '__main__':
    n = input()
    print(calc(int(n)))