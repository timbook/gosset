from scipy import stats
from .rv import ContinuousRV

class Cauchy(ContinuousRV):
    def __init__(self, theta=0, sigma=1):
        self.theta = theta
        self.sigma = sigma
        self._rv = stats.cauchy(loc=theta, scale=sigma)

    def __repr__(self):
        return f"Cauchy(theta={self.theta}, sigma={self.sigma})"

class StandardCauchy(Cauchy):
    def __init__(self):
        super().__init__(0, 1)
