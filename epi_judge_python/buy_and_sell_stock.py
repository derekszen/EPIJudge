from typing import List

from test_framework import generic_test


<<<<<<< HEAD
# divide and conquer
def buy_and_sell_stock_once_recursive(prices: list) -> int:
    length = len(prices)
    if(prices is None or length == 1):
        return 0.0
    if(length == 2):
        return prices[1] - prices[0] if prices[1] > prices[0] else 0.0
    return max(buy_and_sell_stock_once(prices[:length//2]), buy_and_sell_stock_once(prices[length//2:]), max(prices[length//2:]) - min(prices[:length//2]) )
=======
def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    return 0.0
>>>>>>> b736406dfb6e8e6be2612e8a57e710baf90a2d3e

# Dynamic programming
def buy_and_sell_stock(prices: list) -> int:
    length = len(prices)
    if(prices is None or length == 1):
        return 0.0
    if(length == 2):
        return prices[1] - prices[0] if prices[1] > prices[0] else 0.0
    
    maxseen = prices[0]
    minseen = prices[0]
    max_value = 0.0
    for p in prices:
        max_value = max(max_value, p - minseen)
        minseen = min(minseen, p)
    return max_value

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
