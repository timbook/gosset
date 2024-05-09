from scipy import stats
from .rv import DiscreteRV

class DUniform(DiscreteRV):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._rv = stats.randint(a, b + 1)

    def __repr__(self):
        return f"DUniform(a={self.a}, b={self.b})"
