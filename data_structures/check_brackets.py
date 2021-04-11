# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

'''
Check if the brackets of a string are correctly opened and closed by using a stack
The stack head is the last element of the list
We push each opening bracket then we pop the last one when we find a closing bracket (and check if they match)
'''
def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":       # opening brackets
            b = Bracket(next, i+1)
            opening_brackets_stack.append(b)

        elif next in ")]}":     # closing brackets
            if len(opening_brackets_stack) == 0:
                first_unmatched_closing_bracket = Bracket(next, i+1)
                return first_unmatched_closing_bracket

            popped_bracket = opening_brackets_stack.pop()
            if not are_matching(popped_bracket.char, next):     # stack is not empty
                wrong_closing_bracket = Bracket(next, i+1)
                return wrong_closing_bracket

    if len(opening_brackets_stack) > 0:
        first_unmatched_opening_bracket = opening_brackets_stack[0]
        return first_unmatched_opening_bracket
    
    return None


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == None:
        print('Success')
    else:
        print(mismatch.position)


if __name__ == "__main__":
    main()
