from scipy import stats
from .rv import ContinuousRV

class LogNormal(ContinuousRV):
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
        self._rv = stats.lognorm(loc=mu, scale=sigma)

    def __repr__(self):
        return f"LogNormal(mu={self.mu}, sigma={self.sigma})"
