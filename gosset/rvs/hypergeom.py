from scipy import stats
from .rv import DiscreteRV

class Hypergeometric(DiscreteRV):
    """
    The hypergeometric distribution random variable. Note the parametrization differs widely and confusingly across sources. Here, it is as follows:
        - N is the total population size
        - M is the total number of successes in the population
        - K is the number of draws from the population

    For example, if you draw 5 cards from a standard deck of playing cards, the number of aces would be (N=52, M=4, K=5)

    f(x) = (M choose x) (N - M choose K - x) / (N choose K)
    """
    def __init__(self, N, M, K):
        self.N = N
        self.M = M
        self.K = K
        self._rv = stats.hypergeom(M=N, n=M, N=K)

    def __repr__(self):
        return f"Hypergeometric(N={self.N}, M={self.M}, K={self.K})"
