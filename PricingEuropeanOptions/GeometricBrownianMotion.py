"""
    Geometric Brownian Motion is a stochastic process is being used to generate
    sample paths that mimic changes in price of an equity over a period of time.
"""

import numpy as np


class GeometricBrownianMotion:

    def simulate_paths(self):
        # Generate prices till the end of the Time period
        while 0 < self.T - self.dt:
            # Brownian motion
            dWt = np.random.normal(0, self.dt**.5)
            # Change in price = expected return + variation(shocks) to the return
            dYt = (self.drift*self.dt) + (self.volatility*dWt)
            # Update current price
            self.current_price += dYt
            # Append new price to series
            self.prices.append(self.current_price)
            # Account for the step in time
            self.T -= self.dt

    def __init__(self, initial_price, drift, volatility, dt, T):
        self.current_price = initial_price
        self.initial_price = initial_price
        # Average Historical return for time period "T"
        self.drift = drift
        # Implied Volatility
        self.volatility = volatility
        # Discrete Time Steps 1/365 days
        self.dt = dt
        # Time period (one year)
        self.T = T
        self.prices = []
        self.simulate_paths()



