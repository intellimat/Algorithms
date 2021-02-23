

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous = previous % 10
        current = current % 10
        temp = current
        current = (previous + current) % 10
        previous = temp
    return current

if __name__ == '__main__':
    input = input()  #sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))