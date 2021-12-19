#given a list of currency denominations, return the minimum change that cannot be represented by said list
def nonConstructibleChange(coins):
    coins.sort()
    coinChange = 0


    for coin in coins:
            if coin > coinChange+1:
                return coinChange+1
            coinChange += coin
    return coinChange+1

currency_list= [5, 7, 1, 1, 2, 3, 22]


#test
print(nonConstructibleChange(currency_list))
