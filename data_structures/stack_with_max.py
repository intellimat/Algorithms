#python3
import sys

# In this stack implementation, getting the max takes always constant time, because we push the correct max for every push in the __stack
# and we pop the last element in __max_stack for every pop in __stack
# so to get the current max we access the last __max_stack element
# The two stacks are synchronized!

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_stack = []   # we use a stack to represent the current max state at any time

    def push(self, a):
        self.__stack.append(a)
        self.add_max(a)     # we update the max stack everytime there's a push

    def pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__max_stack.pop() # we update the max stack everytime there's a pop

    def _max(self):
        assert(len(self.__stack))
        return self.__max_stack[-1]

    def add_max(self, value):
        if len(self.__max_stack) == 0 or value > self.__max_stack[-1]:
            self.__max_stack.append(value)
        else:
            self.__max_stack.append(self.__max_stack[-1])     # we keep the old max


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack._max())
        else:
            assert(0)
