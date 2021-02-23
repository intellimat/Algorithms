
computed = {0:0, 1:1}
def fib(n):
    if n not in computed:
        #compute it
        computed[n] = fib(n-1) + fib(n-2)
    return computed.get(n)  # get it from the dictionary

if __name__ == '__main__':
    n = int(input())
    print(fib(n))