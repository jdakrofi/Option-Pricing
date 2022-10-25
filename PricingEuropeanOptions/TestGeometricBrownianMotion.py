"""
    Testing the use of Geometric Brownian Motion to generate sample paths
    that mimic changes in price of an equity over a period of time.
"""
import matplotlib.pyplot as plt
from GeometricBrownianMotion import GeometricBrownianMotion

if __name__ == '__main__':
    paths = 100
    initial_price = 100
    drift = .08
    volatility = .1
    dt = 1/365
    T = 1
    price_paths = []

    # Generating a set of sample paths
    for _ in range(paths):
        price_paths.append(GeometricBrownianMotion(initial_price, drift, volatility, dt, T).prices)

    for price_path in price_paths:
        plt.plot(price_path)

    plt.xlabel("Days", fontsize=15)
    plt.ylabel("Price", fontsize=15)
    plt.title("Simulated Equity Price Paths", fontsize=20)
    plt.show()

