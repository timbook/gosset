from scipy import stats
from .rv import DiscreteRV

class Binomial(DiscreteRV):
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self._rv = stats.binom(n, p)

    def __repr__(self):
        return f"Binomial(n={self.n}, p={self.p})"

class Bernoulli(Binomial):
    def __init__(self, p):
        super().__init__(1, p)

    def __repr__(self):
        return f"Bernoulli(p={self.p})"
