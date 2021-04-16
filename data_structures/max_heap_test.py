from max_heap import MaxHeap
import random

def is_max_heap(tree):
    tree_size = len(tree)

    if tree_size == 0 or tree_size == 1:
        return True

    for i in range(0, tree_size):
        left_child_index = 2*i + 1
        right_child_index = 2*i + 2

        if ( (left_child_index < tree_size and tree[left_child_index] > tree[i]) or
            (right_child_index < tree_size and tree[right_child_index] > tree[i]) ):
            return False

    return True

def test_max_heap(n, max_heap):

    for i in range(n):
        print('i = ', i)
        # random operation generator
        op = random.randint(1,4)
        
        if op == 1:     # perform insert(value)
            value = random.randint(0,1000)
            max_heap.insert(value)

            assert(is_max_heap(max_heap.get_tree()))

        elif op == 2:    # perform extract_max()
            _max = max_heap.extract_max()

            assert(is_max_heap(max_heap.get_tree()))

        elif op == 3:    # perform remove(i)
            i = random.randint(0, max_heap.get_size())

            assert(is_max_heap(max_heap.get_tree()))

        elif op == 4:    # perform change_priority(i, new_priority)
            i = random.randint(0, max_heap.get_size()) # index
            new_priority = random.randint(0, 1000)
            max_heap.change_priority(i, new_priority)

            assert(is_max_heap(max_heap.get_tree()))



if __name__ == '__main__':
    n = int(input('Number of random operations to perform: '))

    max_heap = MaxHeap()

    test_max_heap(n, max_heap)