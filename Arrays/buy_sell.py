'''
O(n) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def buy_sell(prices):
        buy,profit = prices[0],0
        for i in prices:
            if i < buy:
                buy = i
            elif i-buy > profit:
                profit = i-buy
        return profit

print(buy_sell([7,1,5,3,6,4]))