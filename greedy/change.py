# Uses python3


# Available coins: 1, 5, 10
# Greedy choice: take as many greater value coins as you can, then again with the second most valuable coin and then with the third
# It's a safe move because if in our optimal solution we don't use the most valuable coins, we can sum up smaller coins and substitute the group of coins
# with one single coin that has greater value. So the overall value is the same but we now have used less coins. Furthermore we can iterate this process and 
# the value will always remain the same but the amount coins will decrease. (So we gotta use for sure all the greatest value coins in our optimal solution)
def get_change(m):
    #the coins in the array are ordered from the end  10(i=0), 5(i=1), 1(i=2)
    takenCoins  = [0,0,0] #coins[i] is the amount of i coin taken
    coinsValues = [10,5,1]
    sum = 0
    i = 0
    while m > 0 and i < len(coinsValues):
        #print(f'iteration {i}')
        #print(f'm = {m}, coinsValues[{i}] = {coinsValues[i]}')
        i_amountTaken = m // coinsValues[i]
        #print(f'i_amountTaken = {i_amountTaken}')
        takenCoins[i] = i_amountTaken
        sum += i_amountTaken
        m = m - i_amountTaken * coinsValues[i]
        i += 1
    return sum

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
