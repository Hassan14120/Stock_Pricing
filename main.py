def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        current_profit = price - min_price
        if current_profit > max_profit:
            max_profit = current_profit
    return max_profit
prices = [5, 7, 2,3,45,6,8]
if max_profit(prices) == 0: 
    print("No profit can be made for today! Close and go home")
print("The max profit is : ",max_profit(prices))
