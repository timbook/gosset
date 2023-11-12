from scipy import stats
from .rv import DiscreteRV

class Poisson(DiscreteRV):
    def __init__(self, lambda_):
        self.lambda_ = lambda_
        self._rv = stats.poisson(lambda_)

    def __repr__(self):
        return f"Poisson(lambda_={self.lambda_})"
