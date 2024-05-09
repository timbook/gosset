from scipy import stats
from .rv import ContinuousRV

class Gamma(ContinuousRV):
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta
        self._rv = stats.gamma(a=alpha, scale=beta)

    def __repr__(self):
        return f"Gamma(alpha={self.alpha}, beta={self.beta})"

class Exponential(Gamma):
    def __init__(self, beta):
        super().__init__(1, beta)

    def __repr__(self):
        return f"Exponential(beta={self.beta})"
