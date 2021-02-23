# python3

def compute_min_refills(distance, tankCapacity, x):
    currentTank = tankCapacity
    numRefills = 0
    current = 0
    x = [0] + x + [distance]
    n = len(x)

    while current < n-1:
        if x[current+1] - x[current] > tankCapacity:
            #tank is full but next stop is too far away ==> impossible
            return -1
        elif x[current+1] - x[current] <= currentTank: # advance if you can
            currentTank = currentTank - (x[current+1] - x[current])
            current += 1
        else:
            #refill
            currentTank = tankCapacity
            numRefills += 1

    return numRefills

if __name__ == '__main__':
    distance      = int(input())
    tankCapacity  = int(input())
    n             = int(input())
    x             = list(map(int,input().split()))
    print(compute_min_refills(distance, tankCapacity, x))
