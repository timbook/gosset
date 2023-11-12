from scipy import stats
from .rv import DiscreteRV

class NegativeBinomial(DiscreteRV):
    def __init__(self, r, p):
        self.r = r
        self.p = p
        self._rv = stats.nbinom(r, p)

    def __repr__(self):
        return f"NegativeBinomial(r={self.r}, p={self.p})"

class Geometric(NegativeBinomial):
    def __init__(self, p):
        super().__init__(1, p)

    def __repr__(self):
        return f"Geometric(p={self.p})"
