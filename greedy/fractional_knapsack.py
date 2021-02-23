# Uses python3
import sys

def get_optimal_value(capacity, items):
    value = 0.
    i = 0
    while capacity > 0 and i < len(items):
        #take the most valueable item
        item = items[i]
        i_quantityTaken = min(item[1], capacity)
        value += item[0] * i_quantityTaken / item[1]
        capacity -= i_quantityTaken
        i += 1
    return value

def takeMostValuable(elem):
    return elem[0] / elem[1]


if __name__ == "__main__":
    n, capacity = map(int, input().split()) # n is the amount of items, w is the capacity of a knapsack
    items = []
    for i in range(1,n+1):
        value, weight = map(int, input().split())
        items.append([value,weight])
        items.sort(reverse=True, key=takeMostValuable)
    #print(f'items = {items}')
    print(get_optimal_value(capacity, items))
    #print("{:.10f}".format(opt_value))
