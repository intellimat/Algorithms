# return the number of coins used to change m
# having some denoms
def get_min_change_recursive(money, denoms):

    if money <= 0:
        return 0
    
    min_coins = float('inf')  # biggest value

    for d in denoms:
        if money-d >= 0:
            change = get_min_change_recursive(money-d, denoms)
            if change + 1 < min_coins:
                min_coins = change + 1
    return min_coins


def get_min_change_dp(money, denoms):
    min_num_coins = [0] + [float('inf')] * (money)

    for m in range(1, money + 1):
        for d in denoms:
            if m >= d:
                num_coins = min_num_coins[m-d] + 1 
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins

    return min_num_coins[money]



if __name__ == '__main__':
    m = int(input())
    denoms = [1,3,4]    # denominations - the order doesn't metter
    coins = get_min_change_dp(m, denoms) 
    print(coins)


