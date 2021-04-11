# python3


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

# Linear complexity: O(n)
def max_sliding_window(sequence, m):
    q = Queue()
    maximums = []
    
    for n in sequence:
        if q.get_size() < m:
            q.push(n)

        if q.get_size() == m:
            maximums.append(q.get_max())
            q.pop()

    return maximums


# Stack that returns the maximum of all elements in constant time
class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_stack = []   # we use a stack to represent the current max state at any time

    def push(self, a):
        self.__stack.append(a)
        self.add_max(a)     # we update the max stack everytime there's a push

    def pop(self):
        assert(len(self.__stack))
        popped_value = self.__stack.pop()
        self.__max_stack.pop() # we update the max stack everytime there's a pop

        return popped_value

    def get_max(self):
        assert(len(self.__stack))
        return self.__max_stack[-1]

    def add_max(self, value):
        if len(self.__max_stack) == 0 or value > self.__max_stack[-1]:
            self.__max_stack.append(value)
        else:
            self.__max_stack.append(self.__max_stack[-1])     # we keep the old max

    def get_size(self):
        return len(self.__stack)

    def print_stack(self):
        for value in self.__stack:
            print(value, end=' ')

    def get_stack(self):
        return self.__stack

# Queue implemented with two stacks
class Queue():
    def __init__(self):
        self.__input_stack = StackWithMax()
        self.__output_stack = StackWithMax()
    
    def push(self, value):
        self.__input_stack.push(value)

    def pop(self):
        assert(self.get_size() > 0)

        if self.__output_stack.get_size() == 0:
            while self.__input_stack.get_size() != 0:
                value = self.__input_stack.pop()
                self.__output_stack.push(value)
        self.__output_stack.pop()

    def get_max(self):
        max_1 = self.__input_stack.get_max()  if self.__input_stack.get_size()  > 0 else 0
        max_2 = self.__output_stack.get_max() if self.__output_stack.get_size() > 0 else 0

        return max(max_1, max_2)

    def get_size(self):
        return self.__input_stack.get_size() + self.__output_stack.get_size()

    # head on the left side, tail on the right side
    def print_queue(self):
        for n in reversed(self.__output_stack.get_stack()):
            print(n, end=' ')
        
        for n in self.__input_stack.get_stack():
            print(n, end=' ')



if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))


