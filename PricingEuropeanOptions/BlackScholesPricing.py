"""
    This class is an implementation of the Black-Scholes model which is used to
    calculate option prices
"""
import math
from scipy.stats import norm


class EuropeanCall:
    def call_price(self, asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate):
        b = math.exp(-risk_free_rate*time_to_expiration)  # continuous discount factor
        numerator_x1 = math.log(asset_price/(b*strike_price)) + (.5*(asset_volatility**2)*time_to_expiration)
        denominator = asset_volatility*(time_to_expiration**.5)
        x1 = numerator_x1/denominator
        dist_x1 = norm.cdf(x1)
        z1 = dist_x1*asset_price
        numerator_x2 = math.log(asset_price/(b*strike_price)) - (.5*(asset_volatility**2)*time_to_expiration)
        x2 = numerator_x2/denominator
        dist_x2 = norm.cdf(x2)
        z2 = b*strike_price*dist_x2
        return z1 - z2

    def __init__(self, asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate):
        self.asset_price = asset_price
        self.asset_volatility = asset_volatility
        self.strike_price = strike_price
        self.time_to_expiration = time_to_expiration
        self.risk_free_rate = risk_free_rate
        self.price = self.call_price(asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate)


class EuropeanPut:
    def put_price(self, asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate):
        b = math.exp(-risk_free_rate*time_to_expiration)  # continuous discount factor
        numerator_x1 = math.log((b*strike_price)/asset_price) + (.5*(asset_volatility**2)*time_to_expiration)
        denominator = asset_volatility*(time_to_expiration**.5)
        x1 = numerator_x1/denominator
        dist_x1 = norm.cdf(x1)
        z1 = b*strike_price*dist_x1
        numerator_x2 = math.log((b*strike_price)/asset_price) - (.5*(asset_volatility**2)*time_to_expiration)
        x2 = numerator_x2/denominator
        dist_x2 = norm.cdf(x2)
        z2 = asset_price*dist_x2
        return z1 - z2

    def __init__(self, asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate):
        self.asset_price = asset_price
        self.asset_volatility = asset_volatility
        self.strike_price = strike_price
        self.time_to_expiration = time_to_expiration
        self.risk_free_rate = risk_free_rate
        self.price = self.put_price(asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate)


"""ep= EuropeanPut(100, .3, 100, 1, .01)
    print(ec.price)"""