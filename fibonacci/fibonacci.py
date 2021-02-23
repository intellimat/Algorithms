
# T(n) = O(2^n), tree's height h=n-1 (worst case), in each level i we have 2^i nodes so T(n)= Σ 2^k, with k from zero to n-1.
# The summatory is a geometric series (partial): Σx^k from zero to n-1, equals 1-2^n / 1-x
# Each node has O(1) complexity
def calcFibNumber(n):
    if n <= 1:
        return n
    else:
        return calcFibNumber(n-1) + calcFibNumber(n-2)

# T(n) = O(n)
def efficientFib(n):
    array = [0,1]   # base cases
    for i in range(2,n+1):
        array.append(array[i-1] + array[i-2])
    return array[n]


try:
    print('Efficient (linear) Fibonacci algorithm used to compute values. ')
    for n in range(0,100):
        print(f'F({n}) =  {efficientFib(n)}')
except KeyboardInterrupt:
    print('Loop ended')