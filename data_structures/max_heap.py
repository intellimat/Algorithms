
# The max_heap implemented down below takes advantage of Python list type, so the current heap size is always equal to the whole list length
# (It could have also been explicitly implemented through dynamic arrays)
class MaxHeap():
    def __init__(self, list_of_values=[]):
        self.tree = [value for value in list_of_values]

        if len(self.tree) > 0:
            # heapify the received values
            self.build_heap()

    def get_size(self):
        return len(self.tree)

    def build_heap(self):
        data = self.tree
        heap_size = len(data)

        i = heap_size // 2
        while i >= 0:
            self.sift_down(i)
            i -= 1

    def sift_down(self, i):
        if i >= 0 and i < len(self.tree):
            data = self.tree
            heap_size = len(data)

            # current node is referenced by index i
            left_child_index = i*2 + 1

            right_child_index = i*2 + 2

            _max = data[i] # suppose the current node is the maximum
            _max_index = i

            if left_child_index < heap_size and data[left_child_index] > _max:
                _max_index = left_child_index
                _max = data[_max_index]

            if  right_child_index < heap_size and data[right_child_index] > _max:
                _max_index = right_child_index
                _max = data[_max_index]
                

            if _max_index != i:
                self.__swap(i, _max_index)
                self.sift_down(_max_index)
    
    def sift_up(self, i):
        def parent_index(index):
            return (index-1) // 2

        while i > 0 and i < len(self.tree) and self.tree[i] > self.tree[parent_index(i)]:
            self.__swap(i, parent_index(i))
            i = parent_index(i)

    def get_tree(self):
        tree = [node for node in self.tree]
        return tree

    def insert(self, value):
        self.tree.append(value)
        last_leaf_index = len(self.tree) - 1
        self.sift_up(last_leaf_index)

    def get_max(self):
        if len(self.tree) > 0:
            _max = self.tree[0] #root
            return _max
        
        return None

    # extract_max() saves the root value (current biggest value of the tree) in a variable, 
    # then swaps the root with the last leaf (i.e. last element of the list),
    # then pops the last list element (which is the max that we need to remove)
    # then fixes the tree by calling repeatedly sift_down starting from the root,
    # then returns the max previously saved in the variable
    def extract_max(self):
        # swap first
        if len(self.tree) > 0:
            _max = self.tree[0]
            last_leaf_index = len(self.tree) - 1
            self.__swap(0, last_leaf_index)
            self.tree.pop(last_leaf_index)
            if len(self.tree) > 0:
                self.sift_down(0)
            return _max
        
        return None

    def remove(self, i):
        if i >= 0 and i < len(self.tree):
            self.change_priority(i, float('inf'))
            self.sift_up(i) # so the element to remove will be moved to the root
            self.extract_max() # then we extract the root

    def change_priority(self, i, new_priority):
        if i >= 0 and i < len(self.tree):
            old_priority = self.tree[i]
            self.tree[i] = new_priority

            if new_priority > old_priority:
                self.sift_up(i)
            elif new_priority < old_priority:
                self.sift_down(i)

    def __swap(self, i, j):
        data = self.tree
        temp = data[i]
        data[i] = data[j]
        data[j] = temp

if __name__ == '__main__':
    max_heap = MaxHeap([600,700,800,900])

    print('max_heap = ', *max_heap.get_tree())
