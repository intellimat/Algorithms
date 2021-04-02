
# discrete knapsack without repetition
# dp
def get_initial_matrix(n, W):
    M = []
    for i in range(n + 1):
        row = []
        for j in range(W + 1):
            row.append(0)
        M.append(row)

    return M
    

def get_optimal_weight(n, W, items_weights):
    optimal_weight = get_initial_matrix(n, W)

    for i in range(1, n + 1):
        item_weight = items_weights[i-1]
        for w in range(1, W + 1):
            best = optimal_weight[i-1][w] # this ith bar is not present in the optimal solution, then we skip it
            if w - item_weight >= 0:
                second_option = optimal_weight[i-1][w - item_weight] + item_weight # or ith bar is present in the optimal solution, so we add it and then we go on looping on the other bars
                if second_option > best:
                    best = second_option
            optimal_weight[i][w] = best
    
    return optimal_weight[n][W]

    
if __name__ == '__main__':
    W, n = map(int,input().split())
    items_weights = list(map(int,input().split()))
    optimal_weight = get_optimal_weight(n, W, items_weights)
    print(optimal_weight)