"""
    These function calculate the payoff for European Call and Put options
    given their strike price and the price of the underlying asset
"""


class European_Call_Payoff:
    def __init__(self, strike):
        self.strike = strike

    def get_payoff(self, stock_price):
        if stock_price > self.strike:
            return stock_price - self.strike
        else:
            return 0


class European_Put_Payoff:
    def __init__(self, strike):
        self.strike = strike

    def get_payoff(self, stock_price):
        if stock_price < self.strike:
            return self.strike - stock_price
        else:
            return 0
