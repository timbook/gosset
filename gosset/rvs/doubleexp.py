from scipy import stats
from .rv import ContinuousRV

class DoubleExponential(ContinuousRV):
    def __init__(self, mu=0, sigma=1):
        self.mu = mu
        self.sigma = sigma
        self._rv = stats.laplace(loc=mu, scale=sigma)

    def __repr__(self):
        return f"DoubleExponential(mu={self.mu}, sigma={self.sigma})"

class Laplace(DoubleExponential):
    def __repr__(self):
        return f"Laplace(mu={self.mu}, sigma={self.sigma})"
