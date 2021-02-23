#Uses python3

def isBetter(current_number, previous_number):
    current_number = str(current_number)
    previous_number = str(previous_number)
    
    concatenated_number_1 = int(current_number + previous_number)
    concatenated_number_2 = int(previous_number + current_number)
    # we just concatenate the two numbers to see how we can generate the largest number
    # the point is to have larger concatenation of numbers on the left of the final number
    if concatenated_number_1 > concatenated_number_2:
        return True
    else:
        return False


def largest_number(numbers):
    answer = ''
    while len(numbers) > 0:
        max_number = numbers[len(numbers)-1] # max_number is the next number to append to the answer (so it's not necessarily the greater of the number in the given sequence)
        for number in numbers:
            if  isBetter(number, max_number):
                max_number = number
        answer += str(max_number) + ''
        numbers.remove(max_number)
    return answer

if __name__ == '__main__':
    n = input()
    numbers = list(map(int, input().split()))
    print(largest_number(numbers))
