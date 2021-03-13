
'''
We are given a primitive calculator that can perform the following three operations with
the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥. 
Given positive integer 𝑛, find the minimum number of operations needed to obtain the number 𝑛
starting from the number 1.
'''

# n >= 1
# dynamic approach
def get_num_of_ops(n):
    if n == 1:
        return (0,[1])

    computed_list = ['',(0,[1])]

    for k in range (2,n+1):
        options = [
            int(k/3) if k % 3 == 0 else None,
            int(k/2) if k % 2 == 0 else None,
            k-1
        ]
        min_t = (float('inf'), [])
        for option in options:
            if option != None:
                num_of_ops = computed_list[option][0] + 1
                sequence = computed_list[option][1] + [k]
                if num_of_ops < min_t[0]:
                    min_t = (num_of_ops, sequence)
        computed_list.append(min_t)

    return computed_list[n]



if __name__ == '__main__':
    n = int(input())
    t = get_num_of_ops(n)
    print(t[0])

    for x in t[1]:
        print(x, end = ' ')
