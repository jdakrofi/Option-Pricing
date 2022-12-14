import matplotlib.pyplot as plt
import numpy as np
from GeometricBrownianMotion import GeometricBrownianMotion
from EuropeanOptions_Payoff import European_Call_Payoff
from BlackScholesPricing import EuropeanCall


def ECs():
    """
        This function generates a hundred sample paths of the price an underlying equity
        The final price of each path is used to calculate the payoff of the option as
        European options can only be exercised at maturity
        The payoff is discounted by the risk-free rate to obtain the present value of the
        option.
        Finally, the average of the 100 option prices is compared with the price of the option generated
        by the Black-Scholes model to observe how similar they are.
    """

    paths = 100
    initial_price = 100
    drift = .08
    volatility = .3
    dt = 1/365
    T = 1
    price_paths = []

    # Generate a set of sample paths
    for _ in range(paths):
        price_paths.append(GeometricBrownianMotion(initial_price, drift, volatility, dt, T).prices)

    call_payoffs = []
    ec = European_Call_Payoff(100)
    risk_free_rate = .01
    for price_path in price_paths:
        # The last stock price in the series generated by the Geometric Brownian
        # Motion is used to determine the payoff.
        # The risk_free_rate is used to discount the payoff as it received at the
        # end of the year in this example
        call_payoffs.append(ec.get_payoff(price_path[-1])/(1 + risk_free_rate))

    for price_path in price_paths:
        plt.plot(price_path)

    plt.xlabel("Days", fontsize=15)
    plt.ylabel("Price", fontsize=15)
    plt.title("Simulated Equity Price Paths", fontsize=20)
    plt.show()

    print("Monte Carlo Expected option price: " + str(np.average(call_payoffs)*100))
    print("Median option price: " + str(np.median(call_payoffs)))

    bs = EuropeanCall(100, .3, 100, 1, .01)
    print("Black Scholes option price: " + str(bs.price))




if __name__ == "__main__":
    ECs()
