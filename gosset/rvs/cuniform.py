from scipy import stats
from .rv import ContinuousRV

class CUniform(ContinuousRV):
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b
        self._rv = stats.uniform(a, b - a)

    def __repr__(self):
        return f"CUniform(a={self.a}, b={self.b})"
