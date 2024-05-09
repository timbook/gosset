from scipy import stats
from .rv import ContinuousRV

class Weibull(ContinuousRV):
    """
    Weibull distribution as parametrized on Wikipedia: https://en.wikipedia.org/wiki/Weibull_distribution

    f(x) = (k/lambda) * (x/lambda)**(k-1) * exp(-(x/lambda)**k)
    """
    def __init__(self, k, lambda_):
        self.k = k
        self.lambda_ = lambda_
        self._rv = stats.weibull_min(c=k, scale=lambda_)

    def __repr__(self):
        return f"Weibull(k={self.k}, lambda_={self.lambda_})"
