from scipy import stats
from .rv import ContinuousRV

class Pareto(ContinuousRV):
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta
        self._rv = stats.pareto(b=beta, scale=alpha)

    def __repr__(self):
        return f"Pareto(alpha={self.alpha}, beta={self.beta})"
