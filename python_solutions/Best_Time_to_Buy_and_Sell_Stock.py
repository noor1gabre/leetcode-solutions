class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize min_price to a large number and max_profit to 0
        min_price = float('inf')
        max_profit = 0
        
        # Loop through each price
        for price in prices:
            # Update min_price to the lowest price seen so far
            if price < min_price:
                min_price = price
            # Calculate the profit if we sold at the current price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit
