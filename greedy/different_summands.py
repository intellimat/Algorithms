# Uses python3

# The goal of this problem is to represent a given positive integer 𝑛 as a sum of as many pairwise
# distinct positive integers as possible. That is, to find the maximum 𝑘 such that 𝑛 can be written as
# 𝑎1 + 𝑎2 + · · · + 𝑎𝑘 where 𝑎1, . . . , 𝑎𝑘 are positive integers and 𝑎𝑖 ̸= 𝑎𝑗 for all 1 ≤ 𝑖 < 𝑗 ≤ 𝑘.

def get_optimal_summands(n):
    summands = []
    previousPrize = 0
    while n > 0:
        if n - previousPrize > 0:
            prize = previousPrize + 1
            previousPrize = prize
            n = n - prize
            summands.append(prize)
        else:
            lastIndex = len(summands) - 1
            summands[lastIndex] = summands[lastIndex] + n
            n = 0

    return summands

if __name__ == '__main__':
    n = int(input())
    opt_summands = get_optimal_summands(n)
    print(len(opt_summands))
    for s in opt_summands:
        print(s, end=' ')
