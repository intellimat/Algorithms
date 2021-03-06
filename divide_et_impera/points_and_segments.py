

def count_covers(bets, segments):
    n = len(segments)

    left_ends  = list(map(lambda elem : elem[0], segments.copy())) # we keep only the left end of the segments
    right_ends = list(map(lambda elem : elem[1], segments.copy())) # we keep only the right end of the segments

    left_ends.sort()
    right_ends.sort()

    result = []

    for x in bets:
        counter_l = binary_search_l(left_ends, 0, len(left_ends)-1, x)
        counter_r = binary_search_r(right_ends, 0, len(right_ends)-1, x)
        #print(f'x = {x}, counter_l = {counter_l}, counter_r = {counter_r}, n = {n}')
        result.append(counter_l + counter_r - n)

    return result

# Binary search to look for elements less or equal to x
def binary_search_l(A, left, right, x):
    counter = 0
    if left > right:
        return counter

    mid = left + (right - left) // 2

    if A[mid] <= x:
        counter += mid - left + 1
        counter += binary_search_l(A,mid+1,right,x)
    else:
        counter += binary_search_l(A,left,mid-1,x)
    
    return counter

# Binary search to look for elements greater or equal to
def binary_search_r(A, left, right, x):
    counter = 0
    if left > right:
        return counter

    mid = left + (right - left) // 2

    if A[mid] >= x:
        counter += right - mid + 1
        counter += binary_search_r(A,left,mid-1,x)
    else:
        counter += binary_search_r(A,mid+1,right,x)
    
    return counter

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    s, p = map(int, input().split())
    segments = []
    for i in range(s):
        segment = list(map(int, input().split()))
        segments.append(segment)

    bets = list(map(int, input().split()))

    cnt = count_covers(bets,segments)

    for x in cnt:
        print(x, end=' ')


