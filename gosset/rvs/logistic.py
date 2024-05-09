from scipy import stats
from .rv import ContinuousRV

class Logistic(ContinuousRV):
    def __init__(self, mu, beta):
        self.mu = mu
        self.beta = beta
        self._rv = stats.logistic(loc=mu, scale=beta)

    def __repr__(self):
        return f"Logistic(mu={self.mu}, beta={self.beta})" 
