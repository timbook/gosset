from scipy import stats
from .rv import ContinuousRV

class Beta(ContinuousRV):
    def __init__(self, alpha=1, beta=1):
        self.alpha = alpha
        self.beta = beta
        self._rv = stats.beta(alpha, beta)

    def __repr__(self):
        return f"Beta(alpha={self.alpha}, beta={self.beta})"
