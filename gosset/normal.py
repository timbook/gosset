from scipy import stats
from .rv import ContinuousRV

class Normal(ContinuousRV):
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
        self._rv = stats.norm(loc=mu, scale=sigma)

    def __repr__(self):
        return f"Normal(mu={self.mu}, sigma={self.sigma})"

class StandardNormal(Normal):
    def __init__(self):
        super().__init__(0, 1)
