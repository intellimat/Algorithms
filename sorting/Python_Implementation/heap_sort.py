'''
In-place heap_sort, no extra space required!
T(n) = O(n log n)
'''
def heap_sort(numbers):
    heap_size = len(numbers)
    build_heap(numbers)

    for _ in range(0, len(numbers) - 1):
        swap(numbers, 0, heap_size - 1)
        heap_size -= 1
        sift_down(numbers, heap_size, 0)


def build_heap(data):
    heap_size = len(data)

    i = heap_size // 2  # we skip the leaves because the don't have children
    # then we fix the nodes' positions so that the max-heap property is respected
    while i >= 0:
        sift_down(data, heap_size, i)
        i -= 1

# sift_down time complexity is O(log n)
def sift_down(data, heap_size, i):
    # current node is placed at i index
    left_child_index = i*2 + 1

    right_child_index = i*2 + 2

    _max = data[i] # suppose the current node is the minimum
    _max_index = i

    if left_child_index < heap_size and data[left_child_index] > _max:
        _max_index = left_child_index
        _max = data[_max_index]

    if  right_child_index < heap_size and data[right_child_index] > _max:
        _max_index = right_child_index
        _max = data[_max_index]
        

    if _max_index != i:
        swap(data, i, _max_index)
        sift_down(data, heap_size, _max_index)

def swap(data, i, j):
    temp = data[i]
    data[i] = data[j]
    data[j] = temp


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    heap_sort(numbers)
    print(*numbers)